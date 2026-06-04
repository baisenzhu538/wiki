/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 从站协议解析
*	文件名称 : node_info.c
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

#include "slave_protoco.h"
#include "node_info.h"

#ifdef CAN_SLAVE_NODE

void ProtocoStack_SendErrID(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID,uint8_t ErrID);
void (*pSlaveProtoco_CallBack)(TransportCanMsgTypeDef *)=NULL;    //回调函数


//接收到读写指令后回调函数
void SlaveProtoco_SetCallBack(void (*p)(TransportCanMsgTypeDef *))//设置回调函数
{
	pSlaveProtoco_CallBack=p;
}

/*****************************************
函数：RxMsgErr_CallBack
功能：接收分段数据包错误回调函数
参数：
返回：
******************************************/
void RxMsgErr_CallBack(MsgFilterTypeDef *pRxMsg)
{
	if(pRxMsg->DestMacID==0xFF||pRxMsg->DestMacID==0xFE)
		return;
	ProtocoStack_SendErrID(pRxMsg->SrcMacID,
	                       NodeInfo.NodeLink.LocalMACID,
	                       pRxMsg->SourceID,
	                       pRxMsg->FuncID,
	                       ERRID_TRANSPORTERRO);
}
/*****************************************
函数：ProtocoStack_RemoveConnect
功能：定时器回调函数，超时调用该函数删除连接
参数：
返回：
******************************************/
void ProtocoStack_RemoveConnect(uint8_t timenum)//超时断开所有连接
{
	if(timenum==HEART_OVERTIME_TIMENUM)         
	{
		NodeInfo.NodeLink.ConnectFlag=0;
		NodeInfo.NodeLink.HeartbeatFlag=0;
		NodeInfo.NodeLink.IDTest=0;
		TimeTask_Cmd(HEART_OVERTIME_TIMENUM,0x00);          //关闭心跳超时定时器
		TimeTask_Cmd(HEART_SENDTIME_TIMENUM,0x00);          //关闭心跳发送定时器
		TransportLayer_CancelAllSend();                        //删除所有带发送任务
		sIndexTable_SetConnectFlag(NodeInfo.NodeLink.MasterMACID,NodeInfo.NodeLink.ConnectFlag);//设置数据表连接状态
	}
}

/*****************************************
函数：ProtocoStack_SendHeartBeatMsg
功能：定时器回调函数，定时发送心跳报文
参数：
返回：
******************************************/
void ProtocoStack_SendHeartBeatMsg(uint8_t timenum)
{
	TransportCanMsgTypeDef MsgBuff;
	DeviceMarkTypeDef  DeviceMarkBuff;
	MsgBuff.TransportMsgFilter.DestMacID=NodeInfo.NodeLink.MasterMACID;
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo.NodeLink.LocalMACID;
	MsgBuff.TransportMsgFilter.SourceID =0x00;
	if(NodeInfo.NodeLink.ConnectFlag==0x01)
	 MsgBuff.TransportMsgFilter.FuncID   =FUNCID_HEART;
	else
	 MsgBuff.TransportMsgFilter.FuncID   =FUNCID_WAIT;
	
	MsgBuff.TransportMsgFilter.Ack      =0x01;//报文不需响应
	MsgBuff.TransportMsgManage.ErrID    =0x00;
  
	MsgBuff.TransportMsgData.DataSize   =sizeof(DeviceMarkTypeDef);
	MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
	if(MsgBuff.TransportMsgData.Data==NULL)
	 return;
	DeviceMarkBuff.can_nodeid=NodeInfo_GetNodeId();
	DeviceMarkBuff.devicenum =NodeInfo_GetDeviceNum();
	DeviceMarkBuff.devicetype=NodeInfo_GetDeviceType();
	Mem_copy(MsgBuff.TransportMsgData.Data,&DeviceMarkBuff,MsgBuff.TransportMsgData.DataSize);
	
	TransportLayer_TxMsg(&MsgBuff);
}

/*****************************************
函数：ProtocoStack_TimeInit
功能：协议栈定时器初始化
参数：
返回：
******************************************/
void ProtocoStack_TimeInit(void)//定时器初始化
{
	TimeTaskTypeDef TimeTask;
	
	TimeTask.callback=1;
	TimeTask.enable=0x00;
	TimeTask.time_value=HEART_OVERTIME; //3s未收到心跳
	TimeTask.time_mode=0x01;            //不自动复位定时值
	TimeTask.TimeTack_CallBack=ProtocoStack_RemoveConnect;
	TimeTask_Add(HEART_OVERTIME_TIMENUM,&TimeTask);
	
	TimeTask.callback=1;
	TimeTask.enable=0x00;
	TimeTask.time_value=HEART_SENDTIME;    //定时发送心跳报文
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=ProtocoStack_SendHeartBeatMsg;
	TimeTask_Add(HEART_SENDTIME_TIMENUM,&TimeTask);
}




/*****************************************
函数：ProtocoStack_SendErrID
功能：发送错误响应
参数：pRxMsg 接收数据包地址
返回：
******************************************/
void ProtocoStack_SendErrID(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID,uint8_t ErrID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FUNCID_EXCEPTIONS;
	MsgBuff.TransportMsgFilter.Ack      =0x01;
	MsgBuff.TransportMsgManage.ErrID    =ErrID;
	MsgBuff.TransportMsgManage.ErrFunc  =FuncID;
	
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}

/*****************************************
函数：ProtocoStack_SendAsk
功能：发送正常响应报文
参数：DestMacID 目标ID
      SourceID  发送索引表地址数据
      mode      返回数据
返回：
******************************************/
void ProtocoStack_SendAsk(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID,uint8_t mode)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FuncID;
	MsgBuff.TransportMsgFilter.Ack      =0x01;      //响应报文
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	
	if(mode==0x01)
	{
	 MsgBuff.TransportMsgData.DataSize   =sIndexTable_GetDataLen(DestMacID,SourceID);
	 MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
	 if(MsgBuff.TransportMsgData.Data==NULL)
		 return;
	 sIndexTable_ReadData(DestMacID,SourceID,MsgBuff.TransportMsgData.Data);
	}
	else
	 MsgBuff.TransportMsgData.DataSize   =0x00;
	
	if(TransportLayer_TxMsg(&MsgBuff)!=0xFF&&MsgBuff.TransportMsgData.DataSize!=0)
		Mem_free(MsgBuff.TransportMsgData.Data);
}

/*****************************************
函数：ProtocoStack_SendInfo
功能：发送正常响应报文
参数：DestMacID 目标ID
      SourceID  发送索引表地址数据
      mode      返回数据
返回：
******************************************/
void ProtocoStack_SendInfo(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FuncID;
	MsgBuff.TransportMsgFilter.Ack      =0x01;      //响应报文
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	
 MsgBuff.TransportMsgData.DataSize   =GetInfoSize(SourceID);
 MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
 if(MsgBuff.TransportMsgData.Data==NULL)
	return;
 ReadNodeInfo(SourceID,MsgBuff.TransportMsgData.Data);

	if(TransportLayer_TxMsg(&MsgBuff)!=0xFF&&MsgBuff.TransportMsgData.DataSize!=0)
		Mem_free(MsgBuff.TransportMsgData.Data);
}
/*****************************************
函数：ProtocoStack_WriteSerialPort
功能：写数据到串口端口
参数：SourceID  资源表端口号
      *data     发送数据段地址
      datasize  发送数据段长度
返回：0x00      节点为连接
      0x01      节点分配内存失败
      0x02      发送失败
      0xFF      发送成功
******************************************/
uint8_t ProtocoStack_WriteSerialPort(uint8_t SourceID,void *data,uint8_t datasize)
{
	TransportCanMsgTypeDef MsgBuff;
	if(NodeInfo_GetConnectFlag()==0x00)//检测节点是否接入
		return 0x00;
	MsgBuff.TransportMsgFilter.DestMacID=NodeInfo_GetMastId();
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo_GetNodeId();
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FUNCID_WRITEPORT;
	MsgBuff.TransportMsgFilter.Ack      =0x00;      //响应报文
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	
 MsgBuff.TransportMsgData.DataSize   =datasize;
 MsgBuff.TransportMsgData.Data       =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
 if(MsgBuff.TransportMsgData.Data==NULL)
	return 0x01;
 Mem_copy(MsgBuff.TransportMsgData.Data,data,datasize);
	if(TransportLayer_TxMsg(&MsgBuff)!=0xFF&&MsgBuff.TransportMsgData.DataSize!=0)
	{
		Mem_free(MsgBuff.TransportMsgData.Data);
		return 0x02;
	}
	return 0xFF;
}

/*****************************************
函数：ProtocoStack_ReadPort
功能：读端口操作
参数：pRxMsg 接收数据包地址
返回：
******************************************/
void ProtocoStack_RxReadPort(NodeLinkTypeDef *pLink,TransportCanMsgTypeDef *pRxMsg)
{
	if(pLink->ConnectFlag==0x01)
	{
		if(sIndexTable_GetDataLen(pRxMsg->TransportMsgFilter.SrcMacID,pRxMsg->TransportMsgFilter.SourceID)==NULL)
		{
			ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,//数据不存在报文
		                         pLink->LocalMACID,
		                         pRxMsg->TransportMsgFilter.SourceID,
			                       pRxMsg->TransportMsgFilter.FuncID,
		                         ERRID_UNDEFINEDATA);
			return;
		}
		
		ProtocoStack_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID,
		                     pLink->LocalMACID,
		                     pRxMsg->TransportMsgFilter.SourceID,
		                     pRxMsg->TransportMsgFilter.FuncID,
		                     0x01);//发送响应数据
	}
	else
	{
		ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,//发送未连接报文
		                       pLink->LocalMACID,
		                       pRxMsg->TransportMsgFilter.SourceID,
		                       pRxMsg->TransportMsgFilter.FuncID,
		                       ERRID_NOTCONNECT);
	}
	if(pSlaveProtoco_CallBack!=NULL)
		(*pSlaveProtoco_CallBack)(pRxMsg);
}

/*****************************************
函数：ProtocoStack_WritePort
功能：写端口操作
参数：pRxMsg 接收数据包地址
返回：
******************************************/
void ProtocoStack_RxWritePort(NodeLinkTypeDef *pLink,TransportCanMsgTypeDef *pRxMsg)
{
	uint32_t err;
	if(pLink->ConnectFlag==0x01)
	{
		err=sIndexTable_WriteData(pRxMsg->TransportMsgFilter.SrcMacID,
		                          pRxMsg->TransportMsgFilter.SourceID,
														  pRxMsg->TransportMsgData.Data,
														  pRxMsg->TransportMsgData.DataSize);
		if(pRxMsg->TransportMsgFilter.DestMacID==0xFE||pRxMsg->TransportMsgFilter.DestMacID==0xFF)
			return;
		if(err==0xFF)
		{
			sIndexTable_UpDataLate(pRxMsg->TransportMsgFilter.SrcMacID,pRxMsg->TransportMsgFilter.SourceID);//更新触发任务中的last值
			ProtocoStack_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID,
		                       pLink->LocalMACID,
													 pRxMsg->TransportMsgFilter.SourceID,
		                       pRxMsg->TransportMsgFilter.FuncID,
		                       0x00);//发送响应
		}
		else if(err==0x00)
		{
			ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
		                         pLink->LocalMACID,
														 pRxMsg->TransportMsgFilter.SourceID,
		                         pRxMsg->TransportMsgFilter.FuncID,
														 ERRID_UNDEFINEFUNCID);//节点不存在
		}
		else
		{
			ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
		                         pLink->LocalMACID,
													   pRxMsg->TransportMsgFilter.SourceID,
		                         pRxMsg->TransportMsgFilter.FuncID,
													   ERRID_DATAUNMATE);   //数据不匹配
		}
 } 
 else
 {
	ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
	                       pLink->LocalMACID,
	                       pRxMsg->TransportMsgFilter.SourceID,
	                       pRxMsg->TransportMsgFilter.FuncID,
	                       ERRID_NOTCONNECT);
 }
 if(pSlaveProtoco_CallBack!=NULL)
		(*pSlaveProtoco_CallBack)(pRxMsg);
}

/*****************************************
函数：ProtocoStack_RxHeart
功能：心跳报文处理
参数：pRxMsg 接收数据包地址
返回：
******************************************/
void ProtocoStack_RxHeart(NodeLinkTypeDef *pLink,TransportCanMsgTypeDef *pRxMsg)
{
	if(pLink->HeartbeatFlag==0x00&&pRxMsg->TransportMsgFilter.DestMacID==0xFF)//未连接且心跳报文为广播报文，判断为主机心跳
	{
		pLink->MasterMACID=pRxMsg->TransportMsgFilter.SrcMacID;
		pLink->HeartbeatFlag=0x01;
	
		TimeTask_RestCount(HEART_OVERTIME_TIMENUM);           //复位定时器并启动定时器
		TimeTask_Cmd(HEART_OVERTIME_TIMENUM,0x01);
		
	  TimeTask_RestCount(HEART_SENDTIME_TIMENUM);           //复位定时器并启动定时器
	  TimeTask_Cmd(HEART_SENDTIME_TIMENUM,0x01);          //启动心跳报文
	}
	else if(pLink->HeartbeatFlag==0x01)                    //已经获取主机心跳
	{
		if(pLink->MasterMACID==pRxMsg->TransportMsgFilter.SrcMacID)
		{
			TimeTask_RestCount(HEART_OVERTIME_TIMENUM);//复位定时器
		}
	}
}

/*****************************************
函数：ProtocoStack_RxHeart
功能：连接报文处理
参数：pRxMsg 接收数据包地址
返回：
******************************************/
void ProtocoStack_RxConnect(NodeLinkTypeDef *pLink,TransportCanMsgTypeDef *pRxMsg)
{
	DeviceMarkTypeDef *pDeviceMark;
	if(pLink->HeartbeatFlag==0x01)                               //确认总线是否存在主机心跳
	{
		pDeviceMark=(DeviceMarkTypeDef *)pRxMsg->TransportMsgData.Data;
		if((pDeviceMark->devicetype==NodeInfo_GetDeviceType())&&(pDeviceMark->devicenum==NodeInfo_GetDeviceNum()))//识别为本机设备编号
		{
			if(pLink->ConnectFlag==0x01)                                //已连接
			{
			 if(pRxMsg->TransportMsgFilter.SrcMacID==pLink->MasterMACID)
				{
					if(pDeviceMark->can_nodeid!=NodeInfo_GetNodeId())//非设备控制器重新配置
					{
						NodeInfo_SetNodeId(pDeviceMark->can_nodeid);
					}
				  ProtocoStack_SendInfo(pRxMsg->TransportMsgFilter.SrcMacID,
																pRxMsg->TransportMsgFilter.DestMacID,
																pRxMsg->TransportMsgFilter.SourceID,
																pRxMsg->TransportMsgFilter.FuncID);
					pLink->ConnectFlag=0x01;                                  //发送机器响应信息
					sIndexTable_SetConnectFlag(pRxMsg->TransportMsgFilter.SrcMacID,pLink->ConnectFlag); ////设置数据表连接状态
				}
			 else
				{
					ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
																 pLink->LocalMACID,
																 0x00,
																 pRxMsg->TransportMsgFilter.FuncID,
																 ERRID_CONNECT);
				}
			}
			else                                                         //未连接
			{
				pLink->MasterMACID=pRxMsg->TransportMsgFilter.SrcMacID;
				if(pDeviceMark->can_nodeid!=NodeInfo_GetNodeId())//非设备控制器重新配置
				{
					NodeInfo_SetNodeId(pDeviceMark->can_nodeid);
				}
				ProtocoStack_SendInfo( pRxMsg->TransportMsgFilter.SrcMacID,
															 pRxMsg->TransportMsgFilter.DestMacID,
															 pRxMsg->TransportMsgFilter.SourceID,
															 pRxMsg->TransportMsgFilter.FuncID);
				pLink->ConnectFlag=0x01;//发送机器响应信息
				sIndexTable_SetConnectFlag(pRxMsg->TransportMsgFilter.SrcMacID,pLink->ConnectFlag);
			}
		}
  }
}

/*************************************************************
函数：ProtocoStack_Init
功能：协议栈初始化
参数：无
返回：无
*************************************************************/
void ProtocoStack_Init(void)
{
	TimeTask_Init();
  InfoTable_Init();	//初始化定时器任务模块
  sIndexTable_Init();//初始化参数表
	TransportLayer_Init(RxMsgErr_CallBack);                   //出初始化传输层
  ProtocoStack_TimeInit();                                  //初始化索引表
}

//返回0x01需要释放内存
//返回0x00不需要释放内存
uint8_t ProtocoStack_MsgParsing(NodeLinkTypeDef *pLink,TransportCanMsgTypeDef *pRxMsg)
{
	uint16_t state;
	if(pLink->IDTest==0x03)
		return 0x01;
	if(pRxMsg->TransportMsgFilter.Ack==0x01
		 &&pRxMsg->TransportMsgFilter.FuncID!=FUNCID_CYCLETRIGGER
		 &&pRxMsg->TransportMsgFilter.FuncID!=FUNCID_HEART)//响应报文
	{
		ResponseTask_MsgParsing(pRxMsg);
		return 0x00;
	}
	switch(pRxMsg->TransportMsgFilter.FuncID)
	{
		case FUNCID_HEART:
			ProtocoStack_RxHeart(pLink,pRxMsg);
		  state=0x01;
		  break;
		case FUNCID_READPORT:
			 ProtocoStack_RxReadPort(pLink,pRxMsg);
		   state=0x01;
		   break;
		case FUNCID_WRITEPORT:
			 ProtocoStack_RxWritePort(pLink,pRxMsg);
		   state=0x01;
		   break;
		case FUNCID_CONNECT:
			ProtocoStack_RxConnect(pLink,pRxMsg);
		  state=0x01;
		  break;
		case FUNCID_REMOVECONNECT:
			ProtocoStack_RemoveConnect(HEART_OVERTIME_TIMENUM);//删除连接
		  state=0x01;
		  break;
		case FUNCID_READINFO:
			ProtocoStack_SendInfo(pRxMsg->TransportMsgFilter.SrcMacID,
														pLink->LocalMACID,
														pRxMsg->TransportMsgFilter.SourceID,
														pRxMsg->TransportMsgFilter.FuncID);
		  state=0x01;
			break;
		case FUNCID_IDCHECK:
		  state=0x01;
		  break;
		case FUNCID_CYCLETRIGGER:
			sIndexTable_ReceiveTask(pRxMsg);
			state=0x01;
			break;
		case FUNCID_STATETRIGGER:
			sIndexTable_ReceiveTask(pRxMsg);
			state=0x01;
			break;
		case FUNCID_RENEWTABLE://刷新整机参数表
//			InitiativeTask_RenewTable();
		  ProtocoStack_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID, //返回响应
		                       pLink->LocalMACID,
		                       pRxMsg->TransportMsgFilter.SourceID,
		                       pRxMsg->TransportMsgFilter.FuncID,
		                       0x00
		                      );
			state=0x01;
		break;
		default:
			ProtocoStack_SendErrID(pRxMsg->TransportMsgFilter.SrcMacID,
		                         pLink->LocalMACID,
		                         pRxMsg->TransportMsgFilter.SourceID,
		                         pRxMsg->TransportMsgFilter.FuncID,
		                         ERRID_UNDEFINEFUNCID);
		  state=0x01;
		  break;
	}
	return state;
}

void ProtocoStack_TaskRun(NodeLinkTypeDef *pLink)
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
			if(ProtocoStack_MsgParsing(pLink,&RxMsg)==0x01)
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
void ProtocoStack_RollRun(void)
{
	ProtocoStack_TaskRun(&NodeInfo.NodeLink);
	ResponseTask_TaskRun(&NodeInfo.NodeLink);   //响应任务处理
	sIndexTable_SyncTaskRun();
	TransportLayer_TaskRun();                    //发送报文任务
}

#endif


