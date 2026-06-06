#include "signal_scan.h"

void SignalScan(void)
{
	DigitalSignal_SignalCollect();
	Sensor_InfoColle();
}

void SignalScan_Init(void)
{
	DigitalSignal_Init();
	TIM3_Init(499,72-1);//500us∂® ±…®√Ë
	Timer_T3CallBack(SignalScan);
}



