#ifndef __SELL_APP_H
#define __SELL_APP_H
#include "motor_drive.h"
#include "sensor.h"
#include "serial_procotol.h"

#define SELLERR_RUNNUM    1 //出货失败运行次数
#define SELLTASK_QUEULEN 20
#define SELL_DELAY        50//10ms 定时   

typedef struct 
{
  uint8_t cargo_no;
	uint8_t cargo_num;//出货次数
	uint16_t sn;
}SellTaskTypeDef;
typedef struct 
{
	SellTaskTypeDef  selltask[SELLTASK_QUEULEN];
	uint8_t  q_tail;
	uint8_t  q_head;
	uint8_t  q_len;
}SellTaskQueueTypeDef;

typedef struct
{
	SellTaskQueueTypeDef SellTask;
	uint8_t sell_flag;  //出货标志，0为未出货，1为已经出货
  uint8_t sell_state; //出货状态，0空闲，1出货中
	uint8_t sell_fail;  //出货失败标志位
	uint8_t sell_delay; //出货延时检测红外信号
  uint8_t cargo_s;    //货道状态，0空闲，1出货中，2出货完成
	uint8_t cargo_rn;   //货道出货次数
	uint8_t task_state;
}Sell_TypeDef;

void SellApp_Init(void);
void SellApp_Task(void);
void SellApp_TimeTask(void);//10ms调用一次
uint8_t SellApp_AddTask(SellTaskTypeDef *pSellTask);
uint8_t SellApp_GetSellState(void);
#endif
