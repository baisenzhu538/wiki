#ifndef __TEMP_SENSOR_H
#define __TEMP_SENSOR_H
#include "stm32f10x.h"
#include "stm32f10x_adc.h"
#include "stm32f10x_dma.h"

#define ADC_CHANNEL_NUM  2
#define SAMPLE_SIZE      10 

void TempSensor_Init(void);
uint8_t TempSensor_GetTempVaule(uint8_t sensor_on);
#endif
