#ifndef __CAN_DRIVE_H
#define __CAN_DRIVE_H	 
#include "stm32f10x.h"
#include "stm32f10x_can.h"

 //////////////////////////////////////////////////////////////////////////////////	 
								  
//////////////////////////////////////////////////////////////////////////////////

//CAN接收RX0中断使能
#define CAN_RX0_INT_ENABLE	1		//0,不使能;1,使能.				

#define CAN_INTERFACE1     //PA11 PA12    
//#define CAN_INTERFACE2     //PB8  PB9  
										 							 				    
u8 CAN_Mode_Init(u8 tsjw,u8 tbs2,u8 tbs1,u16 brp,u8 mode);//CAN初始化
 
u8 Can_Send_Msg(u8* msg,u8 len);						//发送数据

u8 Can_Receive_Msg(u8 *buf);							//接收数据

void Can_FilterSet(u8 MasteMacID,u8 SlaveMacID,u8 num);

void Can_NVIC_Init(void);

void Can_GPIO_Init(void);

u8 Can_GetMailBox(CAN_TypeDef* CANx);
//void Can_DriveInit(u8 SlaveMacID);
#endif
