#ifndef __RGB_LED_H
#define __RGB_LED_H
#include "stm32f10x_tim.h"
#include "system_stm32f10x.h"
#include "stm32f10x_dma.h"


#define RGB_MAX_LEDNUM   (uint16_t)9

typedef struct
{
	uint8_t b;
	uint8_t r;
	uint8_t g;
	uint8_t receve;
}COLOR_TypeDef; 

void RgbLed_Init(void);
void Rgb_buffInit(void);
void Send_Rgb(uint32_t rgb);
void Set_RgbLed(COLOR_TypeDef *pcolor);
void Set_RgbLedNum(uint8_t led_num,COLOR_TypeDef *pcolor);
void RgbLed_Task(void);
#endif
