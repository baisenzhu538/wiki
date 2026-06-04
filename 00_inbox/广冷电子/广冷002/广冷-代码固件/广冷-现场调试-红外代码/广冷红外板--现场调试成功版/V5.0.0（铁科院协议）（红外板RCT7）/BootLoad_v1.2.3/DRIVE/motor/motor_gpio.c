#include "motor_gpio.h"


void MotorGpio_AllOff(void)
{
	MDS1=1;
	MDS2=1;
	MDS3=1;
	MDS4=1;
	MDS5=1;
	MDS6=1;
	MDS7=1;
	MDS8=1;
	MDS9=1;
	MDS10=1;
	MDS11=1;
	MDS12=1;
	MDS13=1;
}
void MotorGpio_GpioInit(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 	
 RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD
	                      |RCC_APB2Periph_GPIOC
	                      |RCC_APB2Periph_GPIOB
	                      |RCC_APB2Periph_GPIOE
	                      |RCC_APB2Periph_GPIOA
	                      , ENABLE);	 //使能PB,PE端口时钟	
 /*电机驱动信号引脚初始化*/
 GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
 GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11|GPIO_Pin_8;
 GPIO_Init(GPIOC, &GPIO_InitStructure);
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8;
 GPIO_Init(GPIOA, &GPIO_InitStructure);
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13|GPIO_Pin_0|GPIO_Pin_4|GPIO_Pin_11|GPIO_Pin_2|GPIO_Pin_9;
 GPIO_Init(GPIOD, &GPIO_InitStructure);
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13|GPIO_Pin_11|GPIO_Pin_5;
 GPIO_Init(GPIOB, &GPIO_InitStructure);
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_15;
 GPIO_Init(GPIOE, &GPIO_InitStructure);
 /*电机电源控制*/
 GPIO_InitStructure.GPIO_Pin = GPIO_Pin_7;
 GPIO_Init(GPIOB, &GPIO_InitStructure);
 
 MotorGpio_AllOff();//复位所有电机驱动引脚
 POWER_SW=1;        //使能电机驱动电路
}

void MotorGpio_SetStar(uint8_t motornum)
{
	 switch(motornum)
	 {
		case 0x00:MDS1=0;break;
		case 0x01:MDS2=0;break;
		case 0x02:MDS3=0;break;
		case 0x03:MDS4=0;break;
		case 0x04:MDS5=0;break;
		case 0x05:MDS6=0;break;
		case 0x06:MDS7=0;break;
		case 0x07:MDS8=0;break;
		case 0x08:MDS9=0;break;
		case 0x09:MDS10=0;break;
		case 0x0A:MDS11=0;break;
		case 0x0B:MDS12=0;break;
		case 0x0C:MDS13=0;break;
		default  :break;
	 }
}
void MotorGpio_ResetStar(uint8_t motornum)
{
	 switch(motornum)
	 {
		case 0x00:MDS1=1;break;
		case 0x01:MDS2=1;break;
		case 0x02:MDS3=1;break;
		case 0x03:MDS4=1;break;
		case 0x04:MDS5=1;break;
		case 0x05:MDS6=1;break;
		case 0x06:MDS7=1;break;
		case 0x07:MDS8=1;break;
		case 0x08:MDS9=1;break;
		case 0x09:MDS10=1;break;
		case 0x0A:MDS11=1;break;
		case 0x0B:MDS12=1;break;
		case 0x0C:MDS13=1;break;
		default  :break;
	 }
}


