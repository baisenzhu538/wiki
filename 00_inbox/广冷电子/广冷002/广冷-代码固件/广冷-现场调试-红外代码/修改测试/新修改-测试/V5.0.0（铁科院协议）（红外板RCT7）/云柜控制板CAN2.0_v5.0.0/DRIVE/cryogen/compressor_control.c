#include "compressor_control.h"


void CompressorControl_init(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);	 //使能PB,PE端口时钟
		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13|GPIO_Pin_14;				 //LED0-->PB.5 端口配置
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	GPIO_Init(GPIOC, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
	CompressorControl_SetFan(DISABLE);
	CompressorControl_SetFwv(DISABLE);
	CompressorControl_SetComp(DISABLE);
	CompressorControl_SetSpare(DISABLE);
	
//	CompressorControl_SetFan(ENABLE);
//	CompressorControl_SetFwv(ENABLE);
//	CompressorControl_SetComp(ENABLE);
//	CompressorControl_SetSpare(ENABLE);	
//	while(1);
}

void CompressorControl_SetFan(FunctionalState NewState)
{
	if(NewState)
	 COMPRESSORCONTROL_FAN_ENABLE;
	else
	 COMPRESSORCONTROL_FAN_DISABLE;
}

void CompressorControl_SetFwv(FunctionalState NewState)
{
//	if(NewState)
//	 GPIOB->BRR = GPIO_Pin_13;
//	else
//	 GPIOB->BSRR = GPIO_Pin_13;
}
void CompressorControl_SetComp(FunctionalState NewState)
{
//	if(ElcLock_ReadLockState())
//	{
		if(NewState)
		 COMPRESSORCONTROL_COMP_ENABLE;
		else
		 COMPRESSORCONTROL_COMP_DISABLE;
//	}
//	else
//	{
//		COMPRESSORCONTROL_COMP_DISABLE;
//	}
}

void CompressorControl_SetSpare(FunctionalState NewState)
{
//	if(NewState)
//	 GPIOD->BSRR = GPIO_Pin_7;
//	else
//	 GPIOD->BRR = GPIO_Pin_7;
}

