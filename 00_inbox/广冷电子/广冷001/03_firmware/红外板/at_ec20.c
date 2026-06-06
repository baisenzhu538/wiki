#include "at_EC20.h"
#include "mqtt_recive.h"
#include "cloud_protocol.h"
#include "wireless_hardware_interface.h"
#include "wireless_module_init.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "usart.h"
#include "debug.h"
#include "sys_config.h"
#include "at_air720.h"


typedef	struct
{
	u8 longitude_dir;
	u8 latitude_dir;
	char latitude[10];	//纬度
	char longitude[10];	//经度
}EC20GpsDrive_TypeDef;

EC20GpsDrive_TypeDef	EC20GpsDrive = {0,0,"0000","00000"};

char *EC20EnterCmd[2] = {"+++",				//进入AT模式
							"ATO\r\n",};		//退出AT模式
char *EC20InquireCmd[3]={
						"AT+CSQ\r\n",    		//查询信号强度
						"AT+CREG\r\n",			//查询是否注册到运营商
						"AT+REBT\r\n",			//重启
						};
char *EC20ResponseCmd[3]={
						"\r\nOK\r\n",
						"\r\n+CSQ: ",
						"\r\nCONNECT\r\n"
						};
u8	EC20RssiSta=0;
char EC20Rssi[15]={"NULL"};	//信号强度
char EC20Net[15]= {"NULL"};			//未用
char EC20Mode[15] = {""};		//4G模块工作模式
char EC20Iccid[25] = {"NULL"};
char EC20Latitude[10] = {"00000"};
char EC20Longitude[10] = {"000000"};

u8 EC20_QIOPEN_AT_CMD[100];

NetworkPara_TypeDef	EC20NetworkPara = {"39.96.10.250","11883","TCP"};



void EC20NetworkParaCopy(NetworkPara_TypeDef * NetworkPara)
{
	SysMem_copy((u8*)&EC20NetworkPara, (u8*)NetworkPara, sizeof(NetworkPara_TypeDef));
	memset((char*)EC20_QIOPEN_AT_CMD,0,100);
	sprintf((char*)EC20_QIOPEN_AT_CMD,"AT+QIOPEN=1,0,\"TCP\",\"%s\",%s,0,1\r\n",(char*)"39.96.10.250", "11883");
}

u8 EC20Harware_PowerReset(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				EC20_PWR_CTL = 0;
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
				EC20_PWR_CTL = 1;
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

u8 EC20Harware_ResetModule(void)
{
//	static u16 count = 0;
//	static u8 mode = 0;
//	switch(mode)
//	{
//		case 0x00:
//			{
//				count = 0;
//				EC20_RST_CTL = 1;//拉高
//				mode = 1;
//			}
//			break;
//		case 0x01:
//			{
//				count++;
//				if(count > 200)
//				{
//					count = 0;
//					mode = 2;
//				}
//			}
//			break;
//		case 0x02:
//			{
//				EC20_RST_CTL = 0;//拉低 
//				mode = 3;
//			}
//			break;
//		case 0x03:
//			{
//				count++;
//				if(count > 200)
//				{
//					count = 0;
//					mode = 0;
//					return 0xFF;
//				}
//			}
//			break;
//	}
//	return 0x00;
	return 0xFF;
}



//模块初始化
u8 EC20_Init(void)
{
	static u8 res1 = 0;
	static u8 res2 = 0;
	static u8 first_flag = 1;

	if(first_flag)
	{
		first_flag = 0;
		AuxConfig_GetNetWorkPara(&EC20NetworkPara);
		memset((char*)EC20_QIOPEN_AT_CMD,0,100);
//		sprintf((char*)EC20_QIOPEN_AT_CMD,
//				"AT+QIOPEN=1,0,\"TCP\",\"%s\",%s,0,1\r\n",
//				(char*)EC20NetworkPara.IPaddress, 
//				(char*)EC20NetworkPara.port);		
		sprintf((char*)EC20_QIOPEN_AT_CMD,"AT+QIOPEN=1,0,\"TCP\",\"%s\",%s,0,1\r\n",(char*)"39.96.10.250", "11883");
	}
	if(EC20Harware_ResetModule())
	{
		res1 = 0xFF;
	}
	if(EC20Harware_PowerReset())
	{
		res2 = 0xFF;
	}
	if(res1 == 0xFF && res2 == 0xFF)
	{
		res1 = 0;
		res2 = 0;
		return 0xFF;
	}
	return 0x00;
}




typedef struct
{
	u8 reset_mode;
	u8 mode;
	u8 reply_num;
	u32 wait_time;	
	u8 ip[32];
	int rssi;
}EC20_LinkInfo_TypeDef;
	
EC20_LinkInfo_TypeDef	EC20_LinkInfo;

void EC20_SetMode(u8 mode)
{
	EC20_LinkInfo.mode = mode;
}

//识别模块
u8 EC20_CheckModule(void)
{
	static u8 mode = 0;
	static u16 reply_num = 0;
	static u16 wait_time = 0;
	
	switch(mode)
	{
		case 0://查模块型号
		{	
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CGMM\r\n",strlen("AT+CGMM\r\n"));
			mode = 1;
		}
		break;
		case 1://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"EC20"))	//收到
			{
				mode = 0;	//
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;
			}
//			else if(strstr((char*)Uart4_RxBuf,"Air720"))
//			{
//				AtAir720NetworkParaCopy(&EC20NetworkPara);
//				WirelessModule_ScanJump(0x03,0x00);
//				mode = 0;	//
//				wait_time = 0;	
//				reply_num = 0;
//				return 0x00;
//			}
			else
			{
				wait_time++;
				if(wait_time > 2*100)	//3秒重试
				{
					wait_time = 0;		
					mode = 0;	
					reply_num++;
					if(reply_num > 5)	//重试5次
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

//10ms任务
u8 EC20_ConfigModule(void)
{
	static u8 step  = 0;
	static u8 reply_num = 0;
	static u16 wait_time = 0;
	static u8 reset_mode;
	u8 res = 0;
	
	switch(step)
	{
		case 0x00://发送AT
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT\r\n",strlen("AT\r\n"));
			step = 0x01;
		}
		break;
		case 0x01://等待AT响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x02;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x00;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x02://查SIM卡
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CPIN?\r\n",strlen("AT+CPIN?\r\n"));
			step = 0x03;
		}
		break;
		case 0x03://等待查SIM卡响应
		{
			if(strstr((char*)Uart3_RxBuf,"READY"))	//收到
			{
				step = 0x04;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x02;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x04://查CS业务状态
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CREG?\r\n",strlen("AT+CREG?\r\n"));
			step = 0x05;
		}
		break;
		case 0x05://等待查CS业务状态响应
		{
			if(strstr((char*)Uart3_RxBuf,",1") || strstr((char*)Uart3_RxBuf,",5"))	//收到
			{
				step = 0x06;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x04;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x06://查PS业务状态
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CGREG?\r\n",strlen("AT+CGREG?\r\n"));
			step = 0x07;
		}
		break;
		case 0x07://等待查PS业务状态响应
		{
			if(strstr((char*)Uart3_RxBuf,",1") || strstr((char*)Uart3_RxBuf,",5"))	//收到
			{
				step = 0x08;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x06;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		case 0x08://设置APN
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+QICSGP=1,1,\"CMIOT\",\"\",\"\",1\r\n",
									strlen("AT+QICSGP=1,1,\"CMIOT\",\"\",\"\",1\r\n"));
			step = 0x09;
		}
		break;
		case 0x09://等待设备APN响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x0A;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x08;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		
		case 0x0A://激活场景2
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+QIACT=1\r\n",
									strlen("AT+QIACT=1\r\n"));
			step = 0x0B;
		}
		break;
		case 0x0B://等待激活场景2响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x10;	
				wait_time = 0;	
				reply_num = 0;
			}
			else if(strstr((char*)Uart3_RxBuf,"ERROR"))	
			{
				step = 0x0C;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x0A;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		case 0x0C://反激活PDP
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+QIDEACT=1\r\n",
									strlen("AT+QIDEACT=1\r\n"));
			step = 0x0D;
		}
		break;
		case 0x0D://等待反激活PDP响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x02;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x0C;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		case 0x10://设置同步方式
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CTZU=3\r\n",
									strlen("AT+CTZU=3\r\n"));				
			step = 0x11;
		}
		break;
		case 0x11://等待设置同步响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				reply_num = 0;
				wait_time = 0;
				step = 0x12;
			}
			else
			{
				wait_time++;
				if(wait_time > 100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x10;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		case 0x12://发送同步指令
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+QNTP=1,\"202.112.10.36\",123,1\r\n",
										strlen("AT+QNTP=1,\"202.112.10.36\",123,1\r\n"));
			step = 0x13;
		}
		break;
		case 0x13://等待同步响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				reply_num = 0;
				wait_time = 0;
				step = 0x18;
			}
			else
			{
				wait_time++;
				if(wait_time > 100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x12;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
				
//		case 0x14://激活PDP
//		{
//			memset((char*)Uart3_RxBuf,0,512);
//			WierlessHarware_SendData((u8*)"AT+QIACT=1\r\n",
//									strlen("AT+QIACT=1\r\n"));
//			step = 0x15;
//		}
//		break;
//		case 0x15://等待激活PDP响应
//		{
//			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
//			{
//				step = 0x18;	
//				wait_time = 0;	
//				reply_num = 0;
//			}
//			else if(strstr((char*)Uart3_RxBuf,"ERROR"))	
//			{
//				step = 0x16;	
//				wait_time = 0;	
//				reply_num = 0;
//			}
//			else
//			{
//				wait_time++;
//				if(wait_time > 3*100)	//3秒重试
//				{
//					wait_time = 0;		
//					step = 0x14;	
//					reply_num++;
//					if(reply_num > 5)	//重试5次
//					{
//						reply_num = 0;
//						step = 0xEE;
//					}
//				}
//			}
//		}
//		break;
//		case 0x16://反激活PDP
//		{
//			memset((char*)Uart3_RxBuf,0,512);
//			WierlessHarware_SendData((u8*)"AT+QIDEACT=1\r\n",
//									strlen("AT+QIDEACT=1\r\n"));
//			step = 0x17;
//		}
//		break;
//		case 0x17://等待反激活PDP响应
//		{
//			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
//			{
//				step = 0x02;	
//				wait_time = 0;	
//				reply_num = 0;
//			}
//			else
//			{
//				wait_time++;
//				if(wait_time > 3*100)	//3秒重试
//				{
//					wait_time = 0;		
//					step = 0x16;	
//					reply_num++;
//					if(reply_num > 5)	//重试5次
//					{
//						reply_num = 0;
//						step = 0xEE;
//					}
//				}
//			}
//		}
//		break;
		case 0x18://打开GPS
		{
//			memset((char*)Uart3_RxBuf,0,512);
//			WierlessHarware_SendData((u8*)"AT+QGPS=1\r\n",
//									strlen("AT+QGPS=1\r\n"));
			step = 0x19;
		}
		break;
		case 0x19://等待打开GPS响应
		{
//			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
//			{
//				step = 0x12;	
//				wait_time = 0;	
//				reply_num = 0;
//			}
//			else
//			{
//				wait_time++;
//				if(wait_time > 100)	//3秒重试
//				{
//					wait_time = 0;		
//					step = 0x10;	
//					reply_num++;
//					if(reply_num > 3)	//重试5次
//					{
//						reply_num = 0;
//						step = 0xEE;
						step = 0x20;	
//					}
//				}
//			}
		}
		break;
		case 0x20://打开SOCKET
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)EC20_QIOPEN_AT_CMD,
									strlen((char*)EC20_QIOPEN_AT_CMD));
			step = 0x21;
		}
		break;
		case 0x21://等待连接成功
		{
			if(strstr((char*)Uart3_RxBuf,"+QIOPEN: 0,0"))	//收到
			{
				step = 0x00;	
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;
			}
			else if(strstr((char*)Uart3_RxBuf,"+QIOPEN: 0,"))
			{		
				WierlessHarware_SendData((u8*)"AT+QICLOSE=0\r\n",strlen("AT+QICLOSE=0\r\n"));
				wait_time = 0;		
				reply_num = 0;
				step = 0xEE;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x20;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		default://复位模块 0xEE
		{
			switch(reset_mode)
			{
				case 0:
					{
						res = EC20Harware_ResetModule();		//硬件复位
						if(res == 0xFF)
							reset_mode = 1;
					}
					break;
				case 1:
					{
						res = EC20Harware_PowerReset();		//掉电
						if(res == 0xFF)
						{
							reset_mode = 2;
							wait_time = 0;
						}
					}
					break;
				case 2:
					{
						if(wait_time<1000)
						{
							wait_time++;
						}
						else
						{
							wait_time = 0;
							step = 0x00;
							reset_mode = 0;
						}
					}
					break;
			}	
		}
		break;
		
	}
	return 0x00;
}


//读模块工作模式
char *EC20_ReadModeStr(void)
{
	return EC20Mode;
}

//读信号强度
char *EC20_ReadRssiStr(void)
{
	return EC20Rssi;
}

u8 EC20_ReadRssiSta(void)
{
	return EC20RssiSta;
}

//读网络信息
char *EC20_ReadNetStr(void)
{
	return EC20Net;
}

//读ICCID
char *EC20_ReadIccidStr(void)
{
	return EC20Iccid;
}

//获取纬度
char * AtEC20GpsDrive_GetLatitude(void)
{
	u8 Index = 0;
	if(EC20GpsDrive.latitude_dir == 2)
	{
		EC20Latitude[Index] = '-';
		Index++;
	}
	EC20Latitude[Index] = EC20GpsDrive.latitude[0];
	Index++;
	EC20Latitude[Index] = EC20GpsDrive.latitude[1];
	Index++;
	EC20Latitude[Index] = '.';
	Index++;
	EC20Latitude[Index] = EC20GpsDrive.latitude[2];
	Index++;
	EC20Latitude[Index] = EC20GpsDrive.latitude[3];
	Index++;
	return EC20Latitude;
}

//获取经度
char * AtEC20GpsDrive_GetLongitude(void)
{
	u8 Index = 0;
	if(EC20GpsDrive.longitude_dir == 2)
	{
		EC20Longitude[Index] = '-';
		Index++;
	}
	EC20Longitude[Index] = EC20GpsDrive.longitude[0];
	Index++;
	EC20Longitude[Index] = EC20GpsDrive.longitude[1];
	Index++;
	EC20Longitude[Index] = EC20GpsDrive.longitude[2];
	Index++;
	EC20Longitude[Index] = '.';
	Index++;
	EC20Longitude[Index] = EC20GpsDrive.longitude[3];
	Index++;
	EC20Longitude[Index] = EC20GpsDrive.longitude[4];
	Index++;
	return EC20Longitude;	
}



//解析返回AT响应指令，返回 NULL 不是AT指令 返回 ！NULL 为AT指令
char EC20_ReciveParsing(u8 * data,u16 size)
{
	static u8 step = 0x00;
	char * p = NULL;
	char * rdata;
	u16 rsize;
	switch(step)
	{
		case 0x00:
		{
			p = strstr((char*)Uart3_RxBuf, "+QIURC:");			
			if(p)
			{
				rdata = strstr((char*)p,"\r\n")+strlen("\r\n");
				p = strstr((char*)Uart3_RxBuf, "\"recv\",0,");
				if(p)
				{
					rsize = atoi(p+strlen("\"recv\",0,"));
					MQTT_Pack_Json_Cut((u8*)rdata,rsize);
					while(0);
				}
				
			}
		}
		break;
	}
	return NULL;
}

char EC20_ReadAtSta(void)
{
	return 0x00;
}


static u32 cycle_time = 25*60*100;
void EC20_CSQ_GNSS_CheckReset(void)
{
	cycle_time = 0;
}

u8 ec20_send_enable=1;

//查询CSQ,GNSS
void EC20_CSQ_GNSS_Check(void)
{
	static u8 step  = 0;
	static u8 reply_num = 0;
	static u16 wait_time = 0;
	u8 * pdata = NULL;
	
	if(cycle_time < 10*60*100)
	{
		cycle_time++;
	}
	else
	{
		switch(step)
		{
			case 0x00://查CSQ
			{
				ec20_send_enable = 0;
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CSQ\r\n",
											strlen("AT+CSQ\r\n"));
				step = 0x01;
			}
			break;
			case 0x01://等待查CSQ响应
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CSQ: ");
					if(pdata)
					{
						memset(EC20Rssi, 0, 15);
						pdata += strlen("+CSQ: ");
						SysMem_copy(EC20Rssi, pdata, 2);
						if(*pdata<0x32||*pdata>0x38)
							EC20RssiSta = 0;
						else
							EC20RssiSta = 1;
					}
					step = 0x02;	
					wait_time = 0;	
					reply_num = 0;
					//
				}
				else if(strstr((char*)Uart3_RxBuf,"+CME ERROR:"))
				{
					step = 0x00;
					cycle_time = 0;	
					wait_time = 0;	
					reply_num = 0;
					ec20_send_enable = 1;
				}
				else
				{
					wait_time++;
					if(wait_time > 100)	//3秒重试
					{
						wait_time = 0;		
						step = 0x00;	
						reply_num++;
						if(reply_num > 3)	//重试5次
						{
							reply_num = 0;
							step = 0x00;
							cycle_time = 0;
							ec20_send_enable = 1;
						}
					}
				}
			}
			break;
			case 0x02://查GNSS
			{
//				memset((char*)Uart3_RxBuf,0,512);
//				WierlessHarware_SendData((u8*)"AT+QGPSLOC=0\r\n",
//											strlen("AT+QGPSLOC=0\r\n"));
				step = 0x03;
			}
			break;
			case 0x03://等待查GNSS响应
			{
//				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
//				{
//					if(strstr((char*)Uart3_RxBuf,"+QGPSLOC:"))
//					{
//						pdata = strstr((char*)Uart3_RxBuf,",");
//						if(pdata)
//						{
//							if(strstr((char*)Uart3_RxBuf,"N"))
//							{
//								pdata++;
//								SysMem_copy(EC20GpsDrive.latitude,pdata,4);
//								EC20GpsDrive.latitude_dir = 1;
//							}
//							else if(strstr((char*)Uart3_RxBuf,"S"))
//							{
//								pdata++;
//								SysMem_copy(EC20GpsDrive.latitude,pdata,4);
//								EC20GpsDrive.latitude_dir = 2;
//							}
//							else
//							{
//								memset(EC20GpsDrive.latitude,0,10);
//								SysMem_copy(EC20GpsDrive.latitude,"0000",strlen("0000"));
//								EC20GpsDrive.latitude_dir = 0;
//								step = 0xEE;	
//								wait_time = 0;	
//								reply_num = 0;
//								return ;
//							}				
//							pdata = strstr((char*)pdata,",");
//							if(pdata)
//							{
//								if(strstr((char*)pdata,"E"))
//								{
//									pdata++;
//									SysMem_copy(EC20GpsDrive.longitude,pdata,5);
//									EC20GpsDrive.longitude_dir = 1;
//								}
//								else if(strstr((char*)pdata,"W"))
//								{
//									pdata++;
//									SysMem_copy(EC20GpsDrive.longitude,pdata,5);
//									EC20GpsDrive.longitude_dir = 2;
//								}
//								else
//								{
//									memset(EC20GpsDrive.latitude,0,10);
//									SysMem_copy(EC20GpsDrive.latitude,"00000",strlen("00000"));
//									EC20GpsDrive.latitude_dir = 0;
//									memset(EC20GpsDrive.longitude,0,10);
//									SysMem_copy(EC20GpsDrive.longitude,"00000",strlen("00000"));
//									EC20GpsDrive.longitude_dir = 0;
//									step = 0xEE;	
//									wait_time = 0;	
//									reply_num = 0;
//									return ;
//								}	
//								
//							}
//						}
//					}
//					step = 0x00;
//					cycle_time = 0;	
//					wait_time = 0;	
//					reply_num = 0;
//					//
//				}
//				else if(strstr((char*)Uart3_RxBuf,"+CME ERROR:"))
//				{
//					step = 0x00;
//					cycle_time = 0;	
//					wait_time = 0;	
//					reply_num = 0;
//				}
//				else
//				{
//					wait_time++;
//					if(wait_time > 100)	//3秒重试
//					{
//						wait_time = 0;		
//						step = 0x02;	
//						reply_num++;
//						if(reply_num > 2)	//重试5次
//						{
							reply_num = 0;
							step = 0x00;
							cycle_time = 0;
							ec20_send_enable = 1;
//						}
//					}
//				}
			}
			break;
		}
	}
}


//网络参数配置
int EC20_ModuleConfig(NetworkPara_TypeDef * pNetworkPara)
{
	SysMem_copy(&EC20NetworkPara, pNetworkPara, sizeof(NetworkPara_TypeDef));	//更新缓存
	AuxConfig_UpNetWorkPara(pNetworkPara);	//同步到FLASH
	return 0xFF;
}


EC20TxControlTableTypeDef	EC20TxControlTable = {NULL,NULL,NULL};

//添加数据到队列
u8 EC20_Add_SendData(u8 * data, u16 size)
{
	EC20TxControlBlockTypeDef * pTxBlock;
	if(EC20TxControlTable.table_len == EC20_TXTABLE_MAXLEN)
		return 0x00;
	
	pTxBlock = (EC20TxControlBlockTypeDef*)SysMem_malloc(sizeof(EC20TxControlBlockTypeDef));
	if(pTxBlock == NULL)
		return 0x00;
	pTxBlock->TxUint.lenth = size;
	SysMem_copy((u8*)&pTxBlock->TxUint.data, data, size);
	if(EC20TxControlTable.head == NULL)
	{
		pTxBlock->next = NULL;
		pTxBlock->proir = NULL;
		EC20TxControlTable.head = pTxBlock;
		EC20TxControlTable.tail = pTxBlock;
		EC20TxControlTable.table_len++;
	}
	else
	{
		pTxBlock->next = NULL;
		EC20TxControlTable.tail->next = pTxBlock;
		pTxBlock->proir = EC20TxControlTable.tail;
		EC20TxControlTable.tail = pTxBlock;
		EC20TxControlTable.table_len++;
	}
	return 0xFF;
}

//从队列中获取数据
EC20TxUintTypeDef * EC20_Get_SendData(void)
{
	if(EC20TxControlTable.head == NULL)
		return NULL;
	return &EC20TxControlTable.head->TxUint;
}

//从队列中删除数据
u8 EC20_Remove_SendData(void)
{
	EC20TxControlBlockTypeDef * pTxBlock;
	
	if(EC20TxControlTable.head == NULL)
		return NULL;
	pTxBlock = EC20TxControlTable.head;
	if(EC20TxControlTable.head->next)
		EC20TxControlTable.head->next->proir = NULL;
	EC20TxControlTable.head = EC20TxControlTable.head->next;
	EC20TxControlTable.table_len--;
	SysMem_free(pTxBlock);
	return 0xFF;
}

u8 EC20_Remove_All_SendData(void)
{
	u8 i;
	for(i=0;i<10;i++)
	{
		if(!EC20TxControlTable.table_len)
		{
			break;
		}
		else
		{
			EC20_Remove_SendData();
		}
	}
}

char ec20_at_cmd_buffer[64];
//10ms

void EC20_SendData_Task(void)
{
	static u8 step;
	static u8 reply_num;
	static u16 wait_time;
	static EC20TxUintTypeDef * pTxUint = NULL;
	
	if(!ec20_send_enable)
		return;
	
	switch(step)
	{
		case 0x00://从队列中获取数据
		{
			pTxUint = EC20_Get_SendData();
			if(pTxUint == NULL)
				return;
			step = 0x01;
		}
		break;
		case 0x01://请求发送数据
		{
			memset((char*)Uart3_RxBuf,0,512);
			memset((char*)Uart3_TxBuf,0,512);
			memset((char*)ec20_at_cmd_buffer,0,64);
			sprintf(ec20_at_cmd_buffer,"AT+QISEND=0,%d\r\n",pTxUint->lenth);
			WierlessHarware_SendData((u8*)ec20_at_cmd_buffer,
										strlen(ec20_at_cmd_buffer));
			step = 0x02;
		}
		break;
		case 0x02://等待应答
		{
			if(strstr((char*)Uart3_RxBuf,">"))	//收到
			{
				step = 0x03;
				reply_num = 0;
				wait_time = 0;
			}
			else
			{
				if(wait_time < 100)
					wait_time++;
				else
				{
					wait_time = 0;
					reply_num = 0;
					step = 0x03;
//					reply_num++;
//					if(reply_num > 3)
//					{
//						reply_num = 0;
//						step = 0xEE;
//					}
//					else
//						step = 0x01;
				}
			}
		}
		break;
		case 0x03://发送数据内容
		{
			memset((char*)Uart3_RxBuf,0,512);
			memset((char*)Uart3_TxBuf,0,512);
			WierlessHarware_SendData(pTxUint->data,pTxUint->lenth);
			step = 0x04;
		}
		break;
		case 0x04://等待发送应答
		{
			if(strstr((char*)Uart3_RxBuf,"SEND OK"))	
			{
				
				step = 0xEE;
				reply_num = 0;
				wait_time = 0;
			}
			else if(strstr((char*)Uart3_RxBuf,"ERROR"))
			{
				reply_num++;
				if(reply_num > 3)
				{
					reply_num = 0;
					CloudProtol_Manage_Struct_Clear();					
					MQTT_Start_Reset();
					EC20_Remove_All_SendData();
					WirelessModule_ResetModule();
					step = 0xEE;
				}
			}
			else
			{
				if(wait_time < 100)
					wait_time++;
				else
				{
					wait_time = 0;
//					reply_num++;
//					if(reply_num > 3)
//					{
						reply_num = 0;
						step = 0xEE;
//					}
//					else
//						step = 0x03;
				}
			}
		}
		break;
		case 0xEE://从队列中删除
		{
			EC20_Remove_SendData();
			step = 0x00;
		}
		default:while(0);
	}
}

char EC20_Send_Data(u8 *data, u16 size)
{
	EC20_Add_SendData(data, size);
	return 0xFF;
}

void EC20_SNTP_Task(void)
{
	static u8 step  = 0;
	static u8 reply_num = 0;
	static u16 wait_time = 0;
	static u32	cycle_time = 40*100;
	u8 * pdata = NULL;
	Time_TypeDef ntpTime;
	
	if(cycle_time < 60*100)
	{
		cycle_time++;
	}
	else
	{
		switch(step)
		{
			case 0://查时间
			{
				ec20_send_enable = 0;
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CCLK?\r\n",
											strlen("AT+CCLK?\r\n"));
				step = 1;
			}
			break;
			case 1://等待查时间响应
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CCLK: \"");
					if(pdata)
					{
						pdata += strlen("+CCLK: \"");
						ntpTime.year = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%100+2000;
						if(ntpTime.year>2099)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("00/");
						ntpTime.month = ((*pdata-0x30)*10+(*(pdata+1)-0x30));
						if(ntpTime.month>12)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
							
						pdata += strlen("00/");
						ntpTime.day = ((*pdata-0x30)*10+(*(pdata+1)-0x30));
						if(ntpTime.day>31)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("00,");
						ntpTime.hour = ((*pdata-0x30)*10+(*(pdata+1)-0x30));
						if(ntpTime.hour>23)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("00:");
						ntpTime.min = ((*pdata-0x30)*10+(*(pdata+1)-0x30));
						if(ntpTime.min>59)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("00:");
						ntpTime.sec = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%60;
						if(ntpTime.sec>59)
						{
							wait_time = 0;		
//							step = 2;	
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
								reply_num = 0;
								step = 0x00;
								cycle_time = 0;
								ec20_send_enable = 1;
//							}
							return;
						}
						
						TimeStamp_UpData(&ntpTime);			//更新同步时间
						DgusApp_Set_Time(ntpTime.year%100,ntpTime.month,ntpTime.day,0,ntpTime.hour,ntpTime.min,ntpTime.sec);
					}
					
					wait_time = 0;	
					reply_num = 0;
					step = 2;
//					cycle_time = 0;
//					ec20_send_enable = 1;
				}
				else
				{
					wait_time++;
					if(wait_time > 100)	//3秒重试
					{
						wait_time = 0;		
//						step = 2;	
//						reply_num++;
//						if(reply_num > 3)	//重试5次
//						{
							reply_num = 0;
							step = 0x00;
							cycle_time = 0;
							ec20_send_enable = 1;
//						}
					}
				}
			}
			break;		
			case 2:
			{
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CSQ\r\n",
											strlen("AT+CSQ\r\n"));
				step = 3;
			}
			break;
			case 3:
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CSQ: ");
					if(pdata)
					{
						memset(EC20Rssi, 0, 15);
						pdata += strlen("+CSQ: ");
						SysMem_copy(EC20Rssi, pdata, 2);
						if(*pdata<0x32||*pdata>0x38)
							EC20RssiSta = 0;
						else
							EC20RssiSta = 1;
					}
					step = 0x00;
					cycle_time = 0;	
					wait_time = 0;	
					reply_num = 0;
					ec20_send_enable = 1;
					
					//
				}
				else if(strstr((char*)Uart3_RxBuf,"+CME ERROR:"))
				{
					step = 0x00;
					cycle_time = 0;	
					wait_time = 0;	
					reply_num = 0;
					ec20_send_enable = 1;
				}
				else
				{
					wait_time++;
					if(wait_time > 100)	//3秒重试
					{
						wait_time = 0;		
//						step = 2;	
//						reply_num++;
//						if(reply_num > 3)	//重试5次
//						{
							reply_num = 0;
							step = 0x00;
							cycle_time = 0;
							ec20_send_enable = 1;
//						}
					}
				}
			}
			break;
			
			default:break;
		}
	}
}

//0.01s定时执行
void EC20_TaskRun(void)
{
	static u32 rest_time = 0;
		
	if(CloudProtocol_ReadGoodsSta())
	{
		return;
	}
	
//	if(MQTT_Get_Start_Status())//设备网络不稳定
//	{
//		if(rest_time<5*6000)
//		 rest_time++;
//		else
//		{
//			rest_time=0;					
//			CloudProtol_Manage_Struct_Clear();
//			MQTT_Strat_Reboot();
//			WirelessModule_ResetModule();
////			Iap_SysReset();//系统复位
//		}
//	}
//	else 
//	{
//		rest_time=0;
//	}
	
//	if(CloudProtocol_ReadLink())
//	{
//		EC20_CSQ_GNSS_Check();		
//	}

	if(WirelessModule_ReadRunStaus())
	{
		EC20_SNTP_Task();
//		EC20_CSQ_GNSS_Check();				
	}
	
	EC20_SendData_Task();
}

