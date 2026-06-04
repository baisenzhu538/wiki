#include "dgus_recive.h"

DgusDataPack_TypeDef	DgusDataRecivePack;

u8 DgusDataRecivePackBuffer[DGUS_DATA_BUFFER_MAX_SIZE];
u8 DgusDataRecivePackIndex;
DgusReciveAck_TypeDef	DgusRecive82Ack;
DgusReciveAck_TypeDef	DgusRecive83Ack;

void (*pDgusRecive_DeviceManageId_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceManagePwd_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceManageLogin_Callback)(u8*,u8) = NULL;

void (*pDgusRecive_DeviceManageFixId_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceManageFixPwd_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceManageFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceIdFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_DeviceIdFixOk_Callback)(u8*,u8) = NULL;

void (*pDgusRecive_WifiSsidFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_WifiPwdFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_WifiFixOk_Callback)(u8*,u8) = NULL;

void (*pDgusRecive_TcpIpFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_TcpPortFix_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_TcpFixOk_Callback)(u8*,u8) = NULL;

void (*pDgusRecive_OpenLock_Callback)(u8*,u8) = NULL;

void (*pDgusRecive_ShowHistoryStart_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_ShowHistoryNext_Callback)(u8*,u8) = NULL;
void (*pDgusRecive_ShowHistoryLast_Callback)(u8*,u8) = NULL;

void DgusRecive_Set_ShowHistoryNext_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_ShowHistoryNext_Callback = pfun;
}

void DgusRecive_Set_ShowHistoryLast_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_ShowHistoryLast_Callback = pfun;
}

void DgusRecive_Set_ShowHistoryStart_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_ShowHistoryStart_Callback = pfun;
}

void DgusRecive_Set_OpenLock_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_OpenLock_Callback = pfun;
}

void DgusRecive_Set_TcpIpFix_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_TcpIpFix_Callback = pfun;
}

void DgusRecive_Set_TcpPortFix_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_TcpPortFix_Callback = pfun;
}

void DgusRecive_Set_TcpFixOk_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_TcpFixOk_Callback = pfun;
}

void DgusRecive_Set_WifiSsidFix_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_WifiSsidFix_Callback = pfun;
}

void DgusRecive_Set_WifiPwdFix_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_WifiPwdFix_Callback = pfun;
}

void DgusRecive_Set_WifiFixOk_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_WifiFixOk_Callback = pfun;
}

void DgusRecive_Set_DeviceIdFix_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_DeviceIdFix_Callback = pfun;
}

void DgusRecive_Set_DeviceIdFixOk_Callback(void (pfun)(u8*,u8))
{
	pDgusRecive_DeviceIdFixOk_Callback = pfun;
}

void DgusRecive_Set_DeviceManageFixIdCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManageFixId_Callback = pfun;
}

void DgusRecive_Set_DeviceManageFixPwdCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManageFixPwd_Callback = pfun;
}

void DgusRecive_Set_DeviceManageFixCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManageFix_Callback = pfun;
}

void DgusRecive_Set_DeviceManageIdCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManageId_Callback = pfun;
}

void DgusRecive_Set_DeviceManagePwdCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManagePwd_Callback = pfun;
}

void DgusRecive_Set_DeviceManageLoginCallback(void (*pfun)(u8*,u8))
{
	pDgusRecive_DeviceManageLogin_Callback = pfun;
}

u8	DgusRecive_Get_82Ack(void)
{
	return DgusRecive82Ack.AckFlag;
}

void DgusRecive_Reset_82Ack(void)
{
	DgusRecive82Ack.AckFlag = 0;
}

void DgusRecive_Set_82Ack(u16 VariableAddr)
{
	DgusRecive82Ack.VariableAddr = VariableAddr;	
	DgusRecive82Ack.AckFlag = 0;
}

u8	DgusRecive_Get_83Ack(void)
{
	return DgusRecive83Ack.AckFlag;
}

void DgusRecive_Reset_83Ack(void)
{
	DgusRecive83Ack.AckFlag = 0;
}

void DgusRecive_Set_83Ack(u16 VariableAddr)
{
	DgusRecive83Ack.VariableAddr = VariableAddr;	
	DgusRecive83Ack.AckFlag = 0;
}


void Dgus_ReciveFrame_Task(DgusDataPack_TypeDef * pDgusDataRecivePack)
{
	u16	VariableAddr=0;
	
	//变量地址,0x5000~0xFFFF，1个变量地址对应2个字节
	VariableAddr = pDgusDataRecivePack->Data[0]*256+pDgusDataRecivePack->Data[1];
		
	
	
	switch(pDgusDataRecivePack->Cmd)
	{
		case DGUS_WRITE_CMD://写指令应答
		{
			DgusRecive82Ack.AckFlag = 1;
		}
		break;
		case DGUS_READ_CMD://读指令应答，触发上报
		{
			if(VariableAddr == DgusRecive83Ack.VariableAddr)
			{
				DgusRecive83Ack.AckFlag = 1;
			}
			
			switch(VariableAddr)
			{
				case 0x5500://机器管理登录账号
				{
					if(pDgusRecive_DeviceManageId_Callback)
						(*pDgusRecive_DeviceManageId_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5550://机器管理登录密码
				{		
					if(pDgusRecive_DeviceManagePwd_Callback)
						(*pDgusRecive_DeviceManagePwd_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5420://登录按钮上报
				{
					if(pDgusRecive_DeviceManageLogin_Callback)
						(*pDgusRecive_DeviceManageLogin_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5720://机器管理账号修改
				{
					if(pDgusRecive_DeviceManageFixId_Callback)
						(*pDgusRecive_DeviceManageFixId_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5730://机器管理密码修改
				{
					if(pDgusRecive_DeviceManageFixPwd_Callback)
						(*pDgusRecive_DeviceManageFixPwd_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5750://机器管理账号密码修改确认
				{
					if(pDgusRecive_DeviceManageFix_Callback)
						(*pDgusRecive_DeviceManageFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5780://旧机器编号
				{
					
				}
				break;
				case 0x5790://新机器编号
				{
					if(pDgusRecive_DeviceIdFix_Callback)
						(*pDgusRecive_DeviceIdFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5810://新机器编号确认
				{
					if(pDgusRecive_DeviceIdFixOk_Callback)
						(*pDgusRecive_DeviceIdFixOk_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5840://WIFI SSID
				{
					if(pDgusRecive_WifiSsidFix_Callback)
						(*pDgusRecive_WifiSsidFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5850://WIFI PWD
				{
					if(pDgusRecive_WifiPwdFix_Callback)
						(*pDgusRecive_WifiPwdFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5870://WIFI参数确认
				{
					if(pDgusRecive_WifiFixOk_Callback)
						(*pDgusRecive_WifiFixOk_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x58A0://TCP IP
				{
					if(pDgusRecive_TcpIpFix_Callback)
						(*pDgusRecive_TcpIpFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x58B0://TCP PORT
				{
					if(pDgusRecive_TcpPortFix_Callback)
						(*pDgusRecive_TcpPortFix_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x58D0://TCP参数确定
				{
					if(pDgusRecive_TcpFixOk_Callback)
						(*pDgusRecive_TcpFixOk_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5910://开锁
				{
					if(pDgusRecive_OpenLock_Callback)
						(*pDgusRecive_OpenLock_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x5930://出货日志
				{
					if(pDgusRecive_ShowHistoryStart_Callback)
						(*pDgusRecive_ShowHistoryStart_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;	
				case 0x7020://上一页
				{
					if(pDgusRecive_ShowHistoryLast_Callback)
						(*pDgusRecive_ShowHistoryLast_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				case 0x7030://下一页
				{
					if(pDgusRecive_ShowHistoryNext_Callback)
						(*pDgusRecive_ShowHistoryNext_Callback)(pDgusDataRecivePack->Data,(pDgusDataRecivePack->DataLenth-3));
				}
				break;
				default:break;
			}
		}
		break;
		default:break;
	}
}

void Dgus_ReciveByte_Task(u8 byte)
{
	u8 i=0;
	u16 crc16_a = 0;
	u16 crc16_b = 0;
	
	if(DgusDataRecivePackIndex < 1)
	{
		if(byte == 0x5A)
		{
			DgusDataRecivePackBuffer[DgusDataRecivePackIndex] = byte;
			DgusDataRecivePackIndex++;
			
		}
		else
		{
			DgusDataRecivePackIndex = 0;
		}
	}
	else if(DgusDataRecivePackIndex < 2)
	{
		if(byte == 0xA5)
		{
			DgusDataRecivePackBuffer[DgusDataRecivePackIndex] = byte;
			DgusDataRecivePackIndex++;
						
		}
		else
		{
			DgusDataRecivePackIndex = 0;
		}
	}
	else if(DgusDataRecivePackIndex < 3)
	{
		if(byte < 250)
		{
			DgusDataRecivePackBuffer[DgusDataRecivePackIndex] = byte;
			DgusDataRecivePackIndex++;
			
		}
		else
		{
			DgusDataRecivePackIndex = 0;
		}
	}
	else if(DgusDataRecivePackIndex < 4)
	{
		if(byte == 0x82 || byte == 0x83)
		{
			DgusDataRecivePackBuffer[DgusDataRecivePackIndex] = byte;
			DgusDataRecivePackIndex++;
		}
		else
		{
			DgusDataRecivePackIndex = 0;
		}
	}
	else 
	{
		if(DgusDataRecivePackIndex<255)
		{
			DgusDataRecivePackBuffer[DgusDataRecivePackIndex] = byte;
			DgusDataRecivePackIndex++;
		}
		else
		{
			DgusDataRecivePackIndex = 0;
		}
		
		if((DgusDataRecivePackIndex-3) >= DgusDataRecivePackBuffer[2])
		{
			crc16_a = CRC16_Toggle(&DgusDataRecivePackBuffer[3],(DgusDataRecivePackBuffer[2]-2));
			crc16_b = DgusDataRecivePackBuffer[DgusDataRecivePackIndex-2]*256
						+ DgusDataRecivePackBuffer[DgusDataRecivePackIndex-1];
			
			if(crc16_a == crc16_b)
			{
				DgusDataRecivePack.FixHead = DgusDataRecivePackBuffer[0]*256+DgusDataRecivePackBuffer[1];
				DgusDataRecivePack.DataLenth = DgusDataRecivePackBuffer[2];
				DgusDataRecivePack.Cmd = DgusDataRecivePackBuffer[3];
								
				for(i=0;i<(DgusDataRecivePack.DataLenth-3);i++)
				{
					DgusDataRecivePack.Data[i] = DgusDataRecivePackBuffer[4+i];
				}
				
				DgusDataRecivePack.Crc16 = crc16_b;
				DgusDataRecivePackIndex = 0;
				
				Dgus_ReciveFrame_Task(&DgusDataRecivePack);
			}
			else
			{
				DgusDataRecivePackIndex = 0;
			}			
		}

	}
}


void Dgus_Recive_Init(void)
{
	SerialDevice_Init(COM2);
	SerialDevice_SetReceiveByteCallBack(COM2,Dgus_ReciveByte_Task);
}