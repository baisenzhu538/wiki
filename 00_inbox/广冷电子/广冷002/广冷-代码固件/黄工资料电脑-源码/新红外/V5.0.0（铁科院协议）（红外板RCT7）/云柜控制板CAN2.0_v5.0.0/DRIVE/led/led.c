#include "led.h"
LED_ControlTypeDef LED_Control;
LED_ControlTypeDef LED[3];

Beep_ControlTypeDef Beep_Control;

void LED_Init(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 	
 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC|RCC_APB2Periph_GPIOD, ENABLE);	 //使能PB,PE端口时钟
 
 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;	 //LED0-->PB.5 端口配置
 GPIO_Init(GPIOC, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1;	 //LED0-->PB.5 端口配置
 GPIO_Init(GPIOD, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
 PUSH_LED_DISABLE;

//	PUSH_LED_ENABLE;
}

void LED_SetStart(void)
{
	LED_Control.en=0x01;
}

void LED_Set(u8 dri_no)
{
	if(dri_no == 0)
	{
		LED_SetStart();
	}
	else
	{
		LED[dri_no].en = 0x01;
	}
}


void LED_RunLED(void)
{
	static uint8_t count=0;
	
	if(count<1)
	{
		GPIO_SetBits(GPIOD,GPIO_Pin_1);
		count++;
	}
	else if(count<2)
	{
		
		GPIO_ResetBits(GPIOD,GPIO_Pin_1);
		count++;
	}
	else
	{
		count=0;
	}	
}

//100ms调用一次
void LED_Drive(void)
{
	LED_RunLED();
	
	if(LED_Control.en==0x00&&LED_Control.state==0x00)
	{
		PUSH_LED_ENABLE;
		return;
	}
	if(LED_Control.en==0x00)
	{
		LED_Control.state=0x00;
		PUSH_LED_ENABLE;
	}
	else
	{
		if(LED_Control.glint_cycle<GLINT_TIME)
		 LED_Control.glint_cycle++;
		else
		{
			LED_Control.glint_cycle=0;
			if(LED_Control.state==0x00)
			{
			 PUSH_LED_DISABLE;	
			 LED_Control.state=0x01;
			}
			else
			{
				if(LED_Control.glint_num<GLINT_NUM)
				 LED_Control.glint_num++;
				else
				{
					 LED_Control.en=0;
					 LED_Control.glint_num=0;
				}
				PUSH_LED_ENABLE;
				LED_Control.state=0x00;
			}
		}
	}
}


