/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 升降平台电机驱动模块
*	文件名称 : lift_io_drive.c
*	版    本 : V1.0
*	说    明 : 1.实现电机IO驱动
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
#include "lift_drive.h"
//#include <math.h>
LiftDrive_MotorControlTypeDef LiftDrive_MotorControl;
uint16_t MotorControlTimeTable[((LIFTMOTOR_HIGHESTSPEED_FRE-LIFTMOTOR_LOWESTSPEED_FRE)/LIFTMOTER_UPSTEP_FRC)+1];


void LiftDrive_TableInit(void)
{
	uint16_t i,len;
	len=((LIFTMOTOR_HIGHESTSPEED_FRE-LIFTMOTOR_LOWESTSPEED_FRE)/LIFTMOTER_UPSTEP_FRC)+1;
	for(i=0;i<len;i++)
	{
		MotorControlTimeTable[i]=LIFTMOTOR_TIMER_FRE/(LIFTMOTOR_LOWESTSPEED_FRE+(i*LIFTMOTER_UPSTEP_FRC));
	}
}
void LiftDrive_GpioInit(void)
{
	 GPIO_InitTypeDef  GPIO_InitStructure;
	 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC
													|RCC_APB2Periph_GPIOA
	                        |RCC_APB2Periph_GPIOB
	                        |RCC_APB2Periph_AFIO
													, ENABLE);	 //使能PB,PE端口时钟	
	GPIO_PinRemapConfig(GPIO_PartialRemap2_TIM2,ENABLE);//TIM2引脚重映射
	 /*电机驱动信号引脚初始化*/
	 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_OD; 		 //开漏输出
	 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;
	 GPIO_Init(GPIOC, &GPIO_InitStructure);
	
	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8;
	 GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_OD; 		 //开漏输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
  LIFTMOTOR_LIFTDIR_DOWN;
	LIFTMOTOR_LIFTMOTOR_DISABLE;
	LIFTMOTOR_MOTORDRIVE_DISABLE;
}

void LiftDrive_PwmInit(void)
{
	TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM2, ENABLE);         //时钟使能
	
	//定时器TIM3初始化
	TIM_TimeBaseStructure.TIM_Period = MotorControlTimeTable[0];                     //设置在下一个更新事件装入活动的自动重装载寄存器周期的值	
	TIM_TimeBaseStructure.TIM_Prescaler =0;                       //设置用来作为TIMx时钟频率除数的预分频值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;      //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM2, &TIM_TimeBaseStructure);              //根据指定的参数初始化TIMx的时间基数单位
 
	TIM_ITConfig(TIM2,TIM_IT_Update,ENABLE );                    //使能指定的TIM3中断,允许更新中断

	//中断优先级NVIC设置
	NVIC_InitStructure.NVIC_IRQChannel = TIM2_IRQn;              //TIM3中断
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;    //先占优先级1级
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 3;           //从优先级3级
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;              //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);                              //初始化NVIC寄存器
	
	TIM_OCInitStructure.TIM_Pulse  =2500-1;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM2; //选择定时器模式:TIM脉冲宽度调制模式2
 	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable; //比较输出使能
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_Low; //输出极性:TIM输出比较极性高
	TIM_OC4Init(TIM2, &TIM_OCInitStructure);  //根据T指定的参数初始化外设TIM3 OC2

	TIM_OC4PreloadConfig(TIM2, TIM_OCPreload_Enable);  //使能TIM3在CCR2上的预装载寄存器	  	
	TIM_Cmd(TIM2, DISABLE);			 
}

void LiftDrive_TimerInit(void)
{
	TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	NVIC_InitTypeDef NVIC_InitStructure;

	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM7, ENABLE);         //时钟使能
	
	//定时器TIM3初始化
	TIM_TimeBaseStructure.TIM_Period = 50-1;                      //设置在下一个更新事件装入活动的自动重装载寄存器周期的值	
	TIM_TimeBaseStructure.TIM_Prescaler =7200-1;                    //设置用来作为TIMx时钟频率除数的预分频值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;      //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM7, &TIM_TimeBaseStructure);              //根据指定的参数初始化TIMx的时间基数单位
 
	TIM_ITConfig(TIM7,TIM_IT_Update,ENABLE );                    //使能指定的TIM3中断,允许更新中断

	//中断优先级NVIC设置
	NVIC_InitStructure.NVIC_IRQChannel = TIM7_IRQn;              //TIM3中断
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;    //先占优先级1级
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 3;           //从优先级3级
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;              //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);                              //初始化NVIC寄存器
	
	TIM_Cmd(TIM7, ENABLE);
}

void LiftDrive_Init(void)
{
	LiftDrive_TableInit();
	LiftDrive_PwmInit();
	LiftDrive_GpioInit();
	LiftDrive_TimerInit();
}

uint8_t LiftDrive_GetMotorSta(void)
{
	return LiftDrive_MotorControl.sta;
}	
uint8_t LiftDrive_GetMotorErr(void)
{
	return LiftDrive_MotorControl.err;
}	

void LifeDrive_Enable(void)
{
	LIFTMOTOR_MOTORDRIVE_ENABLE;
}

void LifeDrive_Disable(void)
{
	LIFTMOTOR_MOTORDRIVE_DISABLE;
}

void LifeDrive_StarMotor(uint16_t starspeed,uint16_t highspeed,uint32_t set_stepnum,uint8_t dir)
{
	if(dir)
		LIFTMOTOR_LIFTDIR_UP;//向上
	else
		LIFTMOTOR_LIFTDIR_DOWN;//向下
	LiftDrive_MotorControl.stepnum=0;
	LiftDrive_MotorControl.encoder_posit=0;
	LiftDrive_MotorControl.uplaststep1=0;
	LiftDrive_MotorControl.uplaststep2=0;
  LiftDrive_MotorControl.uplaststep3=0;
	LiftDrive_MotorControl.sta        =0x01;//加速
	LiftDrive_MotorControl.err        =0;
	LiftDrive_MotorControl.starspeed0 =starspeed;
	LiftDrive_MotorControl.runspeed   =starspeed;
	
	LiftDrive_MotorControl.set_stepnum=set_stepnum;
	LiftDrive_MotorControl.highspeed  =highspeed;
	
	LiftDrive_MotorControl.star_posit=Encoder_ReadPulsesNum();
	TIM_Cmd(TIM2, ENABLE);//开启定时器
}

//电机控制，位置模式
void LifeDrive_StarMotorPositMod(uint32_t set_stepnum,uint8_t dir)
{
	uint16_t highestspeed;
	if(set_stepnum<(300*4+300*1+300*1)||set_stepnum==(300*4+300*1+300*1))
	{
		if(set_stepnum<300)
		 highestspeed=0;
		else
		 highestspeed=(set_stepnum-300)/(4+1);
		LifeDrive_StarMotor(0,highestspeed,set_stepnum,dir);
	}
	else 
	{
		if(set_stepnum<((1000-300)*6+1000*1+300*1)||set_stepnum==((1000-300)*6+1000*1+300*1))
		{
			highestspeed=(set_stepnum-(300*1)+(300*6))/(6+1);
			LifeDrive_StarMotor(300,highestspeed,set_stepnum,dir);
		}
		else if(set_stepnum<((1000-300)*6+(1344-1000)*8+1344*1+300*1)||set_stepnum==((1000-300)*6+(1344-1000)*8+1344*1+300*1))
		{
			highestspeed=(set_stepnum-(300*1)-(1000-300)*6+1000*8)/(8+1);
			LifeDrive_StarMotor(300,highestspeed,set_stepnum,dir);
		}
		else
		{
			highestspeed=1344;
			LifeDrive_StarMotor(300,highestspeed,set_stepnum,dir);
		}
	}
}

void LifeDrive_StopMotor(void)
{
	TIM_Cmd(TIM2, DISABLE);//关闭定时器
	LiftDrive_MotorControl.sta=0x00;
}

//电机补偿
void LiftDrive_MotorCountervail(void)
{
	static uint8_t overtime=0;
	static uint8_t clocktime=0;
	int32_t positbuf;
	uint32_t runfre;
	uint32_t actualfre;
	if(LiftDrive_MotorControl.sta==0x00)
	{
		overtime=0;
		return;
	}
	positbuf=Encoder_ReadPulsesNum();
	if(positbuf>LiftDrive_MotorControl.star_posit)
	{
		LiftDrive_MotorControl.encoder_posit=positbuf-LiftDrive_MotorControl.star_posit;
	}
	else
	{
		LiftDrive_MotorControl.encoder_posit=LiftDrive_MotorControl.star_posit-positbuf;
	}
	LiftDrive_MotorControl.stepnum=LiftDrive_MotorControl.encoder_posit/2.56;
	
	//计算电机设置运行速度与实际运行速度的对比
	runfre=LIFTMOTOR_LOWESTSPEED_FRE+LiftDrive_MotorControl.runspeed*10;//计算运行频率
	actualfre=(Encoder_ReadSpeed()*40)/2.56;                            //计算实际运行频率
	if(actualfre<runfre)
	{
		if((runfre/actualfre)>2||actualfre==0)
		{
			if(overtime<20)
			 overtime++;
			else
			{
			 LiftDrive_MotorControl.err=0x01;
			 LifeDrive_StopMotor();
			}
		}
		else if((runfre/actualfre)==2)
		{
			if((runfre%actualfre)>0)
			{
				if(overtime<20)
				 overtime++;
				else
				{
				 LiftDrive_MotorControl.err=0x01;
				 LifeDrive_StopMotor();
				}
			}
			else
				overtime=0;
		}
		else
		{
			overtime=0;
		}	
	}
  else
   overtime=0;
}

void LiftDrive_MotorPulse(void)
{
	LiftDrive_MotorControl.stepnum++;
	if(LiftDrive_MotorControl.stepnum==LiftDrive_MotorControl.set_stepnum
		||LiftDrive_MotorControl.stepnum>LiftDrive_MotorControl.set_stepnum)
	{
		LifeDrive_StopMotor();
		LiftDrive_MotorControl.sta=0x00;
	}
	
	switch(LiftDrive_MotorControl.sta)
	{
		case 0x00:break;
		case 0x01:
			if(LiftDrive_MotorControl.runspeed<LiftDrive_MotorControl.highspeed)
			{
				if(LiftDrive_MotorControl.runspeed<LIFTMOTOR_UPSEPEED1_HIGHEST)
				{
				 LiftDrive_MotorControl.starspeed1=LiftDrive_MotorControl.starspeed0;
				 LiftDrive_MotorControl.uplaststep1++;
			   LiftDrive_MotorControl.runspeed=LiftDrive_MotorControl.starspeed1
					                               +(LiftDrive_MotorControl.uplaststep1/LIFTMOTOR_UPSEPEED1_STEP);				
				}
				else if(LiftDrive_MotorControl.runspeed<LIFTMOTOR_UPSEPEED2_HIGHEST)
				{
         LiftDrive_MotorControl.starspeed2=LiftDrive_MotorControl.starspeed0
					                                 +(LiftDrive_MotorControl.uplaststep1/LIFTMOTOR_UPSEPEED1_STEP);
				 LiftDrive_MotorControl.uplaststep2++;
				 LiftDrive_MotorControl.runspeed=LiftDrive_MotorControl.starspeed2
					                               +(LiftDrive_MotorControl.uplaststep2/LIFTMOTOR_UPSEPEED2_STEP); 
				}
				else if(LiftDrive_MotorControl.runspeed<LIFTMOTOR_UPSEPEED3_HIGHEST)
				{
				 LiftDrive_MotorControl.starspeed3=LiftDrive_MotorControl.starspeed0
					                                 +(LiftDrive_MotorControl.uplaststep1/LIFTMOTOR_UPSEPEED1_STEP)
					                                 +(LiftDrive_MotorControl.uplaststep2/LIFTMOTOR_UPSEPEED2_STEP);
				 LiftDrive_MotorControl.uplaststep3++;
				 LiftDrive_MotorControl.runspeed=LiftDrive_MotorControl.starspeed3
					                              +(LiftDrive_MotorControl.uplaststep3/LIFTMOTOR_UPSEPEED3_STEP);
				}
			}
      else
			 LiftDrive_MotorControl.sta=0x02;			 
			 TIM2->ARR=MotorControlTimeTable[LiftDrive_MotorControl.runspeed];				
			break;
		case 0x02:
			if((LiftDrive_MotorControl.set_stepnum-LiftDrive_MotorControl.stepnum)<LiftDrive_MotorControl.runspeed*1)
				LiftDrive_MotorControl.sta=0x03;
			break;
		case 0x03:
			if(LiftDrive_MotorControl.runspeed>0)
				LiftDrive_MotorControl.runspeed--;
			TIM2->ARR=MotorControlTimeTable[LiftDrive_MotorControl.runspeed];
			break;
	}
}

void TIM2_IRQHandler(void)
{
	if(TIM_GetITStatus(TIM2,TIM_IT_Update)==SET) //溢出中断
	{
   LiftDrive_MotorPulse();
	}
	TIM_ClearITPendingBit(TIM2,TIM_IT_Update);  //清除中断标志位
}

void TIM7_IRQHandler(void)
{
	if(TIM_GetITStatus(TIM7,TIM_IT_Update)==SET) //溢出中断
	{
    EncoderCollect();
		LiftDrive_MotorCountervail();
	}
	TIM_ClearITPendingBit(TIM7,TIM_IT_Update);  //清除中断标志位
}

//设置升降电机驱动IO状态
