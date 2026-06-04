#include "led.h"

void LED_Init(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 	
 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA|RCC_APB2Periph_GPIOB, ENABLE);	 //使能PB,PE端口时钟
	
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15;				 //LED0-->PB.5 端口配置
 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
 GPIO_Init(GPIOA, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5;				 //LED0-->PB.5 端口配置
 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
 GPIO_Init(GPIOB, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
}

void Led_SetRead1(void)
{
	GPIOB->BSRR = GPIO_Pin_4;
}
void Led_ResetRead1(void)
{
	GPIOB->BRR = GPIO_Pin_4;
}

void Led_SetRead2(void)
{
	GPIOA->BSRR = GPIO_Pin_15;
}
void Led_ResetRead2(void)
{
	GPIOA->BRR = GPIO_Pin_15;
}

void Led_SetBlue1(void)
{
	GPIOB->BSRR = GPIO_Pin_5;
}
void Led_ResetBlue1(void)
{
	GPIOB->BRR = GPIO_Pin_5;
}

void Led_SetBlue2(void)
{
	GPIOB->BSRR = GPIO_Pin_3;
}
void Led_ResetBlue2(void)
{
	GPIOB->BRR = GPIO_Pin_3;
}
