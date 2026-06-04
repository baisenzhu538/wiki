#ifndef	_AT_EBYTE_H_
#define	_AT_EBYTE_H_

#include "sys_malloc.h"
#include "stdio.h"
#include "string.h"
#include "sys.h"
#include "NetworkModule.h"

#define	EBYTE_NRST_CTL	PCout(12)		//¸´Î»Òý½Å

u8 AtEbyte_Init(void);
char *AtEbyte_ReadRssiStr(void);
char *AtEbyte_ReadNetStr(void);
char *AtEbyte_ReadModeStr(void);
void AtEbyte_TaskRun(void);
char AtEbyte_ReciveParsing(u8 * data, u16 size);
char AtEbyte_SendData(u8* data,u16 size);
u8 AtEbyte_CheckModule(void);
char AtEbyte_ReadAtSta(void);
char *AtEbyte_ReadIccidStr(void);

void AtEbyte_TCP_Disconnect(void);

int AtEbyte_ModuleConfig(NetworkPara_TypeDef * pNetworkPara);

void AtEbyte_Task_Enable(void);
void AtEbyte_Task_Disable(void);

char * EbyteGpsDrive_GetLatitude(void);
char * EbyteGpsDrive_GetLongitude(void);



#endif	/*_AT_EBYTE_H_*/

