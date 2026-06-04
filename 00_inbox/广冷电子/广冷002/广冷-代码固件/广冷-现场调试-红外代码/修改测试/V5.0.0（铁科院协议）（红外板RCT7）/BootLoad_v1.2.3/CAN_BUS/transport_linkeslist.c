/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN报文发送任务管理链表模块
*	文件名称 : transport_layer.c
*	版    本 : V1.0
*	说    明 : 1.实现加入发送链表的任务进行管理
*            2.实现发送任务的添加与删除
             3.提供任务运行状态的查询接口
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	

#include "transport_linkeslist.h"

TransportTask_LinkesListTypeDef TransportTaskLinkesList;

void TransportTask_TimeCallBack(uint8_t timenum);

void TransportTask_LinkesListInit(void)
{
	TimeTaskTypeDef TimeTask;
	
	TransportTaskLinkesList.head=NULL;
	TransportTaskLinkesList.tail=NULL;
	TransportTaskLinkesList.linkdelist_len=0;
	
	TimeTask.callback=1;
	TimeTask.enable=0x01;
	TimeTask.time_value=TRANSPORT_CALLBACKTIME; 
	TimeTask.time_mode=0x00;                    //自动复位
	TimeTask.TimeTack_CallBack=TransportTask_TimeCallBack;
	TimeTask_Add(TRANSPORT_CALLBACKTIMENUM,&TimeTask);
}

TransportTaskBlockTypeDef *TransportTask_GetLinkesListHead(void)
{
	return TransportTaskLinkesList.head;
}
TransportTaskBlockTypeDef *TransportTask_GetLinkesListTail(void)
{
	return TransportTaskLinkesList.tail;
}
uint32_t TransportTask_GetLinkesListLen(void)
{
	return TransportTaskLinkesList.linkdelist_len;
}

uint32_t TransportTask_GetLinkesListMaxLen(void)
{
	return TRANSPORT_LINKES_MAXLEN;
}
/*************************************************************
函数：TransportTask_TraverseBlockAddr
功能：查找链表中的任务块
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
TransportTaskBlockTypeDef *TransportTask_TraverseBlockAddr(MsgFilterTypeDef *pTransportTaskFilter) //获取对应任务块的地址
{
	TransportTaskBlockTypeDef  *TaskBlock;
	MsgFilterTypeDef           *TaskFilter;
	TaskBlock=TransportTaskLinkesList.head;
	if(TaskBlock==NULL)             //链表中无数据
		return NULL;	
	while(TaskBlock)
	{
		TaskFilter=&(TaskBlock->TransportTask.TxCanMsg.TransportMsgFilter);
		if((TaskFilter->DestMacID==pTransportTaskFilter->DestMacID)
		   &&(TaskFilter->SourceID==pTransportTaskFilter->SourceID)
	     &&(TaskFilter->SrcMacID==pTransportTaskFilter->SrcMacID)
	     &&(TaskFilter->FuncID==pTransportTaskFilter->FuncID)
	     &&(TaskFilter->Ack==pTransportTaskFilter->Ack))
		{
			return TaskBlock;
		}
		TaskBlock=TaskBlock->next;
	}
	return NULL;
}

/*************************************************************
函数：TransportTask_TraverseTaskAddr
功能：查找链表中的任务块
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
TransportTaskTypeDef *TransportTask_TraverseTaskAddr(MsgFilterTypeDef *pTransportTaskFilter) //获取对应任务块的地址
{
	TransportTaskBlockTypeDef  *pTaskBlock;
	pTaskBlock=TransportTask_TraverseBlockAddr(pTransportTaskFilter);
	if(pTaskBlock==NULL)
		return NULL;
  return &pTaskBlock->TransportTask;
}
/*************************************************************
函数：TransportTask_BlockInit
功能：pTaskBlock 任务块地址
参数：blocknum   任务块编号
返回：无
*************************************************************/
void TransportTask_BlockInit(TransportTaskBlockTypeDef *pTaskBlock)
{
	if(pTaskBlock==NULL)
		return;
	pTaskBlock->TransportTask.TransportTaskManage.ErrNum=0;
	pTaskBlock->TransportTask.TransportTaskManage.OverTimeFlag=0;
	pTaskBlock->TransportTask.TransportTaskManage.OverTimeNum=0;
	pTaskBlock->TransportTask.TransportTaskManage.TimeCount=0;
	pTaskBlock->TransportTask.TransportTaskManage.TransportState=0;
	pTaskBlock->TransportTask.TransportTaskManage.TransportCancel=0;
}
/*************************************************************
函数：TimeTask_AddLinkedList
功能：向链表中增加定时器任务块
参数：pTransportTask 任务块地址
返回：0x00     链表空间满
      0x01     队列中存在相同任务号
      0x02     内存分配失败
      0xFF     增加成功
*************************************************************/
uint8_t TransportTask_AddLinkedList(TransportTaskTypeDef *pTransportTask)
{
	TransportTaskBlockTypeDef *pTaskBlock;
	if(TransportTaskLinkesList.linkdelist_len==TRANSPORT_LINKES_MAXLEN)
		return 0x00;                                                        //空间满
	if(TransportTask_TraverseBlockAddr(&(pTransportTask->TxCanMsg.TransportMsgFilter))!=NULL)
		return 0x01;                                                        //队列中已有相同任务号
  pTaskBlock=Mem_malloc(sizeof(TransportTaskBlockTypeDef));	                                                         
	if(pTaskBlock==NULL)
		return 0x02;                                                        //创建失败
	Mem_copy(&pTaskBlock->TransportTask,pTransportTask,sizeof(TransportTaskTypeDef));
	TransportTask_BlockInit(pTaskBlock);                                                //初始化任务块
	if(TransportTaskLinkesList.head==NULL)                                              //链表为空
	{
		pTaskBlock->next=0;
		pTaskBlock->prior=0;
		TransportTaskLinkesList.head=pTaskBlock;
		TransportTaskLinkesList.tail=pTaskBlock;
		TransportTaskLinkesList.linkdelist_len=1;
	}
	else
	{
		pTaskBlock->next=NULL;
		pTaskBlock->prior=TransportTaskLinkesList.tail;
		TransportTaskLinkesList.tail->next=pTaskBlock;
		TransportTaskLinkesList.tail=pTaskBlock;
		TransportTaskLinkesList.linkdelist_len++;
	}
	return 0xFF;                                //创建成功
}

//void TransportTask_Check(void)
//{
//	TransportTaskBlockTypeDef *pTaskBlock;
//	pTaskBlock=TransportTaskLinkesList.head;
//	while(pTaskBlock)
//	{
//		if(((((uint32_t)pTaskBlock->next&0x20000000)!=0x20000000)&&pTaskBlock->next!=NULL)
//			||((((uint32_t)pTaskBlock->prior&0x20000000)!=0x20000000)&&pTaskBlock->prior!=NULL)
//		  )
//		{
//			pTaskBlock=NULL;
//			return;
//		}
//		pTaskBlock=pTaskBlock->next;
//	}
//}

/*************************************************************
函数：TimeTask_RemoveLinkedList
功能：删除定时器任务块
参数：pTransportTaskFilter 任务块标识符
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/
uint8_t TransportTask_RemoveLinkedList(MsgFilterTypeDef *pTransportTaskFilter)
{
	TransportTaskBlockTypeDef *pTaskBlock;
	pTaskBlock=TransportTask_TraverseBlockAddr(pTransportTaskFilter);
	if(pTaskBlock==NULL)             //链表中无数据
		return 0x00;
	if(pTaskBlock->next==NULL&&pTaskBlock->prior==NULL)
	{ 
		TransportTaskLinkesList.tail=0;
		TransportTaskLinkesList.head=0;
		TransportTaskLinkesList.linkdelist_len=0;
	}
	else if(pTaskBlock->next==NULL)
	{
		TransportTaskLinkesList.tail=pTaskBlock->prior;
		TransportTaskLinkesList.tail->next=0;
		TransportTaskLinkesList.linkdelist_len--;
	}
	else if(pTaskBlock->prior==NULL)
	{
		TransportTaskLinkesList.head=pTaskBlock->next;
		TransportTaskLinkesList.head->prior=0;
		TransportTaskLinkesList.linkdelist_len--;
	}
	else 
	{
		pTaskBlock->prior->next=pTaskBlock->next;
		pTaskBlock->next->prior=pTaskBlock->prior;
    TransportTaskLinkesList.linkdelist_len--;		
	}
  Mem_free(pTaskBlock);
	return 0xFF;  //删除成功
}

/*************************************************************
函数：TransportTask_RemoveTask
功能：删除任务块
参数：pTransportTask 任务地址
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/
uint8_t TransportTask_RemoveTask(TransportTaskTypeDef *pTransportTask)
{
	if(TransportTask_RemoveLinkedList(&pTransportTask->TxCanMsg.TransportMsgFilter)==0x00)
		return 0x00;
	return 0xFF;  //删除成功
}

/*************************************************************
函数：TransportTask_TimeCallBack
功能：定时器回调函数
参数：无
返回无
*************************************************************/

void TransportTask_TimeCallBack(uint8_t timenum)
{
	TransportTaskBlockTypeDef *pTaskBlock;
	TransportTaskManageTypeDef *pTaskManage;
	pTaskBlock=TransportTaskLinkesList.head;
	if(pTaskBlock==NULL)
		return;
	while(pTaskBlock)
	{
		pTaskManage=&pTaskBlock->TransportTask.TransportTaskManage;
		if((pTaskManage->OverTimeFlag==0x00)&&(pTaskManage->TransportState==0x01))//未溢出，且数据已经发送
		  pTaskManage->TimeCount++;
		if(pTaskManage->TimeCount==TRANSPORT_OUTTIME||pTaskManage->TimeCount>TRANSPORT_OUTTIME)
		{
			pTaskManage->OverTimeNum++;                                             //超时次数
			pTaskManage->TimeCount=0;
			if(pTaskManage->OverTimeNum==TRANSPORT_OVERTIMENUM
				 ||pTaskManage->OverTimeNum>TRANSPORT_OVERTIMENUM)
			{
				pTaskManage->OverTimeFlag=0x01;
			}
			else
			{
				pTaskManage->TransportState=0x00;//重新发送
			}
		}
		pTaskBlock=pTaskBlock->next;
	}
}

/*************************************************************
函数：TransportTask_GetOverTimeTask
功能：获取任务中的超时任务
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/

TransportTaskTypeDef  *TransportTask_GetOverTimeTask(void)
{
	TransportTaskBlockTypeDef *pTaskBlock;
	TransportTaskManageTypeDef *pTaskManage;
	
	if(TransportTaskLinkesList.head==NULL)
		return NULL;
	pTaskBlock=TransportTaskLinkesList.head;
	while(pTaskBlock!=NULL)
  {
		pTaskManage=&(pTaskBlock->TransportTask.TransportTaskManage);
		if(pTaskManage->OverTimeFlag==0x01)
			return &(pTaskBlock->TransportTask);                      //返回未发送mag地址
		pTaskBlock=pTaskBlock->next;
	}	
	return NULL;
}

/*************************************************************
函数：TransportTask_GetTransportTask
功能：获取链表中待发送报文任务块
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/

TransportTaskTypeDef  *TransportTask_GetTransportTask(void)
{
	TransportTaskBlockTypeDef *pTaskBlock;
	TransportTaskManageTypeDef *pTaskManage;
	
	if(TransportTaskLinkesList.head==NULL)
		return NULL;
	pTaskBlock=TransportTaskLinkesList.head;
	while(pTaskBlock!=NULL)
  {
		pTaskManage=&(pTaskBlock->TransportTask.TransportTaskManage);
		if(pTaskManage->TransportState==0x00)
			return &(pTaskBlock->TransportTask);                      //返回未发送mag地址
		pTaskBlock=pTaskBlock->next;
	}	
	return NULL;
}



void TransportTask_RemoveAllTask(void)
{
	TransportTaskBlockTypeDef *pTaskBlock,*pTaskBlockNext;
	if(TransportTaskLinkesList.head==NULL)
		return;
	pTaskBlock=TransportTaskLinkesList.head;
	pTaskBlockNext=pTaskBlock->next;
	while(pTaskBlock)
	{
		Mem_free(pTaskBlock->TransportTask.TxCanMsg.TransportMsgData.Data);
		Mem_free(pTaskBlock);
		pTaskBlock=pTaskBlockNext;
		pTaskBlockNext=pTaskBlock->next;	
	}
	TransportTaskLinkesList.head=NULL;
	TransportTaskLinkesList.tail=NULL;
	TransportTaskLinkesList.linkdelist_len=0;
}
