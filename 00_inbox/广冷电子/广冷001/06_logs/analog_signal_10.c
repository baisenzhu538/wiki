#include "analog_signal.h"

uint16_t ADC_ValueBuf[SAMPLE_SIZE][ADC_CHANNEL_NUM];

void AnalogSignal_Init(void)
{
	ADC_InitTypeDef 	ADC_InitStructure; 
	GPIO_InitTypeDef  	GPIO_InitStructure;
	DMA_InitTypeDef 	DMA_InitStructure; 
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOC
							|RCC_APB2Periph_ADC1,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);
	
	//温度传感器信号采集引脚配置
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AIN; 		   //上拉输入
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_4|GPIO_Pin_5;
	GPIO_Init(GPIOC, &GPIO_InitStructure);
	
	//电机电流采集引脚配置
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
	GPIO_Init(GPIOB, &GPIO_InitStructure);
	
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
	
	ADC_InitStructure.ADC_Mode 					= ADC_Mode_Independent;	//ADC工作模式:ADC1和ADC2工作在独立模式
	ADC_InitStructure.ADC_ScanConvMode 			= ENABLE;	      		//模数转换工作在扫描模式
	ADC_InitStructure.ADC_ContinuousConvMode 	= ENABLE;				//模数转换工作在连续转换模式
	ADC_InitStructure.ADC_ExternalTrigConv 		= ADC_ExternalTrigConv_None;	//转换由软件而不是外部触发启动
	ADC_InitStructure.ADC_DataAlign 			= ADC_DataAlign_Right;			//ADC数据右对齐
	ADC_InitStructure.ADC_NbrOfChannel 			= ADC_CHANNEL_NUM;				//顺序进行规则转换的ADC通道的数目
	ADC_Init(ADC1, &ADC_InitStructure);			//根据ADC_InitStruct中指定的参数初始化外设ADCx的寄存器   

	ADC_RegularChannelConfig(ADC1, ADC_Channel_14, 1,ADC_SampleTime_71Cycles5);
	ADC_RegularChannelConfig(ADC1, ADC_Channel_15, 2,ADC_SampleTime_71Cycles5);
	ADC_RegularChannelConfig(ADC1, ADC_Channel_8, 3,ADC_SampleTime_71Cycles5);
	
	ADC_Cmd(ADC1, ENABLE);		//使能指定的ADC1
	ADC_DMACmd(ADC1, ENABLE);
	
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);
	DMA_Cmd(DMA1_Channel1,ENABLE);
	
	ADC_ResetCalibration(ADC1);					//使能复位校准  	 
	while(ADC_GetResetCalibrationStatus(ADC1));	//等待复位校准结束
	ADC_StartCalibration(ADC1);	 				//开启AD校准
	while(ADC_GetCalibrationStatus(ADC1));	 	//等待校准结束
	
	ADC_SoftwareStartConvCmd(ADC1, ENABLE);
	DMA_Cmd(DMA1_Channel1,ENABLE);
}

uint16_t AnalogSignal_GetAdcValue(uint8_t adc_channel)
{
	uint32_t value=0;
	uint8_t i;
	if(adc_channel>ADC_CHANNEL_NUM-1)
		return 0x0000;
	for(i=0;i<SAMPLE_SIZE;i++)
	{
		value+=ADC_ValueBuf[i][adc_channel];
	}
	value=value/SAMPLE_SIZE;
	if((value%SAMPLE_SIZE)>(SAMPLE_SIZE/2))
		value+=1;
	return value;
}

