#include "at_ebyte.h"
#include "cloud_protocol.h"
#include "wireless_hardware_interface.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "debug.h"
//#include "mqtt_manage.h"
#include "mqtt_connect.h"


typedef	struct
{
	char longitude[10];	//经度
	char latitude[10];	//纬度
}EbyteGpsDrive_TypeDef;

EbyteGpsDrive_TypeDef	EbyteGpsDrive = {"0.0","0.0"};

char *EbyteEnterCmd[2] = {"+++",				//进入AT模式
							"AT+EXAT\r\n"};		//退出AT模式
char *EbyteInquireCmd[3]={
						"AT+CSQ\r\n",    		//查询信号强度
						"AT+CREG\r\n",			//查询是否注册到运营商
						"AT+REBT\r\n",			//重启
						};
char *EbyteResponseCmd[2]={
	                    "\r\n+OK=",
	                    "\r\n+OK=",
						};
char EbyteRssi[15]={"NULL"};	//信号强度
char EbyteNet[15]= {"NULL"};	//未用
char EbyteMode[15] = {""};		//4G模块工作模式
char EbyteIccid[25] = {"NULL"};


u8 AtEbyteHarware_ResetModule(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				EBYTE_NRST_CTL = 0;
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
				EBYTE_NRST_CTL = 1;
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

u8 AtEbyte_Init(void)
{
	return AtEbyteHarware_ResetModule();
}

//查找字符串	1 有  0 无
char findStr(u8 * dest, u8 * src, u32 outtime)
{
	while(strstr((char*)dest,(char*)src)==0 && outtime--);
	if(outtime <= 0)
		return 0;
	else
		return 1;
}


u8 AtEbyte_CheckModule(void)
{
	static u8 step = 0;
	static u8 retry_num_count = 0;
	static u16 retry_time_count = 0;
	char * pdata = NULL;
	
	switch(step)
	{
		case 0:	//进入AT模式
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"+++",strlen("+++"));			
			step = 1;
		}
		break;
		case 1://等待进入AT模式
		{
			if(retry_time_count < 100)
			{
				retry_time_count++;
			}
			else
			{
				retry_time_count = 0;
				step = 2;
			}
		}
		break;
		case 2://识别模块
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+INFO\r\n",strlen("AT+INFO\r\n"));	
			step = 3;
		}
		break;
		case 3://等待识别模块响应
		{
			if(strstr((char*)Uart4_RxBuf,"LTE-4G"))	//收到
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
					if(retry_num_count < 5)
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
		case 4://查询网络连接信息
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+SOCK\r\n",strlen("AT+SOCK\r\n"));	
			step = 5;			
		}
		break;
		case 5://等待查询网络连接信息响应
		{
			if(strstr((char*)Uart4_RxBuf,"zd.jumiai.cn"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 6;
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
		case 6://读ICCID
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+ICCID\r\n",strlen("AT+ICCID\r\n"));	
			step = 7;
		}
		break;
		case 7://等待读ICCID响应
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 8;
				pdata = strstr((char*)Uart4_RxBuf, "+OK=") + strlen("+OK=");
				SysMem_copy(EbyteIccid,pdata,20);
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
						step = 6;
					}
					else
					{
						retry_num_count = 0;
						retry_time_count = 0;
						step = 0;						
					}
				}
			}
		}
		break;
		case 8://退出AT模式
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+EXAT\r\n",strlen("AT+EXAT\r\n"));	
			step = 9;			
		}
		case 9://等待退出AT模式响应
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到
			{
				retry_time_count = 0;
				retry_num_count = 0;
				step = 0;
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
						step = 8;
					}
					else
					{
						retry_num_count = 0;
						retry_time_count = 0;
						step = 0;						
						return 0xFF;
					}
				}
			}
		}
		break;
		default:break;
	}
	return 0x00;
}


//读模块工作模式
char *AtEbyte_ReadModeStr(void)
{
	return EbyteMode;
}

//读信号强度
char *AtEbyte_ReadRssiStr(void)
{
	return EbyteRssi;
}

//读网络信息
char *AtEbyte_ReadNetStr(void)
{
	return EbyteNet;
}

//读ICCID
char *AtEbyte_ReadIccidStr(void)
{
	return EbyteIccid;
}


//复位模块
void AtEbyte_RestMod(void)
{
	uint32_t i = 0xFFFFFF;
	EBYTE_NRST_CTL = 0;
	while(i--);
}

void EbyteRssiDataClear(void)
{
	u8 i;
	for(i = 0; i < 15; i++)
	{
		EbyteRssi[i] = 0;
	}
}

//校验指令，并返回参数段地址
char* AtEbyte_CmdCheck(char *pRes,char* cmd)
{
	char i,*ps,*pd;
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

char *AtEbyte_GetDataString(char *pRes,char *pStr)
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
char AtEbyte_CmdParsing(char *pResCmd,short int size)
{
	char i;
	char *p;
	if(pResCmd[size-1]!='\n'||pResCmd[size-2]!='\r')
		return NULL;
	if(pResCmd[0]!='\r'||pResCmd[1]!='\n')
		return NULL;
	
	//接收经纬度
	if(strstr((char*)Uart4_RxBuf, "+OK=latitude"))
	{
		p = strstr((char*)Uart4_RxBuf, "latitude:")  + strlen("latitude:");
		AtEbyte_GetDataString(p, (char*)EbyteGpsDrive.latitude);
		
		p = strstr((char*)Uart4_RxBuf, "longitude:")  + strlen("longitude:");
		AtEbyte_GetDataString(p, (char*)EbyteGpsDrive.longitude);
		return 0xFF;
	}
	//接收CSQ值
	else if(strstr((char*)Uart4_RxBuf, "+OK=latitude") == NULL && strstr((char*)Uart4_RxBuf, "+OK="))
	{
		p = strstr((char*)Uart4_RxBuf, "+OK=") + strlen("+OK=");
		p=AtEbyte_GetDataString(p, EbyteRssi);
		return 0xFF;
	}
	return NULL;
	
	
//	for(i=0;i<2;i++)
//	{
//		p=AtEbyte_CmdCheck(pResCmd,EbyteResponseCmd[i]);
//		if(p)
//		 break;
//	}
//	if(*(p+1) == '\r')
//		i = 1;
//	else if(*(p+2) == '\r')
//	{
//		i = 0;
//	}
//	switch(i)
//	{
//		case 0x00://信号强度
//			{
//				EbyteRssiDataClear();
//				p=AtEbyte_GetDataString(p,EbyteRssi);
//			}
//			return 0xFF;
//		case 0x01://网络信息
//			{
//				p=AtEbyte_GetDataString(p,EbyteNet);
//			}
//			return 0xFF;
//		default:return NULL;
//	}
//	return NULL;
}



static char atsta=0;

char AtEbyte_ReadAtSta(void)
{
	return atsta;
}

static u8 Ebyte_Enable = 0x01;
void AtEbyte_Task_Enable(void)
{
	Ebyte_Enable = 0x01;
}
void AtEbyte_Task_Disable(void)
{
	Ebyte_Enable = 0x00;
}

//获取纬度
char * EbyteGpsDrive_GetLatitude(void)
{
	return EbyteGpsDrive.latitude;
}

//获取经度
char * EbyteGpsDrive_GetLongitude(void)
{
	return EbyteGpsDrive.longitude;
}


//10ms
//获取GPS定位信息
u8 EbyteGps_Drive(void)
{
	static u8 mode = 0;
	static u32 wait_time = 0;
	static u32 wait_num = 0;
	static char * pdata = NULL;
	
	switch(mode)
	{
		case 0x00://进入AT指令模式
		{
			WierlessHarware_SendData((u8*)"+++",strlen("+++"));
			mode = 0x01;
		}
		break;			
		case 0x01://等待进入AT指令模式
		{
			wait_time++;
			if(wait_time > 50)
			{
				wait_time = 0;
				mode = 0x02;
			}
		}
		break;
		case 0x02://查询GPS
		{
			memset(Uart4_RxBuf,0,512);		
			WierlessHarware_SendData((u8*)"AT+GPS\r\n",strlen("AT+GPS\r\n"));
			mode = 0x03;
		}
		break;
		case 0x03://等待查询GPS结果
		{
			if(strstr((char*)Uart4_RxBuf, "+OK=latitude"))
			{
				pdata = strstr((char*)Uart4_RxBuf, "latitude:")  + strlen("latitude:");
				AtEbyte_GetDataString(pdata, (char*)EbyteGpsDrive.latitude);
				
				pdata = strstr((char*)Uart4_RxBuf, "longitude:")  + strlen("longitude:");
				AtEbyte_GetDataString(pdata, (char*)EbyteGpsDrive.longitude);
				
				mode = 0x04;
			}
			else
			{
				wait_time++;
				if(wait_time > 200)
				{
					wait_time = 0;
					wait_num++;
					mode = 0x02;
					if(wait_num > 3)
					{
						wait_time = 0;
						wait_num = 0;
						mode = 0x04;
					}
				}
			}
		}
		break;
		case 0x04://查询CSQ
		{
			memset(Uart4_RxBuf,0,512);		
			WierlessHarware_SendData((u8*)"AT+CSQ\r\n",strlen("AT+CSQ\r\n"));
			mode = 0x05;
		}
		break;
		case 0x05://等待查询CSQ结果
		{
			if(strstr((char*)Uart4_RxBuf, "+OK"))
			{
				pdata = strstr((char*)Uart4_RxBuf, "+OK=")  + strlen("+OK=");
				memset(EbyteRssi,0,sizeof(EbyteRssi));
				SysMem_copy(pdata, EbyteRssi, sizeof(EbyteRssi));
						
				mode = 0xFE;
			}
			else
			{
				wait_time++;
				if(wait_time > 200)
				{
					wait_time = 0;
					wait_num++;
					mode = 0x02;
					if(wait_num > 3)
					{
						wait_time = 0;
						wait_num = 0;
						mode = 0xFE;
					}
				}
			}
		}
		break;
		case 0xFE://退出AT指令模式
		{
			memset(Uart4_RxBuf,0,512);		
			WierlessHarware_SendData((u8*)"AT+EXAT\r\n", strlen("AT+EXAT\r\n"));
			mode = 0xFF;
		}
		break;
		case 0xFF://等待确认退出AT指令模式
		{
			if(strstr((char*)Uart4_RxBuf, "+OK"))
				while(0);
			mode = 0;
			wait_num = 0;
			wait_time = 0;
			return 0xFF;
		}
		break;
		default:break;
	}
	return 0x00;
}

//解析返回AT响应指令，返回 NULL 不是AT指令 返回 ！NULL 为AT指令
char AtEbyte_ReciveParsing(u8 * data, u16 size)
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
			p=AtEbyte_CmdCheck((char*)data,EbyteResponseCmd[i]);
			if(p)
			 break;
		}
		switch(i)
		{
			case 0x00://信号强度
				{
					EbyteRssiDataClear();
					p=AtEbyte_GetDataString(p,EbyteRssi);
				}
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

char AtEbyte_SendData(u8* data,u16 size)
{
	WierlessHarware_SendData(data,size);
}

static short int rest_time=0;//复位4G模块驱动时间
static unsigned int time=(60*6000)-7500;
//static unsigned int time = 0;
static char sta=0x00;

//0.01s定时执行
void AtEbyte_TaskRun(void)
{
	u8 ret = 0;
	if(Ebyte_Enable == 0x00)
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
			WirelessModule_ResetModule();
//			Iap_SysReset();//系统复位
		}
	}
	else
	{
		rest_time=0;
	}

	time++;
 	if(time == 60*6000)
	{
		atsta=0x01;
		strcpy(EbyteMode,"AT");
		WierlessHarware_SendData((uint8_t*)EbyteEnterCmd[0], strlen(EbyteEnterCmd[0]));
	  //进入AT模式
	}
	else if(time == ((60*6000)+10))
	{
		WierlessHarware_SendData((uint8_t*)EbyteInquireCmd[0], strlen(EbyteInquireCmd[0]));
		//发送查询网络信号
	}
	else if(time == ((60*6000)+30))
	{
		WierlessHarware_SendData((u8*)"AT+GPS\r\n",strlen("AT+GPS\r\n"));
	}
	else if(time == ((60*6000)+50))
	{
		WierlessHarware_SendData((uint8_t*)EbyteEnterCmd[1], strlen(EbyteEnterCmd[1]));
		//退出AT模式	
	}
	else if(time==((60*6000)+70))
	{
		strcpy(EbyteMode,"TC");
		atsta=0x00;
		time=0;
	}
}



void AtEbyte_TCP_Disconnect(void)
{
	u8 sta = 0;
	WierlessHarware_SendData((uint8_t*)EbyteEnterCmd[0], strlen(EbyteEnterCmd[0]));
	sta = WirelesModule_sendcmd( "AT+SOCK1=0,TCPC,zd.jumiai.cn,1883","\r\n+OK\r\n",500);
	if(sta == 0xFF)
		return;
}

static char EbytecmdBuffer[100];
//10ms


int AtEbyte_ModuleConfig(NetworkPara_TypeDef * pNetworkPara)
{
	static u8 mode = 0;
	static u8 submode = 2;
	static u32 wait_time = 0;
	static u32 wait_num = 0;
//	char * cmd;
//	cmd=SysMem_malloc(100);
//	if(cmd==NULL)
//		return -1;
	memset(EbytecmdBuffer,0,100);
	sprintf(EbytecmdBuffer,"AT+SOCK=TCPC,%s,%s\r\n", pNetworkPara->IPaddress, pNetworkPara->port);

	switch(mode)
	{
		case 0://进入AT指令模式
		{
			WierlessHarware_SendData((u8*)"+++", strlen("+++"));
			mode = 1;
		}
		break;
		case 1://等待进入AT指令模式
		{
			wait_time++;
			if(wait_time > 50)
			{
				wait_time = 0;
				mode = 2;
				mode = submode;
			}
		}
		break;
		case 2://配置SOCKET
		{
			memset(Uart4_RxBuf,0,512);			
			WierlessHarware_SendData((uint8_t*)EbytecmdBuffer,strlen(EbytecmdBuffer));
			mode = 3;
		}
		break;
		case 3://等待配置完成
		{
			if(strstr((char*)Uart4_RxBuf,"+OK"))
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
							mode = 0;
							submode = 2;
							return 0xEE;
						}						
						submode = 2;
						mode = 0;
					}
				}
			}
		}
		break;
		case 4://读配置
		{
			memset(Uart4_RxBuf,0,512);			
			WierlessHarware_SendData((uint8_t*)"AT+SOCK\r\n",strlen("AT+SOCK\r\n"));
			mode = 5;
		}
		break;
		case 5://等待读配置
		{
			if(strstr((char*)Uart4_RxBuf,(char *)pNetworkPara->IPaddress) && strstr((char*)Uart4_RxBuf,(char *)pNetworkPara->port)) 
//			if(strstr((char*)Uart4_RxBuf,"+OK"))
			{
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
							mode = 0;
							submode = 2;
							return 0xEE;
						}						
						mode = 0;
						submode = 4;
					}
				}
			}
		}
		break;
	}
	return 0x00;
}



