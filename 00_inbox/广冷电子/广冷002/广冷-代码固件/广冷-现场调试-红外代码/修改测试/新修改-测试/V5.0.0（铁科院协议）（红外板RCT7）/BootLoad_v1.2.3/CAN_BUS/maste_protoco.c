/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 主站CAN协议解析
*	文件名称 : maste_protoco.c
*	版    本 : V1.0
*	说    明 : 1.主站协议报文的解析
*            
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "maste_protoco.h"

/*****************************************
函数：MasteProtoco_ReadPort
功能：读端口接口函数
参数：
返回：
******************************************/
uint8_t MasteProtoco_ReadPort(uint8_t nodeid,uint8_t sounrcid,void *data)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAckTask;
	TransportCanMsgTypeDef MsgBuff;
	AskTaskTypeDef        AckTask;
	pDeviceManage=DeviceManage_GetDeviceManage(nodeid);
	if(pDeviceManage==NULL)
		return 0x00;         //节点不存在
	if(pDeviceManage->LinkManage.connectflag==0x00)
		return 0x01;         //节点未连接
	pAckTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,sounrcid,FUNCID_READPORT);
	if(pAckTask==NULL)
	{
		MsgBuff.TransportMsgFilter.DestMacID=nodeid;
		MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeDiscern.can_nodeid;//MasterManage.LinkManage.LocalMACID;
		MsgBuff.TransportMsgFilter.SourceID =sounrcid;
		MsgBuff.TransportMsgFilter.FuncID   =FUNCID_READPORT;
		MsgBuff.TransportMsgFilter.Ack      =0x00;//报文需响应
		MsgBuff.TransportMsgManage.ErrID    =0x00;
		MsgBuff.TransportMsgData.DataSize   =0x00;
		MsgBuff.TransportMsgData.Data       =NULL;
		if(TransportLayer_TxMsg(&MsgBuff)==0xFF)
    {
			AckTask.sourceid=sounrcid;
			AckTask.funcid=FUNCID_READPORT;
			AckTask.askfuncid=FUNCID_NONASK;
			AckTask.lifeover=0;
			AckTask.lifeover=0; 
			DeviceManage_AddAskTask(&pDeviceManage->AskTaskTable,&AckTask);
		}
		return 0x03;
	}
	else
	{
		switch(pAckTask->askfuncid)
		{
			case FUNCID_NONASK:
				return 0x02;
			case FUNCID_READPORT:
				Mem_copy(data,pAckTask->devicedata.Data,pAckTask->devicedata.DataSize);
				Mem_free(pAckTask->devicedata.Data);//释放内存
			  DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
				return 0xFF;//数据读取成功
			case FUNCID_EXCEPTIONS:
				DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
				return 0xEE;//读取失败
		}
	}
	return 0x04;
}
/*****************************************
函数：MasteProtoco_WritePort
功能：写端口接口函数
参数：
返回：
******************************************/
uint8_t MasteProtoco_WritePort(uint8_t nodeid,uint8_t sounrcid,void *data,uint8_t datasize)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAckTask;
	TransportCanMsgTypeDef MsgBuff;
	AskTaskTypeDef        AckTask;
	pDeviceManage=DeviceManage_GetDeviceManage(nodeid);
	if(pDeviceManage==NULL)
		return 0x00;         //节点不存在
	if(pDeviceManage->LinkManage.connectflag==0x00)
		return 0x01;         //节点未连接
	pAckTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,sounrcid,FUNCID_WRITEPORT);
	if(pAckTask==NULL)
	{
		MsgBuff.TransportMsgFilter.DestMacID=nodeid;
		MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeDiscern.can_nodeid;//MasterManage.LinkManage.LocalMACID;
		MsgBuff.TransportMsgFilter.SourceID =sounrcid;
		MsgBuff.TransportMsgFilter.FuncID   =FUNCID_WRITEPORT;
		MsgBuff.TransportMsgFilter.Ack      =0x00;//报文需响应
		MsgBuff.TransportMsgManage.ErrID    =0x00;
		MsgBuff.TransportMsgData.DataSize   =datasize;
		MsgBuff.TransportMsgData.Data       =Mem_malloc(datasize);
		if(MsgBuff.TransportMsgData.Data==NULL)
			return 0x04;
		Mem_copy(MsgBuff.TransportMsgData.Data,data,datasize);
		if(TransportLayer_TxMsg(&MsgBuff)==0xFF)
    {
			AckTask.sourceid=sounrcid;
			AckTask.funcid=FUNCID_WRITEPORT;
			AckTask.askfuncid=FUNCID_NONASK;
			AckTask.lifeover=0;
			AckTask.lifeover=0; 
			DeviceManage_AddAskTask(&pDeviceManage->AskTaskTable,&AckTask);
		}
		else
		{
			if(MsgBuff.TransportMsgData.DataSize!=0)
				Mem_free(MsgBuff.TransportMsgData.Data);
		}
		return 0x03;
	}
	else
	{
		switch(pAckTask->askfuncid)
		{
			case FUNCID_NONASK:
				return 0x02;
			case FUNCID_WRITEPORT:
			  DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
				return 0xFF;//数据写完成
			case FUNCID_EXCEPTIONS:
				DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
				return 0xEE;//读取失败
		}
	}
	return 0x05;
}
/*****************************************
函数：MasteProcoto_AskCallBack
功能：响应管理模块正常响应回调函数
参数：
返回：
******************************************/
void MasteProcoto_AskCallBack(TransportCanMsgTypeDef *pRxMsg)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAskTask;
	if(pRxMsg->TransportMsgFilter.FuncID==FUNCID_CYCLETRIGGER)
		return;
//	TransportTask_Check3();
	pDeviceManage=DeviceManage_GetDeviceManage(pRxMsg->TransportMsgFilter.SrcMacID);
	if(pDeviceManage==NULL)
	{
		if(pRxMsg->TransportMsgData.DataSize!=0)
		 Mem_free(pRxMsg->TransportMsgData.Data);
		return;
	}
	if(pRxMsg->TransportMsgFilter.FuncID ==FUNCID_CONNECT)//连接响应报文
	{
		DeviceManage_SetConnectFlag(pDeviceManage);//置位连接标志位
		Mem_copy(&pDeviceManage->nodefilter,pRxMsg->TransportMsgData.Data,sizeof(NodeDiscernTypeDef));
		
		DeviceManage_CallBack(&pDeviceManage->nodefilter,&pDeviceManage->LinkManage);//执行回调函数
		
		if(pRxMsg->TransportMsgData.DataSize!=0)
		 Mem_free(pRxMsg->TransportMsgData.Data);//释放数据包占用内存
	}
	else//更新设备管理模块
	{
		pAskTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,
		                                 pRxMsg->TransportMsgFilter.SourceID,
		                                 pRxMsg->TransportMsgFilter.FuncID);
		if(pAskTask==NULL)
		{
		 if(pRxMsg->TransportMsgData.DataSize!=0)
		  Mem_free(pRxMsg->TransportMsgData.Data);
//		 TransportTask_Check4();
		 return;
		}
		pAskTask->askfuncid=pRxMsg->TransportMsgFilter.FuncID;                                    //正常响应
		pAskTask->devicedata.Data=pRxMsg->TransportMsgData.Data;
		pAskTask->devicedata.DataSize =pRxMsg->TransportMsgData.DataSize;
	}
	
}

/*****************************************
函数：MasteProcoto_ExceptionsCallBack
功能：响应管理模块异常响应回调函数
参数：
返回：
******************************************/
void MasteProcoto_ExceptionsCallBack(TransportTaskTypeDef *pTransportTask,uint8_t ErrID)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAskTask;
	pDeviceManage=DeviceManage_GetDeviceManage(pTransportTask->TxCanMsg.TransportMsgFilter.DestMacID);
	if(pDeviceManage==NULL)
		return;
	if(ErrID==ERRID_NOTCONNECT)
	 pDeviceManage->LinkManage.connectflag=0x00;
	 pAskTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,
	                                  pTransportTask->TxCanMsg.TransportMsgFilter.SourceID,
	                                  pTransportTask->TxCanMsg.TransportMsgFilter.FuncID 
	                                  );
	if(pAskTask==NULL)
		return;
	pAskTask->askfuncid=FUNCID_EXCEPTIONS;//异常响应
  pAskTask->errid   =ErrID;
}

/*****************************************
函数：ProtocoStack_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/

void MasteProtoco_SendHeartBeatMsg(uint8_t timenum)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=0xFF;
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeDiscern.can_nodeid;//MasterManage.LinkManage.LocalMACID;
	MsgBuff.TransportMsgFilter.SourceID =0x00;
	MsgBuff.TransportMsgFilter.FuncID   =FUNCID_HEART;
	MsgBuff.TransportMsgFilter.Ack      =0x01;//报文不需响应
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}
/*****************************************
函数：ProtocoStack_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_SendErrID(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t ErrID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FUNCID_EXCEPTIONS;
	MsgBuff.TransportMsgFilter.Ack      =0x01; //报文不需响应
	MsgBuff.TransportMsgManage.ErrID    =ErrID;
	
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}
/*****************************************
函数：ProtocoStack_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_SendConnectMsg(uint8_t DestMacID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeDiscern.can_nodeid;//MasterManage.LinkManage.LocalMACID;
	MsgBuff.TransportMsgFilter.SourceID =0x01;                              //请求节点信息
	MsgBuff.TransportMsgFilter.FuncID   =FUNCID_CONNECT;
	MsgBuff.TransportMsgFilter.Ack      =0x00;                              //报文需等待响应
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}
/*****************************************
函数：ProtocoStack_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_RxHeart(TransportCanMsgTypeDef *pRxMsg)  
{
	DeviceManageTypeDef *pDeviceManage;
	NodeDiscernTypeDef Filter;
	pDeviceManage=DeviceManage_GetDeviceManage(pRxMsg->TransportMsgFilter.SrcMacID);
	if(pDeviceManage==NULL)
	{
		Filter.can_nodeid=pRxMsg->TransportMsgFilter.SrcMacID;
		DeviceManage_AddDevice(&Filter);                   //发送连接报文
		MasteProtoco_SendConnectMsg(pRxMsg->TransportMsgFilter .SrcMacID);
		return;
	}
	else
	{
		DeviceManage_ResetHeartTime(pDeviceManage);                      //复位定时器
	 if(DeviceManage_GetConnectFlag(pDeviceManage)!=0x01)
		 MasteProtoco_SendConnectMsg(pRxMsg->TransportMsgFilter.SrcMacID);//发送连接报文	
	}
}
/*****************************************
函数：MasteProtoco_RxWait
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_RxWait(TransportCanMsgTypeDef *pRxMsg)  
{
	DeviceManageTypeDef *pDeviceManage;
	NodeDiscernTypeDef Filter;
	pDeviceManage=DeviceManage_GetDeviceManage(pRxMsg->TransportMsgFilter.SrcMacID);
	if(pDeviceManage==NULL)
	{
		Filter.can_nodeid=pRxMsg->TransportMsgFilter.SrcMacID;
		DeviceManage_AddDevice(&Filter);                   //发送连接报文
		MasteProtoco_SendConnectMsg(pRxMsg->TransportMsgFilter .SrcMacID);
		return;
	}
	else
	{
		DeviceManage_ResetHeartTime(pDeviceManage);
    DeviceManage_ResetConnectFlag(pDeviceManage);		//复位定时器
		MasteProtoco_SendConnectMsg(pRxMsg->TransportMsgFilter.SrcMacID);//发送连接报文	
	}
}

void MasteProtoco_RxErrCallBack(MsgFilterTypeDef *pRxMsg)
{
	MasteProtoco_SendErrID(pRxMsg->SrcMacID,
	                       NodeInfo.NodeDiscern.can_nodeid,
	                       pRxMsg->SourceID,
	                       ERRID_TRANSPORTERRO);
}


/*****************************************
函数：MasteProtoco_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_TimeInit(void)//定时器初始化
{
	TimeTaskTypeDef TimeTask;

	TimeTask.callback=1;
	TimeTask.enable=0x01;
	TimeTask.time_value=MASTEHEART_SENDTIME;    //定时发送心跳报文
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=MasteProtoco_SendHeartBeatMsg;
	TimeTask_Add(MASTEHEART_SENDFTIME_TIMENUM,&TimeTask);
}
/*****************************************
函数：MasteProtoco_Init
功能：主站协议栈定时器初始化
参数：
返回：
******************************************/
void MasteProtoco_Init(void)
{
	TimeTask_Init();
	InfoTable_Init();
  TransportLayer_Init(MasteProtoco_RxErrCallBack);	              //初始化设置接收错误回调函数
	ResponseTask_SetAskCallBack(MasteProcoto_AskCallBack);          //设置ID检测响应处理
	ResponseTask_SetExceptionsCallBack(MasteProcoto_ExceptionsCallBack);
	DeviceManage_TaskInit();
	mIndexTable_Init();                                            //资源表初始化
	MasteProtoco_TimeInit();                                       //定时器响应
}
/*****************************************
函数：MasteProtoco_MsgParsing
功能：CAN报文解析
参数：
返回：
******************************************/
//返回0x01需要释放内存
//返回0x00不需要释放内存
uint8_t MasteProtoco_MsgParsing(TransportCanMsgTypeDef *pRxMsg)
{
	if(pRxMsg->TransportMsgFilter.Ack==0x01
		 &&pRxMsg->TransportMsgFilter.FuncID!=FUNCID_HEART
	   &&pRxMsg->TransportMsgFilter.FuncID!=FUNCID_CYCLETRIGGER
	   &&pRxMsg->TransportMsgFilter.FuncID!=FUNCID_WAIT)//响应报文
	{
		ResponseTask_MsgParsing(pRxMsg);
		return 0x00;
	}
	switch(pRxMsg->TransportMsgFilter.FuncID)
	{
		case FUNCID_HEART:
			MasteProtoco_RxHeart(pRxMsg);
			return 0x01;
		case FUNCID_WAIT:
			MasteProtoco_RxWait(pRxMsg);
			return 0x01;
		case FUNCID_CYCLETRIGGER:
			mIndexTable_ReceiveTask(pRxMsg);			
			return 0x01;
		case FUNCID_STATETRIGGER:
			mIndexTable_ReceiveTask(pRxMsg);			
			return 0x01;
		case FUNCID_THRESTRIGGER:
			mIndexTable_ReceiveTask(pRxMsg);			
			return 0x01;
		default:                                                      //需释放内存
			MasteProtoco_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
		                         pRxMsg->TransportMsgFilter.DestMacID,
		                     		0x00,ERRID_UNDEFINEFUNCID);//未定义功能码
		  return 0x01;
	}
}


void MastProtoco_TaskRun(void)
{
	static uint8_t runstate=0;
	static TransportCanMsgTypeDef RxMsg;
	switch(runstate)
	{
		case 0x00:
			if(TransportLayer_RxMsg(&RxMsg)==MSG_QUEUE_GET)
				runstate=0x01;
			break;
		case 0x01:
			if(MasteProtoco_MsgParsing(&RxMsg)==0x01)//释放内存
			 runstate=0x02;
			else
			 runstate=0x00;
			break;
		case 0x02:
			if(RxMsg.TransportMsgData.DataSize!=0x00)
			 Mem_free(RxMsg.TransportMsgData.Data);
			runstate=0x00;
			break;
		default:break;
	}
}

void CanMaste_RollRun(void)
{
	MastProtoco_TaskRun();
	ResponseTask_TaskRun(&NodeInfo.NodeLink);//响应模块
	TransportLayer_TaskRun();
	mIndexTable_SyncTaskRun(); //资源表同步任务
}

