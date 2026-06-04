/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 升降平台电机驱动模块
*	文件名称 : lift_motor.c
*	版    本 : V1.0
*	说    明 : 1.实现电机的控制与电机位置信号采集
*
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-12-14  欧阳
    V1.0    2017-12-17  欧阳
*
*********************************************************************************************************
*/	

#include "lift_motor.h"
LiftMotor_TestTypeDef      LiftMotor_Test={0x00,0x01,0x00};
LiftMotor_TestStateTypeDef LiftMotor_TestState;

LiftMotor_StateTypeDef     LiftMotor_State;
LiftMotor_DriveTypeDef     LiftMotor_Drive;

LiftMotor_ControlTypeDef LiftMotor_Lift;

void LiftMotor_DriveInit(void)
{
	Encoder_Init();  //编码器初始化
  LiftDrive_Init();//升降驱动IO初始化
}
//升降平台运行使能
uint8_t LiftMotor_LiftMotorStar(uint8_t dir,uint16_t set_speed)
{
	if(LiftMotor_Lift.state.sta)
		return 0x00;//电机运行中
//	LiftMotor_Lift.drive.enable   =0x01;
//	LiftMotor_Lift.drive.set_dir  =dir;       //设置方向
//	LiftMotor_Lift.drive.set_speed=set_speed; //设置速度
}
uint8_t LiftMotor_LiftMotorStor(void)
{
	LiftMotor_Lift.drive.enable=0x00;
}

uint8_t LiftMotor_ReadLiftRunState(void)
{
	return LiftMotor_Lift.state.sta;
}
uint8_t LiftMotor_LiftUpLimitState(void)
{
	return LiftMotor_Lift.uplimit.state;
}
uint8_t  LiftMotor_LiftUpLimitRT(void)
{
	if(LiftMotor_Lift.uplimit.rt)
	{
		LiftMotor_Lift.uplimit.rt=0x00;
		return 0x01;
	}
	else
		return 0x00;
}
uint8_t LiftMotor_LiftUpLimitFT(void)
{
	if(LiftMotor_Lift.uplimit.ft)
	{
		LiftMotor_Lift.uplimit.ft=0x00;
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t LiftMotor_LiftLowLimitState(void)
{
	return LiftMotor_Lift.lowlimit.state;
}
uint8_t  LiftMotor_LiftLowLimitRT(void)
{
	if(LiftMotor_Lift.lowlimit.rt)
	{
		LiftMotor_Lift.lowlimit.rt=0x00;
		return 0x01;
	}
	else
		return 0x00;
}
uint8_t LiftMotor_LiftLowLimitFT(void)
{
	if(LiftMotor_Lift.lowlimit.ft)
	{
		LiftMotor_Lift.lowlimit.ft=0x00;
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t LiftMotor_PositControl(int32_t dest_posit)
{
	int32_t src_posit;
	uint16_t stepnum;
	src_posit=Encoder_ReadPulsesNum();
	if(src_posit>dest_posit)
	{
		stepnum=(src_posit-dest_posit)/2.56;
		LifeDrive_StarMotorPositMod(stepnum,LIFTMOTER_STAR_DOWN);
	}
	else if(src_posit<dest_posit)
	{
		stepnum=(dest_posit-src_posit)/2.56;
		LifeDrive_StarMotorPositMod(stepnum,LIFTMOTER_STAR_UP);
	}
	else
		return 0xFF;
  return 0x01;
}
//实时检测电机位置上下限
void LiftMotor_CheckMotorLimit(void)
{
	LiftMotor_Lift.uplimit.state=DigitalSignal_GetSignalLevelBit(0,2);
	LiftMotor_Lift.uplimit.ft|=DigitalSignal_GetSignalFallingBit(0,2);
	LiftMotor_Lift.uplimit.rt|=DigitalSignal_GetSignalRisingBit(0,2);
	
	LiftMotor_Lift.lowlimit.state=DigitalSignal_GetSignalLevelBit(0,3);
	LiftMotor_Lift.lowlimit.ft|=DigitalSignal_GetSignalFallingBit(0,3);
	LiftMotor_Lift.lowlimit.rt|=DigitalSignal_GetSignalRisingBit(0,3);
}

void LiftMotor_MotorTest(void)
{
  if(LiftMotor_Test.en==0x00&&LiftMotor_TestState.sta==0x00)
		return;
	if(LiftMotor_Test.en==0x00)
	{
		LiftMotor_TestState.sta=0;
		LifeDrive_StopMotor();
	}
	else
	{
		switch(LiftMotor_TestState.sta)
		{
			case 0x00:
				LiftMotor_Test.rundelay=5;
			  LiftMotor_TestState.sta=0x01;
				break;
			case 0x01:
				if(LiftMotor_Test.rundelay==0x00)
				{
					if(LiftMotor_LiftUpLimitState())
					{
						LifeDrive_StarMotor(300,300,0xFFFFFFFF,LIFTMOTER_STAR_DOWN);
						LiftMotor_Test.dir=LIFTMOTER_STAR_DOWN;
						LiftMotor_TestState.sta=0x03;
					}
					else
					{
						LifeDrive_StarMotor(300,300,0xFFFFFFFF,LIFTMOTER_STAR_UP);
						LiftMotor_Test.dir=LIFTMOTER_STAR_UP;
						LiftMotor_TestState.sta=0x02;
					}
					LiftMotor_TestState.runtime=0;
					LiftMotor_LiftUpLimitRT();
					LiftMotor_LiftLowLimitRT();
			  }
				break;
			case 0x02://检测上升
				if(LiftMotor_LiftUpLimitRT())
				{
					LifeDrive_StopMotor();
					LiftMotor_Test.rundelay=50;
			    LiftMotor_TestState.sta=0x01;
				}
				else if(LiftDrive_GetMotorSta()==0x00)
				{
					if(LiftDrive_GetMotorErr())
					{
					 LiftMotor_State.err=0x02;
					 LiftMotor_TestState.err=0x02;//电机堵转
					 LiftMotor_TestState.sta=0x00;
					 LiftMotor_Test.en=0x00; 
					}
					else
					 LiftMotor_TestState.sta=0x01;
				}
				else if(LiftMotor_TestState.runtime>LIFTMOTOR_OUTTIME)
				{
					LifeDrive_StopMotor();
					LiftMotor_TestState.err=0x01;
					LiftMotor_State.err=0x01;
					LiftMotor_TestState.sta=0x00;
					LiftMotor_Test.en=0x00;
				}
				break;
			case 0x03://检测下降
				if(LiftMotor_LiftLowLimitRT())
				{
					Encoder_Reset();
					LifeDrive_StopMotor();
					LiftMotor_Test.rundelay=50;
			    LiftMotor_TestState.sta=0x04;
				}
				else if(LiftDrive_GetMotorSta()==0x00)
				{
					if(LiftDrive_GetMotorErr())
					{
					 LiftMotor_State.err=0x02;
					 LiftMotor_TestState.err=0x02;//电机堵转
					 LiftMotor_TestState.sta=0x00;
					 LiftMotor_Test.en=0x00; 
					}
					else
					 LiftMotor_TestState.sta=0x01;
				}
				else if(LiftMotor_TestState.runtime>LIFTMOTOR_OUTTIME)
				{
					LifeDrive_StopMotor();
					LiftMotor_TestState.err=0x01;//电机运行超时
					LiftMotor_State.err=0x01;
					LiftMotor_TestState.sta=0x00;
					LiftMotor_Test.en=0x00;
				}
				break;
			case 0x04:
				if(LiftMotor_Test.rundelay==0x00)
				{
					LifeDrive_StarMotor(0,0,0xFFFFFFFF,LIFTMOTER_STAR_UP);
					LiftMotor_Test.dir=LIFTMOTER_STAR_UP;
					LiftMotor_TestState.sta=0x05;
					LiftMotor_TestState.runtime=0;
					LiftMotor_LiftLowLimitFT();
				}
				break;
			case 0x05:
				if(LiftMotor_LiftLowLimitFT())
				{
					LifeDrive_StopMotor();
          LiftMotor_Test.rundelay=50;
					LiftMotor_TestState.sta=0x06;
				}
				else if(LiftDrive_GetMotorSta()==0x00)
				{
					if(LiftDrive_GetMotorErr())
					{
					 LiftMotor_State.err=0x02;
					 LiftMotor_TestState.err=0x02;//电机堵转
					 LiftMotor_TestState.sta=0x00;
					 LiftMotor_Test.en=0x00; 
					}
					else
					 LiftMotor_TestState.sta=0x06;
				}
				else if(LiftMotor_TestState.runtime>LIFTMOTOR_OUTTIME)
				{
					LifeDrive_StopMotor();
					LiftMotor_TestState.err=0x01;//电机运行超时
					LiftMotor_State.err=0x01;
					LiftMotor_TestState.sta=0x00;
					LiftMotor_Test.en=0x00;
				}
				break;
			case 0x06:
				if(LiftMotor_Test.rundelay==0)
				{
					LiftMotor_Test.en      =0x00;
					LiftMotor_TestState.sta=0x00;
				}
				break;
		}
	}
}

void LiftMotor_MotorContorlTask(void)
{
	if(LiftMotor_Drive.dri_en!=LiftMotor_State.dri_sta)
	{
		if(LiftMotor_Drive.dri_en)
		{
			LifeDrive_Enable();
			LiftMotor_State.dri_sta=0x01;
		}
		else
		{
			LifeDrive_Disable();
			LiftMotor_State.dri_sta=0x00;
		}
	}
  if(LiftMotor_Test.en)
		return;
	if(LiftMotor_Drive.enable==0x00&&LiftMotor_State.sta==0x00)
	{
		if(LiftMotor_LiftLowLimitRT())
		  Encoder_Reset();
		return;
	}
	if(LiftMotor_Drive.enable==0x00)
	{
		LiftMotor_State.sta=0x00;
		LifeDrive_StopMotor();
	}
	else
	{
		switch(LiftMotor_State.sta)
		{
		  case 0x00:
				LiftMotor_PositControl(LiftMotor_Drive.posit);
				LiftMotor_State.sta=0x01;
				break;
			case 0x01:
				if(LiftDrive_GetMotorSta()==0x00)
				{
				 if(LiftDrive_GetMotorErr())
				 {
					 LiftMotor_State.err=0x02;
				 }
				 else
					LiftMotor_State.err=0x00;
				 LiftMotor_State.sta=0x02;
				}
				if(LiftMotor_LiftUpLimitState()||LiftMotor_LiftLowLimitState())
				{
					LifeDrive_StopMotor();
					LiftMotor_State.sta=0x02;
					LiftMotor_State.err=0x03;//升降平台超过限位
				}
				LiftMotor_Test.rundelay=5;
				break;
			case 0x02:
				if(LiftMotor_Test.rundelay==0&&Encoder_ReadSpeed()==0x0000)
				{
				 LiftMotor_Drive.enable=0x00;
				 LiftMotor_State.sta=0x00;
				}
				break;
		}
	}
}

//10ms定时运行
void LiftMotor_TimeTask(void)
{
  if(LiftMotor_Test.rundelay>0)
		LiftMotor_Test.rundelay--;
	if(LiftMotor_TestState.sta)
		LiftMotor_TestState.runtime++;
	LiftMotor_State.posit=Encoder_ReadPulsesNum();
}

void LiftMotor_LiftDriveTask(void)
{
	LiftMotor_CheckMotorLimit();
	LiftMotor_MotorContorlTask();
	LiftMotor_MotorTest();
}

