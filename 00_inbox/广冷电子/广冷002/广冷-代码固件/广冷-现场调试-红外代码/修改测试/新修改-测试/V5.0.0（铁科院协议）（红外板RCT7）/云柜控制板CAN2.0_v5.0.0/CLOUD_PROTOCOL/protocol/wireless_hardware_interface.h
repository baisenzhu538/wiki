#ifndef __WIRELESS_HARDWARE_INTERFACE_H
#define __WIRELESS_HARDWARE_INTERFACE_H
#include "usart.h"
#include "stdio.h"
#include <string.h>
#include "sys_malloc.h"




void WierlessHarware_InterfaceInit(void);
void WierlessHarware_ResetModule(void);
uint16_t WierlessHarware_GetDataLen(void);
uint8_t WierlessHarware_GetData(uint8_t *pDataBuf);
uint8_t WierlessHarware_SendData(uint8_t *pData,uint32_t len);
uint8_t WirelesModule_sendcmd(char *cmd,char *res,uint32_t timeOut);
uint8_t WierlessOuttime_SendData(uint8_t *pData,uint32_t len, uint32_t outtime);//
#endif

