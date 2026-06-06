#ifndef __ENCODER_H
#define __ENCODER_H
#include "stm32f10x.h"
#include "stm32f10x_tim.h"

typedef struct
{
 int16_t  Speed;
 int16_t  Speedbuf;
 int32_t  PulsesNum;
 uint8_t  time;
}EncoderTypedef;

void Encoder_Init(void);
void EncoderCollect(void);
void Encoder_Reset(void);
int32_t Encoder_ReadPulsesNum(void);
int16_t Encoder_ReadSpeed(void);

#endif
