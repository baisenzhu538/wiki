#include "at_air720.h"
#include "cloud_protocol.h"
#include "wireless_hardware_interface.h"
#include "wireless_module_init.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "usart.h"
#include "debug.h"
#include "sys_config.h"
#include "at_ec20.h"
#include "mqtt_recive.h"


char *Air720EnterCmd[2] = {"+++",				//进入AT模式
							"ATO\r\n",};		//退出AT模式
char *Air720InquireCmd[3]={
						"AT+CSQ\r\n",    		//查询信号强度
						"AT+CREG\r\n",			//查询是否注册到运营商
						"AT+REBT\r\n",			//重启
						};
char *Air720ResponseCmd[3]={
						"\r\nOK\r\n",
						"\r\n+CSQ: ",
						"\r\nCONNECT\r\n"
						};
char Air720Rssi[15]={"NULL"};	//信号强度
char Air720Net[15]= {"NULL"};			//未用
char Air720Mode[15] = {""};		//4G模块工作模式
char Air720Iccid[25] = {"NULL"};
u16 testrssi = 0;

u8 AIR720_CIPSTART_AT_CMD[100];
NetworkPara_TypeDef	AIR720NetworkPara = {"zd.jumiai.cn","1883","TCP"};

char AIR720Latitude[10] = {"00.00"};
char AIR720Longitude[10] = {"000.00"};


char * AIR720GpsDrive_GetLatitude(void)
{
	return AIR720Latitude;
}
char * AIR720GpsDrive_GetLongitude(void)
{
	return AIR720Longitude;
}

void AtAir720NetworkParaCopy(NetworkPara_TypeDef * NetworkPara)
{
	SysMem_copy((u8*)&AIR720NetworkPara, (u8*)NetworkPara, sizeof(NetworkPara_TypeDef));
	memset((char*)AIR720_CIPSTART_AT_CMD,0,100);
	sprintf((char*)AIR720_CIPSTART_AT_CMD,"AT+CIPSTART=\"TCP\",\"%s\",%s\r\n",(char*)"zd.jumiai.cn", "1883");
}

char *AtAir720_GetDataString(char *pRes,char *pStr)
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

////模块电源复位
//void AtAirHarware_PowerReset(void)
//{
//	uint32_t i=0xFFFFFF;	
//	AIR720_PWR_CTL = 1;
//	while(i--);
//	i = 0xFFFFFF;
//	AIR720_PWR_CTL = 0;
//	while(i--);
//}

////模块引脚复位
//void AtAirHarware_ResetModule(void)
//{
//	uint32_t i=0xFFFFF;
//	AIR720_RST_CTL = 1;//拉高
//	while(i--);
//	i = 0xFFFFF;
//	AIR720_RST_CTL = 0;//拉低 
//	while(i--);
//}

u8 AtAirHarware_PowerReset(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				AIR720_PWR_CTL = 1;
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
				AIR720_PWR_CTL = 0;
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

u8 AtAirHarware_ResetModule(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				AIR720_RST_CTL = 1;//拉高
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
				AIR720_RST_CTL = 0;//拉低 
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

//模块软件复位
void AtAirSoftWare_ResetModule(void)
{
	WierlessHarware_SendData((u8 *)"AT+RESET\r\n",strlen("AT+RESET\r\n"));	
}

//模块初始化
u8 AtAir720_Init(void)
{
	static u8 res1 = 0;
	static u8 res2 = 0;
	static u8 first_flag = 1;
//	GPIO_InitTypeDef  GPIO_InitStructure;
//		
//	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);	 //使能PB,PE端口时钟
//		
//	
//	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
//	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
//	GPIO_InitStructure.GPIO_Pin  = GPIO_Pin_12;				 //LED0-->PB.5 端口配置
//	GPIO_Init(GPIOC, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
//	
//	GPIO_InitStructure.GPIO_Pin  = GPIO_Pin_2;				 //LED0-->PB.5 端口配置
//	GPIO_Init(GPIOC, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
//	
//	AIR720_NRST_CTL = 0;
//	AIR720_PWR_CTL = 0;
//	AuxConfig_UpNetWorkPara(&AIR720NetworkPara);
	if(first_flag)
	{
		first_flag = 0;
		AuxConfig_GetNetWorkPara(&AIR720NetworkPara);
		memset((char*)AIR720_CIPSTART_AT_CMD,0,100);
		sprintf((char*)AIR720_CIPSTART_AT_CMD,"AT+CIPSTART=\"TCP\",\"%s\",%s\r\n",(char*)"zd.jumiai.cn", "1883");
	}
	if(AtAirHarware_ResetModule())
	{
		res1 = 0xFF;
	}
	if(AtAirHarware_PowerReset())
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




u8 AtAir720_StartWait(u8 * string)
{
	char * pRes = "\r\nSMS READY";
	u8 i;
	for(i = 0; i < strlen(pRes); i++)
	{
		if(*pRes != *string)
			return 0x00;
		pRes++;
		string++;
	}
	return 0x01;
}

#define	CSQ_WAIT_OUTTIME		0x1FFF
#define	CMD_WAIT_OUTTIME		0x1FFF
#define	AT_WAIT_OUTTIME			0x1FFF		//握手超时时间
#define	START_WAIT_OUTTIME		0x2FFF		//等待模块初始化时间
#define	PT_WAIT_OUTTIME			0x1FFF		
#define	CPIN_WAIT_OUTTIME		0xFF		//等待查询SIM卡时间
#define	CGATT_WAIT_OUTTIME		0xFF		//等待查询GPRS时间
#define	CIPMODE_WAIT_OUTTIME	0xFF	//
#define	ATE0_WAIT_OUTTIME		0xFF	//
#define	CIFSR_WAIT_OUTTIME		0xFF


u32 shutwait_time = 0;
u8 tcpstatus = 0;
uint8_t mode = 0x01;
u16 sendAT_num = 0;
u16 sendCPIN_num = 0;
u16 cfun_wait_time;
u16 sendEN_CFUN_num = 0;
u16 sendEX_CFUN_num = 0;
u16 sendCSQ_num = 0;
u16 sendCGATT_num = 0;
u16 sendCIPSHUT_num = 0;
u16 cipshut_wait_time = 0;
u16 sendCSTT_num = 0;
u16 sendCIICR_num = 0;
u16 sendCIPMODE_num = 0;


typedef struct
{
	u8 reset_mode;
	u8 mode;
	u8 reply_num;
	u32 wait_time;	
	u8 ip[32];
	int rssi;
	
}AIR_LinkInfo_TypeDef;
	
AIR_LinkInfo_TypeDef	AIR_LinkInfo = {0,0x00};//BUG
//AIR_LinkInfo_TypeDef	AIR_LinkInfo = {0,0x00};//BUG


void AtAir720_SetMode(u8 mode)
{
	AIR_LinkInfo.mode = mode;
}

u8 AtAir720_CheckModule(void)
{
	static u8 mode = 0;
	static u16 reply_num = 0;
	static u16 wait_time = 0;
	
	switch(mode)
	{
		case 0://查模块型号
		{	
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CGMM\r\n",strlen("AT+CGMM\r\n"));
			mode = 1;
		}
		break;
		case 1://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"Air720"))	//收到
			{
				mode = 0;	//
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;
			}
			else if(strstr((char*)Uart4_RxBuf,"EC20"))
			{
				EC20NetworkParaCopy(&AIR720NetworkPara);
				WirelessModule_ScanJump(0x03,0x03);
				mode = 0;	//
				wait_time = 0;	
				reply_num = 0;
				return 0x00;
			}
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
u8 AtAir720_ConfigModule(void)
{
	static uint32_t time=0;
	u8 res = 0;
	static uint16_t	size = 0;
	static uint8_t* string;	 
	static u32 wait_time = 0;
	static u8 reply_num = 0;
	static u8 reset_num = 0;
	char * pdata = NULL;

	
	switch(AIR_LinkInfo.mode)
	{
		case 0xEE:
		{
			switch(AIR_LinkInfo.reset_mode)
			{
				case 0:
					{
						res = AtAirHarware_ResetModule();		//硬件复位
						if(res == 0xFF)
							AIR_LinkInfo.reset_mode = 1;
					}
					break;
				case 1:
					{
						res = AtAirHarware_PowerReset();		//掉电
						if(res == 0xFF)
							AIR_LinkInfo.reset_mode = 2;
					}
					break;
				case 2:
					{
						AIR_LinkInfo.mode = 0x00;
						AIR_LinkInfo.reset_mode = 0;
					}
					break;
			}			
		}
		break;

/*********************************************** 等待模块启动 ***************************************************/		
		case 0x00://等待模块就绪	-- //等待 "\r\nSMS READY\r\n" 
		{
			if(strstr((char*)Uart4_RxBuf,"SMS READY"))
			{
				AIR_LinkInfo.mode = 0x01;		//模块已就绪，去发送AT指令握手
				wait_time = 0;		
			}		
			else	
			{
				wait_time++;
				if(wait_time > 30*100)
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x01;	//等待超过1min，去发送AT指令握手
				}
			}
		}
		break;
/***************************************************************************************************************/

		
/**********************************************发AT指令握手******************************************************/	
		case 0x01://发送AT
		{	
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT\r\n",strlen("AT\r\n"));
			AIR_LinkInfo.mode = 0x02;
		}
		break;
		case 0x02://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到
			{
				AIR_LinkInfo.mode = 0x03;	//去关闭回显
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x01;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//去复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
		
		

/**********************************************检查SIM卡*********************************************************/		
		case 0x03://检查SIM卡
		{
			
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CPIN?\r\n",strlen("AT+CPIN?\r\n"));
			AIR_LinkInfo.mode = 0x04;
		}
		break;
		case 0x04://等待响应
		{			
			if(strstr((char*)Uart4_RxBuf,"\r\n+CPIN: READY\r\n"))	//收到响应
			{
				AIR_LinkInfo.mode = 0x05;	//去查CSQ
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x03;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/

//STEP5
/***************************************************************************************************************/
		case 0x05:
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+ICCID\r\n",strlen("AT+ICCID\r\n"));
			AIR_LinkInfo.mode = 0x06;
		}
		break;
		case 0x06:
		{
			if(strstr((char*)Uart4_RxBuf,"+ICCID: "))	//收到响应
			{
				AIR_LinkInfo.mode = 0x07;	//去查CSQ
				wait_time = 0;	
				reply_num = 0;
				pdata = strstr((char*)Uart4_RxBuf,"+ICCID: ") + strlen("+ICCID: ");
				SysMem_copy(Air720Iccid, pdata, 20);
				
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x05;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/

//STEP5		
/*************************************************查CSQ**********************************************************/		
		case 0x07://查CSQ
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CSQ\r\n",strlen("AT+CSQ\r\n"));
			AIR_LinkInfo.mode = 0x08;
		}
		break;
		case 0x08://等待响应
		{
			u8 * data = NULL;
			u8 i = 0;
			u8 j = 0;
			int sum = 0;
			
			if(strstr((char*)Uart4_RxBuf,"\r\n+CSQ: "))
			{
				data = (u8*)(strstr((char*)Uart4_RxBuf,"\r\n+CSQ: ") + strlen("\r\n+CSQ: "));
				AtAir720_GetDataString((char*)(data),Air720Rssi);
				for(i = 0; i < 3; i++)
				{
					
					if(*(data+i) == ',')
						break;
					sum *= 10;
					sum += *(data+i) - 0x30;
				}
				AIR_LinkInfo.rssi = sum;


			}
			
			if(AIR_LinkInfo.rssi > 0)	//RSSI值大于0
			{
				AIR_LinkInfo.mode = 0x09;	//去查当前GPRS符着情况
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;				
					AIR_LinkInfo.mode = 0x07;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
		
		
//STEP6		
/*******************************************查询当前GPRS符着情况*************************************************/		
		case 0x09://查询当前GPRS符着情况
		{
			
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CGATT?\r\n",strlen("AT+CGATT?\r\n"));
			AIR_LinkInfo.mode = 0x0A;
		}
		break;
		case 0x0A://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\n+CGATT: 1"))	//附着成功
			{
				AIR_LinkInfo.mode = 0x0B;	
				wait_time = 0;	
				reply_num = 0;
			}
			else	//无响应
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x09;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
	

//设置为单链接模式
/***************************************************************************************************************/
		case 0x0B://设置单链接
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIPMUX=0\r\n",strlen("AT+CIPMUX=0\r\n"));
			AIR_LinkInfo.mode = 0x0C;
		}
		break;//等待应答
		case 0x0C:
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到响应
			{
				AIR_LinkInfo.mode = 0x0D;	//去查CSQ
				wait_time = 0;	
				reply_num = 0;
				
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x0B;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
	
//设置为慢发模式
/***************************************************************************************************************/
		case 0x0D://设置慢发
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIPQSEND=1\r\n",strlen("AT+CIPQSEND=1\r\n"));
			AIR_LinkInfo.mode = 0x0E;
		}
		break;//等待应答
		case 0x0E:
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到响应
			{
				AIR_LinkInfo.mode = 0x0F;	//去查CSQ
				wait_time = 0;	
				reply_num = 0;
				
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x0D;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
	
//设置非透传传输模式		
/***************************************************************************************************************/
		case 0x0F:
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIPMODE=0\r\n",strlen("AT+CIPMODE=0\r\n"));
			AIR_LinkInfo.mode = 0x10;
		}
		break;
		case 0x10:
		{
			if(strstr((char*)Uart4_RxBuf,"OK"))	//收到响应
			{
				AIR_LinkInfo.mode = 0x11;	
				wait_time = 0;	
				reply_num = 0;
				
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x0F;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/
		
//STEP9		
/*********************************************** 设置APN ***************************************************/
		case 0x11://设置APN，移动物联
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CSTT=\"CMIOT\"\r\n",strlen("AT+CSTT=\"CMIOT\"\r\n"));
			AIR_LinkInfo.mode = 0x12;
		}
		break;
		case 0x12://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\nOK\r\n"))	//收到
			{
				AIR_LinkInfo.mode = 0x13;	//去激活移动场景
				wait_time = 0;	
				reply_num = 0;
			}
			else	//无响应
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x11;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;//复位
					}
				}
			}
		}
		break;
/***********************************************************************************************************/		

		
//STEP10	
/********************************************* 激活移动场景 *************************************************/
		
		case 0x13://激活移动场景
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIICR\r\n",strlen("AT+CIICR\r\n"));
			AIR_LinkInfo.mode = 0x14;
		}
		break;
		case 0x14://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\nOK\r\n"))	//收到
			{
				AIR_LinkInfo.mode = 0x15;	//去查IP
				wait_time = 0;	
				reply_num = 0;
			}
			else	//无响应
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x13;	
					reply_num++;
					if(reply_num > 5)	//重试3次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;//复位	
					}
				}
			}
		}
		break;
/***********************************************************************************************************/		
		

//STEP11		
/**********************************************查本机IP*******************************************************/		
		case 0x15://查IP
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIFSR\r\n",strlen("AT+CIFSR\r\n"));
			AIR_LinkInfo.mode = 0x16;
		}
		break;
		case 0x16://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\n"))	//收到
			{
				AIR_LinkInfo.mode = 0x17;	//去建立TCP连接
				wait_time = 0;	
				reply_num = 0;
			}
			else	//无响应
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x15;	
					reply_num++;
					if(reply_num > 10)	//重试5次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/


//STEP12
/***********************************************建立TCP*********************************************************/
		case 0x17://建立TCP连接
		{
			memset((char*)Uart4_RxBuf,0,512);
			WierlessHarware_SendData((u8*)AIR720_CIPSTART_AT_CMD, strlen((char*)AIR720_CIPSTART_AT_CMD));
			AIR_LinkInfo.mode = 0x18;
		}
		break;
		case 0x18://等待响应
		{
			if(strstr((char*)Uart4_RxBuf,"\r\nOK\r\n"))	//配置成功
			{
				AIR_LinkInfo.mode = 0x19;	//去等待TCP建立
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					AIR_LinkInfo.mode = 0x17;	
					reply_num++;
					if(reply_num > 5)	//重试3次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
		case 0x19://等待建立
		{
			if(strstr((char*)Uart4_RxBuf,"CONNECT OK"))	//建立成功
			{
				AIR_LinkInfo.mode = 0x00;	
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;		
			}
			else	//无响应
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					reply_num++;
					if(reply_num > 10)	//重试3次
					{
						reply_num = 0;
						AIR_LinkInfo.mode = 0xEE;	//复位
					}
				}
			}
		}
		break;
/***************************************************************************************************************/

	}	 
	return 0x00;
}


//读模块工作模式
char *AtAir720_ReadModeStr(void)
{
	return Air720Mode;
}

//读信号强度
char *AtAir720_ReadRssiStr(void)
{
	return Air720Rssi;
}

//读网络信息
char *AtAir720_ReadNetStr(void)
{
	return Air720Net;
}

//读ICCID
char *AtAir720_ReadIccidStr(void)
{
	return Air720Iccid;
}

void AtAir720RssiDataClear(void)
{
//	u8 i;
//	for(i = 0; i < 15; i++)
//	{
//		Air720Rssi[i] = 0;
//	}
}

u8 AtAir720_CmdCheckCMP(char *pRes, char * cmd)
{
	char i,*ps,*pd;
	ps=cmd;
	pd=pRes;
	while(*ps)
	{
		if((*ps)!=(*pd))
			return 0x01;
		ps++;
		pd++;
	}
	return 0x00;
}

//校验指令，并返回参数段地址
char* AtAir720_CmdCheck(char *pRes,char* cmd)
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





AtCheckSta_TypeDef	AtCheckSta;

//解析返回AT响应指令，返回 NULL 不是AT指令 返回 ！NULL 为AT指令
char AtAir720_ReciveParsing(u8 * data, u16 size)
{
	char i;
	u8 res = 0;
	char *p;
	
	if(data[size-1]=='\n'
		&&data[size-2]=='\r'
		&&data[0]=='\r'
		&&data[1]=='\n')
	{
		while(0);
	}
	else
	{
		MQTT_Pack_Json_Cut(data,size);
	}
	return NULL;
}





static short int rest_time=0;//复位4G模块驱动时间
static unsigned int time=0;
static char sta=0x00;
static char atsta=0;

char AtAir720_ReadAtSta(void)
{
	return atsta;
}


u8 AtAir_CloseTcpConnect(void)	//关闭网络连接
{	
	WierlessHarware_SendData((u8 *)"AT+CIPCLOSE\r\n",strlen("AT+CIPCLOSE\r\n"));
	if(findStr(Uart4_RxBuf, (u8*)"\r\nCLOSE OK\r\n", 0x1FFF))
		return 0x01;
	else
		return 0x00;
}

static u16 checkouttime = 0;
static u8  checkmode = 0;
static u32 checktime = 0;
static u8  checknum = 0;
















int AtAir720_ModuleConfig(NetworkPara_TypeDef * pNetworkPara)
{
	SysMem_copy(&AIR720NetworkPara, pNetworkPara, sizeof(NetworkPara_TypeDef));	//更新缓存
	AuxConfig_UpNetWorkPara(pNetworkPara);	//同步到FLASH
	return 0xFF;
}






EC20TxControlTableTypeDef	Air720TxControlTable = {NULL,NULL,NULL};

//添加数据到队列
u8 AIR720_Add_SendData(u8 * data, u16 size)
{
	EC20TxControlBlockTypeDef * pTxBlock;
	if(Air720TxControlTable.table_len == EC20_TXTABLE_MAXLEN)
		return 0x00;
	
	pTxBlock = (EC20TxControlBlockTypeDef*)SysMem_malloc(sizeof(EC20TxControlBlockTypeDef));
	if(pTxBlock == NULL)
		return 0x00;
	pTxBlock->TxUint.lenth = size;
	SysMem_copy((u8*)&pTxBlock->TxUint.data, data, size);
	if(Air720TxControlTable.head == NULL)
	{
		pTxBlock->next = NULL;
		pTxBlock->proir = NULL;
		Air720TxControlTable.head = pTxBlock;
		Air720TxControlTable.tail = pTxBlock;
		Air720TxControlTable.table_len++;
	}
	else
	{
		pTxBlock->next = NULL;
		Air720TxControlTable.tail->next = pTxBlock;
		pTxBlock->proir = Air720TxControlTable.tail;
		Air720TxControlTable.tail = pTxBlock;
		Air720TxControlTable.table_len++;
	}
	return 0xFF;
}

//从队列中获取数据
EC20TxUintTypeDef * AIR720_Get_SendData(void)
{
	if(Air720TxControlTable.head == NULL)
		return NULL;
	return &Air720TxControlTable.head->TxUint;
}

//从队列中删除数据
u8 AIR720_Remove_SendData(void)
{
	EC20TxControlBlockTypeDef * pTxBlock;
	
	if(Air720TxControlTable.head == NULL)
		return NULL;
	pTxBlock = Air720TxControlTable.head;
	if(Air720TxControlTable.head->next)
		Air720TxControlTable.head->next->proir = NULL;
	Air720TxControlTable.head = Air720TxControlTable.head->next;
	Air720TxControlTable.table_len--;
	SysMem_free(pTxBlock);
	return 0xFF;
}

char air720_at_cmd_buffer[64];


//10ms
void AtAir720_SendData_Task(void)
{
	static u8 step;
	static u8 reply_num;
	static u16 wait_time;
	static EC20TxUintTypeDef * pTxUint = NULL;
	
	switch(step)
	{
		case 0x00://从队列中获取数据
		{
			pTxUint = AIR720_Get_SendData();
			if(pTxUint == NULL)
				return;
			step = 0x01;
		}
		break;
		case 0x01://请求发送数据
		{
			memset((char*)Uart4_RxBuf,0,512);
			memset((char*)Uart4_TxBuf,0,512);
			memset((char*)air720_at_cmd_buffer,0,64);
			sprintf(air720_at_cmd_buffer,"AT+CIPSEND=%d\r\n",pTxUint->lenth);
			WierlessHarware_SendData((u8*)air720_at_cmd_buffer,
										strlen(air720_at_cmd_buffer));
			step = 0x02;
		}
		break;
		case 0x02://等待应答
		{
			if(strstr((char*)Uart4_RxBuf,">"))	//收到
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
					reply_num++;
					if(reply_num > 3)
						step = 0xEE;
					else
						step = 0x01;
				}
			}
		}
		break;
		case 0x03://发送数据内容
		{
			memset((char*)Uart4_RxBuf,0,512);
			memset((char*)Uart4_TxBuf,0,512);
			WierlessHarware_SendData(pTxUint->data,pTxUint->lenth);
			step = 0x04;
		}
		break;
		case 0x04://等待发送应答
		{
			if(strstr((char*)Uart4_RxBuf,"SEND OK"))	
			{
				
				step = 0xEE;
				reply_num = 0;
				wait_time = 0;
			}
			else
			{
				if(wait_time < 100)
					wait_time++;
				else
				{
//					wait_time = 0;
//					reply_num++;
//					if(reply_num > 3)
						step = 0xEE;
//					else
//						step = 0x04;
				}
			}
		}
		break;
		case 0xEE://从队列中删除
		{
			AIR720_Remove_SendData();
			step = 0x00;
		}
		default:while(0);
	}
}



char AtAir720_SendData(u8* data,u16 size)
{
	AIR720_Add_SendData(data, size);
	return 0xFF;
}







void AtAir720_CSQ_Check(void)
{
	static u16 wait_time = 0x00;
	static u8 reply_num = 0x00;
	static u8 step = 0x00;
	int sum = 0;
	char * data;
	u8 i;
	static u32 cycle_time = 0x00;
	
	if(cycle_time < 2*60*100)
	{
		cycle_time++;
	}
	else
	{
		switch(step)
		{
			case 0x00://查CSQ
			{
				memset((char*)Uart4_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CSQ\r\n",strlen("AT+CSQ\r\n"));
				step = 0x01;
			}
			break;
			case 0x01://等待应答
			{
				if(strstr((char*)Uart4_RxBuf,"\r\n+CSQ: "))
				{
					data = strstr((char*)Uart4_RxBuf,"\r\n+CSQ: ") + strlen("\r\n+CSQ: ");
					AIR_LinkInfo.rssi = atoi(data);
					memset(Air720Rssi,0,15);
					SysMem_copy(Air720Rssi, data, 2);
					step = 0x00;
					cycle_time = 0;
				}
				else
				{
					wait_time++;
					if(wait_time > 1*100)	//1秒重试
					{
						wait_time = 0;				
						reply_num++;
						step = 0x00;
						if(reply_num > 3)	//重试3次
						{
							reply_num = 0;
							step = 0x00;
							cycle_time = 0;
						}
					}
				}
			}
			break;
		}
	}
}




//0.01s定时执行
void AtAir720_TaskRun(void)
{
	if(CloudProtocol_ReadGoodsSta())
	{
		return;
	}
	
	if(MQTT_Get_Start_Status() && CloudProtocol_ReadLink()==0x00)//设备网络不稳定
	{
		if(rest_time<5*6000)
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
		AtAir720_CSQ_Check();
	}
	AtAir720_SendData_Task();
}




