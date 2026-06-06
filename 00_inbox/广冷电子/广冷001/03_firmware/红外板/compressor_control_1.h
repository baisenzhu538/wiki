#ifndef __COMPRESSOR_CONTROL_H
#define __COMPRESSOR_CONTROL_H
#include "stm32f10x.h"
#include "elc_lock.h"



#define RELAY1_CTL_PC3_ENABLE           	      GPIOC->BSRR = GPIO_Pin_13
#define RELAY1_CTL_PC3_DISABLE                    GPIOC->BRR = GPIO_Pin_13

#define RELAY2_CTL_PC2_ENABLE                     GPIOC->BSRR = GPIO_Pin_14
#define RELAY2_CTL_PC2_DISABLE                    GPIOC->BRR = GPIO_Pin_14

#define COMPRESSORCONTROL_FAN_ENABLE      RELAY2_CTL_PC2_ENABLE
#define COMPRESSORCONTROL_FAN_DISABLE     RELAY2_CTL_PC2_DISABLE

#define COMPRESSORCONTROL_COMP_ENABLE     RELAY1_CTL_PC3_ENABLE
#define COMPRESSORCONTROL_COMP_DISABLE    RELAY1_CTL_PC3_DISABLE

//#define COMPRESSORCONTROL_DEMISET_ENABLE  RELAY3_CTL_PB13_ENABLE
//#define COMPRESSORCONTROL_DEMISET_DISABLE RELAY3_CTL_PB13_DISABLE


void CompressorControl_init(void);
void CompressorControl_SetFan(FunctionalState NewState);
void CompressorControl_SetFwv(FunctionalState NewState);
void CompressorControl_SetComp(FunctionalState NewState);
void CompressorControl_SetSpare(FunctionalState NewState);
#endif
