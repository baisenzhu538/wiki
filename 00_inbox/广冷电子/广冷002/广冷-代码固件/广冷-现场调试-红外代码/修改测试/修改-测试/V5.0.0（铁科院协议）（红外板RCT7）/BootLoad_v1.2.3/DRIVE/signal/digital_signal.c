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
#include "digital_signal.h"

DigitalSignal_SignalManageTypeDef SignalManage;

void DigitalSignal_SetFilterTime(uint8_t group_num,uint8_t time)
{
	uint8_t i;
	for(i=0;i<SignalManage.siggroup[group_num].sigmaxnum;i++)
	{
		SignalManage.siggroup[group_num].filtertime[i]=time;
	}
}

void DigitalSignal_Init(void)
{
	SignalGpio_GpioInit();
	SignalManage.sg_enable=0x00000001;
	SignalManage.sg_maxnum=1;
	
	
	SignalManage.siggroup[0].sigmaxnum=3;
	SignalManage.siggroup[0].readsignal=SignalGpio_ReadLevel1;
	DigitalSignal_SetFilterTime(0,2);
	
	
	SignalManage.siggroup[1].sigmaxnum=13;
	SignalManage.siggroup[1].readsignal=SignalGpio_ReadLevel2;
	DigitalSignal_SetFilterTime(1,10);
	
	
	SignalManage.siggroup[2].sigmaxnum=13;
	SignalManage.siggroup[2].readsignal=SignalGpio_ReadLevel3;
	DigitalSignal_SetFilterTime(2,10);
}


uint32_t DigitalSignal_GetSignalLevel(uint8_t group)
{
	return SignalManage.siggroup[group].sigstate;
}

uint8_t DigitalSignal_GetSignalLevelBit(uint8_t group,uint8_t sig_ch)
{
	if(SignalManage.siggroup[group].sigstate&(0x00000001<<sig_ch))
	 return 0x01;
	else
	 return 0x00;
}

uint32_t DigitalSignal_GetSignalFalling(uint8_t group)
{
	uint32_t state;
	state=SignalManage.siggroup[group].fallingstate;
  SignalManage.siggroup[group].fallingstate=0x00000000;
	return state;
}

uint32_t DigitalSignal_GetSignalRising(uint8_t group)
{
	uint32_t state;
	state=SignalManage.siggroup[group].risingstate;
  SignalManage.siggroup[group].risingstate=0x00000000;
	return state;
}

uint8_t DigitalSignal_GetSignalFallingBit(uint8_t group,uint8_t sig_ch)
{
	if(SignalManage.siggroup[group].fallingstate&0x00000001<<sig_ch)
	{
		SignalManage.siggroup[group].fallingstate&=(~(0x00000001<<sig_ch));
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t DigitalSignal_GetSignalRisingBit(uint8_t group,uint8_t sig_ch)
{
	if(SignalManage.siggroup[group].risingstate&0x00000001<<sig_ch)
	{
		SignalManage.siggroup[group].risingstate&=(~(0x00000001<<sig_ch));
		return 0x01;
	}
	else
		return 0x00;
}

uint32_t DigitalSignal_ReadCodeId(void)
{
	return SignalGpio_ReadCode();
}

void DigitalSignal_GroupCollect(DigitalSignal_SigGroupTypeDef *pSigGroup)
{
	uint8_t i;
	uint32_t Bit1=0x00000001;
	uint32_t BitNum;
	for(i=0;i<pSigGroup->sigmaxnum;i++)
	{
		BitNum=Bit1<<i;
		if((*pSigGroup->readsignal)(i))
		{
			pSigGroup->signalconnect_L[i]=0;
			if((pSigGroup->sigstate&BitNum)==0)
			{
				pSigGroup->signalconnect_H[i]++;
				if(pSigGroup->signalconnect_H[i]==pSigGroup->filtertime[i])
				{
					pSigGroup->signalconnect_H[i]=0;
					pSigGroup->sigstate|=BitNum;
					pSigGroup->risingstate|=BitNum;
				}
			}
		}
		else
		{
			pSigGroup->signalconnect_H[i]=0;
			if(pSigGroup->sigstate&BitNum)
			{
				pSigGroup->signalconnect_L[i]++;
				if(pSigGroup->signalconnect_L[i]==pSigGroup->filtertime[i])
				{
					pSigGroup->signalconnect_L[i]=0;
					pSigGroup->sigstate&=(~BitNum);
					pSigGroup->fallingstate|=BitNum;
				}
			}
		}
	}
}
void DigitalSignal_SignalCollect(void)
{
	uint8_t i;
	uint32_t Bit1=0x00000001;
	uint32_t BitNum;
	
	for(i=0;i<SignalManage.sg_maxnum;i++)
	{
		BitNum=Bit1<<i;
		if(SignalManage.sg_enable&BitNum)
		{
			DigitalSignal_GroupCollect(&SignalManage.siggroup[i]);
		}
	}
}
