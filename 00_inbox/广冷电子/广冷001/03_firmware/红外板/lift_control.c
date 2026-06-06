#include "lift_control.h"

LiftControl_MotorTestTypeDef LiftControl_MotorTest;
LiftControl_MotorTestStateTypeDef LiftControl_MotorTestState;

void LiftControl_TestTaskInit(void)
{
	LiftControl_MotorTest.test_en=0x01;
	LiftControl_MotorTestState.test_sta=0x00;
}

void LiftControl_TimeTask(void)
{
 if(LiftControl_MotorTestState.delay>0)
	 LiftControl_MotorTestState.delay--;
}
void LiftControl_TestTask(void)
{
	if((LiftControl_MotorTest.test_en==0x00)&&(LiftControl_MotorTestState.test_sta==0x00))
	  return;
	if(LiftControl_MotorTest.test_en==0x00)
	{
		LiftControl_MotorTestState.test_sta=0;
	}
	else
	{
		switch(LiftControl_MotorTestState.test_sta)
    {
			case 0x00://未启动测试
				LiftControl_MotorTestState.delay=5;//延时50ms
			  LiftControl_MotorTestState.test_sta=0x01;
				break;
			case 0x01:
				if(LiftControl_MotorTestState.delay==0)
				{
					if(LiftMotor_LiftUpLimitState())
					{
						LiftMotor_LiftMotorStar(0x00,0x00);//升降下行
						LiftControl_MotorTestState.dir=0x00;
					}
					else
					{
						LiftMotor_LiftMotorStar(0x01,0x00);//升降上行
						LiftControl_MotorTestState.dir=0x01;
					}
					LiftMotor_LiftUpLimitRT();
					LiftMotor_LiftUpLimitFT();
					LiftMotor_LiftLowLimitRT();
					LiftMotor_LiftLowLimitFT();
					LiftControl_MotorTestState.test_sta=0x02;
			  }
				break;
			case 0x02://等待电机测试启动
				if(LiftMotor_ReadLiftRunState())
				{
					LiftControl_MotorTestState.test_sta=0x03;
				}
				break;
			case 0x03://等待电机停止
				if(LiftMotor_ReadLiftRunState()==0x00)
				{
					if((LiftMotor_LiftUpLimitState()||LiftMotor_LiftUpLimitRT())&&(LiftControl_MotorTestState.dir==0x01))
					{
						LiftMotor_LiftMotorStar(0x00,0x00);//升降下行
						LiftControl_MotorTestState.dir=0x00;
						LiftControl_MotorTestState.test_sta=0x02;
					}
					else if((LiftMotor_LiftLowLimitState()||LiftMotor_LiftLowLimitRT())&&(LiftControl_MotorTestState.dir==0x00))//电机到位
					{
						LiftControl_MotorTest.test_en=0x00;
						LiftControl_MotorTestState.test_sta =0x00;
						LiftControl_MotorTestState.test_err=0x00;
					}
					else
					{
						LiftControl_MotorTest.test_en=0x00;
						LiftControl_MotorTestState.test_err=0x01;
						LiftControl_MotorTestState.test_sta=0x00;
					}
				}
				break;
		}
	}
}
