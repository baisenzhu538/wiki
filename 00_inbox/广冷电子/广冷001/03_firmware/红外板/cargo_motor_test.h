#ifndef __CARGO_MOTOR_TEST_H
#define __CARGO_MOTOR_TEST_H
#include "motor_drive.h"
#include "stdio.h"
#include "sys_malloc.h"
#include "err_code.h"
typedef __packed struct 
{
	uint8_t contain_no;//货柜号
	uint8_t shelf_no;  //层架编号
  uint8_t cargo_no;  //货道编号
	uint8_t cargo_num;//出货次数
}CargoMotorTestCmdTypeDef;

typedef __packed struct 
{
	CargoMotorTestCmdTypeDef SellId;
	uint8_t       sta;
	uint8_t       err_num;
	uint32_t      err1;
}CargoMotorTaskTestCmdTypeDef;

typedef void(*pCargoMotorTest_TaskFinishCallBackTypeDef)(CargoMotorTaskTestCmdTypeDef *);

typedef struct
{
	uint8_t en;        //使能位
	uint8_t sta;       //状态位
  CargoMotorTestCmdTypeDef TestCmd;
	pCargoMotorTest_TaskFinishCallBackTypeDef pCargoMotorTest_TaskFinishCallBack;
}CargoMotorTestTypeDef;



void CargoMotor_TestTask(void);
void CargoMotor_TestSet(CargoMotorTestCmdTypeDef *pCargoMotorTestCmd,pCargoMotorTest_TaskFinishCallBackTypeDef pCallBack);
#endif
