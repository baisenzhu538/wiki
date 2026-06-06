#include "serial_procotol.h"
/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 下位机串口通讯模块
*	文件名称 : serial_procotol.c
*	版    本 : V1.0
*	说    明 : 1.串口数据的编码和解码与协议解析
*            2.出货任务的创建
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
SerialPacketTypeDef    SerialRxPacket;
SerialTxBufTypeDef     SerialTxBuf;
Device_SysStateTypedef Device_SysState;
SerialTaskTypeDef      SerialTask;

void SerialProcotol_SetTaskState(uint8_t state)
{
	SerialTask.TaskRunState=state;
}

void SerialProcotol_Init(void)
{
	SerialDevice_Init();          //串口初始化
	SerialTask.TaskRunState=0;
	SerialTask.CycTimeCount=CYC_TX_TIME;
	SerialTask.CycTxTime   =CYC_TX_TIME;
}

uint32_t Procotol_Checksum32(uint8_t size,uint8_t *data)
{
	uint32_t checksum=0;
	uint16_t i;
	for(i=0;i<size;i++)
	{
		checksum+=data[i];
	}
	return checksum;
}

void Procotol_Memcopy(uint8_t* pd_data,uint8_t* ps_data,uint16_t datalen)
{
	uint16_t i;
	for(i=0;i<datalen;i++)
	{
		pd_data[i]=ps_data[i];
	}
}

void SerialProcotol_GetSysState(void)
{
	Device_SysState.body_s     =Sensor_GetBodyIrState();
	Device_SysState.door_s     =Sensor_GetDoorSWState();
	Device_SysState.m_errstate =MotorDrive_GetErrState();
	Device_SysState.sell_s     =SellApp_GetSellState();
}
uint8_t SerialProcotol_SendCmd(uint8_t funcid,uint8_t resid,uint8_t cmd,uint16_t sn,uint8_t *data,uint16_t datasize)
{
	if(SerialTxBuf.BufState==0x00)//buff未被占用
	{
	 SerialTxBuf.PackBuf.pckhead.funcid =funcid;
	 SerialTxBuf.PackBuf.pckhead.resid  =resid;
	 SerialTxBuf.PackBuf.pckhead.command=cmd;
	 SerialTxBuf.PackBuf.pckhead.sn     =sn;
	 SerialTxBuf.PackBuf.pckhead.packet_size=datasize;
	 Procotol_Memcopy(SerialTxBuf.PackBuf.databuf,data,datasize);
	 if((funcid==0x01)||(funcid==0x04))
		SerialTxBuf.Ack=0x01;
	 else if((funcid==0x02)||(funcid==0x03))		 
		SerialTxBuf.Ack=0x00;//不需要响应
	 SerialTxBuf.txnum=PCK_TX_NUM;
	 SerialTxBuf.RespTime=PCK_RESP_TIME;
	 SerialTxBuf.BufState=0x01;//buf占用
	 SerialTxBuf.resperr =0x00;//错误位置0
	 return 0x01;			
	}
	return 0x00;
}
//10ms调用该程序
void SerialProcotol_TimeTask(void)
{
	if(SerialTxBuf.BufState==0x02)//待响应报文
	{
		if(SerialTxBuf.RespTime>0)
		 SerialTxBuf.RespTime--;
	}
	if(SerialTask.CycTimeCount>0)
	 SerialTask.CycTimeCount--;
}
void SerialProcotol_TxRun(void)
{
	if(SerialTxBuf.BufState==0x01)//未发送报文
	{
		if(Uart_SendPack(COM1,(uint8_t*)&SerialTxBuf.PackBuf,SerialTxBuf.PackBuf.pckhead.packet_size+PCK_HEAD_LEN))//发送成功
		{
			if(SerialTxBuf.Ack==0x00)
			{
				SerialTxBuf.BufState=0x00;//解除占用
			}
			else
			{
				SerialTxBuf.BufState=0x02;//标志响应报文
			}
		}
	}
	else if(SerialTxBuf.BufState==0x02)//待响应报文
	{
		if((SerialTxBuf.RespTime==0)||(SerialTxBuf.resperr==0x01))//响应超时或响应错误
		{
			if(SerialTxBuf.txnum)    //重发次数
			{
				if(Uart_SendPack(COM1,(uint8_t*)&SerialTxBuf.PackBuf,SerialTxBuf.PackBuf.pckhead.packet_size+PCK_HEAD_LEN))//再次发送成功
				{
					SerialTxBuf.resperr=0;
					SerialTxBuf.RespTime=PCK_RESP_TIME;//重新配置响应超时
					SerialTxBuf.txnum--;
				}
			}
			else
			 SerialTxBuf.BufState=0x00;  //解除占用
		}
	}
}
//周期发送设备状态码
void SerialProcotol_CycSendDeviceState(void)
{
	if(SerialTask.CycTimeCount==0)
	{
	 SerialProcotol_GetSysState();
	 if(SerialProcotol_SendCmd(0x02,0x00,0x03,0,(uint8_t*)&Device_SysState,sizeof(Device_SysState)))
	 {
		 SerialTask.CycTimeCount=SerialTask.CycTxTime;
	 }
	}
}
void SerialProcotol_CmParsing(SerialPacketTypeDef *pPack)
{
	uint8_t i;
	SellTaskTypeDef SellTask;
	switch(pPack->pckhead.command)
	{
		case 0x01:
			if(Sensor_GetGoodsIr1Err())
				SerialProcotol_SetTaskState(0x08);
			else
			{
				for(i=0;i<pPack->pckhead.packet_size;i+=2)
				{
					SellTask.cargo_no =pPack->databuf[i];
					SellTask.cargo_num=pPack->databuf[i+1];
					SellTask.sn       =pPack->pckhead.sn;
					SellApp_AddTask(&SellTask);
				}
				SerialProcotol_SetTaskState(0x03);
		  }
			break;
		case 0x02://读取设备状态
			SerialProcotol_SetTaskState(0x09);
			break;
		case 0x03://复位电机
			MotorDrive_RestPosit();
		  SerialProcotol_SetTaskState(0x03);
			break;
		case 0x04:
			
			break;
	}
}


void SerialProcotol_RepParsing(SerialPacketTypeDef *pPack)
{
 SerialProcotol_SetTaskState(0x00);
 if(SerialTxBuf.BufState!=0x02)
	 return;
 switch(pPack->pckhead.resid)
 {
	 case 0x00://正常响应
		if((SerialTxBuf.PackBuf.pckhead.command==pPack->pckhead.command)&&(SerialTxBuf.PackBuf.pckhead.sn==pPack->pckhead.sn))
		{
			SerialTxBuf.BufState=0x00;//解除占用
		}
		break;
	 case 0x02://数据错误
		if(SerialTxBuf.BufState==0x02)
		{
			SerialTxBuf.resperr=0x01;
		}
		break;
 }
}

void SerialProcotol_TaskRun(void)
{
	uint16_t datalen;
	switch(SerialTask.TaskRunState)
	{
		case 0x00:
			datalen=Usart_GetDataPackLen(COM1);
			if((datalen!=0xEEEE)&&(datalen!=0x00))
			{
			 Usart_GetDataPack(COM1,datalen,(uint8_t*)&SerialRxPacket);
			 SerialProcotol_SetTaskState(0x01);
			}
			else if(datalen==0xEEEE)//数据错误
			{
				SerialProcotol_SetTaskState(0x05);
			}
			break;
		case 0x01://校验数据包头
      SerialProcotol_SetTaskState(0x02);
			break;
		case 0x02:
				switch(SerialRxPacket.pckhead.funcid)
				{
				  case 0x01://指令码
					 SerialProcotol_CmParsing(&SerialRxPacket);
					 break;
				  case 0x02://响应码
					 SerialProcotol_RepParsing(&SerialRxPacket);
					 break;
					default://功能码不存在
						SerialProcotol_SetTaskState(0x06);
					 break;
				}
			break;
		
		case 0x03://发送正常响应码
			if(SerialProcotol_SendCmd(0x02,0x00,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
       SerialProcotol_SetTaskState(0x00);
			break;
//		case 0x04://数据头错误
//			if(SerialProcotol_SendCmd(0x02,0x01,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
//       SerialProcotol_SetTaskState(0x00);
//			break;
		case 0x05://数据错误
			if(SerialProcotol_SendCmd(0x02,0x02,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
       SerialProcotol_SetTaskState(0x00);
			break;
		case 0x06://功能码不存在
			if(SerialProcotol_SendCmd(0x02,0x04,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
       SerialProcotol_SetTaskState(0x00);
		  break;
		case 0x07:
			if(SerialProcotol_SendCmd(0x02,0x03,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
			 SerialProcotol_SetTaskState(0x00);
		break;
		case 0x08://红外传感器故障
			if(SerialProcotol_SendCmd(0x02,0x0A,SerialRxPacket.pckhead.command,SerialRxPacket.pckhead.sn,0,0))
			 SerialProcotol_SetTaskState(0x00);
		break;
		case 0x09://返回设备状态码
			SerialProcotol_GetSysState();
			if(SerialProcotol_SendCmd(0x02,0x0B,SerialRxPacket.pckhead.command,0,(uint8_t*)&Device_SysState,sizeof(Device_SysState)))
			 SerialProcotol_SetTaskState(0x00);
			break;
		default:
			SerialProcotol_SetTaskState(0x00);
		break;
	}
	SerialProcotol_CycSendDeviceState();//周期发送设备状态码
	SerialProcotol_TxRun();//循环调用发送程序
}

