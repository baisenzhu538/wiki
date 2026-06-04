#ifndef __LOCK_APP_H
#define __LOCK_APP_H
#include "stm32f10x.h"
#include "elc_lock.h"

typedef struct
{
	uint8_t contain;
	uint8_t  en;
	uint8_t  sta;//0´ò¿ª£¬¹Ø±Õ
	uint8_t  err;
	uint8_t  opentime;
}ElcLockAppTypeDef;

typedef  struct
{
	uint8_t contain;
	uint8_t sta;
	uint8_t err;
	uint8_t receve;
}ElcLockStateTypeDef;

typedef __packed struct
{
 uint8_t elclock_num;
  __packed struct
	{
		uint8_t contain;
		uint8_t sta;
		uint8_t err;
		uint8_t receve;
	}State[3];
}ElcLockResportStateTypeDef;

void LockApp_ResportSta(uint8_t cmd);
void LockApp_OpenDoor(uint8_t contain);
void LockApp_TaskRun(void);
void LockApp_Init(void);
#endif

