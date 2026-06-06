#ifndef __ANALOG_SIGNAL_H
#define __ANALOG_SIGNAL_H
#include "stm32f10x.h"
#include "stm32f10x_adc.h"
#include "stm32f10x_dma.h"




#define ADC_CHANNEL_NUM  3
#define SAMPLE_SIZE      10 


uint16_t AnalogSignal_GetAdcValue(uint8_t adc_channel);
void AnalogSignal_Init(void);
#endif
