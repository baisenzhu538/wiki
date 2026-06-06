#ifndef _TIMER_H
#define _TIMER_H
#include "stm32f10x_tim.h"
#include "stdint.h"

void TIM3_Init(u16 arr,u16 psc);
void Timer_T3CallBack(void (*p)(void));

#endif
