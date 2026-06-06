#ifndef __SYS_STA_H
#define __SYS_STA_H
#include "stm32f10x.h"
//#include "elc_lock.h"
#include "tempcontrol.h"
#include "sell_app.h"

#define  SYSINIT_STARTIME 20  //100ms定时
#define  SYSINIT_OUTTIME  200 //20s超时

typedef struct
{
	uint8_t contain;
	uint8_t sta;
	uint8_t err;
	uint8_t receve;
}SysState_ElcLockStaTypeDef;
	
typedef struct
{
 uint8_t  contain; //货柜号
 uint8_t  lift_sta;
 uint8_t  tarck_sta;
 uint16_t receve;
}SysState_LiftStaTypeDef;

typedef __packed struct
{
 uint8_t  contain_no;
 uint8_t  sensor_no;
 uint8_t  sta;
 uint8_t  err;
}SysState_BodyAndIrStaTypeDef;

typedef __packed struct
{
	uint8_t sensor_num;
	SysState_BodyAndIrStaTypeDef IrSta[5];
}SysState_IrStaTypeDef;


typedef __packed struct
{
	uint8_t mode_num;   //模块数
	__packed struct
	{
		uint16_t modetype;//模块类型
		uint8_t  Contain; //模块归属货柜
		uint8_t  link;    //连接状态 1连接 0断联
	}ModeSta[5];
}SysState_ModeStaTypeDef;


typedef __packed struct
{
	uint8_t Door_num;   //门数量
	__packed struct
	{
		uint8_t contain;
		uint8_t sta;
		uint8_t err;
		uint8_t receve;
	}DoorSta[3];
}SysState_DoorStaTypeDef;

typedef __packed struct
{
	uint8_t Door_num;   //门数量
	__packed struct
	{
		uint8_t contain;
		uint8_t sta;
		uint8_t err;
		uint8_t temp;
		uint8_t mode;
		uint8_t config;
	}DoorSta[3];
}SysState_TempSysTypeDef;

typedef __packed struct
{
	uint8_t lift_num;   //门数量
	__packed struct
	{
	 uint8_t  contain; //货柜号
	 uint8_t  lift_sta;
	 uint8_t  tarck_sta;
	 uint8_t  receve;
	 uint32_t lift_posit; //升降平台位置
	}liftsta[2];
}SysState_LiftSysTypeDef;


typedef __packed struct
{
 SysState_ModeStaTypeDef   SysState_ModeSta;   //系统模块连接状态
 SysState_DoorStaTypeDef   SysState_DoorSta;   //门状态
 SysState_TempSysTypeDef   SysState_TempSysSta;
 SysState_LiftSysTypeDef   SysState_LiftSysSta;
 SysState_IrStaTypeDef     SysState_IrSensor;
}SysState_DeviceStaTypeDef;




typedef struct
{
	uint8_t initset;  //设置进行初始化
	uint8_t initsta;  //初始化状态
	uint8_t inittime; //初始化运行时间
	uint8_t initerr:4;  //初始化错误标志位
	uint8_t initflag:4;//初始化标志位
}SysState_InitTypeDef;

void SysSta_Task(void);
void sysSta_SendDeviceSta(uint8_t cmd);
void sysSta_SendBodySta(uint8_t cmd);
void sysSta_SendIrSta(uint8_t cmd);
void sysSta_SendLiftSta(uint8_t cmd);
#endif
