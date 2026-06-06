#include "signal_gpio.h"


void SignalGpio_GpioInit(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA
							|RCC_APB2Periph_GPIOC
							|RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOD
							|RCC_APB2Periph_GPIOE
							|RCC_APB2Periph_AFIO
							, ENABLE);	 
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
	
	/*传感器电平信号采集*/
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU; 		     //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	
		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8
								|GPIO_Pin_9
								|GPIO_Pin_10
								|GPIO_Pin_11
								|GPIO_Pin_12;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6
								|GPIO_Pin_7
								|GPIO_Pin_8
								|GPIO_Pin_9;
	GPIO_Init(GPIOC, &GPIO_InitStructure);

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8
								|GPIO_Pin_9
								|GPIO_Pin_10
								|GPIO_Pin_11
								|GPIO_Pin_12
								|GPIO_Pin_13
								|GPIO_Pin_14
								|GPIO_Pin_15;
	GPIO_Init(GPIOD, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4
								|GPIO_Pin_5
								|GPIO_Pin_8
								|GPIO_Pin_9
								|GPIO_Pin_10
								|GPIO_Pin_11
								|GPIO_Pin_12
								|GPIO_Pin_13
								|GPIO_Pin_14
								|GPIO_Pin_15;
	GPIO_Init(GPIOE, &GPIO_InitStructure);

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13
								|GPIO_Pin_14
								|GPIO_Pin_15;
	GPIO_Init(GPIOB, &GPIO_InitStructure);	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4
								|GPIO_Pin_5
								|GPIO_Pin_6
								|GPIO_Pin_7;
	GPIO_Init(GPIOA, &GPIO_InitStructure);

	//传感器电源控制引脚
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		     //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	PBout(1)=1;
	 
}


uint8_t SignalGpio_ReadLevel1(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return PEin(5);//闸门电机1报警信号
		case 1:return PEin(4);//闸门电机2报警信号
		default:return 0;
	}
}

uint8_t SignalGpio_ReadLevel2(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return !PAin(12);	//MOTOR SW1
		case 1:return !PAin(11);	//MOTOR SW2
		case 2:return !PAin(10);	//MOTOR SW3
		case 3:return !PAin(9);	//MOTOR SW4
		case 4:return !PAin(8);	//MOTOR SW5
		case 5:return !PCin(9);	//MOTOR SW6
		case 6:return !PCin(8);	//MOTOR SW7
		case 7:return !PCin(7);	//MOTOR SW8
		default:return 0;
	}
}

uint8_t SignalGpio_ReadLevel3(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return !PDin(9);	//MOTOR LINK1
		case 1:return !PDin(10);	//MOTOR	LINK2
		case 2:return !PDin(11);	//MOTOR	LINK3
		case 3:return !PDin(12);	//MOTOR	LINK4
		case 4:return !PDin(13);	//MOTOR	LINK5
		case 5:return !PDin(14);	//MOTOR	LINK6
		case 6:return !PDin(15);	//MOTOR	LINK7
		case 7:return !PCin(6);	//MOTOR	LINK8
		default:return 0;
	}
}

uint8_t SignalGpio_ReadLevel4(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return PEin(14);	//SW1
		case 1:return PEin(15);	//SW2
		case 2:return PBin(13);	//SW3
		case 3:return PBin(14);	//SW4
		case 4:return PBin(15);	//SW5
		case 5:return PDin(8);	//SW6
		default:return 0;
	}
}

uint8_t SiganlGpio_ReadLevel5(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return PEin(8);	//PNP2
		case 1:return PEin(9);	//PNP1
		case 2:return PEin(10);	//PNP IR
		case 3:return PEin(11);	//NPN IR
		case 4:return PEin(12);	//NPN2
		case 5:return PEin(13);	//NPN1
		default:return 0;
	}
}

uint8_t SiganlGpio_ReadLevel6(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0:return !PAin(7);
		case 1:return !PAin(6);
		case 2:return !PAin(5);
		case 3:return !PAin(4);
		default:return 0;
	}
}

void SignalGpio_EncodeInit(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA,ENABLE);

	//拨码开关信号引脚初始化
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPD; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4
								|GPIO_Pin_5
								|GPIO_Pin_6
								|GPIO_Pin_7;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
}

//读取编码器ID
uint32_t SignalGpio_ReadCode(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;
	uint16_t i;
	uint32_t Id=0;
	
	SignalGpio_EncodeInit();
	for(i=0;i<0xFF;i++)
	{
		Id=((~GPIOA->IDR)&0x000F);
		if(!PAin(7))
			Id |= 0x1<<0;
		else
			Id &= ~(0x1<<0);
		
		if(!PAin(6))
			Id |= 0x1<<1;
		else
			Id &= ~(0x1<<1);
		
		if(!PAin(5))
			Id |= 0x1<<2;
		else
			Id &= ~(0x1<<2);
		
		if(!PAin(4))
			Id |= 0x1<<3;
		else
			Id &= ~(0x1<<3);
			
	}
	return Id;
}
