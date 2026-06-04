#include "temp_sensor.h"

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

uint16_t ADC_ValueBuf[SAMPLE_SIZE][ADC_CHANNEL_NUM];

void TempSensor_Init(void)
{
	ADC_InitTypeDef ADC_InitStructure; 
	GPIO_InitTypeDef  GPIO_InitStructure;
	DMA_InitTypeDef DMA_InitStructure; 
	
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA |RCC_APB2Periph_ADC1,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AIN; 		   //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1|GPIO_Pin_2;
	GPIO_Init(GPIOA, &GPIO_InitStructure);
	
	ADC_DeInit(ADC1);  //复位ADC1 
	
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&ADC1->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (u32)ADC_ValueBuf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;  
	DMA_InitStructure.DMA_BufferSize =SAMPLE_SIZE*ADC_CHANNEL_NUM;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_HalfWord; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_HalfWord; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Circular;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel1,&DMA_InitStructure);  
	DMA_Cmd(DMA1_Channel1,ENABLE);
	
	ADC_InitStructure.ADC_Mode = ADC_Mode_Independent;	//ADC工作模式:ADC1和ADC2工作在独立模式
	ADC_InitStructure.ADC_ScanConvMode = ENABLE;	      //模数转换工作在扫描模式
	ADC_InitStructure.ADC_ContinuousConvMode = ENABLE;	//模数转换工作在连续转换模式
	ADC_InitStructure.ADC_ExternalTrigConv = ADC_ExternalTrigConv_None;	//转换由软件而不是外部触发启动
	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right;	//ADC数据右对齐
	ADC_InitStructure.ADC_NbrOfChannel = 2;	//顺序进行规则转换的ADC通道的数目
	ADC_Init(ADC1, &ADC_InitStructure);	//根据ADC_InitStruct中指定的参数初始化外设ADCx的寄存器   
  
	ADC_RegularChannelConfig(ADC1, ADC_Channel_1, 1,ADC_SampleTime_71Cycles5);
  ADC_RegularChannelConfig(ADC1, ADC_Channel_2, 2,ADC_SampleTime_71Cycles5);
	
	ADC_Cmd(ADC1, ENABLE);	//使能指定的ADC1
	ADC_DMACmd(ADC1, ENABLE);
	
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);
	DMA_Cmd(DMA1_Channel1,ENABLE);
	
	ADC_ResetCalibration(ADC1);	//使能复位校准  	 
	while(ADC_GetResetCalibrationStatus(ADC1));	//等待复位校准结束
	ADC_StartCalibration(ADC1);	 //开启AD校准
	while(ADC_GetCalibrationStatus(ADC1));	 //等待校准结束
	
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);
	DMA_Cmd(DMA1_Channel1,ENABLE);
}

uint16_t TempSensor_GetAdcValue(uint8_t adc_channel)
{
	uint32_t value=0;
	uint8_t i;
	for(i=0;i<SAMPLE_SIZE;i++)
	{
		value+=ADC_ValueBuf[i][adc_channel];
	}
	value=value/SAMPLE_SIZE;
	if((value%SAMPLE_SIZE)>(SAMPLE_SIZE/2))
		value+=1;
	return value;
}

uint8_t TempSensor_GetTempVaule(uint8_t sensor_on)
{
	unsigned long res;
	float res_f;
	uint16_t adc_value;
	uint8_t i;
	uint8_t temp;
	adc_value=TempSensor_GetAdcValue(sensor_on);
	
	res_f=(float)(adc_value*10.00)/(4096-adc_value);
	res=res_f*1000;
	
	if(res>=Temp_res[0])
		temp=1;
	else if(res<=Temp_res[90])
		temp=90;
//	if((temp>Temp_res[0])||(temp<Temp_res[90]))//传感器错误
//		return 0xFF;
	else
	{
		for(i=0;i<90;i++)
		{
			if(((res<Temp_res[i])&&(res>Temp_res[i+1]))||(res==Temp_res[i])||(res==Temp_res[i+1]))
			{
				if((res-Temp_res[i+1])>(Temp_res[i+1]-res))
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
	
