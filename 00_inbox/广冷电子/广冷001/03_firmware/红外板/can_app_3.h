#ifndef __CAN_APP_H
#define __CAN_APP_H
#include "canbus_api.h"
#include "digital_signal.h"
#include "motor_drive.h"
#include "cryogen_drive.h"
#include "sensor.h"
#include "tempcontrol.h"
#include "sellmotor.h"
#include "led.h"

//#include "lift_motor.h"
//#include "lift_posit.h"
//#include "speed_motor.h"
//#include "power_control.h"


#define NODE_DEV_TYPE                   (uint16_t)0x0137      //设备型号
#define NODE_CONTROLLER_DEVICE_VER      (uint32_t)0x03020001
#define NODE_FIRSTLEVEL_DEVICE_VER      (uint32_t)0x03020001
#define NODE_SECONDLEVEL_DEVICE_VER     (uint32_t)0x03020001


//货道控制参数
extern MotorDrive_RegisterMapTypedef  MotorDrive_RegisterMap[MOTOR_MANAGE_MAXNUN];
extern MotorDriveTypedef MotorDrive;
//压缩机控制参数
extern CryogenDriveStateTypeDef CryogenDriveState;
extern CryogenDriveInfoTypeDef  CryogenDriveInfo;
extern CryogenControlTypeDef    CryogenControl[3];
//传感器信号组控制参数
extern SensorGroupTypeDef SensorGroup[3];
//LED灯
extern LED_ControlTypeDef LED[3];
extern LED_ControlTypeDef LED_Control;

void CanApp_SysInit(void);

#endif
