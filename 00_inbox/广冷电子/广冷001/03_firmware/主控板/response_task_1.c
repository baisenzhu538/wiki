/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 报文响应管理模块
*	文件名称 : response_task.c
*	版    本 : V1.0
*	说    明 : 1.实现内存的动态管理
*            2.实现内存的分配释放
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/

#include "response_task.h"

void (*ResponeTask_AskCallBack)(TransportCanMsgTypeDef *pRxMsg);
void (*ResponeTask_ExceptionsCallBack)(TransportTaskTypeDef *pTransportTask,uint8_t);

void ResponseTask_SetAskCallBack(void(*pCallBack)(TransportCanMsgTypeDef *pRxMsg))
{
	ResponeTask_AskCallBack=pCallBack;
}
void ResponseTask_SetExceptionsCallBack(void(*pCallBack)(TransportTaskTypeDef *pTransportTask,uint8_t))
{
	ResponeTask_ExceptionsCallBack=pCallBack;
}

void ResponseTask_TaskRun(NodeLinkTypeDef *pLink)
{
	TransportTaskTypeDef *pTransportTask;
	pTransportTask=TransportTask_GetOverTimeTask();
	if(pTransportTask!=NULL)
	{
		if(ResponeTask_ExceptionsCallBack!=NULL)
		 (*ResponeTask_ExceptionsCallBack)(pTransportTask,ERRID_ASKOVERTIME);          //超时调用回调,传递超时错误码
		if(TransportTask_GetTxMsgDataLen(pTransportTask)!=0)
		 Mem_free(TransportTask_GetTxMsgDataAddr(pTransportTask));                      //释放内存
		TransportTask_RemoveTask(pTransportTask);                                      //释放内存
	}
}

void ResponseTask_MsgParsing(TransportCanMsgTypeDef  *pRxMsg)
{
	MsgFilterTypeDef TaskFilter;
  TransportTaskTypeDef *pTransportTask;
	
	TaskFilter.DestMacID=pRxMsg->TransportMsgFilter.SrcMacID;
	TaskFilter.SrcMacID =pRxMsg->TransportMsgFilter.DestMacID;
	TaskFilter.SourceID =pRxMsg->TransportMsgFilter.SourceID;
	TaskFilter.Ack      =0x00;
	if(pRxMsg->TransportMsgFilter.FuncID!=FUNCID_EXCEPTIONS)//非异常响应报文
	{
		TaskFilter.FuncID=pRxMsg->TransportMsgFilter.FuncID;  //查找相应响应任务
		pTransportTask=TransportTask_TraverseTaskAddr(&TaskFilter);
		if(pTransportTask==NULL)
		{
			if(pRxMsg->TransportMsgData.DataSize !=0)
			 Mem_free(pRxMsg->TransportMsgData.Data);
			return;
		}
		if(ResponeTask_AskCallBack!=NULL)          //执行了回调函数需要在函数中释放内存，此处不在操作
			(*ResponeTask_AskCallBack)(pRxMsg);      //调用回调
		else if(pRxMsg->TransportMsgData.DataSize!=0)
			Mem_free(pRxMsg->TransportMsgData.Data);
		if(TransportTask_GetTxMsgDataLen(pTransportTask)!=0)//确认响应任务是否申请了报文空间
		 Mem_free(TransportTask_GetTxMsgDataAddr(pTransportTask));
		
	  TransportTask_RemoveTask(pTransportTask);  //执行回调函数并删除传输任务
		return;
	}
	else
	{
		TaskFilter.FuncID   =pRxMsg->TransportMsgManage.ErrFunc; //查找相应响应任务
		pTransportTask=TransportTask_TraverseTaskAddr(&TaskFilter);
		if(pTransportTask==NULL)
		{
			if(pRxMsg->TransportMsgData.DataSize !=0)
			 Mem_free(pRxMsg->TransportMsgData.Data);
			return;
		}

		switch(pRxMsg->TransportMsgManage.ErrID)
		{
			case 0x01:
			case 0x02:
			case 0x03:
			case 0x05:
			case 0x06:
				if(ResponeTask_ExceptionsCallBack!=NULL)
				 (*ResponeTask_ExceptionsCallBack)(pTransportTask,pRxMsg->TransportMsgManage.ErrID);//调用回调函数并传递错误码
				
				if(pRxMsg->TransportMsgData.DataSize!=0)
				 Mem_free(pRxMsg->TransportMsgData.Data );
				if(TransportTask_GetTxMsgDataLen(pTransportTask)!=0)
				 Mem_free(TransportTask_GetTxMsgDataAddr(pTransportTask));//释放内存
			  TransportTask_RemoveTask(pTransportTask);                //取消传输任务调用回调函数
			break;
			case 0x04://分段传输错误
				TransportTask_AddErrNum(pTransportTask);             //标记错误次数
				if(TransportTask_GetErrNum(pTransportTask)<RESPONSETASK_ERRNUM)
				{
     			if(TransportTask_GetTxMsgState(pTransportTask)==0x01)//发送完成重新启动发送
					  TransportTask_ResetTxMsgState(pTransportTask);     //重新发送
					else
						TransportTask_SetTxMsgReSend(pTransportTask);      //取消本次发送,重新发送
				}
				else                                                   //取消传输任务
				{
					if(ResponeTask_ExceptionsCallBack!=NULL)
					 (*ResponeTask_ExceptionsCallBack)(pTransportTask,pRxMsg->TransportMsgManage.ErrID);      //调用回调
					if(TransportTask_GetTxMsgDataLen(pTransportTask)!=0)//确认响应任务是否申请了报文空间
					 Mem_free(TransportTask_GetTxMsgDataAddr(pTransportTask));
					TransportTask_RemoveTask(pTransportTask);
				}
				if(pRxMsg->TransportMsgData.DataSize!=0)
				 Mem_free(pRxMsg->TransportMsgData.Data );
				break;
			default:break;
		}
	}
}
/*以下为外部调用接口*/
