#ifndef	_AT_EC20_H_
#define	_AT_EC20_H_


#include "NetworkModule.h"
#include "sys_malloc.h"
#include "stdio.h"
#include "string.h"
#include "sys.h"



#define	EC20_RST_CTL	PCout(12)		//复位引脚
#define	EC20_PWR_CTL	PCout(1)		//电源引脚

#define	EC20_TXTABLE_MAXLEN	10


typedef	struct
{
	u16 lenth;
	u8 data[768];
}EC20TxUintTypeDef;



typedef struct _EC20TxControlBlockTypeDef
{
	struct _EC20TxControlBlockTypeDef *proir;
	struct _EC20TxControlBlockTypeDef *next;
	EC20TxUintTypeDef TxUint;
}EC20TxControlBlockTypeDef;


typedef struct 
{
	EC20TxControlBlockTypeDef *head;
	EC20TxControlBlockTypeDef *tail;
	uint32_t table_len;                         //任务表长度
}EC20TxControlTableTypeDef;




u8 EC20_Init(void);
u8 EC20_ReadRssiSta(void);
char *EC20_ReadRssiStr(void);
char *EC20_ReadNetStr(void);
char *EC20_ReadModeStr(void);
void EC20_TaskRun(void);
char EC20_ReciveParsing(u8 * data,u16 size);
char EC20_Send_Data(u8 *data, u16 size);
u8 EC20_CheckModule(void);
char EC20_ReadAtSta(void);
char *EC20_ReadIccidStr(void);

u8 EC20Harware_PowerReset(void);
u8 EC20Harware_ResetModule(void);
void EC20Harware_ModuleInit(void);
u8 EC20_CloseTcpConnect(void);			//关闭网络连接
void EC20_SetMode(u8 mode);
u8 EC20_ConfigModule(void);
int EC20_ModuleConfig(NetworkPara_TypeDef * pNetworkPara);
void EC20NetworkParaCopy(NetworkPara_TypeDef * NetworkPara);
char * AtEC20GpsDrive_GetLatitude(void);
char * AtEC20GpsDrive_GetLongitude(void);

#endif	/*_AT_EC20_H_*/

