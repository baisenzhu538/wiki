#ifndef __PROTOCOL_APP_H
#define __PROTOCOL_APP_H
#include "rs232drive.h"
#include "device_protocol.h"
#include "sell_app.h"
#include "lock_app.h"
#include "tempcontrol.h"
#include "sys_sta.h"
#include "sys_config.h"
#include "cargo_motor_test.h"
#include "miscs.h"

#define DEV_TYPE  (uint16_t)0x0137       //设备型号
#define DEV_LEVEL (uint16_t)0x1000       //设备级别 0x0000 控制器 0x1000 一级终端  0x2000 二级终端
//#define DEV_VER   (uint32_t)0x00030402   //V3.4.2 /2019/01/16
//#define DEV_VER   (uint32_t)0x00030403   //V3.4.3 /2019/01/18  新增模式识别，合并二代机云小柜控制程序
#define DEV_VER   (uint32_t)0x00040102     //V3.5.0 /2019/02/21 

void ProtocolApp_Init(void);
void ProtocolApp_TimeTask(void);
void ProtocolApp_TaskRun(void);
uint8_t ProtocolApp_ReadDeviceCode(void);

#endif

