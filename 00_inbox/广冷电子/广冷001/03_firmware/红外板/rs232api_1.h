#ifndef __RS232API_H
#define __RS232API_H
#include "stm32f10x.h"
#include "rs232drive.h"


uint8_t Rs232Api_SendData(uint8_t *Data,uint16_t size);
void Rs232Api_SetReceiveCallBackFun(void (*pFun)(uint8_t* Data,uint16_t size));
void Rs232Api_UartInit(void);
void Rs232Api_ReceiveData(uint8_t *Data,uint16_t size);
void Rs232Api_TimeTask(void);
#endif
