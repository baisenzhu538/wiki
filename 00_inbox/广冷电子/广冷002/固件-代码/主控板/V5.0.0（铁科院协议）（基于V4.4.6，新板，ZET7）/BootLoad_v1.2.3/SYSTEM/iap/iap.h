#ifndef __IAP_H
#define __IAP_H
#include "stm32f10x.h"


//#define IAP_USER_MODE
#define IAP_BOOTLOAD_MODE

#define IAP_USER_FLASHSIZE    ((uint32_t)(100*1024))            //用户程序flash大小  

#define IAP_BOOTLOAD_SIZE     ((uint32_t)(6*1024))             //bootload所占空间,32KB

#define IAP_USER_ADDR         (FLASH_BASE+IAP_BOOTLOAD_SIZE)    //应用程序偏移地址

#define IAP_BACKUPAREA_ADDR   (IAP_USER_ADDR+IAP_USER_FLASHSIZE)//备份区域flash地址
         
#define IAP_FWCHECK_BYTENUM    16                               //固件校验码字节数


#if STM32_FLASH_SIZE<256
#define IAP_UPFLAG_ADDR ((uint32_t) (FLASH_BASE+(IAP_BOOTLOAD_SIZE-(1*1024))))
#else
#define IAP_UPFLAG_ADDR ((uint32_t) (FLASH_BASE+(IAP_BOOTLOAD_SIZE-(2*1024))))
#endif



typedef struct
{
 u16 packet_num;
 u16 packet_size;
 unsigned char buf[256];
}FirmwareBuffTypeDef;

typedef struct
{
 uint32_t FW_Size;
 uint8_t  FW_Check[IAP_FWCHECK_BYTENUM];
}FirmwareInfoTypeDef;

typedef  void (*iapfun)(void);

void Iap_SetBase(void);
void Iap_TaskRun(void);
void Iap_LoadApp(void);
void Iap_Rest_UpData(void);
uint8_t Iap_UpData_Finish(FirmwareInfoTypeDef *pFirmwareInfo);
uint8_t Iap_UpDataApp(FirmwareBuffTypeDef *pApp_Buf);
#endif

