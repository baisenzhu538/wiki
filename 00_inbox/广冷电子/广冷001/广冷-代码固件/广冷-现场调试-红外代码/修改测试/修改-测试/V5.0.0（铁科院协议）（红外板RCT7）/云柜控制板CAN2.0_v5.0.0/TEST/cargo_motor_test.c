#include "cargo_motor_test.h"

CargoMotorTestTypeDef CargoMotorTest={0,0,0,0,NULL};


void CargoMotor_Init(void)
{
	
}

void CargoMotor_TestSet(CargoMotorTestCmdTypeDef *pCargoMotorTestCmd,pCargoMotorTest_TaskFinishCallBackTypeDef pCallBack)
{
	CargoMotorTest.en=0x01;
	SysMem_copy((uint8_t*)&CargoMotorTest.TestCmd,(uint8_t*)pCargoMotorTestCmd,sizeof(CargoMotorTestCmdTypeDef));
	CargoMotorTest.pCargoMotorTest_TaskFinishCallBack=pCallBack;
}
void CargoMotor_TestTask(void)
{
	CargoMotorTaskTestCmdTypeDef TaskTestCmd;
	if(CargoMotorTest.en==0x00&&CargoMotorTest.sta==0x00)
		return;
	if(CargoMotorTest.en==0x00)
	{
		CargoMotorTest.sta=0x00;
	}
	else
	{
		switch(CargoMotorTest.sta)
		{
			case 0x00:
				SysMem_copy((uint8_t*)&TaskTestCmd.SellId,(uint8_t*)&CargoMotorTest.TestCmd,sizeof(CargoMotorTestCmdTypeDef));
			  if(MotorDrive_GetLinkStateBit(TaskTestCmd.SellId.cargo_no,TaskTestCmd.SellId.shelf_no))
				{
					TaskTestCmd.sta=0x00;
					TaskTestCmd.err_num=0x01;
					TaskTestCmd.err1   =CARGO_MOTOR_LINKERR;
					CargoMotorTest.sta=0x02;
				}
				else if(MotorDrive_SetBit(TaskTestCmd.SellId.cargo_no,TaskTestCmd.SellId.shelf_no))
					CargoMotorTest.sta=0x01;
				break;
			case 0x01:
				if(MotorDrive_GetRunState()==0x00)
				{
					CargoMotorTest.sta=0x02;
					TaskTestCmd.sta=0x01;
					TaskTestCmd.err_num=0x01;
					TaskTestCmd.err1   =CARGO_MOTOR_NORMAL;
					if(MotorDrive_GetRunErrState()==0x01)//电机超时
					{
						TaskTestCmd.sta=0x00;
						TaskTestCmd.err1=CARGO_MOTOR_OUTIME;
					}
					else//电机堵转
					{
						TaskTestCmd.sta=0x00;
						TaskTestCmd.err1=CARGO_MOTOR_BLOCK;
					}
						
				}
				break;
			case 0x02:
				if(CargoMotorTest.pCargoMotorTest_TaskFinishCallBack)
					(*CargoMotorTest.pCargoMotorTest_TaskFinishCallBack)(&TaskTestCmd);
				CargoMotorTest.sta=0x00;
				CargoMotorTest.en =0x00;
				CargoMotorTest.pCargoMotorTest_TaskFinishCallBack=NULL;
				break;
		}
	}
}





