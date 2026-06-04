#include "step_motor.h"



#define MOTOR_STAR_CYCLE  1500

void SetMotor_PwmInit(void)
{
 
	TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;
	GPIO_InitTypeDef GPIO_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_TIM1|RCC_APB2Periph_GPIOE
	                       |RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOD
	                       |RCC_APB2Periph_GPIOB|RCC_APB2Periph_AFIO, 
	                        ENABLE);
	GPIO_PinRemapConfig(GPIO_FullRemap_TIM1,ENABLE);
	//脉冲输出引脚 PE14 step
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_14;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOE, &GPIO_InitStructure);	
	//PC6 复位驱动芯片rst
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOC, &GPIO_InitStructure);	
	//PC7 驱动使能enable
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOC, &GPIO_InitStructure);	
	//PD15 休眠sleep
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOD, &GPIO_InitStructure);
	//PB15 方向选择 dir
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	NVIC_InitStructure.NVIC_IRQChannel = TIM1_CC_IRQn;     //捕获比较中断
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure);
  TIM_ITConfig(TIM1,TIM_IT_CC4, ENABLE );	
	TIM_ClearITPendingBit(TIM1,TIM_IT_CC4);
	

	TIM_TimeBaseStructure.TIM_Period = 20000;//90-1.25us 45-0.625us  22.5-0.3125us //设置在下一个更新事件装入活动的自动重装载寄存器周期的值	
	TIM_TimeBaseStructure.TIM_Prescaler =4; //4                  //设置用来作为TIMx时钟频率除数的预分频值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;      //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM1, &TIM_TimeBaseStructure);              //根据指定的参数初始化TIMx的时间基数单位
 
	TIM_OCInitStructure.TIM_Pulse  =2500;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM2; //选择定时器模式:TIM脉冲宽度调制模式2
 	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable; //比较输出使能
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_Low;//TIM_OCPolarity_High; //输出极性:TIM输出比较极性高
	TIM_OC4Init(TIM1, &TIM_OCInitStructure);  //根据T指定的参数初始化外设TIM3 OC2

	TIM_OC4PreloadConfig(TIM1, TIM_OCPreload_Enable);  //使能TIM3在CCR2上的预装载寄存器
	TIM_ARRPreloadConfig(TIM1, ENABLE);
	
  
	TIM_Cmd(TIM1, DISABLE);  
	TIM_CtrlPWMOutputs(TIM1, DISABLE);	
}

void StepMotor_RestDrive(void)
{
	uint32_t i=0xFFFF;
	GPIO_ResetBits(GPIOC,GPIO_Pin_6);
	while(i) i--;
	GPIO_SetBits(GPIOC,GPIO_Pin_6);
}
void StepMotor_SetSleep(void)
{
	GPIO_SetBits(GPIOD,GPIO_Pin_15);
}
void StepMotor_ResetSleep(void)
{
	GPIO_ResetBits(GPIOD,GPIO_Pin_15);
}

void StepMotor_SetDir(void)
{
	GPIO_SetBits(GPIOB,GPIO_Pin_15);
}
void StepMotor_ResetDir(void)
{
	GPIO_ResetBits(GPIOB,GPIO_Pin_15);
}

void StepMotor_SetEnable(void)
{
	GPIO_SetBits(GPIOC,GPIO_Pin_7);
}
void StepMotor_ResetEnable(void)
{
	GPIO_ResetBits(GPIOC,GPIO_Pin_7);
}

uint32_t PwmConut;
uint32_t CycleTime;
uint8_t StepMotor_Set(uint32_t angle,uint32_t time)
{
	PwmConut=angle*16;
	CycleTime=(time*1000000)/angle;
	TIM1->ARR=CycleTime;
	TIM_Cmd(TIM1,ENABLE);
  TIM_CtrlPWMOutputs(TIM1, ENABLE);		
}

void StepMotor_Init(void)
{
	SetMotor_PwmInit();
	StepMotor_ResetEnable();
	
	StepMotor_Set(1000,3);
}
void TIM1_CC_IRQHandler(void)
{
	static uint32_t i=0;
	if(TIM_GetITStatus(TIM1,TIM_IT_CC4)==SET) //溢出中断
	{
		
	 if(PwmConut>0)
	 PwmConut--;
	 if(PwmConut==0)
	 {
		TIM_Cmd(TIM1, DISABLE);  
	  TIM_CtrlPWMOutputs(TIM1, DISABLE);
	 }		 
	}
	TIM_ClearITPendingBit(TIM1,TIM_IT_CC4);  //清除中断标志位
}
