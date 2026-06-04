#ifndef __SENSOR_H
#define __SENSOR_H
#include "digital_signal.h"

#define SENSOR_ERR_CT  1000//传感器错误计时周期
typedef struct
{
	uint8_t s; //状态
	uint8_t rt;//上升沿触发
	uint8_t ft;//下降沿触发
	uint8_t err;//传感器故障
	uint32_t t_conunt;
}SensorTypeDef;

typedef struct
{
  SensorTypeDef goods_ir1;
	SensorTypeDef goods_ir2;
	SensorTypeDef body_ir;
	SensorTypeDef door_sw;
}SensorInfoTypeDef;

void Sensor_InfoColle(void);

uint8_t Sensor_GetGoodsIr1FT(void);
uint8_t Sensor_GetGoodsIr2FT(void);
uint8_t Sensor_GetGoodsIr1RT(void);
uint8_t Sensor_GetGoodsIr2RT(void);
uint8_t Sensor_GetGoodsIr1Err(void);
uint8_t Sensor_GetGoodsIr2Err(void);
uint8_t Sensor_GetBodyIrState(void);
uint8_t Sensor_GetDoorSWState(void);
#endif
