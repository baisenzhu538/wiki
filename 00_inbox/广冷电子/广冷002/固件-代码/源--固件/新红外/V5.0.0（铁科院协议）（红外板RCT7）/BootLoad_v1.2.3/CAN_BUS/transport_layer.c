/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN协议栈数据传输层
*	文件名称 : transport_layer.c
*	版    本 : V1.0
*	说    明 : 1.实现CAN驱动层与协议层的数据交换与转换
*            2.实现CAN传输报文的任务管理
*            3.实现分段报文分拆的发送与接收组合
*						 4.实现传输错误回调协议层函数
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "transport_layer.h"
SectionMsgTypeDef RX_SectionMsgBuff[RX_SECTIONMSG_BUFFSIZE];//创建分段接收缓存
void (*Transport_Section)(MsgFilterTypeDef *)=NULL;

/*************************************************************
函数：TransportLayer_EnableTimeTask
功能：启动指定定时器
参数：无
返回：无
*************************************************************/
void TransportLayer_EnableTimeTask(uint8_t timenum)
{
 TimeTask_Cmd(timenum,0x01);
 TimeTask_RestCount(timenum);
}
/*************************************************************
函数：TransportLayer_DisableTimeTask
功能：关闭指定定时器
参数：无
返回：无
*************************************************************/
void TransportLayer_DisableTimeTask(uint8_t timenum)
{
	TimeTask_Cmd(timenum,0x00);
	TimeTask_ReadOverflowFlag(timenum);
	TimeTask_RestCount(timenum);
}
/*************************************************************
函数：TransportLayer_RxFirstSection
功能：分段数据无分段处理函数
参数：无
返回：无
*************************************************************/
void TransportLayer_RestTimeTask(uint8_t timenum)
{
 TimeTask_ReadOverflowFlag(timenum);
 TimeTask_RestCount(timenum);
}
/*************************************************************
函数：TransportLayer_RxFirstSection
功能：分段数据无分段处理函数
参数：无
返回：无
*************************************************************/
void TransportLayer_TimeTaskCallBack(uint8_t timenum)
{
	uint8_t i_buffnum;
	for(i_buffnum=0;i_buffnum<RX_SECTIONMSG_BUFFSIZE;i_buffnum++)
	{
		if(i_buffnum==timenum)
		{
     if(Transport_Section!=NULL)
      (*Transport_Section)(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter);//调用回调函数			
		 RX_SectionMsgBuff[i_buffnum].state=0;   
		 TransportLayer_DisableTimeTask(timenum);//关闭定时器
		}
	}
}

void TransportLayer_TimeTaskInit(void)
{
	TimeTaskTypeDef TimeTask;
	uint8_t i_timenum;
	TimeTask.callback=1;  //回调
	TimeTask.time_value=5;//50ms定时
	TimeTask.enable=0;    //使能
	TimeTask.time_mode=TIMEMODE_NONAUTOREST;
	TimeTask.TimeTack_CallBack=TransportLayer_TimeTaskCallBack;
	for(i_timenum=0;i_timenum<RX_SECTIONMSG_BUFFSIZE;i_timenum++)
	 TimeTask_Add(i_timenum,&TimeTask);//初始化接收队列
}


void TransportLayer_Init(void (*p)(MsgFilterTypeDef *))
{
	Transport_Section=p;            //设置回调函数
	TransportLayer_TimeTaskInit();  //初始化定时器任务
	TransportTask_LinkesListInit(); //初始化发送链表
	MsgQueue_Init(); 
}
/*************************************************************
函数：TransportLayer_RxFirstSection
功能：分段数据无分段处理函数
参数：无
返回：无
*************************************************************/
static void TransportLayer_RxNonSection(CanMsgTypeDef *pMsg)
{
	TransportCanMsgTypeDef Msg;
	
	MEM_COPY_FOURBYTE(&Msg.TransportMsgFilter,&pMsg->MsgFilter);//赋值报文ID
	MEM_COPY_FOURBYTE(&Msg.TransportMsgManage,&pMsg->MsgManage);//赋值报文管理标志
	
	Msg.TransportMsgData.DataSize   =pMsg->MsgData.DataSize;
	Msg.TransportMsgData.Data       =(uint8_t*)Mem_malloc(Msg.TransportMsgData.DataSize);
	if((Msg.TransportMsgData.Data!=NULL)||(Msg.TransportMsgData.DataSize==0x00))//空间不足丢弃该数据
	{
	 Mem_copy(Msg.TransportMsgData.Data,pMsg->MsgData.Data,Msg.TransportMsgData.DataSize);//发送系统忙标志
	 if(MsgQueue_AddRxMsg(&Msg)==MSG_QUEUE_FULL)//加入失败
	 {
		if(Msg.TransportMsgData.DataSize!=0x00)
		 Mem_free(Msg.TransportMsgData.Data);
	 }
	}
	
}
/*************************************************************
函数：TransportLayer_RxFirstSection
功能：分段数据第一分段处理函数
参数：无
返回：无
*************************************************************/
static void TransportLayer_RxFirstSection(CanMsgTypeDef *pMsg)
{
	uint8_t i_buffnum;
	for(i_buffnum=0;i_buffnum<RX_SECTIONMSG_BUFFSIZE;i_buffnum++)
	{
		if(RX_SectionMsgBuff[i_buffnum].state==STATE_SECTIONMSG_BUFFFREE)
		{
			TransportLayer_EnableTimeTask(i_buffnum);                        //开启超时检测
			RX_SectionMsgBuff[i_buffnum].state=STATE_SECTIONMSG_BUFFOCCUPY;
			
			MEM_COPY_FOURBYTE(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter,&pMsg->MsgFilter);//赋值报文ID
			
			RX_SectionMsgBuff[i_buffnum].DataSize =pMsg->MsgData.DataSize;
			Mem_copy(RX_SectionMsgBuff[i_buffnum].Data,pMsg->MsgData.Data,pMsg->MsgData.DataSize);
			
			RX_SectionMsgBuff[i_buffnum].SegNum=0;
			RX_SectionMsgBuff[i_buffnum].SegNum++;
			return;
		}
	}
}
/*************************************************************
函数：TransportLayer_RxMiddleSection
功能：分段数据中间分段处理函数
参数：无
返回：无
*************************************************************/
static void TransportLayer_RxMiddleSection(CanMsgTypeDef *pMsg)
{
	uint8_t i_buffnum;
	for(i_buffnum=0;i_buffnum<RX_SECTIONMSG_BUFFSIZE;i_buffnum++)
	{
		if(RX_SectionMsgBuff[i_buffnum].state==STATE_SECTIONMSG_BUFFOCCUPY)
		{
			if(*((uint32_t*)(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter))
				    ==*((uint32_t*)(&pMsg->MsgFilter)))
			{
				if(RX_SectionMsgBuff[i_buffnum].SegNum==pMsg->MsgManage.SegNum) //校验分段号
				{
				 TransportLayer_RestTimeTask(i_buffnum);               //复位计时器
				 Mem_copy((RX_SectionMsgBuff[i_buffnum].Data+RX_SectionMsgBuff[i_buffnum].DataSize),pMsg->MsgData.Data,pMsg->MsgData.DataSize);
				 RX_SectionMsgBuff[i_buffnum].DataSize+=pMsg->MsgData.DataSize;
				 RX_SectionMsgBuff[i_buffnum].SegNum++;
				}
				else//分段传输出错，调用回调函数并释放相应缓存
				{
					if(Transport_Section!=NULL)
					(*Transport_Section)(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter); /*此处调用回调函数*/
					TransportLayer_DisableTimeTask(i_buffnum);                            //关闭相应超时定时器
					RX_SectionMsgBuff[i_buffnum].state=STATE_SECTIONMSG_BUFFFREE;         //释放缓存
				}
			}
		}
	}
}
/*************************************************************
函数：TransportLayer_RxLastSection
功能：分段数据最后分段处理函数
参数：无
返回：无
*************************************************************/
static void TransportLayer_RxLastSection(CanMsgTypeDef *pMsg)
{
	TransportCanMsgTypeDef Msg;
	uint8_t i_buffnum;
	for(i_buffnum=0;i_buffnum<RX_SECTIONMSG_BUFFSIZE;i_buffnum++)
	{
		if(RX_SectionMsgBuff[i_buffnum].state==STATE_SECTIONMSG_BUFFOCCUPY)
		{
			if(*((uint32_t*)(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter))
				    ==*((uint32_t*)(&pMsg->MsgFilter)))
			{
				if(RX_SectionMsgBuff[i_buffnum].SegNum==pMsg->MsgManage.SegNum) //校验分段号
				{
					TransportLayer_DisableTimeTask(i_buffnum);                   //关闭超时检测	
					Mem_copy((RX_SectionMsgBuff[i_buffnum].Data+RX_SectionMsgBuff[i_buffnum].DataSize),pMsg->MsgData.Data,pMsg->MsgData.DataSize);//复制数据
					
					RX_SectionMsgBuff[i_buffnum].DataSize+=pMsg->MsgData.DataSize;
					
					MEM_COPY_FOURBYTE(&Msg.TransportMsgFilter,&pMsg->MsgFilter);//赋值报文ID
          MEM_COPY_FOURBYTE(&Msg.TransportMsgManage,&pMsg->MsgManage);
					
					Msg.TransportMsgData.DataSize =RX_SectionMsgBuff[i_buffnum].DataSize;
					Msg.TransportMsgData.Data     =(uint8_t*)Mem_malloc(Msg.TransportMsgData.DataSize);
					if(Msg.TransportMsgData.Data!=NULL)//空间不足丢弃该报文
					{
					 Mem_copy(Msg.TransportMsgData.Data,RX_SectionMsgBuff[i_buffnum].Data,Msg.TransportMsgData.DataSize);
					 if(MsgQueue_AddRxMsg(&Msg)==MSG_QUEUE_FULL)//加入失败释放内存
					 {
						 Mem_free(Msg.TransportMsgData.Data);
					 }
					}
					RX_SectionMsgBuff[i_buffnum].state=STATE_SECTIONMSG_BUFFFREE;//释放分段传输缓存
				}
				else
				{
					if(Transport_Section!=NULL)
					(*Transport_Section)(&RX_SectionMsgBuff[i_buffnum].SectionMsgFilter);/*此处调用回调函数*/
					RX_SectionMsgBuff[i_buffnum].state=STATE_SECTIONMSG_BUFFFREE;//释放缓存
				}
			}
		}
	}
}

/*************************************************************
函数：TransportLayer_ReceiveQueue
功能：与驱动层对接接口函数
参数：无
返回：无
*************************************************************/
void TransportLayer_ReceiveQueue(CanMsgTypeDef *pMsg)
{
	switch(pMsg->MsgManage.SegPolo)
	{
		case MSG_RX_NONSECTION:
			TransportLayer_RxNonSection(pMsg);
		break;
		case MSG_RX_FIRSTSECTION:
			TransportLayer_RxFirstSection(pMsg);
			break;
		case MSG_RX_MIDDLESECTION:
			TransportLayer_RxMiddleSection(pMsg);
			break;
		case MSG_RX_LASTSECTION:
			TransportLayer_RxLastSection(pMsg);
			break;
		default:break;
	}
}

uint8_t TransportLayer_RxMsg(TransportCanMsgTypeDef *pMsgBuff)
{
	if(MsgQueue_GetRxMsg(pMsgBuff)==MSG_QUEUE_GET)
	 return 0xFF;
	return 0x00;
}


/*发送操作模块*/
static CanMsgTypeDef CanMsgBuff;
static TransportTaskTypeDef  *pTransportTask;
static TxTaskManageTypeDef TxTaskManage={
	                                       MSG_TX_GETQUEUE,
	                                       TX_SECTION_GETMSG,
	                                       TX_SING_GETMSG,
	                                       NULL
                                        };

static void TransportLayer_TxBuffInit(void)
{
	CanMsgBuff.MsgManage.SegPolo=0x00;
	CanMsgBuff.MsgData.DataSize =0x00;
	CanMsgBuff.MsgManage.ErrID  =0x00;
	CanMsgBuff.MsgManage .ErrFunc =0x00;
	CanMsgBuff.MsgManage.SegNum =0x00;
	CanMsgBuff.MsgManage.SegPolo=0x00;
}

uint8_t TransportLayer_TxMsg(TransportCanMsgTypeDef *pMsgBuff)
{
	TransportTaskTypeDef TransportTask;
	Mem_copy(&TransportTask.TxCanMsg,pMsgBuff,sizeof(TransportCanMsgTypeDef));
	if(TransportTask_AddLinkedList(&TransportTask)==0xFF)
	 return 0xFF;
	
	return 0x00;
}
/*************************************************************
函数：TransportLayer_TxNonSection
功能：无分段发送报文处理
参数：pMsgBuff
返回：无
*************************************************************/
static uint8_t TransportLayer_TxNonSection(TransportCanMsgTypeDef *pMsgBuff)
{
	if(TxTaskManage.TxSingleState==TX_SING_FINNISH)
		TxTaskManage.TxSingleState=TX_SING_GETMSG;
  switch(TxTaskManage.TxSingleState)
	{
		case TX_SING_GETMSG:
		  MEM_COPY_FOURBYTE(&CanMsgBuff.MsgManage,&pMsgBuff->TransportMsgManage);
		  MEM_COPY_FOURBYTE(&CanMsgBuff.MsgFilter,&pMsgBuff->TransportMsgFilter);
		
//			Mem_copy(&CanMsgBuff.MsgFilter,&pMsgBuff->TransportMsgFilter,sizeof(MsgFilterTypeDef));
//		  Mem_copy(&CanMsgBuff.MsgManage,&pMsgBuff->TransportMsgManage,sizeof(MsgManageTypeDef));
		
		  CanMsgBuff.MsgManage.SegNum=0x00;
		  CanMsgBuff.MsgManage.SegPolo=0x00;
		  Mem_copy(CanMsgBuff.MsgData.Data,pMsgBuff->TransportMsgData.Data,pMsgBuff->TransportMsgData.DataSize);
		  CanMsgBuff.MsgData.DataSize=pMsgBuff->TransportMsgData.DataSize;
		
		  TxTaskManage.TxSingleState=TX_SING_SEND;
			break;
		case TX_SING_SEND:
			if(Can_SendMsag(&CanMsgBuff)==0xFF)
				TxTaskManage.TxSingleState=TX_SING_FINNISH;
			break;
			default:break;
	}
  return TxTaskManage.TxSingleState;
}

/*************************************************************
函数：TransportLayer_TxSection
功能：分段发送报文
参数：pMsgBuff
返回：无
*************************************************************/
static uint8_t TransportLayer_TxSection(TransportCanMsgTypeDef *pMsgBuff)
{
	static uint16_t datalen,datalenbuf;
	if(TxTaskManage.TxSectionState==TX_SECTION_FINISH)
		TxTaskManage.TxSectionState=TX_SECTION_GETMSG;
  switch(TxTaskManage.TxSectionState)
	{
		case TX_SECTION_GETMSG:
		  MEM_COPY_FOURBYTE(&CanMsgBuff.MsgFilter,&pMsgBuff->TransportMsgFilter);
		  MEM_COPY_FOURBYTE(&CanMsgBuff.MsgManage,&pMsgBuff->TransportMsgManage);
//			Mem_copy(&CanMsgBuff.MsgFilter,&pMsgBuff->TransportMsgFilter,sizeof(MsgFilterTypeDef));
//		  Mem_copy(&CanMsgBuff.MsgManage,&pMsgBuff->TransportMsgManage,sizeof(MsgManageTypeDef));
		
		  datalen=pMsgBuff->TransportMsgData.DataSize;
		  datalenbuf=pMsgBuff->TransportMsgData.DataSize;
		  CanMsgBuff.MsgManage.SegPolo=0x00;
	    CanMsgBuff.MsgManage.SegNum =0x00;
      TxTaskManage.TxSectionState=TX_SECTION_CONVERT;
			break;
		case TX_SECTION_CONVERT:
			if(datalen>MSG_MAXBYTESIZE)
			{
			 Mem_copy(CanMsgBuff.MsgData.Data,pMsgBuff->TransportMsgData.Data+(datalenbuf-datalen),MSG_MAXBYTESIZE);
		   CanMsgBuff.MsgData.DataSize=MSG_MAXBYTESIZE;
			 if(CanMsgBuff.MsgManage.SegPolo==0x00)
				 CanMsgBuff.MsgManage.SegPolo=0x01;//第一分段
			 else
			   CanMsgBuff.MsgManage.SegPolo=0x02;  //中间分段
			 datalen-=7;
			 TxTaskManage.TxSectionState=TX_SECTION_MIDDLE;
			}
		  else
			{
			 Mem_copy(CanMsgBuff.MsgData.Data,pMsgBuff->TransportMsgData.Data+(datalenbuf-datalen),datalen);
		   CanMsgBuff.MsgData.DataSize=datalen;
			 CanMsgBuff.MsgManage.SegPolo=0x03;  //最后分段
			 TxTaskManage.TxSectionState=TX_SECTION_LAST;
			}
			break;
		case TX_SECTION_MIDDLE:
			if(Can_SendMsag(&CanMsgBuff)==0xFF)
			{
				TxTaskManage.TxSectionState=TX_SECTION_CONVERT;
				CanMsgBuff.MsgManage.SegNum++;
			}
			break;
		case TX_SECTION_LAST:
			if(Can_SendMsag(&CanMsgBuff)==0xFF)
				TxTaskManage.TxSectionState=TX_SECTION_FINISH;
			break;
			default:break;
	}
  return TxTaskManage.TxSectionState;
}

static void TransportLayer_Receive(void)
{
 Can_Receive();
}
/*************************************************************
函数：TransportLayer_SendQueue
功能：驱动传输层数据发送
参数：无
返回：无
*************************************************************/
static void TransportLayer_SendQueue(void)
{
	switch(TxTaskManage.TaskState)
	{
		case MSG_TX_GETQUEUE:
      pTransportTask=TransportTask_GetTransportTask();
		  if(pTransportTask!=NULL)
			{
				if(TransportTask_GetTxMsgDataLen(pTransportTask)>MSG_MAXBYTESIZE)
					TxTaskManage.TaskState=MSG_TX_SECTION;
				else
					TxTaskManage.TaskState=MSG_TX_NONSECTION;
			}
			break;
		case MSG_TX_NONSECTION:
			if(TransportTask_GetTxMsgCancel(pTransportTask)==0x00)            //检查是否取消传输
			{
				if(TransportLayer_TxNonSection(&pTransportTask->TxCanMsg)==0xFF)
				 TxTaskManage.TaskState=MSG_TX_FINISH;
			}
			else if(TransportTask_GetTxMsgCancel(pTransportTask)==0x01) //取消发送
			 TxTaskManage.TaskState=MSG_TX_FREEMEM;
			else if(TransportTask_GetTxMsgCancel(pTransportTask)==0x02) //重新发送,返回状态1，重新获取数据包
			{
				TransportTask_ResetTxMsgReSend(pTransportTask);
				TransportLayer_TxBuffInit();
				TxTaskManage.TaskState=MSG_TX_GETQUEUE;
			}
			
			break;
		case MSG_TX_SECTION:
			
			if(TransportTask_GetTxMsgCancel(pTransportTask)==0x00)
			{
				if(TransportLayer_TxSection(&pTransportTask->TxCanMsg)==0xFF)
				 TxTaskManage.TaskState=MSG_TX_FINISH;
			}
			else if(TransportTask_GetTxMsgCancel(pTransportTask)==0x01) //取消发送
       TxTaskManage.TaskState=MSG_TX_FREEMEM;
			else if(TransportTask_GetTxMsgCancel(pTransportTask)==0x02) //重新发送,返回状态1，重新获取数据包
			{
				TransportTask_ResetTxMsgReSend(pTransportTask);
				TransportLayer_TxBuffInit();
				TxTaskManage.TaskState=MSG_TX_GETQUEUE;
			}
			
			break;
		case MSG_TX_FINISH:
			if(TransportTask_GetTxMsgAsk(pTransportTask)==0x00)           //检测是否需要响应
			{
		   TransportLayer_TxBuffInit();//初始化buff
       TransportTask_SetTxMsgState(pTransportTask);            //修改传输完成标志
		   TxTaskManage.TaskState=MSG_TX_GETQUEUE;
			}
			else
				TxTaskManage.TaskState=MSG_TX_FREEMEM;
			break;
		case MSG_TX_FREEMEM:
      if(TransportTask_GetTxMsgDataLen(pTransportTask)!=0)			//清除该传输任务并释放内存空间
			 Mem_free(TransportTask_GetTxMsgDataAddr(pTransportTask));
		  TransportLayer_TxBuffInit();
		  TransportTask_RemoveTask(pTransportTask);
		  TxTaskManage.TaskState=MSG_TX_GETQUEUE;
			break;
		default:break;
	}
}

void TransportLayer_CancelAllSend(void)
{
	TransportTask_RemoveAllTask();       //删除所有传输任务和发送任务
	TxTaskManage.pTransportTask=NULL;
	TxTaskManage.TaskState=MSG_TX_GETQUEUE;
	TxTaskManage.TxSectionState=TX_SECTION_GETMSG;
	TxTaskManage.TxSingleState=TX_SING_GETMSG;
}
void TransportLayer_TaskRun(void)
{
	TransportLayer_Receive();
	TransportLayer_SendQueue();
}
