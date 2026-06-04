#include "sensor.h"

SensorInfoTypeDef SensorInfo;
SensorGroupTypeDef SensorGroup[3];


//温度传感器参数表
const short Temp_res[91] = {
	27494,26325,25212,24153,23144,22184,21268,20396,
	19564,18771,18015,17294,16605,15948,15320,14720,
	14148,13600,13077,12577,12099,11641,11204,10785,
	10384,10000,9632,9280,8943,8620,
	8310,8012,7728,7454,7192,6940,6699,6467,6244,6030,
	5825,5628,5438,5256,5080,4912,4750,4594,4444,4300,
	4161,4027,3898,3774,3654,3539,3428,3322,3219,3119,
	3023,2931,2842,2756,2673,2593,2517,2441,2369,2299,
	2232,2167,2105,2044,1985,1929,1874,1821,1770,1720,
	1673,1626,1581,1538,1496,1455,1416,1378,1341,1305,
	1270};

	

	//传感器组信号电平获取
uint8_t Sensor_ReadSensorLeve1(uint8_t Signal_ch)
{
	if(SensorGroup[1].s&(0x00000001<<Signal_ch))
	 return 0x01;
	else
	 return 0x00;
}

//传感器组信号电平获取
uint8_t Sensor_ReadSensorLeve2(uint8_t Signal_ch)
{
	if(SensorGroup[2].s&(0x00000001<<Signal_ch))
	 return 0x01;
	else
	 return 0x00;
}


void Sensor_Init(void)
{
	AnalogSignal_Init();
	DigitalSignal_Init();
}

void Sensor_IrErrCheck(SensorTypeDef *pIr)
{
	if(pIr->s==0x01)
	{
		if(pIr->t_conunt<SENSOR_ERR_CT)
		{
			pIr->t_conunt++;
		}
		else
			pIr->err=0x01;
	}
	else
	{
		pIr->err=0x00;
		pIr->t_conunt=0;
	}
}


void Sensor_InfoColle(void)
{	
	DigitalSignal_SignalCollect();
	
	SensorInfo.goods_ir[0].s = DigitalSignal_GetSignalLevelBit(4,3);
	SensorInfo.goods_ir[0].rt|=DigitalSignal_GetSignalRisingBit(4,3);		
	SensorInfo.goods_ir[0].ft|=DigitalSignal_GetSignalFallingBit(4,3);
	
	Sensor_IrErrCheck(&SensorInfo.goods_ir[0]);
	
//	SensorInfo.motor_alm[0].s = DigitalSignal_GetSignalLevelBit(0,0);
//	SensorInfo.motor_alm[0].rt |= DigitalSignal_GetSignalRisingBit(0,0);
//	SensorInfo.motor_alm[0].ft |= DigitalSignal_GetSignalFallingBit(0,0);
//		
//	SensorInfo.motor_alm[1].s = DigitalSignal_GetSignalLevelBit(0,1);
//	SensorInfo.motor_alm[1].rt |= DigitalSignal_GetSignalRisingBit(0,1);
//	SensorInfo.motor_alm[1].ft |= DigitalSignal_GetSignalFallingBit(0,1);
//			
//	SensorInfo.motor_up[0].s = DigitalSignal_GetSignalLevelBit(3,0);
//	SensorInfo.motor_up[0].rt |= DigitalSignal_GetSignalRisingBit(3,0);
//	SensorInfo.motor_up[0].ft |= DigitalSignal_GetSignalFallingBit(3,0);
//	
//	SensorInfo.motor_down[0].s = DigitalSignal_GetSignalLevelBit(3,1);
//	SensorInfo.motor_down[0].rt |= DigitalSignal_GetSignalRisingBit(3,1);
//	SensorInfo.motor_down[0].ft |= DigitalSignal_GetSignalFallingBit(3,1);
//		
//	SensorInfo.motor_up[1].s = DigitalSignal_GetSignalLevelBit(3,3);
//	SensorInfo.motor_up[1].rt |= DigitalSignal_GetSignalRisingBit(3,3);
//	SensorInfo.motor_up[1].ft |= DigitalSignal_GetSignalFallingBit(3,3);
//	
//	SensorInfo.motor_down[1].s = DigitalSignal_GetSignalLevelBit(3,4);
//	SensorInfo.motor_down[1].rt |= DigitalSignal_GetSignalRisingBit(3,4);
//	SensorInfo.motor_down[1].ft |= DigitalSignal_GetSignalFallingBit(3,4);
	
	SensorInfo.key[0].s = DigitalSignal_GetSignalLevelBit(5,0);
	SensorInfo.key[0].rt |= DigitalSignal_GetSignalRisingBit(5,0);
	SensorInfo.key[0].ft |= DigitalSignal_GetSignalFallingBit(5,0);

	SensorInfo.key[1].s = DigitalSignal_GetSignalLevelBit(5,1);
	SensorInfo.key[1].rt |= DigitalSignal_GetSignalRisingBit(5,1);
	SensorInfo.key[1].ft |= DigitalSignal_GetSignalFallingBit(5,1);
	
	SensorInfo.key[2].s = DigitalSignal_GetSignalLevelBit(5,2);
	SensorInfo.key[2].rt |= DigitalSignal_GetSignalRisingBit(5,2);
	SensorInfo.key[2].ft |= DigitalSignal_GetSignalFallingBit(5,2);

	SensorInfo.key[3].s = DigitalSignal_GetSignalLevelBit(5,3);
	SensorInfo.key[3].rt |= DigitalSignal_GetSignalRisingBit(5,3);
	SensorInfo.key[3].ft |= DigitalSignal_GetSignalFallingBit(5,3);	
	
	SensorInfo.test_button.s = DigitalSignal_GetSignalLevelBit(3,4);
	SensorInfo.test_button.rt |= DigitalSignal_GetSignalRisingBit(3,4);
	SensorInfo.test_button.ft |= DigitalSignal_GetSignalFallingBit(3,4);		
}

uint8_t Sensor_Get_TestButtonSta(void)
{
	return SensorInfo.test_button.s;
}

uint8_t	Sensor_Get_TestButtonRt(void)
{
	if(SensorInfo.test_button.rt)
	{
		SensorInfo.test_button.rt = 0;
		return 1;
	}
	else
		return 0;
}

uint8_t	Sensor_Get_TestButtonFt(void)
{
	if(SensorInfo.test_button.ft)
	{
		SensorInfo.test_button.ft = 0;
		return 1;
	}
	else
		return 0;
}

uint8_t Sensor_Get_KeySta(uint8_t key_no)
{
	if(key_no>=4)
		return 0;
	
	return SensorInfo.key[key_no].s;
}

uint8_t Sensor_Get_KeyRt(uint8_t key_no)
{
	if(key_no>=4)
		return 0;
	
	if(SensorInfo.key[key_no].rt)
	{
		SensorInfo.key[key_no].rt = 0;
		return 1;
	}
	else
		return 0;
}

uint8_t Sensor_Get_KeyFt(uint8_t key_no)
{
	if(key_no>=4)
		return 0;
	
	if(SensorInfo.key[key_no].ft)
	{
		SensorInfo.key[key_no].ft = 0;
		return 1;
	}
	else
		return 0;	
}

//检货传感器故障获取
uint8_t Sensor_Get_GoodsIrErr(uint8_t ir_no)
{
	if(ir_no >= 2)
		return 0;
	
	return SensorInfo.goods_ir[ir_no].err;
}

//获取检货传感器状态
uint8_t Sensor_Get_GoodsSta(uint8_t ir_no)
{
	if(ir_no >= 2)
		return 0;
	
	return SensorInfo.goods_ir[ir_no].s;
}

//获取检货传感器信号边沿上升沿
uint8_t Sensor_Get_GoodsIrRT(uint8_t ir_no)
{
	if(ir_no >= 2)
		return 0;
	
	if(SensorInfo.goods_ir[ir_no].rt)
	{
		SensorInfo.goods_ir[ir_no].rt=0;
		return 0x01;
	}
	else
		return 0x00;
}

//获取检货传感器信号边沿下降沿
uint8_t Sensor_Get_GoodsIrFT(uint8_t ir_no)
{	
	if(ir_no >= 2)
		return 0;
	
	if(SensorInfo.goods_ir[ir_no].ft)
	{
		SensorInfo.goods_ir[ir_no].ft=0;
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t Sensor_Read_GoodsIrFt(uint8_t ir_no)
{
	return SensorInfo.goods_ir[ir_no].ft;
}

uint8_t Sensor_Read_GoodsIrRt(uint8_t ir_no)
{
	return SensorInfo.goods_ir[ir_no].rt;
}

uint8_t Sensor_Get_MotorAlmSta(uint8_t motor_no)
{	
	if(motor_no >= 2)
		return 0;
	return SensorInfo.motor_alm[motor_no].s;
}

uint8_t Sensor_Get_MotorAlmRt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_alm[motor_no].rt)
	{
		SensorInfo.motor_alm[motor_no].rt = 0;
		return 1;
	}
	else
		return 0;
}

uint8_t Sensor_Get_MotorAlmFt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_alm[motor_no].ft)
	{
		SensorInfo.motor_alm[motor_no].ft = 0;
		return 1;
	}
	else
		return 0;	
}

uint8_t Sensor_Get_MotorUpSta(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	return SensorInfo.motor_up[motor_no].s;
}

uint8_t Sensor_Get_MotorUpRt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_up[motor_no].rt)
	{
		SensorInfo.motor_up[motor_no].rt = 0;
		return 1;
	}
	else
		return 0;
}

uint8_t Sensor_Get_MotorUpFt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_up[motor_no].ft)
	{
		SensorInfo.motor_up[motor_no].ft = 0;
		return 1;
	}
	else
		return 0;	
}

uint8_t Sensor_Get_MotorDownSta(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	return SensorInfo.motor_down[motor_no].s;	
}	

uint8_t Sensor_Get_MotorDownRt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_down[motor_no].rt)
	{
		SensorInfo.motor_down[motor_no].rt = 0;
		return 1;
	}
	else
		return 0;		
}

uint8_t Sensor_Get_MotorDownFt(uint8_t motor_no)
{
	if(motor_no >= 2)
		return 0;
	
	if(SensorInfo.motor_down[motor_no].ft)
	{
		SensorInfo.motor_down[motor_no].ft = 0;
		return 1;
	}
	else
		return 0;		
}

float Sensor_GetMotorCurrent(void)
{
	float current;
	uint16_t advalue;
	
	advalue=AnalogSignal_GetAdcValue(0x02);
	current=((3.3/0xFFF)*advalue)*2;
	
	return current;
}

uint8_t Sensor_GetTempVaule(uint8_t sensor_on)
{
	unsigned long res;
	float res_f;
	uint16_t adc_value;
	uint8_t i;
	uint8_t temp;
	
	adc_value=AnalogSignal_GetAdcValue(sensor_on)+40;	
	res_f=(float)(adc_value*10.00)/(4096-adc_value);
	res=res_f*1000;
	
	if((res>Temp_res[0])
		||(res<Temp_res[90]))//传感器错误
		return 0xFF;
	else
	{
		for(i=0;i<90;i++)
		{
			if(((res<Temp_res[i])&&(res>Temp_res[i+1]))
				||(res==Temp_res[i])||(res==Temp_res[i+1]))
			{
				if((res-Temp_res[i+1])
					>(Temp_res[i+1]-res))
				{
					temp=i;
				}
				else
				{
					temp=i+1;
				}
			}
		}
	}
	
	return temp;
}

uint8_t Sensor_GetHumidVaule(uint8_t sensor_on)//获取湿度
{
	unsigned long res;
	float res_f;
	uint16_t adc_value;
	uint8_t i;
	uint8_t humid;
	
	adc_value=AnalogSignal_GetAdcValue(sensor_on);  //得到AD值
	res_f=(float)(adc_value*3.3)/4096;              //得到电压值
	humid=(uint8_t)(res_f/0.03);                    //湿度值=输出电压/0.03
	
	return humid;
}

uint8_t Sensor_GetTemp(void)
{
	return Sensor_GetTempVaule(0x01);//J3,制冷
}

uint8_t	Sensor_GetTemp2(void)
{
	return (Sensor_GetTempVaule(0x00)+3);//J4，常温
}

uint8_t Sensor_GetHumid(void)
{
//	return Sensor_GetHumidVaule(0x05);
	return 50;
}

uint8_t Sensor_GetHumid2(void)
{
	return 50;
}