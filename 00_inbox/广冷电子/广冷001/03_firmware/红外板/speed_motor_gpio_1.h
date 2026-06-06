#ifndef	_SPEED_MOTOR_GPIO_H_
#define	_SPEED_MOTOR_GPIO_H_

#include "sys.h"
#include "stm32f10x_tim.h"

void SpeedMotorGpio_Power_Enable(uint8_t motor_no);
void SpeedMotorGpio_Power_Disable(uint8_t motor_no);
void SpeedMotorGpio_Dir_Forward(uint8_t motor_no);
void SpeedMotorGpio_Dir_Reverse(uint8_t motor_no);
void SpeedMotorGpio_Dir_Brake(uint8_t motor_no);
void SpeedMotorGpio_Dir_Idle(uint8_t motor_no);
void SpeedMotorGpio_PWM_Set(u8 motor_no,u8 duty);
void SpeedMotorGpio_Init(void);


#endif	/*_SPEED_MOTOR_GPIO_H_*/

