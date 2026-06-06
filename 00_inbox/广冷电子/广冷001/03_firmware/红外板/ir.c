#include "ir.h"

//8个灯珠一组，4ms内完成一轮扫描，
//4051选通接收灯珠，595依次开启发射灯珠，开启500us后？
//确认有无接收到。

Ir_TypeDef	IrTask;

void Ir_Delay(u32 cnt)
{
	u32 i;
	
	for(i=0;i<cnt;i++)
	{
		while(0);
	}
}

void Ir_Select_Send(u8 no,u8 enable)
{
	u8 i;
	u16 mask;
	
	if(enable)
		mask=((u16)0x0101<<no);
	else
		mask=0;

	IR_595_RCLK=0;
	Ir_Delay(15);
	for(i=0;i<16;i++)
	{
		IR_595_SRCLK=0;
		Ir_Delay(15);
		if(mask&((u16)0x8000>>i))
		{
			IR_595_QD1=1;
//			IR_595_QD3=1;
		}
		else
		{
			IR_595_QD1=0;
			IR_595_QD3=0;
		}
		Ir_Delay(15);
		
		IR_595_SRCLK=1;
		
		Ir_Delay(15);
		
	}
	IR_595_RCLK=1;
	Ir_Delay(15);
}

u8 Ir_Read_Recive(u8 no)
{
	switch(no)
	{
		case 0:
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
		case 1:
		{
			IR_4051_A=1;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
		case 2:
		{
			IR_4051_A=0;
			IR_4051_B=1;
			IR_4051_C=0;			
		}
		break;
		case 3:
		{
			IR_4051_A=1;
			IR_4051_B=1;
			IR_4051_C=0;			
		}
		break;
		case 4:
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=1;			
		}
		break;
		case 5:
		{
			IR_4051_A=1;
			IR_4051_B=0;
			IR_4051_C=1;			
		}
		break;
		case 6:
		{
			IR_4051_A=0;
			IR_4051_B=1;
			IR_4051_C=1;			
		}
		break;
		case 7:
		{
			IR_4051_A=1;
			IR_4051_B=1;
			IR_4051_C=1;			
		}
		break;
		default:
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
	}

	if(IR_4051_IN1)
		IrTask.x1=1;
	else
		IrTask.x1=0;
	
	if(IR_4051_IN2)
		IrTask.x2=1;
	else
		IrTask.x2=0;
	
	if(IR_4051_IN3)
		IrTask.x3=1;
	else
		IrTask.x3=0;
	
	if(IR_4051_IN4)
		IrTask.x4=1;
	else
		IrTask.x4=0;	

//	if((IR_4051_IN1&&IR_4051_IN2)||(IR_4051_IN3&&IR_4051_IN4))
//	if(IR_4051_IN1&&IR_4051_IN2&&IR_4051_IN3&&IR_4051_IN4)
	if(IR_4051_IN3&&IR_4051_IN4)
//	if(IR_4051_IN1&&IR_4051_IN2)
		return 1;
	else
		return 0;
}



void Ir_Scan_Task(void)
{

	
	if(IrTask.sta==0xFF)
	{
		IR_LEVEL_OUT=1;
		IR_LED_OUT=1;
	}
	else
	{
		IR_LEVEL_OUT=0;
		IR_LED_OUT=0;
	}
	
	switch(IrTask.step)
	{
		case 0://选择发射管，接收管。(开)
		{		
			Ir_Read_Recive(IrTask.no);			
			Ir_Select_Send(IrTask.no,1);
			
			IrTask.step=1;
			IrTask.scan_cnt=10;
			IrTask.ok_cnt_on=0;
		}
		break;
		case 1:
		{
			if(Ir_Read_Recive(IrTask.no))
			{
				IrTask.ok_cnt_on++;
			}
			
			if(IrTask.scan_cnt)
				IrTask.scan_cnt--;
			else
			{
				IrTask.step=2;
			}
		}
		break;
		case 2://选择发射管，接收管。(关)
		{
			Ir_Select_Send(IrTask.no,0);	
			
			IrTask.step=3;
			IrTask.scan_cnt=5;
			IrTask.ok_cnt_off=0;
		}
		break;
		case 3:
		{	
			if(!Ir_Read_Recive(IrTask.no))
			{
				IrTask.ok_cnt_off++;
			}
			
			if(IrTask.scan_cnt)
				IrTask.scan_cnt--;
			else
			{
				if(IrTask.ok_cnt_off>2&&IrTask.ok_cnt_on>1)
				{
					IrTask.sta|=0x1<<IrTask.no;
				}
				else
				{
					IrTask.sta &=~(0x1<<IrTask.no);
				}
				IrTask.step=4;
				IrTask.no++;
				IrTask.no%=8;	
				IrTask.scan_cnt=10;				
			}
		}
		break;
		case 4:
		{
			if(IrTask.scan_cnt)
				IrTask.scan_cnt--;
			else
			{
				IrTask.step=0;
			}
		}
		break;
	}
}

void Ir_Init(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;

	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA
							|RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOC, ENABLE);	

	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	
//	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2;	 
//	GPIO_Init(GPIOA, &GPIO_InitStructure);	

	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1|GPIO_Pin_2;	 
	GPIO_Init(GPIOB, &GPIO_InitStructure);	

	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2;	 
	GPIO_Init(GPIOA, &GPIO_InitStructure);		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13|GPIO_Pin_14|GPIO_Pin_15|GPIO_Pin_6;	 
	GPIO_Init(GPIOC, &GPIO_InitStructure);	
	
	
	
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING; 		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_14|GPIO_Pin_15;	 
	GPIO_Init(GPIOB, &GPIO_InitStructure);	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;	 
	GPIO_Init(GPIOC, &GPIO_InitStructure);	

	IR_595_RCLK=0;
	IR_595_SRCLK=0;
}