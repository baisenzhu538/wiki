#include "signal_scan.h"

void SignalScan(void)
{
	DigitalSignal_SignalCollect();
//	Sensor_InfoColle();
}

void SignalScan_Init(void)
{
	DigitalSignal_Init();
	TIM3_Init(999,72);//1ms∂® ±…®√Ë
	Timer_T3CallBack(SignalScan);
}



