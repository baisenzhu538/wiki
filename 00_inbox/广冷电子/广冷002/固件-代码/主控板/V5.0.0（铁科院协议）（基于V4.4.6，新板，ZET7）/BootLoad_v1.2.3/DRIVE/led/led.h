#ifndef __LED_H
#define __LED_H	 
#include "sys.h"

#define LED0 PBout(5)// PB5
#define LED1 PEout(5)// PE5	

void LED_Init(void);//≥ı ºªØ
uint8_t read_id(void);
void SetLed(uint8_t data);
uint8_t KeyRead(void);
#endif
