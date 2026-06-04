#ifndef __COMPRESSOR_CONTROL_H
#define __COMPRESSOR_CONTROL_H
#include "stm32f10x.h"


void CompressorControl_init(void);
void CompressorControl_SetFan(FunctionalState NewState);
void CompressorControl_SetFwv(FunctionalState NewState);
void CompressorControl_SetComp(FunctionalState NewState);
void CompressorControl_SetSpare(FunctionalState NewState);
#endif
