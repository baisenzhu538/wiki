#ifndef __LIFT_MOTOR_H
#define __LIFT_MOTOR_H
#include "lift_drive.h"
#include "encoder.h"
#include "sensor.h"

#define LIFTDIR_TIME         10 //100ms,周期10ms
#define TARCKDIR_OUTTIME     10
#define LIFTMOTOR_OUTTIME    800 
#define TARCKMOTOR_OUTTIME   500
#define LIFTSTRO_TIME        50


typedef struct
{
	uint8_t  en;//测试
	uint8_t  dir;
	uint16_t rundelay;
}LiftMotor_TestTypeDef;

typedef struct
{
	uint8_t  sta;//测试
	uint8_t  err;//错误位
	uint16_t runtime;//运行时间
}LiftMotor_TestStateTypeDef;

typedef struct
{
	uint32_t enable:4;    //使能位
	uint32_t dri_en:4;    //驱动使能
	int32_t  posit:24;
}LiftMotor_DriveTypeDef;

typedef struct
{
	uint32_t sta:4;     //电机运行状态
	uint32_t err:3;
	uint32_t dri_sta:1; //驱动状态
	int32_t  posit:24;
}LiftMotor_StateTypeDef;

typedef struct
{
	uint8_t  state;           //电机运行上限
  uint8_t  ft;
  uint8_t  rt;	
  uint8_t  receve;
}LiftMotor_LimitTypeDef;

typedef struct
{
	uint32_t dt_count;            //切换时间
	uint32_t ot_count;            //运行超时
	uint32_t bt_count;            //刹车时间
	uint32_t st_count;            //停止时间
	
	LiftMotor_DriveTypeDef drive;
	LiftMotor_StateTypeDef state;
	
  LiftMotor_LimitTypeDef uplimit;
	LiftMotor_LimitTypeDef lowlimit;
	
	void (*fSetMotor)(uint8_t);
	void (*fSetMotorDir)(uint8_t);
	void (*fSetMotorBrak)(uint8_t);
}LiftMotor_ControlTypeDef;


extern LiftMotor_ControlTypeDef LiftMotor_Lift;
extern LiftMotor_StateTypeDef LiftMotor_State;
extern LiftMotor_DriveTypeDef LiftMotor_Drive;
extern LiftMotor_TestTypeDef      LiftMotor_Test;
extern LiftMotor_TestStateTypeDef LiftMotor_TestState;

uint8_t LiftMotor_LiftUpLimitState(void);
uint8_t  LiftMotor_LiftUpLimitRT(void);
uint8_t LiftMotor_LiftUpLimitFT(void);
uint8_t LiftMotor_LiftLowLimitState(void);
uint8_t  LiftMotor_LiftLowLimitRT(void);
uint8_t LiftMotor_LiftLowLimitFT(void);
uint8_t LiftMotor_ReadLiftRunState(void);

uint8_t LiftMotor_LiftMotorStar(uint8_t dir,uint16_t set_speed);
uint8_t LiftMotor_LiftMotorStor(void);
uint8_t LiftMotor_TarckMotorStar(uint8_t dir,uint16_t set_speed);
uint8_t LiftMotor_TarckMotorStor(void);
void LiftMotor_DriveInit(void);
void LiftMotor_LiftDriveTask(void);
void LiftMotor_TimeTask(void);
#endif
