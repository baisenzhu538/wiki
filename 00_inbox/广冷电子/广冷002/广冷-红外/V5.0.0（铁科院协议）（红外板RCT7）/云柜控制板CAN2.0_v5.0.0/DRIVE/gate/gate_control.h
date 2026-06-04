#ifndef __GATE_CONTROL_H
#define __GATE_CONTROL_H
#include "speed_motor.h"

#define GATECONTROL_GATEOPEN  0x00
#define GATECONTROL_GATECLOSE 0x01


typedef struct
{
	uint8_t en_test;
	uint8_t test_sta;
	uint8_t test_closerr_num;
	uint8_t test_openerr_num;
	uint8_t  en; //使能端
	uint8_t  sta;//运行状态
	uint8_t  err;//错误位
	uint8_t  dir;//控制方向
	uint16_t runtime;//运行时间
	uint8_t  outtime;//超时时间
	uint8_t  doorsta;//门状态
	
}GateControlTypeDef;


void GateControl_GateDoorTestTask(void);
uint8_t GateControl_StarCloseDoor(void);
uint8_t GateControl_StarOpenDoor(void);
#endif
