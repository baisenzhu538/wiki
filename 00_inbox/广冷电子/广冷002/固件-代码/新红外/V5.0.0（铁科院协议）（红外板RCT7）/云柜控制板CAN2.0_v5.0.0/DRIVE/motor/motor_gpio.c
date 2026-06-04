/*
*********************************************************************************************************
* 应用平台 : STM32F103
*	模块名称 : 矩阵货道电机IO接口程序
*	文件名称 : motor_gpio.c
*	版    本 : V1.0
*	说    明 : 此文件主要实现驱动的硬件接口，其主要实现一下几个接口函数用于上层驱动调用
             1 .MotorGpio_RestAll_Y
						 2 .MotorGpio_RestAll_X
						 3 .MotorGpio_Set_X
						 4 .MotorGpio_Set_Y
						 5 .MotorGpio_GoodState_SetSignalChannal
						 6 .MotorGpio_MotorLink_SetSignalChannal
						 7 .MotorGpio_GetMotorCurrent
						 8 .MotorGpio_GetLinkSignalLevel
						 9 .MotorGpio_GetGoodsSignalLevel
						 10.MotorGpio_GetGoodsSignalLevelFalling
						 11.MotorGpio_GetGoodsSignalLevelRising
						 12.MotorGpio_GetGoodsSignalLevelLowTime
						 13.MotorGpio_GetGoodsSignalLevelHightTime
*	修改记录 :
*		版本号  日期       作者    说明
*		V1.0    2018-12-29 OUSI    
*********************************************************************************************************
*/


#include "motor_gpio.h"




void MotorGpio_RestAll_Y(void)
{
	MOTOR_Y_ALL_DISABLE;
}

void MotorGpio_RestAll_X(void)
{
	MOTOR_X_ALL_DISABLE;
}

void MotorGpio_Set_X(uint8_t ch)
{	
	MOTOR_X_ALL_DISABLE;
	
	switch(ch)
	{
		case 0:	MOTOR_X0_ENABLE;break;
		case 1:	MOTOR_X1_ENABLE;break;
		case 2:	MOTOR_X2_ENABLE;break;
		case 3:	MOTOR_X3_ENABLE;break;
		case 4:	MOTOR_X4_ENABLE;break;
		case 5:	MOTOR_X5_ENABLE;break;
		case 6:	MOTOR_X6_ENABLE;break;
		case 7:	MOTOR_X7_ENABLE;break;
		case 8:	MOTOR_X8_ENABLE;break;
		case 9:	MOTOR_X9_ENABLE;break;
		case 10:MOTOR_X10_ENABLE;break;
		case 11:MOTOR_X11_ENABLE;break;
		case 12:MOTOR_X12_ENABLE;break;
		case 13:MOTOR_X13_ENABLE;break;
		case 14:MOTOR_X14_ENABLE;break;
		case 15:MOTOR_X15_ENABLE;break;
		default:MOTOR_X_ALL_DISABLE;		
	}
}

void MotorGpio_Set_Y(uint8_t ch)
{
	MOTOR_Y_ALL_DISABLE;
	
	switch(ch)
	{
		case 0:	MOTOR_Y0_ENABLE;break;
		case 1:	MOTOR_Y1_ENABLE;break;
		case 2:	MOTOR_Y2_ENABLE;break;
		case 3:	MOTOR_Y3_ENABLE;break;
		case 4:	MOTOR_Y4_ENABLE;break;
		case 5:	MOTOR_Y5_ENABLE;break;
		case 6:	MOTOR_Y6_ENABLE;break;
		case 7:	MOTOR_Y7_ENABLE;break;
		default:MOTOR_Y_ALL_DISABLE;
	}
}

float MotorGpio_GetMotorCurrent(void)
{
	Sensor_GetMotorCurrent();
}

void MotorGpio_GpioInit(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB
						  |RCC_APB2Periph_GPIOD
						  |RCC_APB2Periph_GPIOG
						  , ENABLE);	 //使能PB,PE端口时钟	
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);

	/*电机驱动信号引脚初始化*/
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	
	//Y轴引脚初始化,74HCT4514PW
	GPIO_InitStructure.GPIO_Pin = 
								 GPIO_Pin_3
								|GPIO_Pin_4
								|GPIO_Pin_5
								|GPIO_Pin_6
								|GPIO_Pin_7;
	GPIO_Init(GPIOD, &GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
	//X轴引脚初始化,SN74HC4515DW
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9
								|GPIO_Pin_10
								|GPIO_Pin_11
								|GPIO_Pin_12
								|GPIO_Pin_10;
	GPIO_Init(GPIOG, &GPIO_InitStructure);

	MotorGpio_RestAll_Y();//关闭Y轴输出
	MotorGpio_RestAll_X();//关闭X轴输出
	
//	MotorGpio_Set_X(0);
//	MotorGpio_Set_Y(0);
////	while(1);
}


