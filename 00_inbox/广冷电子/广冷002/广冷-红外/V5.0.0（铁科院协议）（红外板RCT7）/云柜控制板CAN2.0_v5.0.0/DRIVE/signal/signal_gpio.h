#ifndef __SIGNAL_GPIO_
#define __SIGNAL_GPIO_
#include "stm32f10x.h"
#include "sys.h"


#define SIGNAL_MAXCHN      12

#define SIG_DETECT1        PCin(6)
#define SIG_DETECT2        PCin(7)

#define ENCODER1_CH1_PB6   PBin(6)
#define ENCODER1_CH1_PB7   PBin(7)

#define SW_DETECT1         PDin(15)
#define SW_DETECT2         PDin(14)
#define SW_DETECT3         PEin(15)
#define SW_DETECT4         PEin(14)
#define SW_DETECT5         PEin(7)
#define SW_DETECT6         PBin(1)

#define LOCK_STATUS        PBin(12)
#define OPTO_SENSOR_PB8    PBin(8)




void SignalGpio_GpioInit(void);
uint8_t SignalGpio_ReadLevel1(uint8_t Signal_ch);
uint8_t SignalGpio_ReadLevel2(uint8_t Signal_ch);
uint8_t SignalGpio_ReadLevel3(uint8_t Signal_ch);
uint8_t SignalGpio_ReadLevel4(uint8_t Signal_ch);
uint8_t SiganlGpio_ReadLevel5(uint8_t Signal_ch);
uint8_t SiganlGpio_ReadLevel6(uint8_t Signal_ch);
uint32_t SignalGpio_ReadCode(void);
#endif
