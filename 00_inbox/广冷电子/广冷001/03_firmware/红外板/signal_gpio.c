#include "signal_gpio.h"



void SignalGpio_GpioInit(void)
{
//	 GPIO_InitTypeDef  GPIO_InitStructure;
//	 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD
//	                        |RCC_APB2Periph_GPIOC
//	                        |RCC_APB2Periph_GPIOB
//	                        |RCC_APB2Periph_GPIOE
//	                        |RCC_APB2Periph_GPIOA
//	                        , ENABLE);	 
	
//	 /*电机位置信号输入引脚初始化*/	
//	 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU; 		     //上拉输入
//	 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz\
//		
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6|GPIO_Pin_7|GPIO_Pin_4|GPIO_Pin_5;
//	 GPIO_Init(GPIOC, &GPIO_InitStructure);
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8|GPIO_Pin_15;
//	 GPIO_Init(GPIOD, &GPIO_InitStructure);
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12|GPIO_Pin_10|GPIO_Pin_8|GPIO_Pin_7;
//	 GPIO_Init(GPIOE, &GPIO_InitStructure);
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15|GPIO_Pin_0|GPIO_Pin_1;
//	 GPIO_Init(GPIOB, &GPIO_InitStructure);	
//	 /*电机连接信号输入引脚初始化*/
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_12|GPIO_Pin_10|GPIO_Pin_9;
//	 GPIO_Init(GPIOC, &GPIO_InitStructure);
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_14|GPIO_Pin_1|GPIO_Pin_6|GPIO_Pin_12|GPIO_Pin_3|GPIO_Pin_10;
//	 GPIO_Init(GPIOD, &GPIO_InitStructure);
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_14|GPIO_Pin_12|GPIO_Pin_10|GPIO_Pin_6;
//	 GPIO_Init(GPIOB, &GPIO_InitStructure);
//	 
//	 //传感器信号引脚初始化
//	 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2|GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5;
//	 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPD; 		 //推挽输出
//	 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
//	 GPIO_Init(GPIOE, &GPIO_InitStructure);
	
	 //拨码开关信号引脚初始化
 
}

uint8_t SignalGpio_ReadLevel1(uint8_t Signal_ch)
{
	switch(Signal_ch)
	{
		case 0x00:return PEin(2);
		case 0x01:return PEin(3);
		case 0x02:return PEin(4);
		case 0x03:return PEin(5);
		default:  return 0x00;
	}	
}

uint8_t SignalGpio_ReadLevel2(uint8_t Signal_ch)
{
 uint8_t state;
 switch(Signal_ch)
 {
	case 0x00:state=MPS1;break;
	case 0x01:state=MPS2;break;
	case 0x02:state=MPS3;break;
	case 0x03:state=MPS4;break;
	case 0x04:state=MPS5;break;
	case 0x05:state=MPS6;break;
	case 0x06:state=MPS7;break;
	case 0x07:state=MPS8;break;
	case 0x08:state=MPS9;break;
	case 0x09:state=MPS10;break;
	case 0x0A:state=MPS11;break;
	case 0x0B:state=MPS12;break;
	case 0x0C:state=MPS13;break;
	default  :state=0x00;break;
 }
 return state;
}
uint8_t SignalGpio_ReadLevel3(uint8_t Signal_ch)
{
	uint8_t state;
 switch(Signal_ch)
 {
	case 0x00:state=MLS1;break;
	case 0x01:state=MLS2;break;
	case 0x02:state=MLS3;break;
	case 0x03:state=MLS4;break;
	case 0x04:state=MLS5;break;
	case 0x05:state=MLS6;break;
	case 0x06:state=MLS7;break;
	case 0x07:state=MLS8;break;
	case 0x08:state=MLS9;break;
	case 0x09:state=MLS10;break;
	case 0x0A:state=MLS11;break;
	case 0x0B:state=MLS12;break;
	case 0x0C:state=MLS13;break;
	default  :state=0x00;break;
 }
 return state;
}

void SignalGpio_EncodeInit(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB
												|RCC_APB2Periph_GPIOA
												, ENABLE);

 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPD; 		 
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2;
 GPIO_Init(GPIOB, &GPIO_InitStructure);
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3|GPIO_Pin_4|GPIO_Pin_5|GPIO_Pin_6|GPIO_Pin_7;
 GPIO_Init(GPIOA, &GPIO_InitStructure);	
}
//读取编码器ID
uint32_t SignalGpio_ReadCode(void)
{
	uint16_t i,j;
	uint32_t Id=0,idbuf;
	SignalGpio_EncodeInit();
	for(i=0;i<0xFF;i++)
  {
	  idbuf=0;
		idbuf|=((~GPIOB->IDR)&0x0007);
		for(j=0;j<3;j++)
		{
			if(idbuf&(0x04>>j))
				Id|=0x01<<j;
			else
				Id&=~(0x01<<j);
		}
		idbuf=0;
    idbuf|=((~GPIOA->IDR)&0x00F8)>>3;
		for(j=0;j<5;j++)
		{
			if(idbuf&(0x10>>j))
				Id|=0x01<<(j+3);
			else
				Id&=~(0x01<<(j+3));
		}
	}
	return Id;
}
