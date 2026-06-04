#include "compressor_control.h"


void CompressorControl_init(void)
{
	 GPIO_InitTypeDef  GPIO_InitStructure;
		
	 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE);	 //使能PB,PE端口时钟
		
	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6|GPIO_Pin_7|GPIO_Pin_8|GPIO_Pin_9;				 //LED0-->PB.5 端口配置
	 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
	 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	 GPIO_Init(GPIOB, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
	CompressorControl_SetFan(DISABLE);
	CompressorControl_SetFwv(DISABLE);
	CompressorControl_SetComp(DISABLE);
	CompressorControl_SetSpare(DISABLE);
}

void CompressorControl_SetFan(FunctionalState NewState)
{
	if(NewState)
	 GPIOB->BRR = GPIO_Pin_6;
	else
	 GPIOB->BSRR = GPIO_Pin_6;
}

void CompressorControl_SetFwv(FunctionalState NewState)
{
	if(NewState)
	 GPIOB->BRR = GPIO_Pin_7;
	else
	 GPIOB->BSRR = GPIO_Pin_7;
}
void CompressorControl_SetComp(FunctionalState NewState)
{
	if(NewState)
	 GPIOB->BRR = GPIO_Pin_8;
	else
	 GPIOB->BSRR = GPIO_Pin_8;
}

void CompressorControl_SetSpare(FunctionalState NewState)
{
	if(NewState)
	 GPIOB->BRR = GPIO_Pin_9;
	else
	 GPIOB->BSRR = GPIO_Pin_9;
}

