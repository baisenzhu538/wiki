#include "initiative_task.h"

InitiativeTask_LinkesListTypeDef InitiativeTask_LinkesList;//建立链表
InitiativeTask_CallBackTypeDef   InitiativeTask_CallBack;

//复位初始化标志位，更新主机参数表
void InitiativeTask_RenewTable(void)
{
	InitiativeTask_BlockTypeDef   *pInitiativeTask_Block=NULL;
	if(InitiativeTask_LinkesList.head==NULL)
		return;
	pInitiativeTask_Block=InitiativeTask_LinkesList.head;
	while(pInitiativeTask_Block)
	{
		pInitiativeTask_Block->InitiativeTask.TriggerManage.cycleinit=0;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.stateinit=0;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.thresholdinit=0;
		pInitiativeTask_Block=pInitiativeTask_Block->next;
	}
}
/*****************************************
函数：InitiativeTask_SendMsg
功能：发送正常响应
参数：
返回：
******************************************/
uint8_t InitiativeTask_SendMsg(NodeLinkTypeDef *pLink,MsgFilterTypeDef *pFilter,uint8_t funcid)
{
	TransportCanMsgTypeDef MsgBuff;
	uint8_t state=0x00;
	if(pFilter->DestMacID==0x00)
	 MsgBuff.TransportMsgFilter.DestMacID=pLink->MasterMACID;
	else
		MsgBuff.TransportMsgFilter.DestMacID=pFilter->DestMacID;
	if(pFilter->SrcMacID==0x00)
	 MsgBuff.TransportMsgFilter.SrcMacID =pLink->LocalMACID;
	else
	 MsgBuff.TransportMsgFilter.SrcMacID =pFilter->SrcMacID;
	
	MsgBuff.TransportMsgFilter.SourceID =pFilter->SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =funcid;
	if(funcid==FUNCID_CYCLETRIGGER)
	 MsgBuff.TransportMsgFilter.Ack      =0x01;//需等待响应
	else
	 MsgBuff.TransportMsgFilter.Ack      =0x00;
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	

	MsgBuff.TransportMsgData.DataSize   =IndexTable_GetDataLen(pFilter->SourceID);
	
	if(MsgBuff.TransportMsgData.DataSize!=0xFFFF&&MsgBuff.TransportMsgData.DataSize!=0xFFFE)//节点存在
	{
		MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
		IndexTable_ReadData(pFilter->SourceID,MsgBuff.TransportMsgData.Data);
		if(TransportLayer_TxMsg(&MsgBuff)!=0xFF)
			Mem_free(MsgBuff.TransportMsgData.Data);
		else
			state=0xFF;
  }
	return state;
}



void InitiativeTask_LinkesListInit(InitiativeTask_CallBackTypeDef *pInitiativeTask_CallBack)
{
	TimeTaskTypeDef TimeTask;
	InitiativeTask_LinkesList.head=0;
	InitiativeTask_LinkesList.tail=0;
	InitiativeTask_LinkesList.taskstate=0;
	InitiativeTask_LinkesList.linkdelist_len=0;
	InitiativeTask_CallBack.InitiativeTask_CycleCallBack=pInitiativeTask_CallBack->InitiativeTask_CycleCallBack;
	InitiativeTask_CallBack.InitiativeTask_StateCallBack=pInitiativeTask_CallBack->InitiativeTask_StateCallBack;
	InitiativeTask_CallBack.InitiativeTask_ThresholdCallBack=pInitiativeTask_CallBack->InitiativeTask_ThresholdCallBack;
	
	TimeTask.callback=1;                           //初始化定时器
	TimeTask.enable=1;
	TimeTask.time_value=1;                         //10ms定时
	TimeTask.time_mode=0x00;                       //自复位定时器                  
	TimeTask.TimeTack_CallBack=InitiativeTask_TimeRun;
	TimeTask_Add(INITIATIVETASK_TIMENUM,&TimeTask);
}

/*************************************************************
函数：InitiativeTask_TraverseBlockNum
功能：查找链表中的任务块
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
InitiativeTask_BlockTypeDef *InitiativeTask_TraverseBlockNum(MsgFilterTypeDef *pInitiativeTaskFilter) //获取对应任务块的地址
{
	InitiativeTask_BlockTypeDef *pTaskBlock;
	MsgFilterTypeDef            *pTaskFilter;
	if(InitiativeTask_LinkesList.head==NULL)             //链表中无数据
		return NULL;
	pTaskBlock=InitiativeTask_LinkesList.head;
	pTaskFilter=&pTaskBlock->InitiativeTask.InitiativeTaskFilter;
	while(((pTaskFilter->DestMacID!=pInitiativeTaskFilter->DestMacID)
		    ||pTaskFilter->SourceID !=pInitiativeTaskFilter->SourceID
	      ||(pTaskFilter->SrcMacID!=pInitiativeTaskFilter->SrcMacID))
	      &&(pTaskBlock!=NULL))
	{
		pTaskBlock=pTaskBlock->next;
	}
	if(pTaskBlock==NULL)                                         //无对应任务块
		pTaskBlock=NULL;
	else
    return pTaskBlock;
	return pTaskBlock;
}

/*************************************************************
函数：InitiativeTask_AddLinkedList
功能：向链表中增加定时器任务块
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表空间满
      0x01     队列中存在相同任务号
      0x02     内存分配失败
      0xFF     增加成功
*************************************************************/
uint8_t InitiativeTask_AddLinkedList(InitiativeTaskTypeDef *pInitiativeTask)
{
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	if(InitiativeTask_LinkesList.linkdelist_len==INITIATIVETASK_TASKMAXSIZE)
		return 0x00;                                                        //空间满
	if(InitiativeTask_TraverseBlockNum(&pInitiativeTask->InitiativeTaskFilter)!=NULL)
		return 0x01;                                                        //队列中已有相同任务号
  pInitiativeTask_Block=Mem_malloc(sizeof(InitiativeTask_BlockTypeDef));
	if(pInitiativeTask_Block==NULL)
		return 0x02;                              //创建失败
	Mem_copy(&pInitiativeTask_Block->InitiativeTask,pInitiativeTask,sizeof(InitiativeTaskTypeDef));
	if(InitiativeTask_LinkesList.head==NULL)          //链表为空
	{
		pInitiativeTask_Block->next=0;
		pInitiativeTask_Block->prior=0;
		InitiativeTask_LinkesList.head=pInitiativeTask_Block;
		InitiativeTask_LinkesList.tail=pInitiativeTask_Block;
		InitiativeTask_LinkesList.linkdelist_len++;
	}
	else
	{
		pInitiativeTask_Block->next=NULL;
		InitiativeTask_LinkesList.tail->next=pInitiativeTask_Block;
		pInitiativeTask_Block->prior=InitiativeTask_LinkesList.tail;
		InitiativeTask_LinkesList.tail=pInitiativeTask_Block;
		InitiativeTask_LinkesList.linkdelist_len++;
	}
	return 0xFF;                                //创建成功
}

/*************************************************************
函数：InitiativeTask_RemoveLinkedList
功能：删除定时器任务块
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/
uint8_t InitiativeTask_RemoveLinkedList(MsgFilterTypeDef *pInitiativeTaskFilter)
{
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(pInitiativeTaskFilter);
	if(pInitiativeTask_Block==NULL)             //链表中无数据
		return 0x00;
	if((InitiativeTask_LinkesList.linkdelist_len==1)&&(InitiativeTask_LinkesList.head==InitiativeTask_LinkesList.tail))//链表中只存在一个节点，头尾相同
	{ 
		InitiativeTask_LinkesList.tail=0;
		InitiativeTask_LinkesList.head=0;
	}
	else if(pInitiativeTask_Block->next==NULL)//链表中最后一个节点
	{
		InitiativeTask_LinkesList.tail=pInitiativeTask_Block->prior;
		InitiativeTask_LinkesList.tail->next=0;
	}
	else if(pInitiativeTask_Block->prior==NULL)//链表中第一个节点
	{
		InitiativeTask_LinkesList.head=pInitiativeTask_Block->next;
		InitiativeTask_LinkesList.head->prior=0;
	}
	else 
	{
		pInitiativeTask_Block->prior->next=pInitiativeTask_Block->next;
		pInitiativeTask_Block->next->prior=pInitiativeTask_Block->prior;	
	}
	InitiativeTask_LinkesList.linkdelist_len--;
  Mem_free(pInitiativeTask_Block);
	return 0xFF;  //删除成功
}

/*************************************************************
函数：InitiativeTask_RevampLinkedList
功能：修改定时器任务块参数
参数：无
返回：无
*************************************************************/
uint8_t InitiativeTask_RevampLinkedList(InitiativeTaskTypeDef *pInitiativeTask)
{
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(&pInitiativeTask->InitiativeTaskFilter);
	if(pInitiativeTask_Block==NULL)             //链表中无数据
	  return 0x00;
	Mem_copy(&pInitiativeTask_Block->InitiativeTask,pInitiativeTask,sizeof(InitiativeTaskTypeDef));
	return 0xFF;
}

/*************************************************************
函数：InitiativeTask_TimeRun
功能：定时器回调任务函数
参数：timetasknum 定时器任务参数
返回：
*************************************************************/
void InitiativeTask_TimeRun(uint8_t timetasknum)
{
	InitiativeTask_BlockTypeDef  *pTaskBlock;
	TriggerManageTypeDef         *pTriggermanage;
	pTaskBlock=InitiativeTask_LinkesList.head;
	if(pTaskBlock==NULL||InitiativeTask_LinkesList.taskstate==0x00)//链表中无任务或者任务终止
		return;
	while(pTaskBlock)
	{ 
		pTriggermanage=&pTaskBlock->InitiativeTask.TriggerManage;
    if((pTriggermanage->cycle_enable==0x01)&&(pTriggermanage->overtimeflag==0x00))
		{
			pTriggermanage->timecount++;
			if(pTriggermanage->timecount==pTriggermanage->time)
			{
				pTriggermanage->overtimeflag=0x01;
				pTriggermanage->timecount=0;                        //清除定时值
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
void InitiativeTask_TaskRun(NodeLinkTypeDef *pLinkManage)
{
	static InitiativeTask_BlockTypeDef   *pInitiativeTask_Block=NULL;
	MsgFilterTypeDef                     *pTaskFilter;
	TriggerManageTypeDef                 *pTriggerManage;
	if(pLinkManage->ConnectFlag==0x00)        //未连接返回
	{
		InitiativeTask_LinkesList.taskstate=0x00;//任务终止
		return;
	}
	InitiativeTask_LinkesList.taskstate=0x01;//任务进行中
	if(InitiativeTask_LinkesList.head==NULL)
	{
		pInitiativeTask_Block=NULL;
		return;
	}
	if(pInitiativeTask_Block==NULL)
		pInitiativeTask_Block=InitiativeTask_LinkesList.head;
	
	pTaskFilter=&pInitiativeTask_Block->InitiativeTask.InitiativeTaskFilter;
	pTriggerManage=&pInitiativeTask_Block->InitiativeTask.TriggerManage;
	if(pTriggerManage->cycle_enable==0x01)
	{
		if(pTriggerManage->overtimeflag==0x01||pTriggerManage->cycleinit==0)
		{
		 pTriggerManage->cycleinit=1;
		 pTriggerManage->overtimeflag=0x00;
		 InitiativeTask_SendMsg(pLinkManage,pTaskFilter,FUNCID_CYCLETRIGGER);
		}
	}
	if(pTriggerManage->state_enable)
	{
		uint32_t sourcedata=0x00000000;
		IndexTable_ReadData(pTaskFilter->SourceID,&sourcedata);
		if((pTriggerManage->last!=sourcedata)||(pTriggerManage->stateinit==0))//触发或者未初始化
		{
			if(InitiativeTask_SendMsg(pLinkManage,pTaskFilter,FUNCID_STATETRIGGER))
			{
			 pTriggerManage->stateinit=1;                                        //完成初始化
			 pTriggerManage->last=sourcedata;
			}
		}		  
	}
	else if(pTriggerManage->threshold_enable)
	{
		uint32_t sourcedata=0x00000000;
		uint8_t  state=0x00;
		IndexTable_ReadData(pTaskFilter->SourceID,&sourcedata);
		if(sourcedata<pTriggerManage->lower_limit)
		  state=0;
		else if(sourcedata>pTriggerManage->upper_limit)
			state=1;
		else
			state=2;
		if((state!=pTriggerManage->last)||(pTriggerManage->thresholdinit==0))
		{
		 if(InitiativeTask_SendMsg(pLinkManage,pTaskFilter,FUNCID_THRESTRIGGER))
		 {
			pTriggerManage->thresholdinit=1;                                    //完成初始化
		  pTriggerManage->last=state;
		 }
		}
	}
		pInitiativeTask_Block=pInitiativeTask_Block->next;
}
/*以下为外部应用调用接口函数*/

uint8_t InitiativeTask_Add(InitiativeTaskTypeDef *pInitiativeTask)
{
	uint8_t return_state;
	return_state=InitiativeTask_AddLinkedList(pInitiativeTask);
	return return_state;
}


uint8_t InitiativeTask_Remove(MsgFilterTypeDef *pInitiativeTaskFilter)
{
	uint8_t return_state;
  return_state=InitiativeTask_RemoveLinkedList(pInitiativeTaskFilter);
	return return_state;
}


InitiativeTask_BlockTypeDef *InitiativeTask_GetAddr(MsgFilterTypeDef *pInitiativeTaskFilter)
{
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(pInitiativeTaskFilter);
	return pInitiativeTask_Block;
}

/*************************************************************
函数：InitiativeTask_UpdataLast
功能：更新触发任务的Last值
参数：SourceID 触发索引地址
      time     定时时间10ms单位
返回：
*************************************************************/
void InitiativeTask_UpdataLast(uint8_t SourceID)
{
	InitiativeTaskTypeDef InitiativeTask;
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	InitiativeTask.InitiativeTaskFilter.DestMacID=0x00;
  InitiativeTask.InitiativeTaskFilter.SrcMacID=0x00;
	InitiativeTask.InitiativeTaskFilter.FuncID  =0x00;//定时触发报文
  InitiativeTask.InitiativeTaskFilter.SourceID=SourceID;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(&InitiativeTask.InitiativeTaskFilter);
	if(pInitiativeTask_Block!=NULL)//触发链表中没有该节点的触发任务
	{
	 IndexTable_ReadData(SourceID,&pInitiativeTask_Block->InitiativeTask.TriggerManage.last);
	}
}

/*************************************************************
函数：InitiativeTask_SetCycle
功能：设置定时触发任务
参数：SourceID 触发索引地址
      time     定时时间10ms单位
返回：
*************************************************************/
uint8_t InitiativeTask_SetCycle(uint8_t SourceID,uint16_t time)
{
	InitiativeTaskTypeDef InitiativeTask;
	uint8_t state;
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	InitiativeTask.InitiativeTaskFilter.DestMacID=0x00;
  InitiativeTask.InitiativeTaskFilter.SrcMacID=0x00;
	InitiativeTask.InitiativeTaskFilter.FuncID  =FUNCID_CYCLETRIGGER;//定时触发报文
  InitiativeTask.InitiativeTaskFilter.SourceID=SourceID;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(&InitiativeTask.InitiativeTaskFilter);
	if(pInitiativeTask_Block==NULL)//触发链表中没有该节点的触发任务
	{
		InitiativeTask.TriggerManage.state_enable=0;
	  InitiativeTask.TriggerManage.threshold_enable=0;
		InitiativeTask.TriggerManage.cycle_enable=1;
		InitiativeTask.TriggerManage.overtimeflag=0;
		InitiativeTask.TriggerManage.cycleinit=0;//未初始化
		InitiativeTask.TriggerManage.time=time;
		InitiativeTask.TriggerManage.timecount=0;
		state=InitiativeTask_Add(&InitiativeTask);
	}
	else
	{
		pInitiativeTask_Block->InitiativeTask.TriggerManage .cycleinit=0;//未初始化
		pInitiativeTask_Block->InitiativeTask.TriggerManage.cycle_enable=1;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.overtimeflag=0;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.time=time;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.timecount=0;
		return 0xFF;
	}
	return state;
}
/*************************************************************
函数：InitiativeTask_SetThreshold
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
uint8_t InitiativeTask_SetThreshold(uint8_t SourceID,uint32_t low,uint32_t up)
{
	InitiativeTaskTypeDef InitiativeTask;
	uint8_t state;
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	InitiativeTask.InitiativeTaskFilter.DestMacID=0x00;
  InitiativeTask.InitiativeTaskFilter.SrcMacID=0x00;
	InitiativeTask.InitiativeTaskFilter.FuncID  =FUNCID_THRESTRIGGER;//阀值触发报文
  InitiativeTask.InitiativeTaskFilter.SourceID=SourceID;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(&InitiativeTask.InitiativeTaskFilter);
	if(pInitiativeTask_Block==NULL)//触发链表中没有该节点的触发任务
	{
		InitiativeTask.TriggerManage.state_enable=0;
	  InitiativeTask.TriggerManage.cycle_enable=0;
		InitiativeTask.TriggerManage.threshold_enable=1;
		InitiativeTask.TriggerManage.last=0;
		InitiativeTask.TriggerManage.thresholdinit=0;//未初始化
		InitiativeTask.TriggerManage.lower_limit=low;
		InitiativeTask.TriggerManage.upper_limit=up;
		state=InitiativeTask_Add(&InitiativeTask);
	}
	else
	{
		pInitiativeTask_Block->InitiativeTask.TriggerManage .thresholdinit=0;//未初始化
		pInitiativeTask_Block->InitiativeTask.TriggerManage.threshold_enable=1;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.last=0;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.lower_limit=low;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.upper_limit=up;
		return 0xFF;
	}
	return state;
}

/*************************************************************
函数：InitiativeTask_SetState
功能：设置状态触发任务
参数：SourceID 触发索引地址
返回：
*************************************************************/

uint8_t InitiativeTask_SetState(uint8_t SourceID)
{
	InitiativeTaskTypeDef InitiativeTask;
	uint8_t state;
	InitiativeTask_BlockTypeDef *pInitiativeTask_Block;
	InitiativeTask.InitiativeTaskFilter.DestMacID=0x00;
  InitiativeTask.InitiativeTaskFilter.SrcMacID=0x00;
	InitiativeTask.InitiativeTaskFilter.FuncID  =FUNCID_STATETRIGGER;//状态触发报文
  InitiativeTask.InitiativeTaskFilter.SourceID=SourceID;
	pInitiativeTask_Block=InitiativeTask_TraverseBlockNum(&InitiativeTask.InitiativeTaskFilter);
	if(pInitiativeTask_Block==NULL)                              //触发链表中没有该节点的触发任务
	{
		InitiativeTask.TriggerManage.cycle_enable=0;
		InitiativeTask.TriggerManage.threshold_enable=0;
		InitiativeTask.TriggerManage.state_enable=1;
		InitiativeTask.TriggerManage.last=0;
		InitiativeTask.TriggerManage.stateinit=0;//未初始化
		state=InitiativeTask_Add(&InitiativeTask);
	}
	else
	{
		pInitiativeTask_Block->InitiativeTask.TriggerManage .stateinit=0;//未初始化
		pInitiativeTask_Block->InitiativeTask.TriggerManage.state_enable=1;
		pInitiativeTask_Block->InitiativeTask.TriggerManage.last=0;
		return 0xFF;
	}
	return state;
}

void InitiativeTask_RestInitFlag(void)
{
	InitiativeTask_BlockTypeDef *pTaskBlock;
	pTaskBlock=InitiativeTask_LinkesList.head;
	while(pTaskBlock)
	{
		pTaskBlock->InitiativeTask.TriggerManage.cycleinit=0;
		pTaskBlock->InitiativeTask.TriggerManage.stateinit=0;
		pTaskBlock->InitiativeTask.TriggerManage.thresholdinit=0;
		pTaskBlock=pTaskBlock->next;
	}
}




