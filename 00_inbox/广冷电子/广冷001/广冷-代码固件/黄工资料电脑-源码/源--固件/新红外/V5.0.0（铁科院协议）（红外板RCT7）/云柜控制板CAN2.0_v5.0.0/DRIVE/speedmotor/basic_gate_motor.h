#ifndef	_BASIC_GATE_MOTOR_H_
#define	_BASIC_GATE_MOTOR_H_

#include "speed_motor_gpio.h"
#include "sensor.h"
#include <string.h>

#define	BASIC_GATE_MOTOR_MAX_NUM	2


typedef	struct
{
	uint8_t	enable;
	uint8_t	dir;		//0 关门，1 开门；关门触发上限位，开门触发下限位
	uint8_t	speed;
	uint8_t	refresh_sn;
	uint8_t	reciver[2];
	uint16_t	outtime;
}BasicGateMotor_Drive_TypeDef;

typedef	struct
{
	uint8_t	com:1;
	uint8_t	posit:1;
	uint8_t	outtime:1;
	uint8_t	reciver:5;
}BasicGateMotor_ErrSta_TypeDef;

typedef	struct
{
	uint8_t	up_sw_sta:1;
	uint8_t	down_sw_sta:1;
	uint8_t	reciver:6;
}BasicGateMotor_Limite_TypeDef;

typedef	struct
{
	uint8_t	state;
	BasicGateMotor_ErrSta_TypeDef	errsta;
	BasicGateMotor_Limite_TypeDef	limite;
	uint8_t	reciver[5];
}BasicGateMotor_State_TypeDef;

typedef	struct
{
	uint8_t	step;
	uint16_t	runtime;
}BasicGateMotor_Step_TypeDef;

typedef	struct
{
	BasicGateMotor_Drive_TypeDef	drive;
	BasicGateMotor_State_TypeDef	state;
	BasicGateMotor_Step_TypeDef		step;
}BasicGateMotor_Manage_TypeDef;

extern BasicGateMotor_Manage_TypeDef	BasicGateMotorManage[BASIC_GATE_MOTOR_MAX_NUM];



void BasicGateMotor_Set(uint8_t motor_no,uint8_t dir,uint8_t speed,uint16_t outtime);
void BasicGateMotor_TIM_Task(void);
void BasicGateMotor_Task(void);
void BasicGateMotor_Init(void);

uint8_t BasicGateMotor_Get_Enable(uint8_t motor_no);
uint8_t BasicGateMotor_Get_State(uint8_t motor_no);
uint8_t BasicGateMotor_Get_ErrStaCom(uint8_t motor_no);
uint8_t BasicGateMotor_Get_ErrStaOuttime(uint8_t motor_no);
uint8_t BasicGateMotor_Get_ErrStaPosit(uint8_t motor_no);
uint8_t BasicGateMotor_Get_LimiteDownSwSta(uint8_t motor_no);
uint8_t BasicGateMotor_Get_LimiteUpSwSta(uint8_t motor_no);

#endif	/*_BASIC_GATE_MOTOR_H_*/

