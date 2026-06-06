#include "rs232drive.h"
Rs232SnManageTypeDef       Rs232SnManage={0};
Rs232TxControlTableTypeDef Rs232TxControlTable={NULL,NULL,NULL};
Rs232RxQueueTypeDef        Rs232RxQueue={0,0,RS232DRIVE_PACKQUEUE_MAXLEN,{NULL}};

uint8_t (*pRs232Drive_UserReceiveCallBack)(uint8_t*,uint16_t)=NULL;

void Rs232Drive_SetUserReceiveFun(uint8_t (*pFun)(uint8_t*,uint16_t))
{
	pRs232Drive_UserReceiveCallBack=pFun;
}
uint32_t Rs232Drive_GetSn(void)
{
	Rs232SnManage.SN++;
	return Rs232SnManage.SN;
}

uint32_t Rs232Drive_CheckSum(uint8_t *data,uint16_t size)
{
	uint32_t i=0,check=0;
	uint32_t *buf;
	buf=(uint32_t*)data;
	for(i=0;i<(size/4);i++)
	{
		check+=BigtoLittle32(*buf);
		buf++;
	}
	if(size%4)
	{
		check+=BigtoLittle32((*buf)&(0xFFFFFFFF>>((4-(size%4))*8)));
	}
	return check;
}


/*************************************************************
函数：DeviceTranspot_AddRxMsg
功能：接收数据报文存入队列中
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t Rs232Drive_AddDataQueue(Rs232DataPackTypeDef *pRxPack)
{
	if((Rs232RxQueue.tail==Rs232RxQueue.head)&&(Rs232RxQueue.queuelen==0))
	 return RS232_RXQUEUE_FULL;              //队列满
	Rs232RxQueue.pDataPack[Rs232RxQueue.tail]=pRxPack;
	Rs232RxQueue.tail++;
	Rs232RxQueue.queuelen--;
	if(Rs232RxQueue.tail==RS232DRIVE_PACKQUEUE_MAXLEN)
		Rs232RxQueue.tail=0;
	return RS232_RXQUEUE_ADD;
}

/*************************************************************
函数：DeviceTranspot_GetRxMsg
功能：从缓存队列中获取报文
参数：msg 消息指针
返回：MSG_QUEUE_NULL 队列空
      MSG_QUEUE_GET  数据获取成功
*************************************************************/
Rs232DataPackTypeDef *Rs232Drive_GetDataQueue(void)
{
	Rs232DataPackTypeDef *pRxPack;
	if((Rs232RxQueue.tail==Rs232RxQueue.head)&&(Rs232RxQueue.queuelen==RS232DRIVE_PACKQUEUE_MAXLEN))
		return NULL;	//队列无数据
  pRxPack=Rs232RxQueue.pDataPack[Rs232RxQueue.head];
	Rs232RxQueue.pDataPack[Rs232RxQueue.head]=NULL;
	Rs232RxQueue.head++;
	Rs232RxQueue.queuelen++;
	if(Rs232RxQueue.head==RS232DRIVE_PACKQUEUE_MAXLEN)
		Rs232RxQueue.head=0;
	return pRxPack;
}

//从API接口获取数据
void Rs232Drive_ReceiveApiData(uint8_t* Data,uint16_t size)
{
	Rs232DataPackTypeDef *pDataPack;
  if(size<12)
		return;
	pDataPack=(Rs232DataPackTypeDef*)Data;
	if(((pDataPack->Head.datalen+12)==size))
	{
		pDataPack=SysMem_malloc(size);
		if(pDataPack!=NULL)
		{
			SysMem_copy((void*)pDataPack,(void*)Data,size);
			if(Rs232Drive_AddDataQueue(pDataPack)==RS232_RXQUEUE_FULL)
			{
				SysMem_free(pDataPack);
			}
		}
	}
}

/*************************************************************
函数：TransportTask_TraverseBlockAddr
功能：查找链表中的任务块
参数：SN 任务流水码
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
Rs232TxControlBlockTypeDef *Rs232Drive_TraverseTaskBlock(uint32_t Sn)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	if(Rs232TxControlTable.head==NULL)
		return NULL;
	pTxBlock=Rs232TxControlTable.head;
	while(pTxBlock)
	{
		if(pTxBlock->TxUint.sn==Sn)
			return pTxBlock;
    pTxBlock=pTxBlock->next;
	}
	return NULL;
}

/*************************************************************
函数：TransportTask_TraverseBlockAddr
功能：查找链表中的任务块
参数：SN 任务流水码
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
Rs232TxUintTypeDef *Rs232Drive_TraverseTxUint(uint32_t Sn)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	pTxBlock=Rs232Drive_TraverseTaskBlock(Sn);
	if(pTxBlock==NULL)
	 return NULL;
	return &pTxBlock->TxUint;
}

/*************************************************************
函数：DeviceTranspot_AddTxTask
功能：增加报文发送任务
参数：SN 任务流水码
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
uint8_t Rs232Drive_AddTxUint(Rs232TxUintTypeDef *pTxUint)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	if(Rs232TxControlTable.table_len==RS232DRIVE_TXTABLE_MAXLEN)
		return 0x00;//链表满
	if(Rs232Drive_TraverseTxUint(pTxUint->DataPack->SN))
		return 0x01;//已经有相同任务
	pTxBlock=SysMem_malloc(sizeof(Rs232TxControlBlockTypeDef));
	if(pTxBlock==NULL)
		return 0x02;//空间满
	SysMem_copy((void*)&pTxBlock->TxUint,(void*)pTxUint,sizeof(Rs232TxUintTypeDef));
	if(Rs232TxControlTable.head==NULL)
	{
		pTxBlock->next=NULL;
		pTxBlock->proir=NULL;
		Rs232TxControlTable.head=pTxBlock;
		Rs232TxControlTable.tail=pTxBlock;
		Rs232TxControlTable.table_len++;
	}
	else
	{
		pTxBlock->next=NULL;
		Rs232TxControlTable.tail->next=pTxBlock;
		pTxBlock->proir=Rs232TxControlTable.tail;
		Rs232TxControlTable.tail=pTxBlock;
		Rs232TxControlTable.table_len++;
	}
	return 0xFF;
}

/*************************************************************
函数：DeviceTranspot_AddTxTask
功能：增加报文发送任务
参数：SN 任务流水码
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
uint8_t Rs232Drive_RemoveTxUint(uint32_t Sn)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	pTxBlock=Rs232Drive_TraverseTaskBlock(Sn);
	if(pTxBlock==NULL)
		return 0x00;//任务不存在
	if((Rs232TxControlTable.table_len==1)&&(Rs232TxControlTable.head==Rs232TxControlTable.tail))//链表只剩下一个任务
	{
		Rs232TxControlTable.head=NULL;
		Rs232TxControlTable.tail=NULL;
	}
	else if(pTxBlock->next==NULL)//最后一个
	{
		Rs232TxControlTable.tail=pTxBlock->proir;
		Rs232TxControlTable.tail->next=NULL;
	}
	else if(pTxBlock->proir==NULL)//第一个
	{
		Rs232TxControlTable.head=pTxBlock->next;
		Rs232TxControlTable.head->proir=NULL;
	}
	else//中间
	{
		pTxBlock->next->proir=pTxBlock->proir;
		pTxBlock->proir->next=pTxBlock->next;
	}
	Rs232TxControlTable.table_len--;
	SysMem_free(pTxBlock);
	return 0xFF;
}

/*************************************************************
函数：DeviceTranspot_GetTxTask
功能：从链表中获取待发送任务
参数：msg 消息指针
返回：MSG_QUEUE_NULL 队列空
      MSG_QUEUE_GET  数据获取成功
*************************************************************/
Rs232TxUintTypeDef *Rs232Drive_GetTxUint(void)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	
	if(Rs232TxControlTable.head==NULL)
		return NULL;
	pTxBlock=Rs232TxControlTable.head;
	while(pTxBlock)
	{
		if(pTxBlock->TxUint.txsta==0x00)
			return &pTxBlock->TxUint;
		pTxBlock=pTxBlock->next;
	}
	return NULL;
}

Rs232TxUintTypeDef *Rs232Drive_GetOuTimeUint(void)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	if(Rs232TxControlTable.head==NULL)
		return NULL;
	pTxBlock=Rs232TxControlTable.head;
	while(pTxBlock)
	{
		if(pTxBlock->TxUint.outtimenum==RS232DRIVE_RES_OUTTIMENUM)
			return &pTxBlock->TxUint;
		pTxBlock=pTxBlock->next;
	}
	return NULL;
}

uint8_t Rs232Drive_SendData(uint8_t *Data,uint16_t size)
{
	Rs232TxUintTypeDef TxUint;
	TxUint.ack=0x01;
	TxUint.sn =Rs232Drive_GetSn();
	
	TxUint.DataPack=SysMem_malloc(sizeof(Rs232DataHeadTypeDef)+4+size);
	if(TxUint.DataPack==NULL)
		return 0x01;
	SysMem_copy(TxUint.DataPack->Data,Data,size);
	TxUint.DataPack->SN=TxUint.sn;
	TxUint.DataPack->Head.AA=0xAA;
	TxUint.DataPack->Head.BB=0xBB;
	TxUint.DataPack->Head.datalen=size;
	TxUint.DataPack->Head.checksum=Rs232Drive_CheckSum((uint8_t*)&TxUint.DataPack->SN,size+4);
	if(Rs232Drive_AddTxUint(&TxUint)!=0xFF)
	{
		SysMem_free(TxUint.DataPack);
		return 0x02;
	}
	return 0xFF;
}

uint8_t Rs232Drive_SendAck(uint32_t Sn)
{
	Rs232TxUintTypeDef TxUint;
	TxUint.txsta=0x00;
	TxUint.outime=0x00;
	TxUint.outtimenum=0x00;
	TxUint.ack=0x00;
	TxUint.sn =Sn;
	TxUint.DataPack=SysMem_malloc(sizeof(Rs232DataHeadTypeDef)+4);
	if(TxUint.DataPack==NULL)
		return 0x00;
	TxUint.DataPack->SN=Sn;
	TxUint.DataPack->Head.datalen=0x00;
	TxUint.DataPack->Head.checksum=Rs232Drive_CheckSum((uint8_t*)&Sn,sizeof(Sn));;
	TxUint.DataPack->Head.AA=0xAA;
	TxUint.DataPack->Head.BB=0xBB;
	if(Rs232Drive_AddTxUint(&TxUint)!=0xFF)
	{
		SysMem_free(TxUint.DataPack);
		return 0x00;
	}
	return 0xFF;
}
uint8_t Rs232Drive_ReceiveAck(Rs232DataPackTypeDef *pRxPack)
{
	Rs232TxUintTypeDef *pTxUint;
	pTxUint=Rs232Drive_TraverseTxUint(pRxPack->SN);
	if(pTxUint==NULL)
		return 0xFF;
	if(pTxUint->txsta)
	{
		if(pTxUint->DataPack)
		 SysMem_free(pTxUint->DataPack);//释放数据包内存
	  Rs232Drive_RemoveTxUint(pTxUint->sn);
		return 0xFF;
	}
	return 0x00;
}


void Rs232Drive_Init(void)
{
	Rs232Api_UartInit();
	Rs232Api_SetReceiveCallBackFun(Rs232Drive_ReceiveApiData);
}
//串口发送数据任务
void Rs232Drive_TxTaskRun(void)
{
	Rs232TxUintTypeDef *pTxUint;
	pTxUint=Rs232Drive_GetTxUint();
	if(pTxUint==NULL)
		return;
	if(Rs232Api_SendData((uint8_t*)pTxUint->DataPack,(pTxUint->DataPack->Head.datalen+sizeof(Rs232DataHeadTypeDef)+4)))//发送成功
	{
		Rs232Drive_SetTxState(pTxUint);
		if(Rs232Drive_GetAckFlag(pTxUint)==0x00)//无需应答
    {
      if(pTxUint->DataPack)
				SysMem_free(pTxUint->DataPack);//释放数据包内存
			Rs232Drive_RemoveTxUint(pTxUint->sn);
		}
	}
}

void Rs232Drive_RemoveOutTimeUint(void)
{
	Rs232TxUintTypeDef *pTxUint;
	pTxUint=Rs232Drive_GetOuTimeUint();//获取未响应报文
	if(pTxUint!=NULL)//删除超时未响应报文
	{
		if(pTxUint->DataPack)
		 SysMem_free(pTxUint->DataPack);//释放数据包内存
	  Rs232Drive_RemoveTxUint(pTxUint->sn);
	}
}

void Rs232Drive_ReceiveTask(void)
{
	static uint8_t runstate=0;
	static Rs232DataPackTypeDef *pDataPack;
	uint32_t checksum;
	switch(runstate)
	{
		case 0x00://获取数据包
			pDataPack=Rs232Drive_GetDataQueue();
			if(pDataPack!=NULL)
			{
				checksum=Rs232Drive_CheckSum((uint8_t*)&pDataPack->SN,pDataPack->Head.datalen+4);
		    if(checksum!=pDataPack->Head.checksum)//非法数据包
				{
					runstate=0x04;
				}
				else
				{
				if(pDataPack->Head.datalen==0x0000)//应答数据包
				 runstate=0x01;
				else
				 runstate=0x02;
			  }
			}
			break;
		case 0x01:
			if(Rs232Drive_ReceiveAck(pDataPack)==0xFF)
			 runstate=0x04;
			break;
		case 0x02://发送应答
			if(Rs232Drive_SendAck(pDataPack->SN)==0xFF)
				runstate=0x03;
			break;
		case 0x03://上传数据到上层应用
			if(pRs232Drive_UserReceiveCallBack!=NULL)
			 (*pRs232Drive_UserReceiveCallBack)(pDataPack->Data,pDataPack->Head.datalen);
			runstate=0x04;
			break;
		case 0x04://释放数据包内存
			SysMem_free(pDataPack);
			runstate=0x00;
			break;
	}
}
//外部调用任务
void Rs232Drive_TimeTask(void)
{
	Rs232TxControlBlockTypeDef *pTxBlock;
	pTxBlock=Rs232TxControlTable.head;
	if(pTxBlock==NULL)
		return;
	while(pTxBlock)
	{
		if(pTxBlock->TxUint.txsta&&(pTxBlock->TxUint.outtimenum<RS232DRIVE_RES_OUTTIMENUM))
		{
			if(pTxBlock->TxUint.outime<RS232DRIVE_RES_OUTTIME)
			 pTxBlock->TxUint.outime++;
			else//超时无响应
			{
				pTxBlock->TxUint.outime=0x00;
				if(pTxBlock->TxUint.outtimenum<RS232DRIVE_RES_OUTTIMENUM)
				{
					pTxBlock->TxUint.outtimenum++;
					Rs232Drive_ResetTxState((&pTxBlock->TxUint));//重新发送数据
				}
			}
		}
		pTxBlock=pTxBlock->next;
	}
}

void Rs232Drive_TaskRun(void)
{
	Rs232Drive_ReceiveTask();
	Rs232Drive_TxTaskRun();
	Rs232Drive_RemoveOutTimeUint();
}
