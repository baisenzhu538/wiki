#ifndef	_ESP32_H_
#define	_ESP32_H_

#include "sys.h"
#include "sys_config.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "usart.h"
#include "wireless_hardware_interface.h"
#include "mqtt_recive.h"
#include "format.h"

#define	ESP32_RST_CTL	while(0)		//复位引脚
#define	ESP32_PWR_CTL	PCout(1)		//电源引脚

#define	ESP32_TXTABLE_MAXLEN	10

typedef	struct
{
	u16 lenth;
	u8 data[768];
}ESP32TxUintTypeDef;



typedef struct _ESP32TxControlBlockTypeDef
{
	struct _ESP32TxControlBlockTypeDef *proir;
	struct _ESP32TxControlBlockTypeDef *next;
	ESP32TxUintTypeDef TxUint;
}ESP32TxControlBlockTypeDef;


typedef struct 
{
	ESP32TxControlBlockTypeDef *head;
	ESP32TxControlBlockTypeDef *tail;
	uint32_t table_len;                         //任务表长度
}ESP32TxControlTableTypeDef;



void ESP32_TaskRun(void);
u8 ESP32_ConfigModule(void);
u8 ESP32_CheckModule(void);
char ESP32_ReciveParsing(u8 * data,u16 size);
char ESP32_Send_Data(u8 *data, u16 size);
u8 ESP32_Init(void);
char ESP32_ReadAtSta(void);
u8 ESP32Harware_ReadRssiSta(void);
void Itest(void);


#endif	/*_ESP32_H_*/

