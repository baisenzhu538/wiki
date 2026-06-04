#include "device_protocol.h"
#include "iap.h"

DeviceLinkInfoTypeDef DeviceLinkInfo;
DeviceInfoTypeDef     DeviceInfo={0x2001,0x01,0,0,{0},{0}};

uint8_t (*pfDeviceProtocol_UserCmdCallBack)(uint8_t Cmd,uint8_t *Data,uint16_t size);

/*************************************************************
函数：DeviceProtocol_SetDeviceInfo
功能：设置设备信息参数
参数：Info 设备信息结构体地址
返回：无
*************************************************************/
void DeviceProtocol_SetDeviceInfo(DeviceInfoTypeDef *Info)
{
	SysMem_copy(&DeviceInfo,Info,sizeof(DeviceInfoTypeDef));
}
/*************************************************************
函数：DeviceProtocol_SetUserCallBackFun
功能：用于设置自定义指令回调函数，用户需将自定义指令解析函数加载
      到协议层上，才能实现数据的上传
参数：用户函数指针
返回：无
*************************************************************/
void DeviceProtocol_SetUserCallBackFun(uint8_t (*pFun)(uint8_t,uint8_t*,uint16_t))
{
	pfDeviceProtocol_UserCmdCallBack=pFun;
}


/*************************************************************
函数：DeviceProtocol_TxMsg
功能：发送报文
参数：func   功能码
      cmd    指令码
      *data  数据段指针
      size   数据段长度
返回：0x00   内存分配失败
      0x01   发送设备
      0xFF   发送成功
*************************************************************/
uint8_t DeviceProtocol_TxMsg(uint8_t func,uint8_t cmd,uint8_t *data,uint16_t size)
{
  DeviceTransport_ProtocolBuffTypeDef *pTxMsgBuff;
	pTxMsgBuff=SysMem_malloc(size+sizeof(ProtocolHeadTypeDef));
	if(pTxMsgBuff==NULL)
		return 0x00;//内存分配失败
	if(size)
	 SysMem_copy(pTxMsgBuff->Data,data,size);
	pTxMsgBuff->protocolhead.command =cmd;
	pTxMsgBuff->protocolhead.func_id =func;
	pTxMsgBuff->protocolhead.pakesize=size;
	pTxMsgBuff->protocolhead.sn      =DeviceTransport_GetTxSn();
	pTxMsgBuff->protocolhead.destdev_no=0x00;
	pTxMsgBuff->protocolhead.destdev_type=0x0000;
	pTxMsgBuff->protocolhead.srcdev_no=DeviceInfo.dev_no;
	pTxMsgBuff->protocolhead.srcdev_type=DeviceInfo.dev_typ;
	if(DeviceTranspot_AddTxMsg(pTxMsgBuff)==DEVICE_QUEUE_ADD)
		return 0xFF;
	SysMem_free(pTxMsgBuff);
	return 0x01;//发送失败
}
/*************************************************************
函数：mDeviceProtocol_ForwardTxMsg
功能：其他通讯接口通过调用该接口实现数据的转发
参数：*data  代转发数据指针
      size   待转发数据段大小
返回：0x00   内存分配失败
      0x01   发送设备
      0xFF   发送成功
*************************************************************/
uint8_t mDeviceProtocol_ForwardTxMsg(uint8_t *data,uint16_t size)
{
  DeviceTransport_ProtocolBuffTypeDef *pTxMsgBuff;
	pTxMsgBuff=SysMem_malloc(size);
	if(pTxMsgBuff==NULL)
		return 0x00;//内存分配失败
	if(size)
	 SysMem_copy(pTxMsgBuff,data,size);
	if(DeviceTranspot_AddTxMsg(pTxMsgBuff)==DEVICE_QUEUE_ADD)
		return 0xFF;
	SysMem_free(pTxMsgBuff);
	return 0x01;//发送失败
}

//发送心跳报文
uint8_t DeviceProtocol_TxHeart(void)
{
	return DeviceProtocol_TxMsg(0x02,0x00,NULL,0x00);
}
//发送连接申请报文
uint8_t DeviceProtocol_TxLinkMsg(void)
{
	return DeviceProtocol_TxMsg(0x03,0x06,NULL,0x00);
}

//发送触发报文
uint8_t DeviceProtocol_TxTriggerMsg(uint8_t cmd,uint8_t *data,uint16_t size)
{
	return DeviceProtocol_TxMsg(0x03,cmd,data,size);
}

//发送响应报文
uint8_t DeviceProtocol_TxResportMsg(uint8_t cmd,uint8_t *data,uint16_t size)
{
	return DeviceProtocol_TxMsg(0x04,cmd,data,size);
}
//发送异常响应报文
uint8_t DeviceProtocol_TxExceptionsMsg(uint8_t cmd,uint8_t errid)
{
	return DeviceProtocol_TxMsg(0x05,cmd,&errid,0x01);
}

//接收心跳报文处理
uint8_t DeviceProtocol_ReceiveHeart(DeviceTransport_ProtocolBuffTypeDef *pRxBuff)
{
	if(DeviceLinkInfo.heart_flag)
	{
		DeviceLinkInfo.heart_outtime=0x00;//清0定时器
	}
	else
	{
		DeviceLinkInfo.heart_flag=0x01;
		DeviceLinkInfo.heart_outtime =0x00;
	}
	//添加转发心跳代码
}

void DeviceProtocol_HeartTimeReset(void)
{
	DeviceLinkInfo.heart_outtime =0x00;
}
//接收到指令码
uint8_t DeviceProtocol_ReceiveCommand(DeviceTransport_ProtocolBuffTypeDef *pRxBuff)
{
	DeviceProtocol_HeartTimeReset();
	if(pRxBuff->protocolhead.command<0x10)
	{
		switch(pRxBuff->protocolhead.command)
		{
			case 0x01://进入升级模式
				Iap_Rest_UpData();
			  DeviceProtocol_TxResportMsg(pRxBuff->protocolhead.command,NULL,0x00);
				break;
			case 0x02://固件升级完成
				if(Iap_UpData_Finish((FirmwareInfoTypeDef*)&pRxBuff->Data)==0x00)//写入数据错误
				{
					DeviceProtocol_TxExceptionsMsg(pRxBuff->protocolhead.command,0x04);//固件升级失败
				}
				break;
			case 0x03://固件数据包
				if(Iap_UpDataApp((FirmwareBuffTypeDef*)&pRxBuff->Data)==0xFF)//数据写入成功
				{
					DeviceProtocol_TxResportMsg(pRxBuff->protocolhead.command,NULL,0x00);
				}
				else                                       //数据写入失败
				{
					DeviceProtocol_TxExceptionsMsg(pRxBuff->protocolhead.command,0x03);
				}
				break;
			case 0x04://固件重传
				Iap_Rest_UpData();
			  DeviceProtocol_TxResportMsg(pRxBuff->protocolhead.command,NULL,0x00);
				break;
			case 0x05://读取设备信息
				DeviceProtocol_TxResportMsg(pRxBuff->protocolhead.command,(uint8_t*)&DeviceInfo,sizeof(DeviceInfo));
				break;
			case 0x06://建立连接
				if(DeviceLinkInfo.heart_flag)
				{
					DeviceLinkInfo.link_flag=0x01;
					DeviceProtocol_TxResportMsg(pRxBuff->protocolhead.command,(uint8_t*)&DeviceInfo,sizeof(DeviceInfo));//发送响应报文回传设备信息并建立连接
				}
				break;
			default:
				break;
		}
  }
	else//用户自定义指令
	{
		uint8_t state;
		if(pfDeviceProtocol_UserCmdCallBack!=NULL)
		{
			state=pfDeviceProtocol_UserCmdCallBack(pRxBuff->protocolhead.command,pRxBuff->Data,pRxBuff->protocolhead.pakesize);
			if(state)
			{
				DeviceProtocol_TxExceptionsMsg(pRxBuff->protocolhead.command,state);
			}
	  }
	}
 return 0x00;
}

uint8_t DeviceProtocol_MsgParsing(DeviceTransport_ProtocolBuffTypeDef *pRxBuff)
{
	if(pRxBuff->protocolhead.func_id==0x01)//指令码
	{
		DeviceProtocol_ReceiveCommand(pRxBuff);
	}
	else if(pRxBuff->protocolhead.func_id==0x02)//心跳码
	{
		DeviceProtocol_ReceiveHeart(pRxBuff);
	}
}





//定时器任务10ms运行
void DeviceProtocol_TimeTask(void)
{
	if(DeviceLinkInfo.heart_flag)//接收到心跳
	{
		DeviceLinkInfo.heart_outtime++;//心跳超时计数
		if(DeviceLinkInfo.heart_outtime>DEVICE_HEARTOUTTIME)
		{
			DeviceLinkInfo.link_flag=0x00;
			DeviceLinkInfo.heart_flag=0x00;
			DeviceLinkInfo.heart_time=0x00;
			DeviceLinkInfo.link_time=0x00;
		}
		else if(DeviceLinkInfo.link_flag)//已连接
		{
			DeviceLinkInfo.heart_time++;
			if(DeviceLinkInfo.heart_time>DEVICE_HEARTTIME)//发送心跳
			{
				DeviceLinkInfo.heart_time=0x00;
				DeviceProtocol_TxHeart();
			}
		}
		else//未连接
		{
			DeviceLinkInfo.link_time++;
			if(DeviceLinkInfo.link_time>DEVICE_LINKTIME)
			{
				DeviceLinkInfo.link_time=0x00;
				DeviceProtocol_TxLinkMsg();//发送连接码
			}
		}
	}
}

void DeviceProtocol_ReceiveTaskRun(void)
{
	uint8_t forward_state;
	static uint8_t state;
	static DeviceTransport_ProtocolBuffTypeDef *pProtocolBuff;
	switch(state)
	{
		case 0x00:
			pProtocolBuff=DeviceTranspot_GetRxMsg();
		  if(pProtocolBuff!=NULL)
				state=0x01;
			break;
		case 0x01:
			if((pProtocolBuff->protocolhead.destdev_type==DeviceInfo.dev_typ)
				 &&(pProtocolBuff->protocolhead.destdev_no==DeviceInfo.dev_no))
			{
				if(DeviceTransport_CompareRxSn(pProtocolBuff->protocolhead.sn)==0xFF)//检测是否存在相同Sn码，相同则丢弃该数据
			   state=0x03;
				else
				 state=0x04;
			}
			else//其他地址报文
			{
				state=0x02;
			}
			break;
		case 0x02://转发数据
//			forward_state=MasteProtoco_WriteSerialPort(pProtocolBuff->protocolhead.destdev_type,
//																								 pProtocolBuff->protocolhead.destdev_no,
//																								 0xFF,
//																								 pProtocolBuff,
//																								 pProtocolBuff->protocolhead.pakesize+sizeof(ProtocolHeadTypeDef)
//																								 );												
//       switch(forward_state)
//			 {
//				 case 0x00:
//				 case 0x01:
//				 case 0x02:
//				 case 0x03:
//				 case 0xFF:
//				 default:
//					 if((pProtocolBuff->protocolhead.destdev_type==0xFFFF)&&(pProtocolBuff->protocolhead.destdev_no==0xFF))
//						state=0x03;
//					 else
//						state=0x04;
//				 break;
//			 }
//			break;
		case 0x03://数据处理
      DeviceProtocol_MsgParsing(pProtocolBuff);
		  state=0x04;
			break;
		case 0x04://释放数据内存
			SysMem_free(pProtocolBuff);
		  state=0x00;
			break;
	}
}

void DeviceProtocol_TaskRun(void)
{
	DeviceProtocol_ReceiveTaskRun();
	DeviceTransport_TxTask();
}

void DeviceProtocol_Init(void)
{
	
}


































