#ifndef __SIGNAL_GPIO_
#define __SIGNAL_GPIO_
#include "stm32f10x.h"
#include "sys.h"

//电平信号引脚宏定义
#define OPENDOOR_SIGNAL   PEin(3)
#define INFRARED_SIGNAL1  PEin(5)
#define INFRARED_SIGNAL2  PEin(4)
#define HUMANBODY_SIGNAL  PEin(2)

//CodeId 引脚宏定义
#define IN1               PCin(0)
#define IN2               PCin(1)
#define IN3               PCin(2)
#define IN4               PCin(3)
#define IN5               PAin(0)
#define IN6               PAin(1)

//电机位置信号引脚宏
#define MPS1  PCin(7)
#define MPS2  PCin(6)
#define MPS3  PDin(15)
#define MPS4  PDin(8)
#define MPS5  PEin(12)
#define MPS6  PBin(15)
#define MPS7  PEin(10)
#define MPS8  PEin(8)
#define MPS9  PCin(4)
#define MPS10 PEin(7)
#define MPS11 PCin(5)
#define MPS12 PBin(0)
#define MPS13 PBin(1)
//电机连接信号引脚宏
#define MLS1   PCin(12)
#define MLS2   PCin(10)
#define MLS3   PDin(14)
#define MLS4   PDin(1)
#define MLS5   PDin(6)
#define MLS6   PDin(12)
#define MLS7   PCin(9)
#define MLS8   PBin(14)
#define MLS9   PBin(12)
#define MLS10  PBin(10)
#define MLS11  PDin(3)
#define MLS12  PDin(10)
#define MLS13  PBin(6)

void SignalGpio_GpioInit(void);
uint8_t SignalGpio_ReadLevel1(uint8_t Signal_ch);
uint8_t SignalGpio_ReadLevel2(uint8_t Signal_ch);
uint8_t SignalGpio_ReadLevel3(uint8_t Signal_ch);
uint32_t SignalGpio_ReadCode(void);
#endif
