#include "encoder.h"
//#include <math.h>
EncoderTypedef Encoder;
void Encoder_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStructure;
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;
  TIM_ICInitTypeDef  TIM_ICInitStructure;
  
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM4, ENABLE);	//使能定时器3时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB|RCC_APB2Periph_AFIO, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6|GPIO_Pin_7;	//设置编码器信号输入引脚
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOB, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
	
	TIM_TimeBaseStructure.TIM_Period = 0xFFFF;                   //设置在下一个更新事件装入活动的自动重装载寄存器周期的值1s定时
	TIM_TimeBaseStructure.TIM_Prescaler =0;                      //设置用来作为TIMx时钟频率除数的预分频值 0.1ms
	TIM_TimeBaseStructure.TIM_ClockDivision = 0;                 //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM4, &TIM_TimeBaseStructure); 
	TIM_EncoderInterfaceConfig(TIM4, TIM_EncoderMode_TI12, TIM_ICPolarity_Falling, TIM_ICPolarity_Rising); //TIM_ICPolarity_Rising?????
	TIM4->CNT = 0;
	TIM_Cmd(TIM4, ENABLE); 
}


void Encoder_Reset(void)
{
	Encoder.PulsesNum=0x00;
	TIM4->CNT=0;
}

int32_t Encoder_ReadPulsesNum(void)
{
	return Encoder.PulsesNum;
}

int16_t Encoder_ReadSpeed(void)
{
	return Encoder.Speed;
}
//定时器10ms中断采集
void EncoderCollect(void)
{
	int16_t cnt;
	cnt=TIM4->CNT;
	Encoder.Speedbuf+=cnt;
	if(Encoder.time<5)
	{
		Encoder.time++;
	}
	else
	{
		if(Encoder.Speedbuf<0)
		 Encoder.Speed=0-Encoder.Speedbuf;
		else
		 Encoder.Speed=Encoder.Speedbuf;
		Encoder.Speedbuf=0;
		Encoder.time=0;
	}
	Encoder.PulsesNum+=cnt;
	TIM4->CNT=0x00;
}