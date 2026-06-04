#include "misc_gpio.h"


void MiscGpio_Init(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA
							|RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOC, ENABLE);	
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;			
	GPIO_Init(GPIOC, &GPIO_InitStructure);		
	
//	GPIO_ResetBits(GPIOC,GPIO_Pin_3);	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1|GPIO_Pin_2;			
	GPIO_Init(GPIOC, &GPIO_InitStructure);			
	
//	GPIO_ResetBits(GPIOC,GPIO_Pin_15);	
	GPIO_ResetBits(GPIOC,GPIO_Pin_1);	
	GPIO_ResetBits(GPIOC,GPIO_Pin_2);	
	
	
	GPIO_ResetBits(GPIOC,GPIO_Pin_0);	
	
	GPIO_SetBits(GPIOC,GPIO_Pin_0);		
}

//照明灯
void MiscGpio_MainLight_Enable(void)
{
	GPIO_SetBits(GPIOC,GPIO_Pin_0);		
}

void MiscGpio_MainLight_Disable(void)
{
	GPIO_ResetBits(GPIOC,GPIO_Pin_0);	
}

