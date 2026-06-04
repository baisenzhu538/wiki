#ifndef __AT_7S4_H
#define __AT_7S4_H
#include "sys_malloc.h"
#include "stdio.h"
#include "string.h"
#include "NetworkModule.h"

#define	AT7S4_NRST_CTL	PCout(12)		//¸´Î»Òý½Å

u8 At7S4_Init(void);
char *At7S4_ReadRssiStr(void);
char *At7S4_ReadNetStr(void);
char *At7S4_ReadIccidStr(void);
void At7S4_TaskRun(void);
char At7S4_ReciveParsing(u8 * data,u16 size);
char At7S4_SendData(u8* data,u16 size);
u8 At7s4_CheckModule(void);
char At7S4_ReadAtSta(void);
int At7S4_ModuleConfig(NetworkPara_TypeDef * pNetworkPara);

char * At7S4GpsDrive_GetLatitude(void);
char * At7S4GpsDrive_GetLongitude(void);

void At7S4_Task_Disable(void);
void At7S4_Task_Enable(void);

#endif
 

