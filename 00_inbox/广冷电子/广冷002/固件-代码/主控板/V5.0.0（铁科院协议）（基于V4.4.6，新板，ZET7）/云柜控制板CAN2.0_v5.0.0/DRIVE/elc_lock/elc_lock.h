#ifndef __ELC_LOCK_H
#define __ELC_LOCK_H
#include "stm32f10x.h"
#include "device_protocol.h"
#include "digital_signal.h"

#define ELCLOCK_OPEN_OVERTIMR 100


#define ELCLOCK_OPEN1          GPIO_SetBits(GPIOC,GPIO_Pin_15)

#define ELCLOCK_CLOSE1        GPIO_ResetBits(GPIOC,GPIO_Pin_15) 



typedef struct
{
	uint8_t  en;
	uint8_t  sta;//0´ò¿ª£¬¹Ø±Õ
	uint8_t  err;
	uint8_t  opentime;
}ElcLockDriveTypeDef;

typedef struct
{
 uint8_t state;
 uint8_t ft;
 uint8_t rt;
 uint8_t receve;
}ElcLockSignalTypeDef;

void ElcLock_GpioInit(void);
void ElcLock_TaskRun(void);
uint8_t ElcLock_ReadLockState(void);
uint8_t ElcLock_ReadEnableSta(void);
uint8_t ElcLock_ReadLockErr(void);
void ElcLock_SetEnable(void);
void ElcLock_ResetEnable(void);

#endif
