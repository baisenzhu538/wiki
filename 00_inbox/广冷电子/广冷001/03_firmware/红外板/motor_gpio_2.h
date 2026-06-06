#ifndef __MOTOR_GPIO_H
#define __MOTOR_GPIO_H
#include "sys.h"

//电机控制信号引脚宏
#define MDS1    PCout(11)
#define MDS2    PAout(8)
#define MDS3    PDout(13)
#define MDS4    PDout(0)
#define MDS5    PDout(4)
#define MDS6    PDout(11)
#define MDS7    PCout(8)
#define MDS8    PBout(13)
#define MDS9    PBout(11)
#define MDS10   PEout(15)
#define MDS11   PDout(2)
#define MDS12   PDout(9)
#define MDS13   PBout(5)
//电机电源控制
#define POWER_SW PBout(7)

void MotorGpio_GpioInit(void);
uint8_t MotorGpio_ReadMls(uint8_t motornum);
uint8_t MotorGpio_ReadMps(uint8_t motornum);
void MotorGpio_ResetStar(uint8_t motornum);
void MotorGpio_SetStar(uint8_t motornum);
#endif
