#include "rgb_led.h"

uint8_t Rgb_led_buff[RGB_MAX_LEDNUM*24+1]={0};//RGB LED显示缓存一个字节一个位
uint8_t Dma_flag=0;

void RgbLed_Init(void)
{
  TIM_TimeBaseInitTypeDef  TIM_TimeBaseStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
  TIM_OCInitTypeDef  TIM_OCInitStructure;
	GPIO_InitTypeDef GPIO_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_TIM1|RCC_APB2Periph_GPIOE|RCC_APB2Periph_AFIO, ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	GPIO_PinRemapConfig(GPIO_FullRemap_TIM1,ENABLE);
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;				
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP; 		 //推挽输出
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
  GPIO_Init(GPIOE, &GPIO_InitStructure);	
	
	
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&TIM1->CCR1);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (u32)Rgb_led_buff; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralDST;  
	DMA_InitStructure.DMA_BufferSize =RGB_MAX_LEDNUM*24+1;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_HalfWord; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel5,&DMA_InitStructure);  
	DMA_Cmd(DMA1_Channel5,DISABLE);
	
	DMA_ITConfig(DMA1_Channel5,DMA_IT_TC,ENABLE);
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel5_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure); 
	DMA_ClearITPendingBit(DMA1_IT_TC5);
	
	//定时器TIM3初始化
	TIM_TimeBaseStructure.TIM_Period = 90;//90-1.25us 45-0.625us  22.5-0.3125us //设置在下一个更新事件装入活动的自动重装载寄存器周期的值	
	TIM_TimeBaseStructure.TIM_Prescaler =0x00;                   //设置用来作为TIMx时钟频率除数的预分频值
	TIM_TimeBaseStructure.TIM_ClockDivision = TIM_CKD_DIV1;      //设置时钟分割:TDTS = Tck_tim
	TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up;  //TIM向上计数模式
	TIM_TimeBaseInit(TIM1, &TIM_TimeBaseStructure);              //根据指定的参数初始化TIMx的时间基数单位
 
	TIM_OCInitStructure.TIM_Pulse  =0;
	TIM_OCInitStructure.TIM_OCMode = TIM_OCMode_PWM2; //选择定时器模式:TIM脉冲宽度调制模式2
 	TIM_OCInitStructure.TIM_OutputState = TIM_OutputState_Enable; //比较输出使能
	TIM_OCInitStructure.TIM_OCPolarity = TIM_OCPolarity_Low; //输出极性:TIM输出比较极性高
	TIM_OC1Init(TIM1, &TIM_OCInitStructure);  //根据T指定的参数初始化外设TIM3 OC2

	TIM_OC1PreloadConfig(TIM1, TIM_OCPreload_Enable);  //使能TIM3在CCR2上的预装载寄存器
	TIM_ARRPreloadConfig(TIM1, ENABLE);
	
	TIM_DMACmd(TIM1,TIM_DMA_Update,DISABLE);
	
	TIM_Cmd(TIM1, ENABLE);  
	TIM_CtrlPWMOutputs(TIM1, ENABLE);	
  
  Send_Rgb(0x00000000);//清空所有显示	
}

void Set_RgbLedNum(uint8_t led_num,COLOR_TypeDef *pcolor)
{
	uint8_t i;
	uint8_t len=0;
	if(Dma_flag==1)
		return;
	for(i=0;i<24;i++)
	{
		len=(led_num*24)+i;
		if(*((u32*)pcolor)&0x00800000>>i)
		 Rgb_led_buff[len]=45;//输出1
		else
		 Rgb_led_buff[len]=23;//输出0
	}
	Rgb_led_buff[RGB_MAX_LEDNUM*24]=0;
	DMA1_Channel5->CNDTR=RGB_MAX_LEDNUM*24+1;
	DMA_Cmd(DMA1_Channel5,ENABLE);
	TIM_DMACmd(TIM1,TIM_DMA_Update,ENABLE);
	Dma_flag=1;
}

void Set_RgbLed(COLOR_TypeDef *pcolor)
{
	uint8_t i=0;
	uint8_t j=0;
	uint8_t len=0;
	                 //  |  ||GREEN||RED||BLUE|
	                 //0x 00   00     00   00
	if(Dma_flag==1)
		return;
	for(j=0;j<RGB_MAX_LEDNUM;j++)
	{
		for(i=0;i<24;i++)
		{
			len=(j*24)+i;
			if(*((u32*)pcolor)&0x00800000>>i)
			 Rgb_led_buff[len]=45;//输出1
			else
			 Rgb_led_buff[len]=23;//输出0
		}
  }
  Rgb_led_buff[RGB_MAX_LEDNUM*24]=0;
	DMA1_Channel5->CNDTR=RGB_MAX_LEDNUM*24+1;
	DMA_Cmd(DMA1_Channel5,ENABLE);
	TIM_DMACmd(TIM1,TIM_DMA_Update,ENABLE);
	Dma_flag=1;
}

void Send_Rgb(uint32_t rgb)
{
	uint8_t i=0;
	uint8_t j=0;
	uint8_t len=0;
	uint32_t RGB=rgb;//  |  ||GREEN||RED||BLUE|
	                 //0x 00   00     00   00
	if(Dma_flag==1)
		return;
	for(j=0;j<RGB_MAX_LEDNUM;j++)
	{
		for(i=0;i<24;i++)
		{
			len=(j*24)+i;
			if(RGB&0x00800000>>i)
			 Rgb_led_buff[len]=45;//输出1
			else
			 Rgb_led_buff[len]=23;//输出0
		}
  }
  Rgb_led_buff[RGB_MAX_LEDNUM*24]=0;
	DMA1_Channel5->CNDTR=RGB_MAX_LEDNUM*24+1;
	DMA_Cmd(DMA1_Channel5,ENABLE);
	TIM_DMACmd(TIM1,TIM_DMA_Update,ENABLE);
	Dma_flag=1;
}

//DMA传输完成中断，失能定时器DMA与DMA模块
void DMA1_Channel5_IRQHandler(void)
{
	if(DMA_GetITStatus(DMA1_IT_TC5)!=RESET)
	{
		DMA_ClearITPendingBit(DMA1_IT_TC5);
		DMA1_Channel5->CNDTR=0;
		TIM_DMACmd(TIM1,TIM_DMA_Update,DISABLE);//必须关闭，否则会造成输出异常
		DMA_Cmd(DMA1_Channel5,DISABLE);
    Dma_flag=0;
	}
} 


u8 BLN_ChangeFlag=0;
u8 distributionConut=0;
#define BLN_DISATRIBUTION_TOLAL 100
float R_BLN_TIMER_LEVEL;
float G_BLN_TIMER_LEVEL;
float B_BLN_TIMER_LEVEL;
COLOR_TypeDef BLN_Color={0,0,0,0};

u16 colorChangeConut=0;
void colorChange(void)
{
	switch(colorChangeConut/5)
	{
		case 0:
			BLN_Color.r=250-(colorChangeConut%5)*50;
			BLN_Color.b=(colorChangeConut%5)*50;
			break;
		case 1:
			BLN_Color.b=250-(colorChangeConut%5)*50;
			BLN_Color.g=(colorChangeConut%5)*50;
			break;
		case 2:
			BLN_Color.g=250-(colorChangeConut%5)*50;
			BLN_Color.r=(colorChangeConut%5)*50;
			break;
		
	}
	colorChangeConut++;
	if(colorChangeConut/5>=3) 
		colorChangeConut=0;
}
void RgbLed_Task(void)
{
	BLN_Color.r=(u8)(R_BLN_TIMER_LEVEL*distributionConut+0.5);
	BLN_Color.g=(u8)(G_BLN_TIMER_LEVEL*distributionConut+0.5);
	BLN_Color.b=(u8)(B_BLN_TIMER_LEVEL*distributionConut+0.5);		
	Set_RgbLed(&BLN_Color);
	
	if(BLN_ChangeFlag==0)
	{
		distributionConut++;
		if(distributionConut>=BLN_DISATRIBUTION_TOLAL)
		BLN_ChangeFlag=1;
	}
	else
	{
		if(distributionConut) 
			distributionConut--;
		else
		{
			BLN_ChangeFlag=0;
			colorChange();
			R_BLN_TIMER_LEVEL=(float)BLN_Color.r/BLN_DISATRIBUTION_TOLAL;
			G_BLN_TIMER_LEVEL=(float)BLN_Color.g/BLN_DISATRIBUTION_TOLAL;
			B_BLN_TIMER_LEVEL=(float)BLN_Color.b/BLN_DISATRIBUTION_TOLAL;
		}
	}
}
