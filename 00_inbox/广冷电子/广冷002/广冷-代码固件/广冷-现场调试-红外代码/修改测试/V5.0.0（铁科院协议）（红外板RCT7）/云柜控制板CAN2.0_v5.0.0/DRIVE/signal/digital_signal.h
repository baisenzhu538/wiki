/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 电平信号采集模块
*	文件名称 : digital_signal.c
*	版    本 : V1.0
*	说    明 : 1.实现电平信号的采集和归类
*
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-12-13  欧阳     
*
*********************************************************************************************************
*/	

#ifndef __DIGITAL_SIGNAL_H
#define __DIGITAL_SIGNAL_H
#include "signal_gpio.h"

#define SIGNAL_MAXNUM 32
#define SIGNALGROUP_MAXNUM 6

#define SIGNALSAMP_MAXTIME         0xFFFF
#define SIGNALSAMP_MAXFILTERTIMER  0xFF
typedef struct 
{
	uint8_t  sigmaxnum;
	uint32_t sigstate;
	uint32_t risingstate;                  //由低到高分别对应0-31号信号弹起状态
	uint32_t fallingstate;                 //由低到高分别对应0-31号信号下压状态
	
	uint16_t  signalsamptime_H[SIGNAL_MAXNUM];
	uint16_t  signalsamptime_L[SIGNAL_MAXNUM];
	
	uint8_t  signalconnect_H[SIGNAL_MAXNUM];
	uint8_t  signalconnect_L[SIGNAL_MAXNUM];
	
	uint8_t   filtertime[SIGNAL_MAXNUM];
	uint8_t  (*readsignal)(uint8_t);
}DigitalSignal_SigGroupTypeDef;

typedef struct 
{
	uint32_t sg_enable;
	uint32_t sg_maxnum;
	DigitalSignal_SigGroupTypeDef siggroup[SIGNALGROUP_MAXNUM];
}DigitalSignal_SignalManageTypeDef;


extern DigitalSignal_SignalManageTypeDef SignalManage;

uint32_t DigitalSignal_GetSignalLevel(uint8_t group);
uint8_t DigitalSignal_GetSignalLevelBit(uint8_t group,uint8_t sig_ch);

uint32_t DigitalSignal_GetSignalFalling(uint8_t group);
uint8_t DigitalSignal_GetSignalFallingBit(uint8_t group,uint8_t sig_ch);

uint32_t DigitalSignal_GetSignalRising(uint8_t group);
uint8_t DigitalSignal_GetSignalRisingBit(uint8_t group,uint8_t sig_ch);


uint16_t DigitalSignal_GetHightLevelTime(uint8_t group,uint8_t sig_ch);
uint16_t DigitalSignal_GetLowLevelTime(uint8_t group,uint8_t sig_ch);

void DigitalSignal_SignalCollect(void);
void DigitalSignal_Init(void);
uint32_t DigitalSignal_ReadCodeId(void);
#endif
