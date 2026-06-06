#ifndef __WIRELESS_MODULE_INIT_H
#define __WIRELESS_MODULE_INIT_H

#include "sys.h"
#include "wireless_hardware_interface.h"
#include "task_manage.h"
#include "at_ec20.h"
#include "esp32.h"

#define WEIRELESS_MODULE_TYPE_NUM  2   //模块型号数量
#define WEIRELESS_MODULE_INIT_TIME 3000  //40s



#define WEIRELESS_MODULE_TYPEDEF_EC20   	0x01
#define WEIRELESS_MODULE_TYPEDEF_ESP32   	0x02

#define	WEIRELESS_MODULE_INIT_TIME_EC20		2000
#define	WEIRELESS_MODULE_INIT_TIME_ESP32	1000	

typedef	struct
{
	u8	en;
	u8	module;
	u16 time;
	
}WirelessModule_ResetDrive_TypeDef;
	 
typedef struct
{
	uint8_t init_sta;
	uint8_t check_sta;
	uint8_t config_sta;
	uint8_t module_type;
	void (*RunTask)(void);
	uint8_t (*ConfigModule)(void);
	uint8_t (*CheckModule)(void);
	u8 (*ModuleInit)(void);
	char (*ReciveParsing)(u8 *,u16);
	char (*SendData)(u8 *,u16);
	char* (*ReadRssiStr)(void);
	char* (*ReadNetStr)(void);  
	char* (*ReadIccidStr)(void);
	char* (*GetLongitude)(void);
	char* (*GetLatitude)(void);	
	char  (*ReadAtSta)(void);		
	u8 (*ReadRssiSta)(void);
	uint16_t InitTime;
}WeirelessModule_AtInterface_TypeDefDef;


typedef struct
{
	uint8_t TypeNum;
	uint8_t RunSta;
	uint8_t InitSta;
	uint8_t InitMod;
	uint16_t InitTime;
	WeirelessModule_AtInterface_TypeDefDef WeirelessModule_AtInterface[WEIRELESS_MODULE_TYPE_NUM];
}WirelessModuleInit_TypeDef;


extern WirelessModuleInit_TypeDef WirelessModuleInit;

char *WirelessModule_ReadRssi(void);
char *WirelessModule_ReadNet(void);
void WirelessModule_RunTask(void);
char WirelessModule_ReadInitSta(void);
void WirelessModule_Init(void);
char WirelessModule_ReciveParsing(u8 *data,u16 size);
char WirelessModule_SendData(u8 * data, u16 size);
char WirelessModule_ReadAtSta(void);
void WirelessModule_RunStateClear(void);
void WirelessModule_ResetModule(void);
void WirelessModule_ResetTask(void);
u8 WirelessModule_ReadTypeNum(void);
u8 WirelessModule_ReadRunStaus(void);
char *WirelessModule_ReadIccid(void);
char * WirelessModule_ReadLatitude(void);
char * WirelessModule_ReadLongitude(void);
void WirelessModule_ScanJump(u8 runsta, u8 typenum);
u8 WirelessModule_ReadRssiSta(void);

#endif


