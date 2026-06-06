#include "sensor.h"
SensorInfoTypeDef SensorInfo;

void Sensor_InfoColle(void)
{
	SensorInfo.body_ir.s=DigitalSignal_GetSignalLevelBit1(0);
	SensorInfo.body_ir.ft|=DigitalSignal_GetSignalFallingBit1(0);
	SensorInfo.body_ir.rt|=DigitalSignal_GetSignalRisingBit1(0);
	
	SensorInfo.door_sw.s=DigitalSignal_GetSignalLevelBit1(1);
	SensorInfo.door_sw.ft|=DigitalSignal_GetSignalFallingBit1(1);
	SensorInfo.door_sw.rt|=DigitalSignal_GetSignalRisingBit1(1);
	
	SensorInfo.goods_ir1.s=DigitalSignal_GetSignalLevelBit1(3);
	SensorInfo.goods_ir1.ft|=DigitalSignal_GetSignalFallingBit1(3);
	SensorInfo.goods_ir1.rt|=DigitalSignal_GetSignalRisingBit1(3);
	
	SensorInfo.goods_ir2.s=DigitalSignal_GetSignalLevelBit1(2);
	SensorInfo.goods_ir2.ft|=DigitalSignal_GetSignalFallingBit1(2);
	SensorInfo.goods_ir2.rt|=DigitalSignal_GetSignalRisingBit1(2);
	
	if(SensorInfo.goods_ir1.s)
	{
	 if(SensorInfo.goods_ir1.t_conunt<SENSOR_ERR_CT)
	 {
	  SensorInfo.goods_ir1.t_conunt++;
	 }
	 else
		 SensorInfo.goods_ir1.err=0x01;
	}
	else
   SensorInfo.goods_ir1.t_conunt=0;
	
	if(SensorInfo.goods_ir2.s)
	{
	 if(SensorInfo.goods_ir2.t_conunt<SENSOR_ERR_CT)
	 {
	  SensorInfo.goods_ir2.t_conunt++;
	 }
	 else
		 SensorInfo.goods_ir2.err=0x01;
	}
	else
   SensorInfo.goods_ir2.t_conunt=0;
}

uint8_t Sensor_GetGoodsIr1Err(void)
{
	return SensorInfo.goods_ir1.err;
}

uint8_t Sensor_GetGoodsIr2Err(void)
{
	return SensorInfo.goods_ir2.err;
}

uint8_t Sensor_GetGoodsIr1FT(void)
{
	if(SensorInfo.goods_ir1.ft)
	{
		SensorInfo.goods_ir1.ft=0x00;
		return 0x01;
	}
	else
		return 0x00;
}
uint8_t Sensor_GetGoodsIr2FT(void)
{
	if(SensorInfo.goods_ir2.ft)
	{
		SensorInfo.goods_ir2.ft=0;
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t Sensor_GetGoodsIr1RT(void)
{
	if(SensorInfo.goods_ir1.rt)
	{
		SensorInfo.goods_ir1.rt=0;
		return 0x01;
	}
	else
		return 0x00;
}
uint8_t Sensor_GetGoodsIr2RT(void)
{
	if(SensorInfo.goods_ir2.rt)
	{
		SensorInfo.goods_ir2.rt=0x00;
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t Sensor_GetBodyIrState(void)
{
	if(SensorInfo.body_ir.s)
		return 0x01;
	else
		return 0x00;
}
uint8_t Sensor_GetDoorSWState(void)
{
	if(SensorInfo.door_sw.s)
		return 0x01;
	else
		return 0x00;
}