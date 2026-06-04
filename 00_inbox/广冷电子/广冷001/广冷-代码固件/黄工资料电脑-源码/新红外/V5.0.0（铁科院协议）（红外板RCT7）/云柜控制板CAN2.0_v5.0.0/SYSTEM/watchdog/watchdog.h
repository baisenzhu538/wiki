#ifndef	_WATCHDOG_H_
#define	_WATCHDOG_H_

#include "stm32f10x.h"
#include "stm32f10x_iwdg.h"


void WatchDog_Init(u8 prer,u16 rlr);
void WatchDog_Drive(void);

#endif	/*_WATCHDOG_H_*/


