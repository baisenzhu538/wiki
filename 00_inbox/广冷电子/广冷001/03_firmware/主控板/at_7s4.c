

#include "at_7s4.h"
#include "cloud_protocol.h"
#include "wireless_hardware_interface.h"
#include "mqtt_connect.h"


char *InquireCmd[3]={
                     "usr.cnAT+CSQ?\r\n",    //查询信号强度
                     "usr.cnAT+SYSINFO?\r\n",//查询网络信息
	                   "usr.cnAT+REBOOT\r\n",
                     };
char *ResponseCmd[2]={
	                    "\r\n+CSQ:",
	                    "\r\n+SYSINFO:",
                     };
char Rssi[15]={"NULL"};
char Net [15]={"NULL"};
char Iccid[25]={"NULL"};
char AT7S4Latitude[10] = {"00.00"};
char AT7S4Longitude[10] = {"000.00"};

char * At7S4GpsDrive_GetLatitude(void)
{
	return AT7S4Latitude;
}
char * At7S4GpsDrive_GetLongitude(void)
{
	return AT7S4Longitude;
}

//void At7S4Harware_ResetModule(void)
//{
//	uint32_t i=0xFFFFF;
//	AT7S4_NRST_CTL = 0;
//	while(i--);
//	i = 0xFFFFF;
//	AT7S4_NRST_CTL = 1;
//	while(i--);
//}

u8 At7S4Harware_ResetModule(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				AT7S4_NRST_CTL = 0;
				mode = 1;
			}
			break;
		case 0x01:
			{
				count++;
				if(count > 200)
				{
					count = 0;
					mode = 2;
				}
			}
			break;
		case 0x02:
			{
				AT7S4_NRST_CTL = 1;
				mode = 3;
			}
			break;
		case 0x03:
			{
				count++;
				if(count > 200)
				{
					count = 0;
					mode = 0;
					return 0xFF;
				}
			}
			break;
	}
	return 0x00;	
}


u8 At7S4_Init(void)
{
	return At7S4Harware_ResetModule();
}

//u8 At7s4_CheckModule(void)
//{
//	return WirelesModule_sendcmd( "usr.cnAT+WKMOD?\r\n","\r\n+WKMOD:NET",150);
//}

/*
u8 At7s4_CheckModule(void)
{
	static u8 mode = 0;
	static u16 reply_num = 0;
	static u16 wait_time = 0;
	
	switch(mode)
	{
		case 0://查模块型号
		{	
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"usr.cnAT+WKMOD?\r\n",strlen("usr.cnAT+WKMOD?\r\n"));
			mode = 1;
		}
		break;
		case 1://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\n+WKMOD:NET"))	//收到
			{
				mode = 0;	//
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;
			}
			else
			{
				wait_time++;
				if(wait_time > 2*100)	//3秒重试
				{
					wait_time = 0;		
					mode = 0;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						mode = 0;	
						return 0xEE;
					}
				}
			}
		}
		break;
		default:return 0xEE;
	}
	return 0x00;
}
*/


u8 At7s4_CheckModule(void)
{
	static u8 step = 0;
	static u8 retry_num_count;
	static u16 retry_time_count;
	char * pdata = NULL;
	
	switch(step)
	{
		case 0://识别模块
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"usr.cnAT+CMDPW\r\n",strlen("usr.cnAT+CMDPW\r\n"));	
			step = 1;
		}
		break;
		case 1://等待识别模块响应
		{
			if(strstr((char*)Uart4_RxBuf,"usr.cn"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 2;
			}
			else
			{		
				if(retry_time_count < 100)
				{
					retry_time_count++;
				}
				else
				{
					retry_time_count = 0;
					if(retry_num_count < 5)
					{
						retry_num_count++;
						step = 0;
					}
					else
					{
						retry_num_count = 0;
						step = 0;
						retry_num_count = 0;
						retry_time_count = 0;
						return 0xEE;
					}
				}
			}
		}
		break;
		case 2://查询网络连接信息
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"usr.cnAT+SOCKA\r\n",strlen("usr.cnAT+SOCKA\r\n"));				
			step = 3;
		}
		break;
		case 3://等待查询网络连接信息响应
		{
			if(strstr((char*)Uart4_RxBuf,"zd.jumiai.cn"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 4;
			}
			else
			{		
				if(retry_time_count < 100)
				{
					retry_time_count++;
				}
				else
				{
					retry_time_count = 0;
					if(retry_num_count < 3)
					{
						retry_num_count++;
						step = 2;
					}
					else
					{
						retry_num_count = 0;
						step = 0;
						retry_num_count = 0;
						retry_time_count = 0;
						return 0xEE;
					}
				}
			}
		}
		break;
		case 4://查询ICCID
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"usr.cnAT+ICCID\r\n",strlen("usr.cnAT+ICCID\r\n"));				
			step = 5;
		}
		break;
		case 5://等待查询ICCID响应
		{
			if(strstr((char*)Uart4_RxBuf,"+ICCID:"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 0;
				pdata = strstr((char*)Uart4_RxBuf, "+ICCID: ") + strlen("+ICCID: ");
				SysMem_copy(Iccid, pdata, 20);
				return 0xFF;
			}
			else
			{		
				if(retry_time_count < 100)
				{
					retry_time_count++;
				}
				else
				{
					retry_time_count = 0;
					if(retry_num_count < 3)
					{
						retry_num_count++;
						step = 4;
					}
					else
					{
						retry_num_count = 0;
						step = 0;
						retry_num_count = 0;
						retry_time_count = 0;
						return 0xEE;
					}
				}
			}
		}
		break;
	}
	return 0x00;
}



char *At7S4_ReadRssiStr(void)
{
	return Rssi;
}

char *At7S4_ReadNetStr(void)
{
	return Net;
}

char *At7S4_ReadIccidStr(void)
{
	return Iccid;
}

//校验指令，并返回参数段地址
char* At7S4_CmdCheck(char *pRes,char* cmd)
{
	char *ps,*pd;
  ps=cmd;
	pd=pRes;
	while(*ps)
	{
		if((*ps)!=(*pd))
			return NULL;
		ps++;
		pd++;
	}
	return pd;//返回数据段
}

char *At7S4_GetDataString(char *pRes,char *pStr)
{
	char *pR;
	char *pS;
	pR=pRes;
	pS=pStr;
	while((*pR)!=','&&(*pR)!='\0'&&(*pR)!='\r')
	{
		*pS=*pR;
		pS++;
		pR++;
	}
	*pS='\0';
	if(*pR==',')
		return (++pR);
	else
		return NULL;
}
//解析返回AT响应指令，返回 NULL 不是AT指令 返回 ！NULL 为AT指令
char At7S4_ReciveParsing(u8 * data,u16 size)
{
	char i;
	char *p;
	
	
	if(data[size-1]=='\n'
		&&data[size-2]=='\r'
		&&data[0]=='\r'
		&&data[1]=='\n')
	{
		for(i=0;i<2;i++)
		{
			p=At7S4_CmdCheck((char*)data,ResponseCmd[i]);
			if(p)
			 break;
		}
		switch(i)
		{
			case 0x00://信号强度
				p=At7S4_GetDataString(p,Rssi);
				return 0xFF;
			case 0x01://网络信息
				p=At7S4_GetDataString(p,Net);
			  p=At7S4_GetDataString(p,Net);
				return 0xFF;
			default:return NULL;
		}
	}
	else
	{
		MQTT_Pack_Json_Cut(data,size);
	}
	return NULL;
}

char At7S4_SendData(u8* data,u16 size)
{
	WierlessHarware_SendData(data,size);
}


//0.01s定时执行
static short int rest_time=0;//复位4G模块驱动时间
static unsigned int time=(30*6000)-7500;
static char sta=0x00;
static char atsta=0;

char At7S4_ReadAtSta(void)
{
	return atsta;
}

static u8 At7S4_Enable = 0x01;
void At7S4_Task_Enable(void)
{
	At7S4_Enable = 0x01;
}
void At7S4_Task_Disable(void)
{
	At7S4_Enable = 0x00;
}

void At7S4_TaskRun(void)
{
	if(At7S4_Enable == 0x00)
		return ;
	if(CloudProtocol_ReadGoodsSta())
	{
		return;
	}
	if(MQTT_Get_Start_Status() && CloudProtocol_ReadLink()==0x00)//设备网络不稳定
	{
		if(rest_time<(5*6000))
		 rest_time++;
		else
		{
			rest_time=0;			
			CloudProtol_Manage_Struct_Clear();
			MQTT_Strat_Reboot();
			WirelessModule_ResetModule();//复位模块
//			Iap_SysReset();//系统复位		
		}
	}
	else
	{
		rest_time=0;
	}
	
	time++;
	if(time==10)
		atsta=0;
	else if(time==30*6000)//一分钟更新一次
	{
		 atsta=0x01;
		 time=0;
		 sta=!sta;
		 if(sta)
		 {
			 WierlessHarware_SendData((uint8_t*)InquireCmd[0], strlen(InquireCmd[0]));
	//	  printf("%s\n",InquireCmd[0]);//发送查询网络信号
		 }
		 else
		 {
			 WierlessHarware_SendData((uint8_t*)InquireCmd[0], strlen(InquireCmd[0]));
	//	  printf("%s\n",InquireCmd[1]);//发送查询网络信息
		 }
	}
}

static char Usr7S4cmdBuffer[100];
//10ms
int At7S4_ModuleConfig(NetworkPara_TypeDef * pNetworkPara)
{
	static u8 mode = 2;
	static u8 submode = 2;
	static u32 wait_time = 0;
	static u32 wait_num = 0;
//	char * cmd;
//	cmd=SysMem_malloc(100);
//	if(cmd==NULL)
//		return -1;
	memset(Usr7S4cmdBuffer,0,100);
	sprintf(Usr7S4cmdBuffer,"usr.cnAT+SOCKA=TCP,%s,%s\r\n", pNetworkPara->IPaddress, pNetworkPara->port);

	switch(mode)
	{
//		case 0://进入AT指令模式
//		{
//			WierlessHarware_SendData((u8*)"+++", strlen("+++"));
//			mode = 1;
//		}
//		break;
//		case 1://等待进入AT指令模式
//		{
//			wait_time++;
//			if(wait_time > 50)
//			{
//				wait_time = 0;
//				mode = 2;
//				mode = submode;
//			}
//		}
//		break;
		case 2://配置SOCKET
		{
			memset(Uart4_RxBuf,0,512);			
			WierlessHarware_SendData((uint8_t*)Usr7S4cmdBuffer,strlen(Usr7S4cmdBuffer));
			mode = 3;
		}
		break;
		case 3://等待配置完成
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))
				mode = 4;
			else
			{
				wait_time++;
				if(wait_time > 200)
				{
					mode = 2;
					wait_time = 0;
					wait_num++;
					if(wait_num % 3 == 0)
					{
						if(wait_num == 9)
						{
							wait_num = 0;
							mode = 2;
							submode = 2;
							return 0xEE;
						}						
						submode = 2;
						mode = 2;
					}
				}
			}
		}
		break;
		case 4://读配置
		{
			memset(Uart4_RxBuf,0,512);			
			WierlessHarware_SendData((uint8_t*)"usr.cnAT+SOCKA\r\n",strlen("usr.cnAT+SOCKA\r\n"));
			mode = 5;
		}
		break;
		case 5://等待读配置
		{
			if(strstr((char*)Uart4_RxBuf,(char *)pNetworkPara->IPaddress) && strstr((char*)Uart4_RxBuf,(char *)pNetworkPara->port)) 
//			if(strstr((char*)Uart4_RxBuf,"+OK"))
			{
				wait_num = 0;
				mode = 2;
				submode = 2;
				return 0xFF;
			}
			else
			{
				wait_time++;
				if(wait_time > 200)
				{
					mode = 4;
					wait_time = 0;
					wait_num++;
					if(wait_num % 3 == 0)
					{
						if(wait_num == 9)
						{
							wait_num = 0;
							mode = 2;
							submode = 2;
							return 0xEE;
						}						
						mode = 2;
						submode = 4;
					}
				}
			}
		}
		break;
	}
	return 0x00;
}