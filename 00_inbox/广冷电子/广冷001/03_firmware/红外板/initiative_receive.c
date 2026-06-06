#include "initiative_receive.h"

InitiativeReceiveTableTypeDef InitiativeReceiveTable;
void (*pInitiativeReceive_CallBack)(TransportCanMsgTypeDef *)=NULL;



/*****************************************
函数：Initiative_SendMsg
功能：发送正常响应
参数：
返回：
******************************************/
void InitiativeReceive_GetTableData(uint8_t sourceID,void *pdata,void *ptabledata)
{
	uint8_t size;
	size=sourceID/64;
	Mem_copy(pdata,ptabledata,(0x01<<size));
}

/*****************************************
函数：Initiative_SendMsg
功能：发送正常响应
参数：
返回：
******************************************/
uint8_t InitiativeReceive_GetTableDataLen(uint8_t sourceID)
{
	uint8_t size=0;
	size=0x01<<(sourceID/64);
	return size;
}
/*****************************************
函数：Initiative_SendMsg
功能：发送正常响应
参数：
返回：
******************************************/
uint8_t InitiativeReceive_SendMsg(InitiativeReceiveTypeDef *pInitiativeReceive,uint8_t funcid)
{
	TransportCanMsgTypeDef MsgBuff;
	uint8_t state=0x00;
	MsgBuff.TransportMsgFilter.DestMacID=pInitiativeReceive->can_nodeid;//从站节点ID
	
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeDiscern.can_nodeid;//本节点ID
	
	
	MsgBuff.TransportMsgFilter.SourceID =pInitiativeReceive->sourceid;
	MsgBuff.TransportMsgFilter.FuncID   =funcid;
	
	if(funcid==FUNCID_CYCLETRIGGER)
	 MsgBuff.TransportMsgFilter.Ack      =0x01;//需等待响应
	else
	 MsgBuff.TransportMsgFilter.Ack      =0x00;
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	

	MsgBuff.TransportMsgData.DataSize   =InitiativeReceive_GetTableDataLen(pInitiativeReceive->sourceid);
	
	if(MsgBuff.TransportMsgData.DataSize!=0xFFFF)//节点存在
	{
		MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
		
		InitiativeReceive_GetTableData(pInitiativeReceive->sourceid,
		                               MsgBuff.TransportMsgData.Data,
		                               pInitiativeReceive->data);
		if(TransportLayer_TxMsg(&MsgBuff)!=0xFF)
			Mem_free(MsgBuff.TransportMsgData.Data);
		else
			state=0xFF;
  }
	return state;
}
/*****************************************
函数：InitiativeReceive_SetCallBack
功能：设置主动接收回调函数
参数：DestMacID 目标ID
      SourceID  发送索引表地址数据
      mode      返回数据
返回：
******************************************/
void InitiativeReceive_SetCallBack(void (*p)(TransportCanMsgTypeDef *))
{
	pInitiativeReceive_CallBack=p;
}

/*****************************************
函数：ProtocoStack_SendAsk
功能：发送正常响应报文
参数：DestMacID 目标ID
      SourceID  发送索引表地址数据
      mode      返回数据
返回：
******************************************/
void InitiativeReceive_SendAsk(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FuncID;
	MsgBuff.TransportMsgFilter.Ack      =0x01;      //响应报文
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}


/*************************************************************
函数：InitiativeReceive_TraverseBlockNum
功能：查找链表中的任务块
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
InitiativeReceiveBlockTypeDef *InitiativeReceive_TraverseBlock(uint8_t nodeid,uint8_t sourceid) //获取对应任务块的地址
{
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	if(InitiativeReceiveTable.head==NULL)             //链表中无数据
		return NULL;
	pTaskBlock=InitiativeReceiveTable.head;
	while(pTaskBlock)
	{
		if(pTaskBlock->ReceiveInfo.can_nodeid==nodeid&&pTaskBlock->ReceiveInfo.sourceid==sourceid)
			return pTaskBlock;
		pTaskBlock=pTaskBlock->next;
	}
	return pTaskBlock;
}


/*************************************************************
函数：InitiativeReceive_AddReceive
功能：增加接收任务
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/

uint8_t InitiativeReceive_AddReceive(InitiativeReceiveTypeDef *pReceive)
{
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	
	if(InitiativeReceiveTable.tablesize==INITIATIVERECEIVE_MAXSIZE)
		return 0x00;                                                        //空间满
	if(InitiativeReceive_TraverseBlock(pReceive->can_nodeid,pReceive->sourceid)!=NULL)
		return 0x01;                                                        //队列中已有相同任务号
  pTaskBlock=Mem_malloc(sizeof(InitiativeReceiveBlockTypeDef));
	if(pTaskBlock==NULL)
		return 0x02;                              //创建失败
	
	Mem_copy(&pTaskBlock->ReceiveInfo,pReceive,sizeof(InitiativeReceiveTypeDef));
	
	if(InitiativeReceiveTable.head==NULL)          //链表为空
	{
		pTaskBlock->next=0;
		pTaskBlock->prior=0;
		InitiativeReceiveTable.head=pTaskBlock;
		InitiativeReceiveTable.tail=pTaskBlock;
		InitiativeReceiveTable.tablesize++;
	}
	else
	{
		pTaskBlock->next=NULL;
		InitiativeReceiveTable.tail->next=pTaskBlock;
		pTaskBlock->prior=InitiativeReceiveTable.tail;
		InitiativeReceiveTable.tail=pTaskBlock;
		InitiativeReceiveTable.tablesize++;
	}
	return 0xFF;                                //创建成功
}
/*************************************************************
函数：InitiativeReceive_RemoveReceive
功能：删除接收任务
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
uint8_t InitiativeReceive_RemoveReceive(InitiativeReceiveTypeDef *pReceive)
{
	InitiativeReceiveBlockTypeDef *TaskBlock;
	TaskBlock=InitiativeReceive_TraverseBlock(pReceive->can_nodeid,pReceive->sourceid);
	if(TaskBlock==NULL)             //链表中无数据
		return 0x00;
	if((InitiativeReceiveTable.tablesize==1)&&(InitiativeReceiveTable.head==InitiativeReceiveTable.tail))//链表中只存在一个节点，头尾相同
	{ 
		InitiativeReceiveTable.tail=0;
		InitiativeReceiveTable.head=0;
	}
	else if(TaskBlock->next==NULL)
	{
		InitiativeReceiveTable.tail=TaskBlock->prior;
		InitiativeReceiveTable.tail->next=0;
	}
	else if(TaskBlock->prior==NULL)
	{
		InitiativeReceiveTable.head=TaskBlock->next;
		InitiativeReceiveTable.head->prior=0;
	}
	else 
	{
		TaskBlock->prior->next=TaskBlock->next;
		TaskBlock->next->prior=TaskBlock->prior;	
	}
	InitiativeReceiveTable.tablesize--;
  Mem_free(TaskBlock);
	return 0xFF;  //删除成功
}

void InitiativeReceive_SetConnectFlag(uint8_t nodeid,uint8_t connectflag)
{
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	
	if(InitiativeReceiveTable.head==NULL)             //链表中无数据
		return;
	pTaskBlock=InitiativeReceiveTable.head;
	while(pTaskBlock)
	{
		if(pTaskBlock->ReceiveInfo.can_nodeid==nodeid)
		{
			pTaskBlock->ReceiveInfo.connectflag=connectflag;
			if(pTaskBlock->ReceiveInfo.connectflag==1)
			{
				pTaskBlock->ReceiveInfo.cycleinit=0;
				pTaskBlock->ReceiveInfo.stateinit=0;
				pTaskBlock->ReceiveInfo.thresholdinit=0;
			}
		}
		pTaskBlock=pTaskBlock->next;
	}
}


//外部调用接口函数

uint8_t InitiativeReceive_SetTrigeerRecive(uint8_t nodeid,uint8_t sourceid,void *addr)
{
	InitiativeReceiveTypeDef Receivetask;
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	uint8_t setflag;
	
	pTaskBlock=InitiativeReceive_TraverseBlock(nodeid,sourceid);
	
	if(pTaskBlock==NULL)
	{
		Receivetask.can_nodeid=nodeid;
	  Receivetask.sourceid  =sourceid;
	  Receivetask.data      =addr;
	  Receivetask.trigger_receive=0x01;
		Receivetask.state_enable=0;
		Receivetask.threshold_enable=0;
		Receivetask.cycle_enable=0;
	  setflag=InitiativeReceive_AddReceive(&Receivetask);
	}
	else
	{
		pTaskBlock->ReceiveInfo.trigger_receive=0x01;
	}
	return setflag;
}

uint8_t InitiativeReceive_SetCycleTrigeer(uint8_t nodeid,uint8_t sourceid,uint16_t time,void *addr)
{
	uint8_t setflag=0x00;
	InitiativeReceiveTypeDef Receivetask;
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	pTaskBlock=InitiativeReceive_TraverseBlock(nodeid,sourceid);
	if(pTaskBlock==NULL)
	{
		Receivetask.can_nodeid=nodeid;
	  Receivetask.sourceid  =sourceid;
	  Receivetask.data      =addr;
		
		Receivetask.trigger_receive=0;
		Receivetask.state_enable=0;
		Receivetask.threshold_enable=0;
		Receivetask.cycle_enable=1;
		Receivetask.time=time;
		Receivetask.cycleinit=0;
	  setflag=InitiativeReceive_AddReceive(&Receivetask);
	}
	else
	{
    pTaskBlock->ReceiveInfo.time=time;
		pTaskBlock->ReceiveInfo.cycle_enable=1;
		pTaskBlock->ReceiveInfo.cycleinit=0;
		setflag=0xFF;
	}
	return setflag;
}


uint8_t InitiativeReceive_SetStateTrigeer(uint8_t nodeid,uint8_t sourceid,void *addr)
{
	uint8_t setflag;
	InitiativeReceiveTypeDef Receivetask;
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	pTaskBlock=InitiativeReceive_TraverseBlock(nodeid,sourceid);
	if(pTaskBlock==NULL)
	{
		Receivetask.can_nodeid=nodeid;
	  Receivetask.sourceid  =sourceid;
	  Receivetask.data      =addr;
		
		Receivetask.trigger_receive=0;
		Receivetask.state_enable=1;
		Receivetask.threshold_enable=0;
		Receivetask.cycle_enable=0;
		Receivetask.stateinit=0;
	  setflag=InitiativeReceive_AddReceive(&Receivetask);
	}
	else
	{
	  pTaskBlock->ReceiveInfo.state_enable=1;
		pTaskBlock->ReceiveInfo.stateinit=0;
		setflag=0xFF;
	}
	return setflag;
}

uint8_t InitiativeReceive_SetThresholdTrigeer(uint8_t nodeid,
                                              uint8_t sourceid,
                                              uint32_t low,
                                              uint32_t up, 
                                              void *addr)
{
	uint8_t setflag;
	InitiativeReceiveTypeDef Receivetask;
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	pTaskBlock=InitiativeReceive_TraverseBlock(nodeid,sourceid);
	if(pTaskBlock==NULL)
	{
		Receivetask.can_nodeid=nodeid;
	  Receivetask.sourceid  =sourceid;
	  Receivetask.data      =addr;
		
		Receivetask.trigger_receive=0;
		Receivetask.threshold_enable=1;
		Receivetask.cycle_enable=0;
		Receivetask.state_enable=0;
		Receivetask.thresholdinit=0;
    
		Receivetask.lower_limit=low;
		Receivetask.upper_limit=up;
		
	  setflag=InitiativeReceive_AddReceive(&Receivetask);
	}
	else
	{
	  pTaskBlock->ReceiveInfo.state_enable=1;
		pTaskBlock->ReceiveInfo.thresholdinit=0;
		pTaskBlock->ReceiveInfo.lower_limit=low;
		pTaskBlock->ReceiveInfo.upper_limit=up;
		setflag=0xFF;
	}
	return setflag;
}

void InitiativeReceive_ReceiveTask(TransportCanMsgTypeDef *pRxMsg)
{
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	
	if(pRxMsg->TransportMsgFilter.Ack==0x00)
	 InitiativeReceive_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID,
														 pRxMsg->TransportMsgFilter.DestMacID,
														 pRxMsg->TransportMsgFilter.SourceID,
														 pRxMsg->TransportMsgFilter.FuncID 
														 );
	
	pTaskBlock=InitiativeReceive_TraverseBlock(pRxMsg->TransportMsgFilter.SrcMacID,
	                                          pRxMsg->TransportMsgFilter.SourceID);
	if(pTaskBlock==NULL)
		return;
	if(pRxMsg->TransportMsgData.DataSize!=0)
	{
	 if(pTaskBlock->ReceiveInfo.trigger_receive==0x01)
	 {
		Mem_copy(pTaskBlock->ReceiveInfo.data,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);
		Mem_copy(&pTaskBlock->ReceiveInfo.last,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);//更新last值
	 }
  }
  if(pInitiativeReceive_CallBack!=NULL)
		(*pInitiativeReceive_CallBack)(pRxMsg);
}
/*************************************************************
函数：InitiativeReceive_TimeTask
功能：触发任务执行函数，循环调用执行
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void InitiativeReceive_TimeTask(uint8_t timenum)
{
	InitiativeReceiveBlockTypeDef *pTaskBlock;
	pTaskBlock=InitiativeReceiveTable.head;
	while(pTaskBlock)
	{
		if(pTaskBlock->ReceiveInfo.connectflag==1)
		{
			if(pTaskBlock->ReceiveInfo.timeoverflag==0x00&&pTaskBlock->ReceiveInfo.cycle_enable==1)
			{
				pTaskBlock->ReceiveInfo.timecount++;
				if(pTaskBlock->ReceiveInfo.timecount==pTaskBlock->ReceiveInfo.time)
				{
					pTaskBlock->ReceiveInfo.timecount=0;
					pTaskBlock->ReceiveInfo.timeoverflag=1;
				}
			}
		}
		pTaskBlock=pTaskBlock->next;
	}
}


/*************************************************************
函数：InitiativeTask_TaskRun
功能：触发任务执行函数，循环调用执行
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void InitiativeReceive_TaskRun(void)
{
	static InitiativeReceiveBlockTypeDef *pTaskBlock;
	if(InitiativeReceiveTable.head==NULL)
		return;
	if(pTaskBlock==NULL)
	 pTaskBlock=InitiativeReceiveTable.head;
	
	if(pTaskBlock->ReceiveInfo.connectflag==1)//判断连接状态
	{	
		if(pTaskBlock->ReceiveInfo.cycle_enable)
		{
			if((pTaskBlock->ReceiveInfo.timeoverflag==0x01)||(pTaskBlock->ReceiveInfo.cycleinit==0))
			{
				pTaskBlock->ReceiveInfo.timeoverflag=0;
				pTaskBlock->ReceiveInfo.cycleinit=1;
				InitiativeReceive_SendMsg(&pTaskBlock->ReceiveInfo,FUNCID_CYCLETRIGGER);
			}
		}
		if(pTaskBlock->ReceiveInfo.state_enable)
		{
			uint32_t Data=0;
			InitiativeReceive_GetTableData(pTaskBlock->ReceiveInfo.sourceid,&Data,pTaskBlock->ReceiveInfo.data);
			if((pTaskBlock->ReceiveInfo.last!=Data)||(pTaskBlock->ReceiveInfo.stateinit==0))
			{
				if(InitiativeReceive_SendMsg(&pTaskBlock->ReceiveInfo,FUNCID_STATETRIGGER))
				{
				 pTaskBlock->ReceiveInfo.stateinit=1;
				 pTaskBlock->ReceiveInfo.last=Data;
				}
			}
		}
		else if(pTaskBlock->ReceiveInfo.threshold_enable)
		{
			uint8_t  state=0;
			uint32_t Data=0;
			
			InitiativeReceive_GetTableData(pTaskBlock->ReceiveInfo.sourceid,&Data,pTaskBlock->ReceiveInfo.data);
			
			if(Data<pTaskBlock->ReceiveInfo.lower_limit)
				state=0;
			else if(Data>pTaskBlock->ReceiveInfo.upper_limit)
				state=1;
			else
				state=2;
			if((pTaskBlock->ReceiveInfo.last!=state)||(pTaskBlock->ReceiveInfo.thresholdinit==0))
			{
				if(InitiativeReceive_SendMsg(&pTaskBlock->ReceiveInfo,FUNCID_THRESTRIGGER))
				{
				 pTaskBlock->ReceiveInfo.thresholdinit=1;
				 pTaskBlock->ReceiveInfo.last=state;
				}
			}
		}
  }
	pTaskBlock=pTaskBlock->next;
}


//模块初始化
void InitiativeReceive_TableInit(void)
{
	TimeTaskTypeDef TimeTask;
	InitiativeReceiveTable.head=NULL;
	InitiativeReceiveTable.tail=NULL;
	InitiativeReceiveTable.tablesize=0;
	
	TimeTask.callback=1;                                  //定时器设置
	TimeTask.enable=0x01;
	TimeTask.time_value=1;                 //10ms
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=InitiativeReceive_TimeTask;
	TimeTask_Add(INITIATIVERECEIVE_TIMENUM,&TimeTask);
}
