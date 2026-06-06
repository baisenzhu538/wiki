#include "dgus_app.h"



DgusApp_ShowQRCode_TypeDef	DgusAppShowQRCode;
DgusApp_ShowTemp_TypeDef	DgusAppShowTemp;
DgusApp_ShowTemp_TypeDef	DgusAppShowTemp2;
DgusApp_ShowNetSta_TypeDef	DgusAppShowNetSta;
DgusAppGotoPage_TypeDef	DgusAppGotoPage;
DgusAppUpTime_TypeDef	DgusAppUpTime;
DgusAppDeviceManageLogin_TypeDef	DgusAppDeviceManageLogin;
DgusAppDeviceId_TypeDef	DgusAppDeviceId;
DgusAppWifiPara_TypeDef	DgusAppWifiPara;
DgusAppTcpPara_TypeDef	DgusAppTcpPara;
DgusApp_ShowStoreSta_TypeDef	DgusAppShowStoreSta;


DgusAppShowHistoryManage_TypeDef	DgusAppShowHistoryManage;

void DgusApp_Recive_ShowHistoryStart(u8 * data,u8 size)
{
	DgusAppShowHistoryManage.page_no = 0;
	DgusAppShowHistoryManage.enable = 1;
}


void DgusApp_Recive_ShowHistoryNext(u8 * data,u8 size)
{
	DgusAppShowHistoryManage.lenth = History_Get_TableLenth();
	if(DgusAppShowHistoryManage.lenth - DgusAppShowHistoryManage.page_no*10)
	{
		DgusAppShowHistoryManage.page_no++;
		DgusAppShowHistoryManage.enable = 1;
	}
}

void DgusApp_Recive_ShowHistoryLast(u8 * data,u8 size)
{
	if(DgusAppShowHistoryManage.page_no)
		DgusAppShowHistoryManage.page_no--;
	DgusAppShowHistoryManage.enable = 1;
}

void DgusApp_ShowHistroyManage_Task(void)
{
//	Time_TypeDef		Time;
//	SellTaskStaTypeDef	TaskSta;
//	
//	if(DgusAppShowHistoryManage.enable)
//	{
//		switch(DgusAppShowHistoryManage.step)
//		{
//			case 0:
//			{
//				DgusAppShowHistoryManage.area_no = 0;
//				DgusAppShowHistoryManage.step = 1;
//			}
//			break;
//			case 1:
//			{
//				switch(DgusAppShowHistoryManage.area_no)
//				{
//					case 0x00:DgusControl_ClearText(0x5950,128);break;
//					case 0x01:DgusControl_ClearText(0x5A50,128);break;
//					case 0x02:DgusControl_ClearText(0x5B50,128);break;
//					case 0x03:DgusControl_ClearText(0x5C50,128);break;
//					case 0x04:DgusControl_ClearText(0x5D50,128);break;
//					case 0x05:DgusControl_ClearText(0x5E50,128);break;
//					case 0x06:DgusControl_ClearText(0x5F50,128);break;
//					case 0x07:DgusControl_ClearText(0x6050,128);break;
//					case 0x08:DgusControl_ClearText(0x6150,128);break;
//					case 0x09:DgusControl_ClearText(0x6250,128);break;
//					default:break;
//				}
//				DgusAppShowHistoryManage.step = 2;
//			}
//			break;
//			case 2:
//			{
//				if(DgusRecive_Get_82Ack())
//				{
//					CloudProtocol_Set_DeviceState(0);
//					
//					DgusAppShowHistoryManage.runtime = 0;
//					DgusAppShowHistoryManage.retry_cnt = 0;
//					
//					if(DgusAppShowHistoryManage.area_no<9)
//					{
//						DgusAppShowHistoryManage.area_no++;
//						DgusAppShowHistoryManage.step = 1;
//					}
//					else
//					{
//						DgusAppShowHistoryManage.area_no = 0;
//						DgusAppShowHistoryManage.step = 3;
//					}
//				}
//				else
//				{
//					if(DgusAppShowHistoryManage.runtime<1*100)
//					{
//						DgusAppShowHistoryManage.runtime++;
//					}
//					else
//					{
//						DgusAppShowHistoryManage.runtime = 0;
//						if(DgusAppShowHistoryManage.retry_cnt<1)
//						{
//							DgusAppShowHistoryManage.retry_cnt++;
//							DgusAppShowHistoryManage.step = 1;
//						}
//						else
//						{			
//							CloudProtocol_Set_DeviceState(104);
//							DgusAppShowHistoryManage.retry_cnt = 0;
//							DgusAppShowHistoryManage.step = 0;
//							DgusAppShowHistoryManage.enable = 0;
//						}
//					}
//				}
//			}
//			break;
//			
//			case 3:
//			{
//				DgusAppShowHistoryManage.lenth = History_Get_TableLenth();
//				DgusAppShowHistoryManage.head = History_Get_TableHead();
//				DgusAppShowHistoryManage.tail = History_Get_TableTail();
//				DgusAppShowHistoryManage.offset = DgusAppShowHistoryManage.page_no*10+DgusAppShowHistoryManage.head;
//				DgusAppShowHistoryManage.cnt =  DgusAppShowHistoryManage.offset;
//				
//				if(DgusAppShowHistoryManage.offset>DgusAppShowHistoryManage.tail
//					||DgusAppShowHistoryManage.lenth == 0)
//				{
//					DgusAppShowHistoryManage.retry_cnt = 0;
//					DgusAppShowHistoryManage.step = 0;
//					DgusAppShowHistoryManage.enable = 0;
//				}
//				else
//				{
//					DgusAppShowHistoryManage.step = 4;
//				}
//			}
//			break;
//			case 4:
//			{			
//				DgusAppShowHistoryManage.step = 5;				
//			}
//			break;
//			case 5:
//			{				
//				SellHistory_Get(DgusAppShowHistoryManage.cnt,&Time,&TaskSta);
//				
//				switch(DgusAppShowHistoryManage.area_no)
//				{
//					case 0:
//					{
//						DgusControl_ShowGoodsHistory(0x5950,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 1:
//					{
//						DgusControl_ShowGoodsHistory(0x5A50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 2:
//					{
//						DgusControl_ShowGoodsHistory(0x5B50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 3:
//					{
//						DgusControl_ShowGoodsHistory(0x5C50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 4:
//					{
//						DgusControl_ShowGoodsHistory(0x5D50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 5:
//					{
//						DgusControl_ShowGoodsHistory(0x5E50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 6:
//					{
//						DgusControl_ShowGoodsHistory(0x5F50,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 7:
//					{
//						DgusControl_ShowGoodsHistory(0x6050,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 8:
//					{
//						DgusControl_ShowGoodsHistory(0x6150,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					case 9:
//					{
//						DgusControl_ShowGoodsHistory(0x6250,
//													Time.year,
//													Time.month,
//													Time.day,
//													Time.hour,
//													Time.min,
//													Time.sec,
//													TaskSta.SellId.contain_no,
//													TaskSta.SellId.shelf_no,
//													TaskSta.SellId.cargo_no,
//													TaskSta.sta,
//													TaskSta.err[0],
//													TaskSta.err[1]);
//					}
//					break;
//					default:break;
//				}
//				DgusAppShowHistoryManage.step = 6;
//			}
//			break;
//			case 6:
//			{
//				if(DgusRecive_Get_82Ack())
//				{					
//					CloudProtocol_Set_DeviceState(0);
//					
//					if(DgusAppShowHistoryManage.cnt<(DgusAppShowHistoryManage.tail-1)
//						&&DgusAppShowHistoryManage.area_no<9)
//					{
//						DgusAppShowHistoryManage.cnt++;
//						DgusAppShowHistoryManage.area_no++;
//						DgusAppShowHistoryManage.runtime = 0;
//						DgusAppShowHistoryManage.retry_cnt = 0;
//						DgusAppShowHistoryManage.step = 5;
//					}
//					else
//					{
//						DgusAppShowHistoryManage.retry_cnt = 0;
//						DgusAppShowHistoryManage.step = 0;
//						DgusAppShowHistoryManage.enable = 0;
//					}
//				}
//				else
//				{
//					if(DgusAppShowHistoryManage.runtime<1*100)
//					{
//						DgusAppShowHistoryManage.runtime++;
//					}
//					else
//					{
//						DgusAppShowHistoryManage.runtime = 0;
//						if(DgusAppShowHistoryManage.retry_cnt<1)
//						{
//							DgusAppShowHistoryManage.retry_cnt++;
//							DgusAppShowHistoryManage.step = 5;
//						}
//						else
//						{
//							CloudProtocol_Set_DeviceState(104);
//							DgusAppShowHistoryManage.retry_cnt = 0;
//							DgusAppShowHistoryManage.step = 0;
//							DgusAppShowHistoryManage.enable = 0;
//						}
//					}
//				}
//			}
//			break;
//			default:break;
//		}
//	}
}

void DgusApp_Recive_OpenLock(u8 * data,u8 size)
{
	ElcLock_SetEnable();
}

void DgusApp_Recive_TcpIpFix(u8 * data,u8 size)
{
	u8	i;
	
	if(size == 0)
		return ;
	
	memset(DgusAppTcpPara.net.IPaddress,0,64);
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppTcpPara.net.IPaddress[i] = data[3+i];
		}
		else
			break;
	}
}

void DgusApp_Recive_TcpPortFix(u8 * data,u8 size)
{
	u8	i;
	
	if(size == 0)
		return ;
	
	memset(DgusAppTcpPara.net.port,0,10);
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppTcpPara.net.port[i] = data[3+i];
		}
		else
			break;
	}	
}

void DgusApp_Recive_TcpFixOk(u8 * data,u8 size)
{
	AuxConfig_UpNetWorkPara(&DgusAppTcpPara.net);
}

void DgusApp_Recive_WifiSsidFix(u8 * data,u8 size)
{
	u8	i;
	
	if(size == 0)
		return ;
	
	memset(DgusAppWifiPara.wifi.ssid,0,16);
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppWifiPara.wifi.ssid[i] = data[3+i];
		}
		else
			break;
	}
}

void DgusApp_Recive_WifiPwdFix(u8 * data,u8 size)
{
	u8	i;
	
	if(size == 0)
		return ;
	
	memset(DgusAppWifiPara.wifi.pwd,0,16);
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppWifiPara.wifi.pwd[i] = data[3+i];
		}
		else
			break;
	}	
}

void DgusApp_Recive_WifiFixOk(u8 * data,u8 size)
{
	AuxConfig_Up_WifiApPara(&DgusAppWifiPara.wifi);
}

void DgusApp_Recive_DeviceIdFix(u8 * data,u8 size)
{
	u8 i;
	
	if(size == 0 || size < 17)
		return ;
	
	for(i=0;i<24;i++)
	{
		DgusAppDeviceId.id[i] = data[3+i];
	}
}

void DgusApp_Recive_DeviceIdFixOk(u8 * data,u8 size)
{
	SysConfig_UP_DeviceId(DgusAppDeviceId.id,24);
	DgusControl_ClearText(0x5790,24);
}

void DgusApp_Recive_DeviceManageFixId(u8 * data,u8 size)
{
	u8 i;
	
	if(size == 0)
		return ;
	
	DgusAppDeviceManageLogin.input.id_size = 0;
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppDeviceManageLogin.input.id[i] = data[3+i];
			DgusAppDeviceManageLogin.input.id_size++;
		}
		else
			break;
	}
}

void DgusApp_Recive_DeviceManageFixPwd(u8 * data,u8 size)
{
	u8 i;
	
	if(size == 0)
		return ;
	
	DgusAppDeviceManageLogin.input.pwd_size = 0;
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppDeviceManageLogin.input.pwd[i] = data[3+i];
			DgusAppDeviceManageLogin.input.pwd_size++;
		}
		else
			break;
	}
}

void DgusApp_Recive_DeviceManageFix(u8 * data,u8 size)
{
	u8 i;	
	
	
	for(i=0;i<DgusAppDeviceManageLogin.input.id_size;i++)
	{
		DgusAppDeviceManageLogin.src.id[i] = DgusAppDeviceManageLogin.input.id[i];
	}
	
	DgusAppDeviceManageLogin.src.id_size = DgusAppDeviceManageLogin.input.id_size;
	
	for(i=0;i<DgusAppDeviceManageLogin.input.pwd_size;i++)
	{
		DgusAppDeviceManageLogin.src.pwd[i] = DgusAppDeviceManageLogin.input.pwd[i];
	}
	
	DgusAppDeviceManageLogin.src.pwd_size = DgusAppDeviceManageLogin.input.pwd_size;
	
	AuxConfig_Up_DgusLoginPara(&DgusAppDeviceManageLogin.src);
}

void DgusApp_Recive_DeviceManageId(u8 * data,u8 size)
{
	u8 i;
	
	if(size == 0)
		return ;
	
	DgusAppDeviceManageLogin.input.id_size = 0;
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppDeviceManageLogin.input.id[i] = data[3+i];
			DgusAppDeviceManageLogin.input.id_size++;
		}
		else
			break;
	}
	
}

void DgusApp_Recive_DeviceManagePwd(u8 * data,u8 size)
{
	u8 i;
	
	if(size == 0)
		return ;
	
	DgusAppDeviceManageLogin.input.pwd_size = 0;
	
	for(i=0;i<size-3;i++)
	{		
		if(data[3+i] != 0xFF)
		{
			DgusAppDeviceManageLogin.input.pwd[i] = data[3+i];
			DgusAppDeviceManageLogin.input.pwd_size++;
		}
		else
			break;
	}
	
}

void DgusApp_Recive_DeviceManageLogin(u8 * data,u8 size)
{
	
	DgusAppDeviceManageLogin.step = 0;
	DgusAppDeviceManageLogin.retry_cnt = 0;
	DgusAppDeviceManageLogin.runtime = 0;
	DgusAppDeviceManageLogin.login_flag = 1;
}

void DgusApp_Login_Task(void)
{
	u8 i;
	
	if(DgusAppDeviceManageLogin.login_flag)
	{
		switch(DgusAppDeviceManageLogin.step)
		{
			case 0x00:
			{
				if(DgusAppDeviceManageLogin.src.id_size != DgusAppDeviceManageLogin.input.id_size
					||DgusAppDeviceManageLogin.src.pwd_size != DgusAppDeviceManageLogin.input.pwd_size)
				{
					DgusAppDeviceManageLogin.runtime = 0;
					DgusAppDeviceManageLogin.retry_cnt = 0;
					DgusAppDeviceManageLogin.step = 0;
					DgusAppDeviceManageLogin.login_flag = 0;
					return ;
				}
				
				for(i=0;i<DgusAppDeviceManageLogin.src.id_size;i++)
				{
					if(DgusAppDeviceManageLogin.src.id[i] != DgusAppDeviceManageLogin.input.id[i])
					{
						DgusAppDeviceManageLogin.runtime = 0;
						DgusAppDeviceManageLogin.retry_cnt = 0;
						DgusAppDeviceManageLogin.step = 0;
						DgusAppDeviceManageLogin.login_flag = 0;
						return ;
					}
				}
				
				for(i=0;i<DgusAppDeviceManageLogin.src.pwd_size;i++)
				{
					if(DgusAppDeviceManageLogin.src.pwd[i] != DgusAppDeviceManageLogin.input.pwd[i])
					{
						DgusAppDeviceManageLogin.runtime = 0;
						DgusAppDeviceManageLogin.retry_cnt = 0;
						DgusAppDeviceManageLogin.step = 0;
						DgusAppDeviceManageLogin.login_flag = 0;
						return ;
					}
				}
				
				DgusAppDeviceManageLogin.step = 1;
				
				memset(DgusAppDeviceManageLogin.input.id,0,20);
				DgusAppDeviceManageLogin.input.id_size = 0;
				
				memset(DgusAppDeviceManageLogin.input.pwd,0,20);
				DgusAppDeviceManageLogin.input.pwd_size = 0;
			}
			break;
			case 0x01:
			{
				DgusControl_ClearText(0x5500,20);
								
				DgusAppDeviceManageLogin.step = 2;
			}
			break;
			case 0x02:
			{
				DgusControl_ClearText(0x5550,20);
				
				DgusAppDeviceManageLogin.step = 3;
			}
			break;
			case 0x03:
			{
				DgusControl_ClearText(0x5720,20);	
				DgusAppDeviceManageLogin.step = 4;
			}
			break;
			case 0x04:
			{
				DgusControl_ClearText(0x5730,20);	
				DgusAppDeviceManageLogin.step = 5;
			}
			break;
			case 0x05:
			{
				DgusControl_ClearText(0x5790,32);	
				DgusAppDeviceManageLogin.step = 6;
			}
			break;
			case 0x06:
			{
				DgusControl_ClearText(0x5840,20);	
				DgusAppDeviceManageLogin.step = 7;
			}
			break;
			case 0x07:
			{
				DgusControl_ClearText(0x5850,20);	
				DgusAppDeviceManageLogin.step = 8;
			}
			break;
			case 0x08:
			{
				DgusControl_ClearText(0x58A0,32);	
				DgusAppDeviceManageLogin.step = 9;
			}
			break;
			case 0x09:
			{
				DgusControl_ClearText(0x58B0,10);	
				DgusAppDeviceManageLogin.step = 0x0A;
			}
			break;
			case 0x0A:
			{				
				DgusControl_GotoPage(2);
				DgusAppDeviceManageLogin.step = 0x0B;
			}
			break;
			case 0x0B:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppDeviceManageLogin.runtime = 0;
					DgusAppDeviceManageLogin.retry_cnt = 0;
					DgusAppDeviceManageLogin.step = 0;
					DgusAppDeviceManageLogin.login_flag = 0;
				}
				else
				{
					if(DgusAppDeviceManageLogin.runtime<1*100)
					{
						DgusAppDeviceManageLogin.runtime++;
					}
					else
					{
						DgusAppDeviceManageLogin.runtime = 0;
						if(DgusAppDeviceManageLogin.retry_cnt<2)
						{
							DgusAppDeviceManageLogin.retry_cnt++;
							DgusAppDeviceManageLogin.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppDeviceManageLogin.retry_cnt = 0;
							DgusAppDeviceManageLogin.step = 0;
							DgusAppDeviceManageLogin.login_flag = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

void DgusApp_Set_Time(u8 year,u8 month,u8 day,u8 week,u8 hour,u8 min,u8 sec)
{
	DgusAppUpTime.year = year;
	DgusAppUpTime.month = month;
	DgusAppUpTime.day = day;
	DgusAppUpTime.week = week;
	DgusAppUpTime.hour = hour;
	DgusAppUpTime.min = min;
	DgusAppUpTime.sec = sec;
	DgusAppUpTime.step = 0;
	DgusAppUpTime.retry_cnt = 0;
	DgusAppUpTime.runtime = 0;
	DgusAppUpTime.enable = 1;
}

void DgusApp_UpTime_Task(void)
{
	if(DgusAppUpTime.enable)
	{
		switch(DgusAppUpTime.step)
		{
			case 0:
			{
				DgusControl_UpTime(DgusAppUpTime.year,
									DgusAppUpTime.month,
									DgusAppUpTime.day,
									DgusAppUpTime.week,
									DgusAppUpTime.hour,
									DgusAppUpTime.min,
									DgusAppUpTime.sec);
				DgusAppUpTime.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppUpTime.runtime = 0;
					DgusAppUpTime.retry_cnt = 0;
					DgusAppUpTime.step = 0;
					DgusAppUpTime.enable = 0;
				}
				else
				{
					if(DgusAppUpTime.runtime<1*100)
					{
						DgusAppUpTime.runtime++;
					}
					else
					{
						DgusAppUpTime.runtime = 0;
						if(DgusAppUpTime.retry_cnt<2)
						{
							DgusAppUpTime.retry_cnt++;
							DgusAppUpTime.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppUpTime.retry_cnt = 0;
							DgusAppUpTime.step = 0;
							DgusAppUpTime.enable = 0;
						}
					}
				}
			}
			break;
		}
	}
}

void DgusApp_Set_Temp2(u8 temp)
{
	DgusAppShowTemp2.temp = temp;
	DgusAppShowTemp2.step = 0;
	DgusAppShowTemp2.retry_cnt =0;
	DgusAppShowTemp2.runtime =0;
	DgusAppShowTemp2.enable = 1;
}

void DgusApp_ShowTemp_Task2(void)
{
	if(DgusAppShowTemp2.enable)
	{
		switch(DgusAppShowTemp2.step)
		{
			case 0:
			{				
				DgusControl_ShowTemp2(DgusAppShowTemp2.temp);
				DgusAppShowTemp2.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowTemp2.runtime = 0;
					DgusAppShowTemp2.retry_cnt = 0;
					DgusAppShowTemp2.step = 0;
					DgusAppShowTemp2.enable = 0;
				}
				else
				{
					if(DgusAppShowTemp2.runtime<1*100)
					{
						DgusAppShowTemp2.runtime++;
					}
					else
					{
						DgusAppShowTemp2.runtime = 0;
						if(DgusAppShowTemp2.retry_cnt<2)
						{
							DgusAppShowTemp2.retry_cnt++;
							DgusAppShowTemp2.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowTemp2.retry_cnt = 0;
							DgusAppShowTemp2.step = 0;
							DgusAppShowTemp2.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}	
}

void DgusApp_Set_Temp(u8 temp)
{
	DgusAppShowTemp.temp = temp;
	DgusAppShowTemp.step = 0;
	DgusAppShowTemp.retry_cnt =0;
	DgusAppShowTemp.runtime =0;
	DgusAppShowTemp.enable = 1;
}

void DgusApp_ShowTemp_Task(void)
{
	if(DgusAppShowTemp.enable)
	{
		switch(DgusAppShowTemp.step)
		{
			case 0:
			{				
				DgusControl_ShowTemp(DgusAppShowTemp.temp);
				DgusAppShowTemp.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowTemp.runtime = 0;
					DgusAppShowTemp.retry_cnt = 0;
					DgusAppShowTemp.step = 0;
					DgusAppShowTemp.enable = 0;
				}
				else
				{
					if(DgusAppShowTemp.runtime<1*100)
					{
						DgusAppShowTemp.runtime++;
					}
					else
					{
						DgusAppShowTemp.runtime = 0;
						if(DgusAppShowTemp.retry_cnt<2)
						{
							DgusAppShowTemp.retry_cnt++;
							DgusAppShowTemp.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowTemp.retry_cnt = 0;
							DgusAppShowTemp.step = 0;
							DgusAppShowTemp.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}	
}

void DgusApp_Set_StoreSta(u8 sta)
{
	DgusAppShowStoreSta.sta = sta;
	DgusAppShowStoreSta.step = 0;
	DgusAppShowStoreSta.retry_cnt = 0;
	DgusAppShowStoreSta.runtime = 0;
	DgusAppShowStoreSta.enable = 1;
}

void DgusApp_ShowStoreSta_Task(void)
{
	if(DgusAppShowStoreSta.enable)
	{
		switch(DgusAppShowStoreSta.step)
		{
			case 0:
			{
				DgusControl_ShowStoreSta(DgusAppShowStoreSta.sta);
				DgusAppShowStoreSta.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowStoreSta.runtime = 0;
					DgusAppShowStoreSta.retry_cnt = 0;
					DgusAppShowStoreSta.step = 0;
					DgusAppShowStoreSta.enable = 0;
				}
				else
				{
					if(DgusAppShowStoreSta.runtime<1*100)
					{
						DgusAppShowStoreSta.runtime++;
					}
					else
					{
						DgusAppShowStoreSta.runtime = 0;
						if(DgusAppShowStoreSta.retry_cnt<2)
						{
							DgusAppShowStoreSta.retry_cnt++;
							DgusAppShowStoreSta.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowStoreSta.retry_cnt = 0;
							DgusAppShowStoreSta.step = 0;
							DgusAppShowStoreSta.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}



DgusAppShowSystemErrorInfo_TypeDef	DgusAppShowSystemErrorInfo;

void DgusApp_Set_ShowSystemErrorInfo(int state)
{
	DgusAppShowSystemErrorInfo.step = 0;
	DgusAppShowSystemErrorInfo.retry_cnt = 0;
	DgusAppShowSystemErrorInfo.runtime = 0;
	DgusAppShowSystemErrorInfo.state = state;
	DgusAppShowSystemErrorInfo.enable = 1;
}

void DgusApp_ShowSystemErrorInfo_Task(void)
{
	if(DgusAppShowSystemErrorInfo.enable)
	{
		switch(DgusAppShowSystemErrorInfo.step)
		{
			case 0:
			{	
				DgusControl_ShowSystemErrorInfo(DgusAppShowSystemErrorInfo.state);
				DgusAppShowSystemErrorInfo.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSystemErrorInfo.runtime = 0;
					DgusAppShowSystemErrorInfo.retry_cnt = 0;
					DgusAppShowSystemErrorInfo.step = 0;
					DgusAppShowSystemErrorInfo.enable = 0;
				}
				else
				{
					if(DgusAppShowSystemErrorInfo.runtime<1*100)
					{
						DgusAppShowSystemErrorInfo.runtime++;
					}
					else
					{
						DgusAppShowSystemErrorInfo.runtime = 0;
						if(DgusAppShowSystemErrorInfo.retry_cnt<2)
						{
							DgusAppShowSystemErrorInfo.retry_cnt++;
							DgusAppShowSystemErrorInfo.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSystemErrorInfo.retry_cnt = 0;
							DgusAppShowSystemErrorInfo.step = 0;
							DgusAppShowSystemErrorInfo.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

DgusAppShowSellErrorInfo_TypeDef	DgusAppShowSellErrorInfo;

void DgusApp_Set_ShowSellErrorInfo(int state)
{
	DgusAppShowSellErrorInfo.step = 0;
	DgusAppShowSellErrorInfo.retry_cnt = 0;
	DgusAppShowSellErrorInfo.runtime = 0;
	DgusAppShowSellErrorInfo.state = state;
	DgusAppShowSellErrorInfo.enable = 1;
}

void DgusApp_ShowSellErrorInfo_Task(void)
{
	if(DgusAppShowSellErrorInfo.enable)
	{
		switch(DgusAppShowSellErrorInfo.step)
		{
			case 0:
			{	
				DgusControl_ShowSellErrorInfo(DgusAppShowSellErrorInfo.state);
				DgusAppShowSellErrorInfo.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSellErrorInfo.runtime = 0;
					DgusAppShowSellErrorInfo.retry_cnt = 0;
					DgusAppShowSellErrorInfo.step = 0;
					DgusAppShowSellErrorInfo.enable = 0;
				}
				else
				{
					if(DgusAppShowSellErrorInfo.runtime<1*100)
					{
						DgusAppShowSellErrorInfo.runtime++;
					}
					else
					{
						DgusAppShowSellErrorInfo.runtime = 0;
						if(DgusAppShowSellErrorInfo.retry_cnt<2)
						{
							DgusAppShowSellErrorInfo.retry_cnt++;
							DgusAppShowSellErrorInfo.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSellErrorInfo.retry_cnt = 0;
							DgusAppShowSellErrorInfo.step = 0;
							DgusAppShowSellErrorInfo.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

DgusAppShowSellLog_TypeDef	DgusAppShowSellLog;

void DgusApp_Set_ShowSellLog(char * orderId)
{
	DgusAppShowSellLog.step = 0;
	DgusAppShowSellLog.retry_cnt = 0;
	DgusAppShowSellLog.runtime = 0;	

	SysMem_copy(DgusAppShowSellLog.orderId,orderId,12);

	DgusAppShowSellLog.enable = 1;
}

void DgusApp_ShowSellLog(void)
{
	if(DgusAppShowSellLog.enable)
	{
		switch(DgusAppShowSellLog.step)
		{
			case 0:
			{	
				DgusControl_ShowSellLogo(DgusAppShowSellLog.orderId);
				DgusAppShowSellLog.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSellLog.runtime = 0;
					DgusAppShowSellLog.retry_cnt = 0;
					DgusAppShowSellLog.step = 0;
					DgusAppShowSellLog.enable = 0;
				}
				else
				{
					if(DgusAppShowSellLog.runtime<1*100)
					{
						DgusAppShowSellLog.runtime++;
					}
					else
					{
						DgusAppShowSellLog.runtime = 0;
						if(DgusAppShowSellLog.retry_cnt<2)
						{
							DgusAppShowSellLog.retry_cnt++;
							DgusAppShowSellLog.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSellLog.retry_cnt = 0;
							DgusAppShowSellLog.step = 0;
							DgusAppShowSellLog.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

void DgusApp_Set_NetSta(u8 sta)
{
	DgusAppShowNetSta.sta = sta;
	DgusAppShowNetSta.step = 0;
	DgusAppShowNetSta.retry_cnt = 0;
	DgusAppShowNetSta.runtime = 0;
	DgusAppShowNetSta.enable = 1;
}
	
void DgusApp_ShowNetSta_Task(void)
{
	static u8 last_link = 0;
	
	  
	if(last_link != MQTT_Get_Start_Status())
	{
		last_link = MQTT_Get_Start_Status();
		DgusApp_Set_NetSta(last_link);
	}
	
	if(DgusAppShowNetSta.enable)
	{
		switch(DgusAppShowNetSta.step)
		{
			case 0:
			{				
				DgusControl_ShowNetSta(DgusAppShowNetSta.sta);
				DgusAppShowNetSta.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowNetSta.runtime = 0;
					DgusAppShowNetSta.retry_cnt = 0;
					DgusAppShowNetSta.step = 0;
					DgusAppShowNetSta.enable = 0;
				}
				else
				{
					if(DgusAppShowNetSta.runtime<1*100)
					{
						DgusAppShowNetSta.runtime++;
					}
					else
					{
						DgusAppShowNetSta.runtime = 0;
						if(DgusAppShowNetSta.retry_cnt<2)
						{
							DgusAppShowNetSta.retry_cnt++;
							DgusAppShowNetSta.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowNetSta.retry_cnt = 0;
							DgusAppShowNetSta.step = 0;
							DgusAppShowNetSta.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}




void DgusApp_Set_GotoPage(u8 page_no)
{
	DgusAppGotoPage.step = 0;
	DgusAppGotoPage.runtime = 0;
	DgusAppGotoPage.retry_cnt = 0;
	DgusAppGotoPage.page_no = page_no;
	DgusAppGotoPage.enable = 1;
}

void DgusApp_ShowGotoPage_Task(void)
{
	static u8 last_link = 0;
	static u8 last_doorsta = 0;
	static u8 last_rssi = 0;
	
	if(!DigitalSignal_ReadCodeId())
	{
		if(MotorTest_Get_Mode() == 0)
		{
			if(CloudProtocol_Get_DeviceState_DoorState())
			{
				if(!last_doorsta)
				{
					last_doorsta = 1;
					DgusApp_Set_GotoPage(9);
				}
			}
			else
			{
				if(last_link != MQTT_Get_Start_Status()
					||last_doorsta
					||last_rssi != WirelessModule_ReadRssiSta())
				{
					last_rssi = WirelessModule_ReadRssiSta();
					last_link = MQTT_Get_Start_Status();
					last_doorsta = 0;
					
					if(MQTT_Get_Start_Status())
					{			
						if(SysConfig_Get_StoreState())
						{
							if(WirelessModule_ReadRssiSta())
							{
								DgusApp_Set_GotoPage(2);
							}
							else
							{
								DgusApp_Set_GotoPage(3);
							}
						}
						else
						{
							if(SysConfig_Get_QrCodeSize())
							{
								DgusApp_Set_GotoPage(5);
							}
							else
							{
								DgusApp_Set_GotoPage(4);
							}
						}
					}
					else
					{
						DgusApp_Set_GotoPage(0);
					}
				}
			}
		}
	}
	if(DgusAppGotoPage.enable)
	{
		switch(DgusAppGotoPage.step)
		{
			case 0:
			{
				DgusControl_GotoPage(DgusAppGotoPage.page_no);
				DgusAppGotoPage.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppGotoPage.runtime = 0;
					DgusAppGotoPage.retry_cnt = 0;
					DgusAppGotoPage.step = 0;
					DgusAppGotoPage.enable = 0;
				}
				else
				{
					if(DgusAppGotoPage.runtime<1*100)
					{
						DgusAppGotoPage.runtime++;
					}
					else
					{
						DgusAppGotoPage.runtime = 0;
						if(DgusAppGotoPage.retry_cnt<2)
						{
							DgusAppGotoPage.retry_cnt++;
							DgusAppGotoPage.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppGotoPage.retry_cnt = 0;
							DgusAppGotoPage.step = 0;
							DgusAppGotoPage.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

typedef	struct
{
	u8	enable;
	u8	step;
	u16	runtime;
	u8	retry_cnt;
	u8	row;
	u8	list;
	u8	motor_err;
}DgusAppShowSellTest_TypeDef;

DgusAppShowSellTest_TypeDef	DgusAppShowSellTest;

void DgusApp_Set_ShowSellTest(u8 row,u8 list,u8 motor_err)
{
	if(DgusAppShowSellTest.enable)
		return ;
	DgusAppShowSellTest.step = 0;
	DgusAppShowSellTest.runtime = 0;
	DgusAppShowSellTest.retry_cnt = 0;
	DgusAppShowSellTest.row = row;
	DgusAppShowSellTest.list = list;
	DgusAppShowSellTest.motor_err = motor_err;
	DgusAppShowSellTest.enable = 1;
}

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
}DgusAppClearMotorCheck_TypeDef;

DgusAppClearMotorCheck_TypeDef	DgusAppClearMotorCheck;

void DgusApp_Set_ClearMotorCheck(void)
{
	if(DgusAppClearMotorCheck.enable)
		return ;
	DgusAppClearMotorCheck.enable = 1;
}

void DgusApp_ClearMotorCheck_Task(void)
{
	if(DgusAppClearMotorCheck.enable)
	{
		switch(DgusAppClearMotorCheck.step)
		{
			case 0:
			{				
				DgusControl_ClearMotorCheck();
				DgusAppClearMotorCheck.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppClearMotorCheck.runtime = 0;
					DgusAppClearMotorCheck.retry_cnt = 0;
					DgusAppClearMotorCheck.step = 0;
					DgusAppClearMotorCheck.enable = 0;
				}
				else
				{
					if(DgusAppClearMotorCheck.runtime<1*100)
					{
						DgusAppClearMotorCheck.runtime++;
					}
					else
					{
						DgusAppClearMotorCheck.runtime = 0;
						if(DgusAppClearMotorCheck.retry_cnt<2)
						{
							DgusAppClearMotorCheck.retry_cnt++;
							DgusAppClearMotorCheck.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppClearMotorCheck.retry_cnt = 0;
							DgusAppClearMotorCheck.step = 0;
							DgusAppClearMotorCheck.enable = 0;
						}
					}
				}
			}
			break;
		}
	}
}

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
}DgusAppClearIrCheck_TypeDef;

DgusAppClearIrCheck_TypeDef	DgusAppClearIrCheck;

void DgusApp_Set_ClearIrCheck(void)
{
	if(DgusAppClearIrCheck.enable)
		return ;
	DgusAppClearIrCheck.enable = 1;
}

void DgusApp_ClearIrCheck_Task(void)
{
	if(DgusAppClearIrCheck.enable)
	{
		switch(DgusAppClearIrCheck.step)
		{
			case 0:
			{				
				DgusControl_ClearIrCheck();
				DgusAppClearIrCheck.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppClearIrCheck.runtime = 0;
					DgusAppClearIrCheck.retry_cnt = 0;
					DgusAppClearIrCheck.step = 0;
					DgusAppClearIrCheck.enable = 0;
				}
				else
				{
					if(DgusAppClearIrCheck.runtime<1*100)
					{
						DgusAppClearIrCheck.runtime++;
					}
					else
					{
						DgusAppClearIrCheck.runtime = 0;
						if(DgusAppClearIrCheck.retry_cnt<2)
						{
							DgusAppClearIrCheck.retry_cnt++;
							DgusAppClearIrCheck.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppClearIrCheck.retry_cnt = 0;
							DgusAppClearIrCheck.step = 0;
							DgusAppClearIrCheck.enable = 0;
						}
					}
				}
			}
			break;
		}
	}
}

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u8	sta;	
	u16	runtime;
}DgusAppShowMotorCheck_TypeDef;

DgusAppShowMotorCheck_TypeDef	DgusAppShowMotorCheck;

void DgusApp_Set_ShowMotorCheck(u8 sta)
{
	if(DgusAppShowMotorCheck.enable)
		return ;
	DgusAppShowMotorCheck.sta = sta;
	DgusAppShowMotorCheck.enable = 1;
}

void DgusApp_ShowMotorCheck_Task(void)
{
	if(DgusAppShowMotorCheck.enable)
	{
		switch(DgusAppShowMotorCheck.step)
		{
			case 0:
			{				
				DgusControl_ShowMotorCheckColor(DgusAppShowMotorCheck.sta);

				DgusAppShowMotorCheck.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowMotorCheck.runtime = 0;
					DgusAppShowMotorCheck.retry_cnt = 0;
					DgusAppShowMotorCheck.step = 2;
//					DgusAppShowIrCheck.enable = 0;
				}
				else
				{
					if(DgusAppShowMotorCheck.runtime<1*100)
					{
						DgusAppShowMotorCheck.runtime++;
					}
					else
					{
						DgusAppShowMotorCheck.runtime = 0;
						if(DgusAppShowMotorCheck.retry_cnt<2)
						{
							DgusAppShowMotorCheck.retry_cnt++;
							DgusAppShowMotorCheck.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowMotorCheck.retry_cnt = 0;
							DgusAppShowMotorCheck.step = 0;
							DgusAppShowMotorCheck.enable = 0;
						}
					}
				}
			}
			break;
			case 2:
			{				
				DgusControl_ShowMotorCheck(DgusAppShowMotorCheck.sta);
				DgusAppShowMotorCheck.step = 3;
			}
			break;
			case 3:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowMotorCheck.runtime = 0;
					DgusAppShowMotorCheck.retry_cnt = 0;
					DgusAppShowMotorCheck.step = 0;
					DgusAppShowMotorCheck.enable = 0;
				}
				else
				{
					if(DgusAppShowMotorCheck.runtime<1*100)
					{
						DgusAppShowMotorCheck.runtime++;
					}
					else
					{
						DgusAppShowMotorCheck.runtime = 0;
						if(DgusAppShowMotorCheck.retry_cnt<2)
						{
							DgusAppShowMotorCheck.retry_cnt++;
							DgusAppShowMotorCheck.step = 2;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowMotorCheck.retry_cnt = 0;
							DgusAppShowMotorCheck.step = 0;
							DgusAppShowMotorCheck.enable = 0;
						}
					}
				}
			}
			break;
		}
	}
}

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u8	sta;	
	u16	runtime;
}DgusAppShowIrCheck_TypeDef;

DgusAppShowIrCheck_TypeDef	DgusAppShowIrCheck;

void DgusApp_Set_ShowIrCheck(u8 sta)
{
	if(DgusAppShowIrCheck.enable)
		return ;
	DgusAppShowIrCheck.sta = sta;
	DgusAppShowIrCheck.enable = 1;
}

void DgusApp_ShowIrCheck_Task(void)
{
	if(DgusAppShowIrCheck.enable)
	{
		switch(DgusAppShowIrCheck.step)
		{
			case 0:
			{				
				DgusControl_ShowIrCheckColor(DgusAppShowIrCheck.sta);

				DgusAppShowIrCheck.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowIrCheck.runtime = 0;
					DgusAppShowIrCheck.retry_cnt = 0;
					DgusAppShowIrCheck.step = 2;
//					DgusAppShowIrCheck.enable = 0;
				}
				else
				{
					if(DgusAppShowIrCheck.runtime<1*100)
					{
						DgusAppShowIrCheck.runtime++;
					}
					else
					{
						DgusAppShowIrCheck.runtime = 0;
						if(DgusAppShowIrCheck.retry_cnt<2)
						{
							DgusAppShowIrCheck.retry_cnt++;
							DgusAppShowIrCheck.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowIrCheck.retry_cnt = 0;
							DgusAppShowIrCheck.step = 0;
							DgusAppShowIrCheck.enable = 0;
						}
					}
				}
			}
			break;
			case 2:
			{				
				DgusControl_ShowIrCheck(DgusAppShowIrCheck.sta);
				DgusAppShowIrCheck.step = 3;
			}
			break;
			case 3:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowIrCheck.runtime = 0;
					DgusAppShowIrCheck.retry_cnt = 0;
					DgusAppShowIrCheck.step = 0;
					DgusAppShowIrCheck.enable = 0;
				}
				else
				{
					if(DgusAppShowIrCheck.runtime<1*100)
					{
						DgusAppShowIrCheck.runtime++;
					}
					else
					{
						DgusAppShowIrCheck.runtime = 0;
						if(DgusAppShowIrCheck.retry_cnt<2)
						{
							DgusAppShowIrCheck.retry_cnt++;
							DgusAppShowIrCheck.step = 2;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowIrCheck.retry_cnt = 0;
							DgusAppShowIrCheck.step = 0;
							DgusAppShowIrCheck.enable = 0;
						}
					}
				}
			}
			break;
		}
	}
}

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u8	row;
	u8	list;
}DgusAppShowSellReset_TypeDef;

DgusAppShowSellReset_TypeDef	DgusAppShowSellReset;

void DgusApp_Set_ShowSellReset(void)
{
	if(DgusAppShowSellReset.enable)
		return ;
	DgusAppShowSellReset.enable = 1;
}

void DgusApp_ShowSellReset_Task(void)
{
	if(DgusAppShowSellReset.enable)
	{
		switch(DgusAppShowSellReset.step)
		{
			case 0:
			{
				DgusControl_ShowSellReset(DgusAppShowSellReset.row,DgusAppShowSellReset.list);
				DgusAppShowSellReset.runtime = 0;
				DgusAppShowSellReset.retry_cnt = 0;
				DgusAppShowSellReset.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSellReset.runtime = 0;
					DgusAppShowSellReset.retry_cnt = 0;
					DgusAppShowSellReset.step = 2;
//					DgusAppShowSellReset.enable = 0;
				}
				else
				{
					if(DgusAppShowSellReset.runtime<1*100)
					{
						DgusAppShowSellReset.runtime++;
					}
					else
					{
						DgusAppShowSellReset.runtime = 0;
						if(DgusAppShowSellReset.retry_cnt<2)
						{
							DgusAppShowSellReset.retry_cnt++;
							DgusAppShowSellReset.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSellReset.retry_cnt = 0;
							DgusAppShowSellReset.step = 0;
							DgusAppShowSellReset.enable = 0;
						}
					}
				}
			}
			break;
			case 2:
			{
				if(DgusAppShowSellReset.row == 0)
				{
					if(DgusAppShowSellReset.list<3)
					{
						DgusAppShowSellReset.list++;
					}
					else
					{
						DgusAppShowSellReset.list = 0;
						DgusAppShowSellReset.row++;
					}
					DgusAppShowSellReset.step = 0;
				}
				else if(DgusAppShowSellReset.row == 1)
				{
					if(DgusAppShowSellReset.list<10)
					{
						DgusAppShowSellReset.list++; 
					}
					else
					{
						DgusAppShowSellReset.list = 0;
						DgusAppShowSellReset.row++;
					}
					DgusAppShowSellReset.step = 0;
				}
				else if(DgusAppShowSellReset.row == 2)
				{
					if(DgusAppShowSellReset.list<10)
					{
						DgusAppShowSellReset.list++;
					}
					else
					{
						DgusAppShowSellReset.list = 0;
						DgusAppShowSellReset.row++;
					}
					DgusAppShowSellReset.step = 0;
				}
				else if(DgusAppShowSellReset.row == 3)
				{
					if(DgusAppShowSellReset.list<10)
					{
						DgusAppShowSellReset.list++;
					}
					else
					{
						DgusAppShowSellReset.list = 0;
						DgusAppShowSellReset.row++;
					}
					DgusAppShowSellReset.step = 0;
				}
				else if(DgusAppShowSellReset.row == 4)
				{
					if(DgusAppShowSellReset.list<5)
					{
						DgusAppShowSellReset.list++;
					}
					else
					{
						DgusAppShowSellReset.list = 0;
						DgusAppShowSellReset.row++;
					}
					DgusAppShowSellReset.step = 0;
				}
				else
				{
					DgusAppShowSellReset.row = 0;
					DgusAppShowSellReset.list = 0;
					DgusAppShowSellReset.step = 0;
					DgusAppShowSellReset.enable = 0;
				}
			}
			break;
		}
	}
}

void DgusApp_ShowSellTest_Task(void)
{
	if(DgusAppShowSellTest.enable)
	{
		switch(DgusAppShowSellTest.step)
		{
			case 0:
			{
				DgusControl_ShowSellTest(DgusAppShowSellTest.row,
										DgusAppShowSellTest.list,
										DgusAppShowSellTest.motor_err);
				DgusAppShowSellTest.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSellTest.runtime = 0;
					DgusAppShowSellTest.retry_cnt = 0;
					DgusAppShowSellTest.step = 2;
//					DgusAppShowSellTest.enable = 0;
				}
				else
				{
					if(DgusAppShowSellTest.runtime<1*100)
					{
						DgusAppShowSellTest.runtime++;
					}
					else
					{
						DgusAppShowSellTest.runtime = 0;
						if(DgusAppShowSellTest.retry_cnt<2)
						{
							DgusAppShowSellTest.retry_cnt++;
							DgusAppShowSellTest.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSellTest.retry_cnt = 0;
							DgusAppShowSellTest.step = 0;
							DgusAppShowSellTest.enable = 0;
						}
					}
				}
			}
			break;
			case 2:
			{
				DgusControl_ShowSellColor(DgusAppShowSellTest.row,
										DgusAppShowSellTest.list,
										DgusAppShowSellTest.motor_err);
				DgusAppShowSellTest.step = 3;
			}
			break;
			case 3:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowSellTest.runtime = 0;
					DgusAppShowSellTest.retry_cnt = 0;
					DgusAppShowSellTest.step = 0;
					DgusAppShowSellTest.enable = 0;
				}
				else
				{
					if(DgusAppShowSellTest.runtime<1*100)
					{
						DgusAppShowSellTest.runtime++;
					}
					else
					{
						DgusAppShowSellTest.runtime = 0;
						if(DgusAppShowSellTest.retry_cnt<2)
						{
							DgusAppShowSellTest.retry_cnt++;
							DgusAppShowSellTest.step = 2;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowSellTest.retry_cnt = 0;
							DgusAppShowSellTest.step = 0;
							DgusAppShowSellTest.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}

void DgusApp_Set_QRCode(u8 * qrcode,u8 size)
{
	u8 i;
	
	DgusAppShowQRCode.qrcode_size = size;
	
	for(i=0;i<size;i++)
	{
		DgusAppShowQRCode.qrcode[i] = *(qrcode+i);
	}
	
	DgusAppShowQRCode.step = 0;
	DgusAppShowQRCode.runtime = 0;
	DgusAppShowQRCode.retry_cnt = 0;
	DgusAppShowQRCode.enable = 1;
}

void DgusApp_ShowQRCode_Task(void)
{
	//发送指令
	//等待应答，重发。
	
	if(DgusAppShowQRCode.enable)
	{
		switch(DgusAppShowQRCode.step)
		{
			case 0:
			{
				DgusControl_ShowQRCode(DgusAppShowQRCode.qrcode,
										DgusAppShowQRCode.qrcode_size);
				DgusAppShowQRCode.step = 1;
			}
			break;
			case 1:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowQRCode.runtime = 0;
					DgusAppShowQRCode.retry_cnt = 0;
					DgusAppShowQRCode.step = 0;
					DgusAppShowQRCode.enable = 0;
				}
				else
				{
					if(DgusAppShowQRCode.runtime<1*100)
					{
						DgusAppShowQRCode.runtime++;
					}
					else
					{
						DgusAppShowQRCode.runtime = 0;
						if(DgusAppShowQRCode.retry_cnt<2)
						{
							DgusAppShowQRCode.retry_cnt++;
							DgusAppShowQRCode.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowQRCode.retry_cnt = 0;
							DgusAppShowQRCode.step = 0;
							DgusAppShowQRCode.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}






DgusApp_ShowDeviceId_TypeDef	DgusAppShowDeviceId;

void DgusApp_Set_DeviceId(u8 * DeviceId)
{
	u8 i;
	
	DgusAppShowDeviceId.step = 0;
	DgusAppShowDeviceId.retry_cnt = 0;
	DgusAppShowDeviceId.runtime = 0;
	
	for(i=0;i<32;i++)
	{
		DgusAppShowDeviceId.DeviceId[i] = *(DeviceId+i);
	}
	
	DgusAppShowDeviceId.enable = 1;
}

void DgusApp_ShowDeviceId_Task(void)
{
	if(DgusAppShowDeviceId.enable)
	{
		switch(DgusAppShowDeviceId.step)
		{
			case 0x00:
			{
				DgusControl_ShowDeviceId(DgusAppShowDeviceId.DeviceId);
				DgusAppShowDeviceId.step = 1;
			}
			break;
			case 0x01:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowDeviceId.runtime = 0;
					DgusAppShowDeviceId.retry_cnt = 0;
					DgusAppShowDeviceId.step = 0;
					DgusAppShowDeviceId.enable = 0;
				}
				else
				{
					if(DgusAppShowDeviceId.runtime<1*100)
					{
						DgusAppShowDeviceId.runtime++;
					}
					else
					{
						DgusAppShowDeviceId.runtime = 0;
						if(DgusAppShowDeviceId.retry_cnt<2)
						{
							DgusAppShowDeviceId.retry_cnt++;
							DgusAppShowDeviceId.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowDeviceId.retry_cnt = 0;
							DgusAppShowDeviceId.step = 0;
							DgusAppShowDeviceId.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
}




DgusAppShowHistory_TypeDef	DgusAppShowHistory;


u8 DgusApp_GetShowHistory_Enable(void)
{
	return DgusAppShowHistory.enable;
}

void DgusApp_SetShowHistory(u16 addr,u16 year,u8 month,u8 day,u8 hour,u8 min,u8 sec,u8 contain_no,u8 shelf_no,u8 cargo_no,u8 sta,u8 err1,u8 err2)
{
	DgusAppShowHistory.step = 0;
	DgusAppShowHistory.retry_cnt = 0;
	DgusAppShowHistory.runtime = 0;
	DgusAppShowHistory.addr = addr;
	DgusAppShowHistory.year = year;
	DgusAppShowHistory.month = month;
	DgusAppShowHistory.day = day;
	DgusAppShowHistory.hour = hour;
	DgusAppShowHistory.min = min;
	DgusAppShowHistory.sec = sec;
	DgusAppShowHistory.contain_no = contain_no;
	DgusAppShowHistory.shelf_no = shelf_no;
	DgusAppShowHistory.cargo_no = cargo_no;
	DgusAppShowHistory.sta = sta;
	DgusAppShowHistory.err1 = err1;
	DgusAppShowHistory.err2 = err2;
	DgusAppShowHistory.enable = 1;
}

void DgusApp_ShowHistory_Task(void)
{
	if(DgusAppShowHistory.enable)
	{
		switch(DgusAppShowHistory.step)
		{
			case 0x00:
			{
				DgusControl_ShowGoodsHistory(DgusAppShowHistory.addr,
											DgusAppShowHistory.year,
											DgusAppShowHistory.month,
											DgusAppShowHistory.day,
											DgusAppShowHistory.hour,
											DgusAppShowHistory.min,
											DgusAppShowHistory.sec,
											DgusAppShowHistory.contain_no,
											DgusAppShowHistory.shelf_no,
											DgusAppShowHistory.cargo_no,
											DgusAppShowHistory.sta,
											DgusAppShowHistory.err1,
											DgusAppShowHistory.err2);
				DgusAppShowHistory.step = 0x01;
			}
			break;
			case 0x01:
			{
				if(DgusRecive_Get_82Ack())
				{
					if(CloudProtocol_Get_DeviceState() == 106)
					{
						CloudProtocol_Set_DeviceState(102);
					}
					else if(CloudProtocol_Get_DeviceState() == 104)
					{
						CloudProtocol_Set_DeviceState(0);
					}
					
					DgusAppShowHistory.runtime = 0;
					DgusAppShowHistory.retry_cnt = 0;
					DgusAppShowHistory.step = 0;
					DgusAppShowHistory.enable = 0;
				}
				else
				{
					if(DgusAppShowHistory.runtime<1*100)
					{
						DgusAppShowHistory.runtime++;
					}
					else
					{
						DgusAppShowHistory.runtime = 0;
						if(DgusAppShowHistory.retry_cnt<2)
						{
							DgusAppShowHistory.retry_cnt++;
							DgusAppShowHistory.step = 0;
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 102)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else
							{
								CloudProtocol_Set_DeviceState(104);
							}
							
							DgusAppShowHistory.retry_cnt = 0;
							DgusAppShowHistory.step = 0;
							DgusAppShowHistory.enable = 0;
						}
					}
				}
			}
			break;
			default:break;
		}
	}
	


}

void DgusApp_Task(void)
{
	DgusApp_ShowSellLog();
	if(DgusAppShowSellLog.enable)
		return ;	
	
	DgusApp_ShowQRCode_Task();
	if(DgusAppShowQRCode.enable)
		return ;
	
	DgusApp_ShowDeviceId_Task();
	if(DgusAppShowDeviceId.enable)
		return ;
	
//	DgusApp_ShowNetSta_Task();
//	if(DgusAppShowNetSta.enable)
//		return ;
//	

	
	DgusApp_ShowGotoPage_Task();
	if(DgusAppGotoPage.enable)
		return ;
		
	DgusApp_UpTime_Task();
	if(DgusAppUpTime.enable)
		return ;
	
//	DgusApp_Login_Task();
//	if(DgusAppDeviceManageLogin.login_flag)
//		return ;
//	
////	DgusApp_ShowHistory_Task();
////	if(DgusAppShowHistory.enable)
////		return ;
//	
//	DgusApp_ShowHistroyManage_Task();
//	if(DgusAppShowHistoryManage.enable)
//		return ;
//	
//	DgusApp_ShowStoreSta_Task();
//	if(DgusAppShowNetSta.enable)
//		return ;
//	

		
	DgusApp_ShowSellErrorInfo_Task();
	if(DgusAppShowSellErrorInfo.enable)
		return ;
	
	DgusApp_ShowSystemErrorInfo_Task();
	if(DgusAppShowSystemErrorInfo.enable)
		return ;
	
	DgusApp_ShowTemp_Task();
	if(DgusAppShowTemp.enable)
		return ;

	DgusApp_ShowTemp_Task2();
	if(DgusAppShowTemp2.enable)
		return ;	
	
	DgusApp_ShowSellTest_Task();
	if(DgusAppShowSellTest.enable)
		return ;
		
	DgusApp_ShowSellReset_Task();
		
	if(DgusAppShowSellReset.enable)
		return ;
	
	DgusApp_ShowIrCheck_Task();
	if(DgusAppShowIrCheck.enable)
		return ;
	
	DgusApp_ClearIrCheck_Task();
	if(DgusAppClearIrCheck.enable)
		return ;
	
	DgusApp_ShowMotorCheck_Task();
	if(DgusAppShowMotorCheck.enable)
		return ;
	
	DgusApp_ClearMotorCheck_Task();
	if(DgusAppClearMotorCheck.enable)
		return ;	
}

void DgusApp_Init(void)
{	
	AuxConfig_Get_DgusLoginPara(&DgusAppDeviceManageLogin.src);
	
	
	
	DgusControl_Init();
	
	DgusRecive_Set_DeviceManageIdCallback(DgusApp_Recive_DeviceManageId);
	DgusRecive_Set_DeviceManagePwdCallback(DgusApp_Recive_DeviceManagePwd);
	DgusRecive_Set_DeviceManageLoginCallback(DgusApp_Recive_DeviceManageLogin);
	DgusRecive_Set_DeviceManageFixIdCallback(DgusApp_Recive_DeviceManageFixId);
	DgusRecive_Set_DeviceManageFixPwdCallback(DgusApp_Recive_DeviceManageFixPwd);
	DgusRecive_Set_DeviceManageFixCallback(DgusApp_Recive_DeviceManageFix);
	DgusRecive_Set_DeviceIdFix_Callback(DgusApp_Recive_DeviceIdFix);
	DgusRecive_Set_DeviceIdFixOk_Callback(DgusApp_Recive_DeviceIdFixOk);
	DgusRecive_Set_WifiSsidFix_Callback(DgusApp_Recive_WifiSsidFix);
	DgusRecive_Set_WifiPwdFix_Callback(DgusApp_Recive_WifiPwdFix);
	DgusRecive_Set_WifiFixOk_Callback(DgusApp_Recive_WifiFixOk);		
	DgusRecive_Set_TcpIpFix_Callback(DgusApp_Recive_TcpIpFix);
	DgusRecive_Set_TcpPortFix_Callback(DgusApp_Recive_TcpPortFix);
	DgusRecive_Set_TcpFixOk_Callback(DgusApp_Recive_TcpFixOk);
	DgusRecive_Set_OpenLock_Callback(DgusApp_Recive_OpenLock);
	DgusRecive_Set_ShowHistoryStart_Callback(DgusApp_Recive_ShowHistoryStart);
	DgusRecive_Set_ShowHistoryNext_Callback(DgusApp_Recive_ShowHistoryNext);
	DgusRecive_Set_ShowHistoryLast_Callback(DgusApp_Recive_ShowHistoryLast);
	
//	DgusApp_Set_NetSta(0);	
//	DgusApp_Set_Temp(5);	
//	DgusApp_Set_Time(0,0,0,0,0,0,0);
	
	if(SiganlGpio_ReadLevel6(0))
	{
		DgusApp_Set_GotoPage(12);
	}
	else
	{
		DgusApp_Set_GotoPage(0);
	}
}

