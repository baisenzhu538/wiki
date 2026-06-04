#ifndef __LIFT_MOTOR_H
#define __LIFT_MOTOR_H
#include "sys.h"


#define DIR_TIME  10 //100ms,周期10ms

typedef struct
{
	uint8_t  enable;    //使能位
	uint8_t  set_dir;       //控制方向，0为顺时针，1为逆时针
	uint16_t set_speed; //电机驱动速度
}LiftMotor_DriveTypeDef;

typedef struct
{
	uint8_t  sta;   //电机运行状态
	uint8_t  dir;   //控制方向，0为顺时针，1为逆时针
	uint16_t speed; //电机运行速度
}LiftMotor_StateTypeDef;

typedef struct
{
	uint8_t  dirflag;
	uint32_t dirtime;           //切换时间
	LiftMotor_DriveTypeDef drive;
	LiftMotor_StateTypeDef state;
}LiftMotor_ControlTypeDef;
 
#define LIFTMOTOR_MOTORGPIO_ENABLE   GPIO_SetBits(GPIOA,GPIO_Pin_6)     //驱动电机
#define LIFTMOTOR_MOTORGPIO_DISABLE  GPIO_ResetBits(GPIOA,GPIO_Pin_6)   //停止电机

#define LIFTMOTOR_MOTORDIR_CW        GPIO_SetBits(GPIOC,GPIO_Pin_4)     //顺时针
#define LIFTMOTOR_MOTORDIR_CCW       GPIO_ResetBits(GPIOC,GPIO_Pin_4)   //逆时针

#define LIFTMOTOR_BRAKE_ENABLE       GPIO_SetBits(GPIOA,GPIO_Pin_7)
#define LIFTMOTOR_BRAKE_DISABLE      GPIO_ResetBits(GPIOA,GPIO_Pin_7)

extern LiftMotor_ControlTypeDef LiftMotor_Control;

void LiftMotor_GpioInit(void);
void LiftMotor_TimeTask(void);
void LiftMotor_Drive(void);
#endif
