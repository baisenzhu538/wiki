#ifndef __LIFT_CONTROL_H
#define __LIFT_CONTROL_H
#include "stm32f10x.h"
#include "lift_motor.h"

typedef struct
{
	uint8_t enable;
	uint8_t contain_no;
	uint8_t shelf_no;
	uint8_t receve;
}LiftControl_LiftTypeDef;

typedef struct
{
	uint8_t enable;
	uint8_t contain_no;
	uint8_t shelf_no;
	uint8_t receve;
}LiftControl_TarckTypeDef;

typedef struct
{
	uint8_t state;
	uint8_t err;
	uint8_t shelf_no;
	uint8_t receve;
}LiftControl_LiftStateTypeDef;

typedef struct
{
	uint8_t state;
	uint8_t err;
	uint8_t shelf_no;
	uint8_t receve;
}LiftControl_TarckStateTypeDef;

typedef struct
{
	uint8_t  test_en;  //²âÊÔÊ¹ÄÜÎ»
	uint8_t  receve1; //²âÊÔ´íÎó
	uint16_t receve2; 
}LiftControl_MotorTestTypeDef;

typedef struct
{
	uint8_t test_sta;  //²âÊÔÊ¹ÄÜÎ»
	uint8_t test_err; //²âÊÔ´íÎó
	uint8_t delay;
  uint8_t dir;	
}LiftControl_MotorTestStateTypeDef;

void LiftControl_TimeTask(void);
void LiftControl_SetLiftStar(uint8_t contain_no,uint8_t shelf_no);
void LiftControl_TestTaskInit(void);
void LiftControl_TestTask(void);

#endif
