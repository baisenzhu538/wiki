#include "lift_motor.h"

LiftMotor_ControlTypeDef LiftMotor_Control;


void LiftMotor_GpioInit(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 	
 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC
	                      |RCC_APB2Periph_GPIOA
	                      , ENABLE);	 //使能PB,PE端口时钟	
 /*电机驱动信号引脚初始化*/
 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4;
 GPIO_Init(GPIOC, &GPIO_InitStructure);
	
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6|GPIO_Pin_7;
 GPIO_Init(GPIOA, &GPIO_InitStructure);
}

void LiftMotor_MotorSet(void)
{
	LIFTMOTOR_MOTORGPIO_ENABLE;
}
void LiftMotor_MotorReset(void)
{
	LIFTMOTOR_MOTORGPIO_DISABLE;
}

uint8_t LiftMotor_MotorStar(uint8_t dir,uint16_t set_speed)
{
	if(LiftMotor_Control.state.sta)
		return 0x00;//电机运行中
	LiftMotor_Control.drive.enable   =0x01;
	LiftMotor_Control.drive.set_dir  =dir;       //设置方向
	LiftMotor_Control.drive.set_speed=set_speed; //设置速度
}

uint8_t LiftMotor_MotorStor(void)
{
	LiftMotor_Control.drive.enable=0x00;
}

void LiftMotor_SetDir(uint8_t dir)
{
	if(dir)
	{
		LIFTMOTOR_MOTORDIR_CW;
	}
	else
	{
		LIFTMOTOR_MOTORDIR_CCW;
	}
}

//设置刹车
void LiftMotor_SetBrake(void)
{
	LIFTMOTOR_BRAKE_ENABLE;
}

void LiftMotor_ResetBrake(void)
{
	LIFTMOTOR_BRAKE_DISABLE;
}






//10ms定时运行
void LiftMotor_TimeTask(void)
{
	if(LiftMotor_Control.dirtime>0)
	 LiftMotor_Control.dirtime--;
}

void LiftMotor_Drive(void)
{
	if((LiftMotor_Control.drive.enable==0x00)&&(LiftMotor_Control.state.sta==0x00))
		return;
  if(LiftMotor_Control.drive.enable==0x00)
	{
		LiftMotor_MotorReset();
		LiftMotor_ResetBrake();
		LiftMotor_Control.state.sta=0x00;
	}
	else
	{
		switch(LiftMotor_Control.state.sta)
		{
			case 0x00://电机未启动
				LiftMotor_Control.state.sta=0x01;
				LiftMotor_Control.dirtime=DIR_TIME;
				LiftMotor_SetDir(LiftMotor_Control.drive.set_dir);
				LiftMotor_Control.state.dir=LiftMotor_Control.drive.set_dir;
				LiftMotor_SetBrake();
				break;
			case 0x01://电机启动中
				if(LiftMotor_Control.dirtime==0)//电机启动
				{
					LiftMotor_MotorSet();
					LiftMotor_Control.state.sta=0x02;
				}
				break;
			case 0x02://电机运行中
				if(LiftMotor_Control.drive.set_dir!=LiftMotor_Control.state.dir)
				{
					LiftMotor_Control.dirtime=DIR_TIME;
					LiftMotor_MotorReset();
					LiftMotor_Control.state.sta=0x03;
				}
				break;
			case 0x03://换向停止
				if(LiftMotor_Control.dirtime==0)
				{
					LiftMotor_Control.state.sta=0x00;
				}
				break;
		}
	}	
}



