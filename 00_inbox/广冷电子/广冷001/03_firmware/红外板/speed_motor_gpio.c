#include "speed_motor_gpio.h"


void SpeedMotorGpio_Power_Enable(uint8_t motor_no)
{
	GPIO_SetBits(GPIOB,GPIO_Pin_7);
}

void SpeedMotorGpio_Power_Disable(uint8_t motor_no)
{
	GPIO_ResetBits(GPIOB,GPIO_Pin_7);
}

void SpeedMotorGpio_Dir_Forward(uint8_t motor_no)
{
	if(motor_no == 1)
	{
		GPIO_ResetBits(GPIOE,GPIO_Pin_0);
		GPIO_SetBits(GPIOE,GPIO_Pin_1);	
	}
	else if(motor_no == 0)
	{
		GPIO_ResetBits(GPIOE,GPIO_Pin_2);
		GPIO_SetBits(GPIOE,GPIO_Pin_3);	
	}
}

void SpeedMotorGpio_Dir_Reverse(uint8_t motor_no)
{
	if(motor_no == 1)
	{
		GPIO_SetBits(GPIOE,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_1);
	}
	else if(motor_no == 0)
	{
		GPIO_SetBits(GPIOE,GPIO_Pin_2);
		GPIO_ResetBits(GPIOE,GPIO_Pin_3);	
	}
}

void SpeedMotorGpio_Dir_Brake(uint8_t motor_no)
{
	if(motor_no == 1)
	{
		GPIO_SetBits(GPIOE,GPIO_Pin_0);
		GPIO_SetBits(GPIOE,GPIO_Pin_1);
	}
	else if(motor_no == 0)
	{
		GPIO_SetBits(GPIOE,GPIO_Pin_2);
		GPIO_SetBits(GPIOE,GPIO_Pin_3);
	}
}

void SpeedMotorGpio_Dir_Idle(uint8_t motor_no)
{
	if(motor_no == 1)
	{
		GPIO_ResetBits(GPIOE,GPIO_Pin_0);
		GPIO_ResetBits(GPIOE,GPIO_Pin_1);
	}
	else if(motor_no == 0)
	{
		GPIO_ResetBits(GPIOE,GPIO_Pin_2);
		GPIO_ResetBits(GPIOE,GPIO_Pin_3);
	}
}

void SpeedMotorGpio_Gpio_Init(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOE
							|RCC_APB2Periph_AFIO,ENABLE);	 
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
//	GPIO_PinRemapConfig(GPIO_PartialRemap_TIM3,ENABLE);
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		     //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0
								|GPIO_Pin_1
								|GPIO_Pin_2
								|GPIO_Pin_3;
	GPIO_Init(GPIOE, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 		     //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8
								|GPIO_Pin_9;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	

}

void SpeedMotorGpio_TIM_Init(void)
{
	TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	TIM_OCInitTypeDef  TIM_OCInitStructure;
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);         //时钟使能
	
	TIM_TimeBaseStructure.TIM_Period =100-1;                     //设置在下一个更新事件装入活动的自动重装载寄存器周期的值	
	TIM_TimeBaseStructure.TIM_Prescaler =720-1;                    //设置用来作为TIMx时钟频率除数的预分频值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;      //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM4, &TIM_TimeBaseStructure);              //根据指定的参数初始化TIMx的时间基数单位
	
	TIM_ARRPreloadConfig(TIM4, ENABLE);
	
	TIM_OCInitStructure.TIM_Pulse  = 0;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1; 				//选择定时器模式:TIM脉冲宽度调制模式2
 	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable; 	//比较输出使能
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High; 		//输出极性:TIM输出比较极性高

	TIM_OC3Init(TIM4,&TIM_OCInitStructure); 
	TIM_OC3PreloadConfig(TIM4, TIM_OCPreload_Enable);  				//使能TIM3在CCR2上的预装载寄存器	
	TIM_ForcedOC3Config(TIM4,TIM_ForcedAction_InActive);			//强制输出不活跃
	
	TIM_OC4Init(TIM4,&TIM_OCInitStructure); 
	TIM_OC4PreloadConfig(TIM4, TIM_OCPreload_Enable);  				//使能TIM3在CCR2上的预装载寄存器	
	TIM_ForcedOC4Config(TIM4,TIM_ForcedAction_InActive);	
	
//	TIM_CtrlPWMOutputs(TIM4, ENABLE);
	TIM_Cmd(TIM4, ENABLE);		
}

void SpeedMotorGpio_PWM_Set(u8 motor_no,u8 duty)
{
	TIM_OCInitTypeDef  TIM_OCInitStructure;

	if(motor_no > 2)
		return ;
	
	if(duty>100)
		duty=100;
	
	TIM_OCInitStructure.TIM_Pulse  = duty;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM1; 				//选择定时器模式:TIM脉冲宽度调制模式2
 	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable; 	//比较输出使能
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_High; 		//输出极性:TIM输出比较极性高
	
	if(motor_no == 1)
	{
		TIM_OC3Init(TIM4,&TIM_OCInitStructure); 
		TIM_OC3PreloadConfig(TIM4, TIM_OCPreload_Enable);  				//使能TIM3在CCR2上的预装载寄存器	
		TIM_CtrlPWMOutputs(TIM4, ENABLE);			
	}
	else if(motor_no == 0)
	{
		TIM_OC4Init(TIM4,&TIM_OCInitStructure); 
		TIM_OC4PreloadConfig(TIM4, TIM_OCPreload_Enable); 
		TIM_CtrlPWMOutputs(TIM4, ENABLE);			
	}
	
}

void SpeedMotorGpio_Hardware_Init(void)
{
	SpeedMotorGpio_Gpio_Init();
	SpeedMotorGpio_TIM_Init();
	SpeedMotorGpio_Dir_Idle(0);
	SpeedMotorGpio_Dir_Idle(1);
	SpeedMotorGpio_PWM_Set(0,0);
	SpeedMotorGpio_PWM_Set(1,0);	
	SpeedMotorGpio_Power_Disable(0);
	SpeedMotorGpio_Power_Disable(1);	
}

void SpeedMotorGpio_Init(void)
{
	SpeedMotorGpio_Hardware_Init();
}

