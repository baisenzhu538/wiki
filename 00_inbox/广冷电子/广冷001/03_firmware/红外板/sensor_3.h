#ifndef __SENSOR_H
#define __SENSOR_H
#include "digital_signal.h"
#include "analog_signal.h"

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
	uint32_t s; //状态
	uint32_t rt;//上升沿触发
	uint32_t ft;//下降沿触发
}SensorGroupTypeDef;

typedef struct
{
	SensorTypeDef goods_ir[1];
	SensorTypeDef motor_up[2];
	SensorTypeDef motor_down[2];
	SensorTypeDef motor_alm[2];
	SensorTypeDef key[4];
	SensorTypeDef test_button;
}SensorInfoTypeDef;

extern SensorInfoTypeDef SensorInfo;

void Sensor_Init(void);

void Sensor_InfoColle(void);

uint8_t Sensor_Get_KeySta(uint8_t key_no);
uint8_t Sensor_Get_KeyRt(uint8_t key_no);
uint8_t Sensor_Get_KeyFt(uint8_t key_no);
uint8_t Sensor_Get_GoodsIrErr(uint8_t ir_no);
uint8_t Sensor_Get_GoodsSta(uint8_t ir_no);
uint8_t Sensor_Get_GoodsIrRT(uint8_t ir_no);
uint8_t Sensor_Get_GoodsIrFT(uint8_t ir_no);
uint8_t Sensor_Get_MotorAlmSta(uint8_t motor_no);
uint8_t Sensor_Get_MotorAlmRt(uint8_t motor_no);
uint8_t Sensor_Get_MotorAlmFt(uint8_t motor_no);
uint8_t Sensor_Get_MotorUpSta(uint8_t motor_no);
uint8_t Sensor_Get_MotorUpRt(uint8_t motor_no);
uint8_t Sensor_Get_MotorUpFt(uint8_t motor_no);
uint8_t Sensor_Get_MotorDownSta(uint8_t motor_no);
uint8_t Sensor_Get_MotorDownRt(uint8_t motor_no);
uint8_t Sensor_Get_MotorDownFt(uint8_t motor_no);

uint8_t Sensor_ReadSensorLeve1(uint8_t Signal_ch);
uint8_t Sensor_ReadSensorLeve2(uint8_t Signal_ch);

float Sensor_GetMotorCurrent(void);
uint8_t Sensor_GetTemp(void);
uint8_t	Sensor_GetTemp2(void);
uint8_t Sensor_GetHumid(void);
uint8_t Sensor_GetHumid2(void);

uint8_t Sensor_Get_TestButtonSta(void);
uint8_t	Sensor_Get_TestButtonRt(void);
uint8_t	Sensor_Get_TestButtonFt(void);

uint8_t Sensor_Read_GoodsIrRt(uint8_t ir_no);
uint8_t Sensor_Read_GoodsIrFt(uint8_t ir_no);


#endif
