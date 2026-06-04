#include "wireless_module_init.h"


WirelessModuleInit_TypeDef WirelessModuleInit;
WirelessModule_ResetDrive_TypeDef	WirelessModule_ResetDrive;

//复位模块设定
void WirelessModule_ResetModule(void)
{
	WirelessModuleInit.RunSta = 0x03;		//去等待初始化
//	WirelessModule_ResetDrive.en = 0x01;	//使能复位模块
//	WirelessModule_ResetDrive.time = 0x00;
	WirelessModule_ResetDrive.module = WirelessModuleInit.TypeNum;	//根据模块类型配置复位模式
}

//复位模块任务
void WirelessModule_ResetTask(void)
{
	if(WirelessModule_ResetDrive.en == 0)
		return ;
	else
	{
		if(WirelessModule_ResetDrive.time < 30)
		{
			WirelessModule_ResetDrive.time++;
			GPIO_ResetBits(GPIOC, GPIO_Pin_1);	
		}
		else if(WirelessModule_ResetDrive.time < 60)
		{
			WirelessModule_ResetDrive.time++;
			GPIO_SetBits(GPIOC, GPIO_Pin_1);	
		}
		else
		{
			WirelessModule_ResetDrive.time = 0;
			WirelessModule_ResetDrive.en = 0;
		}

	}
}



u8 WirelessModule_ReadTypeNum(void)
{
	return WirelessModuleInit.TypeNum;
}

void WirelessModule_Init(void)
{
	WierlessHarware_InterfaceInit();

	//EC20	4G模块
	WirelessModuleInit.WeirelessModule_AtInterface[0].RunTask=EC20_TaskRun;
	WirelessModuleInit.WeirelessModule_AtInterface[0].config_sta = 0;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ConfigModule = EC20_ConfigModule;
	WirelessModuleInit.WeirelessModule_AtInterface[0].CheckModule=EC20_CheckModule;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReciveParsing =EC20_ReciveParsing;
	WirelessModuleInit.WeirelessModule_AtInterface[0].SendData = EC20_Send_Data;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ModuleInit =EC20_Init;
	WirelessModuleInit.WeirelessModule_AtInterface[0].init_sta=0;
	WirelessModuleInit.WeirelessModule_AtInterface[0].module_type=WEIRELESS_MODULE_TYPEDEF_EC20;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReadNetStr =EC20_ReadNetStr;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReadRssiStr=EC20_ReadRssiStr;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReadIccidStr = EC20_ReadIccidStr;
	WirelessModuleInit.WeirelessModule_AtInterface[0].GetLatitude = AtEC20GpsDrive_GetLatitude;
	WirelessModuleInit.WeirelessModule_AtInterface[0].GetLongitude = AtEC20GpsDrive_GetLongitude;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReadAtSta  =EC20_ReadAtSta;
	WirelessModuleInit.WeirelessModule_AtInterface[0].InitTime = WEIRELESS_MODULE_INIT_TIME_EC20;
	WirelessModuleInit.WeirelessModule_AtInterface[0].ReadRssiSta = EC20_ReadRssiSta;
	
	//ESP32	WIFI模块
	WirelessModuleInit.WeirelessModule_AtInterface[1].RunTask=ESP32_TaskRun;
	WirelessModuleInit.WeirelessModule_AtInterface[1].config_sta = 0;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ConfigModule = ESP32_ConfigModule;
	WirelessModuleInit.WeirelessModule_AtInterface[1].CheckModule=ESP32_CheckModule;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReciveParsing =ESP32_ReciveParsing;
	WirelessModuleInit.WeirelessModule_AtInterface[1].SendData = ESP32_Send_Data;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ModuleInit =ESP32_Init;
	WirelessModuleInit.WeirelessModule_AtInterface[1].init_sta=0;
	WirelessModuleInit.WeirelessModule_AtInterface[1].module_type=WEIRELESS_MODULE_TYPEDEF_ESP32;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReadNetStr = NULL;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReadRssiStr= NULL;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReadIccidStr = NULL;
	WirelessModuleInit.WeirelessModule_AtInterface[1].GetLatitude = NULL;
	WirelessModuleInit.WeirelessModule_AtInterface[1].GetLongitude = NULL;
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReadAtSta  =ESP32_ReadAtSta;
	WirelessModuleInit.WeirelessModule_AtInterface[1].InitTime = WEIRELESS_MODULE_INIT_TIME_ESP32;	
	WirelessModuleInit.WeirelessModule_AtInterface[1].ReadRssiSta = ESP32Harware_ReadRssiSta;

}

u8 WirelessModule_ReadRunStaus(void)
{
	if(WirelessModuleInit.RunSta >= 0x04)
		return 0x01;
	else
		return 0x00;
}


void WirelessModule_ScanJump(u8 runsta, u8 typenum)
{
	WirelessModuleInit.TypeNum = typenum;
	WirelessModuleInit.RunSta = runsta;
	WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].check_sta = 0x01;	
	WirelessModuleInit.InitSta=0x01;
}

//模块数据采集运行任务，0.01s运行一次
void WirelessModule_RunTask(void)
{
	u8 res = 0;

	switch (WirelessModuleInit.RunSta)
	{
		case 0x00://初始化
			{
				//看看当前模块是否需要初始化
				if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].init_sta==NULL)	
				{
					//看看当前模块是否具备初始化函数
					if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ModuleInit)	
					{
						//初始化当前模块
						res = WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ModuleInit();
					}
					if(res == 0xFF)
					{
						//去等待初始化完成
						WirelessModuleInit.RunSta=0x01;		
						WirelessModuleInit.InitTime=0x00;
					}
				}
			}
			break;
		case 0x01://等待初始化完成
			{
				if(WirelessModuleInit.InitTime < WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].InitTime)	
				{
					WirelessModuleInit.InitTime++;	//x10ms
				}
				else
				{
					 WirelessModuleInit.InitTime=0;
					//去识别模块类型
					 WirelessModuleInit.RunSta=0x02;	
				}
			}
			break;
		case 0x02://识别模块类型
			{
				uint8_t state = 0;
							
				//看看当前模块是否需要识别
				if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].check_sta == NULL)
				{
					//看看是否具备识别函数
					if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].CheckModule)
					{
						//识别当前模块
						state=WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].CheckModule();
					}
					//识别成功
					if(state==0xFF)		
					{
						WirelessModuleInit.InitSta=0x01;
						//去配置模块
						WirelessModuleInit.RunSta=0x03;		
						//下次不再识别
						WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].check_sta = 0x01;
					}
					//识别失败		
					else if(state==0xEE)	
					{
						//重新开始流程
						WirelessModuleInit.RunSta=0x00;		
						//去识别下一模块类型
						WirelessModuleInit.TypeNum++;		
						if(WirelessModuleInit.TypeNum==WEIRELESS_MODULE_TYPE_NUM)	
							WirelessModuleInit.TypeNum=0;
					}
				}
				else
				{
					//去配置模块
					WirelessModuleInit.RunSta=0x03;		
				}
			}
			break;
		case 0x03://配置
			{
				uint8_t state = 0;
				
				//看看当前模块是否需要配置
				if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].config_sta == NULL)
				{
					//看看是否具备配置函数
					if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ConfigModule)
						state = WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ConfigModule();
					if(state == 0xFF)	//配置成功
					{
						WirelessModuleInit.RunSta = 0x04;
					}
//					else if(state == 0xEE)	//配置失败
//					{
//						WirelessModuleInit.RunSta=0x00;		//重新开始流程
//						WirelessModuleInit.TypeNum++;		//去识别下一模块类型
//					if(WirelessModuleInit.TypeNum==WEIRELESS_MODULE_TYPE_NUM)	
//					 WirelessModuleInit.TypeNum=0;
//					}
				}
				else
				{
					//模块开始通信
					WirelessModuleInit.RunSta = 0x04;
				}
			}
			break;
		case 0x04:	//进入正常运行
			WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].RunTask();
			break;
	}
}

//接收数据处理
char WirelessModule_ReciveParsing(u8 * data, u16 size)
{
	if(WirelessModuleInit.InitSta && WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReciveParsing)
	  return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReciveParsing(data,size);
	else
		return NULL;
}

//发送数据
char WirelessModule_SendData(u8 * data, u16 size)
{
	if(WirelessModuleInit.InitSta && WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].SendData)
	  return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].SendData(data,size);
	else
		return NULL;
	
}

//查询是否模块识别完成
char WirelessModule_ReadInitSta(void)
{
	return WirelessModuleInit.InitSta;
}

//查询模块是否处于AT指令模式
char WirelessModule_ReadAtSta(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadAtSta)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadAtSta();
	else
		return NULL;
}

//获取模块信号强度
char *WirelessModule_ReadRssi(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadRssiStr)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadRssiStr();
	else
		return NULL;
}

u8 WirelessModule_ReadRssiSta(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadRssiSta)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadRssiSta();
	else
		return 0;
}

//获取模块网络模式
char *WirelessModule_ReadNet(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadNetStr)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadNetStr();
	else
		return NULL;
}

//获取SIM卡 ICCID
char *WirelessModule_ReadIccid(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadIccidStr)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].ReadIccidStr();
	else
		return NULL;
}


char * WirelessModule_ReadLatitude(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].GetLatitude)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].GetLatitude();
	else
		return NULL;
}

char * WirelessModule_ReadLongitude(void)
{
	if(WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].GetLongitude)
		return WirelessModuleInit.WeirelessModule_AtInterface[WirelessModuleInit.TypeNum].GetLongitude();
	else
		return NULL;
}



