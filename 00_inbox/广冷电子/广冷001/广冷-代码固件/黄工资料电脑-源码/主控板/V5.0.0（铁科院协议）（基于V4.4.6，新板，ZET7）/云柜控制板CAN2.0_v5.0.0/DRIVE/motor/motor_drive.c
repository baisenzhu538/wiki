/*
*********************************************************************************************************
*
*	模块名称 : 矩阵货道电机驱动程序
*	文件名称 : motor_drive.c
*	版    本 : V1.0
*	说    明 : 实现矩阵貨道控制，链带和弹簧貨道识别，实现链带貨道延时停转，弹簧貨道按信号停转
*	修改记录 :
*		版本号  日期       作者    说明
*		V1.0    2018-12-29 OUSI   
*   V1.0.1  2019-02-12 Waves   修改为通过链带和弹簧触发信号特征判断弹簧或者链带货道
*********************************************************************************************************
*/

#include "motor_drive.h"

MotorDriveTypedef MotorDrive;

void MotorDrive_Init(void)
{
	uint8_t y;
	for(y=0;y<MOTOR_Y_MAX;y++)
	{
	 MotorDrive.position[y].positionstate=0x00000000;
	 MotorDrive.link[y].linkstate        =0x00000000;
	}
	MotorGpio_GpioInit();//初始化IO
}

void MotorDrive_RestPosit(void)
{
//	MotorDrive_MotorManage.drive.runeneable|=((~MotorDrive_MotorManage.position.positionstate)&0x00001FFF);
}

uint8_t MotorDrive_SetBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	if(MotorDrive.state.runstate)//检测电机运行状态
		return 0x00;
	MotorDrive.motorset.runeneable=0x01;
	MotorDrive.motorset.motor_x   =motor_x_ch;
	MotorDrive.motorset.motor_y   =motor_y_ch;
	 return 0xFF;//电机连接，设置驱动位成功
}


void MotorDrive_ResetBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	MotorDrive.motorset.runeneable=0x00;
}



uint32_t MotorDrive_GetLinkState(uint8_t motor_y_ch)
{
	return MotorDrive.link[motor_y_ch].linkstate;
}

uint8_t MotorDrive_GetLinkStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	if(MotorDrive.link[motor_y_ch].linkstate&(0x00000001<<motor_x_ch))
	  return 0x01;
	else
		return 0x00;
}

uint32_t MotorDrive_GetBlockState(uint8_t motor_y_ch)
{
	return MotorDrive.err[motor_y_ch].blockstate;
}

uint32_t MotorDrive_GetErrState(uint8_t motor_y_ch)
{
	return MotorDrive.state.errsta;
}

uint8_t MotorDrive_GetBlockStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.err[motor_y_ch].blockstate&0x00000001<<motor_x_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_GetRisingStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.position[motor_y_ch].risingstate&0x00000001<<motor_x_ch;
	if(state)
	{
		MotorDrive.position[motor_y_ch].risingstate&=(~state);
		return 0x01;
	}
	else
		return 0x00;
	
}
uint8_t MotorDrive_GetFallingStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.position[motor_y_ch].fallingstate&0x00000001<<motor_x_ch;
	if(state)
	{
		MotorDrive.position[motor_y_ch].fallingstate&=(~state);
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t MotorDrive_GetPositionStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.position[motor_y_ch].positionstate&0x00000001<<motor_x_ch;
	if(state)
	 return 0x01;
	else
	 return 0x00;
}
//获取位置信号高电平时间
uint16_t MotorDrive_GetPositionSignal_HightLevelTime(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	return MotorDrive.position[motor_y_ch].hightleveltime[motor_x_ch];
}

float MotorDrive_GetMotorCurrent(void)
{
	return MotorDrive.motorcurrent;
}

//获取位置信号低电平时间
uint16_t MotorDrive_GetPositionSignal_LowLevelTime(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	return MotorDrive.position[motor_y_ch].lowleveltime[motor_x_ch];
}

uint8_t MotorDrive_GetRunState(void)
{
	uint32_t state;
	return MotorDrive.state.runstate;
}
uint8_t MotorDrive_GetEnState(void)
{
	uint32_t state;
	state=MotorDrive.motorset.runeneable;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint32_t MotorDrive_GeOTState(uint8_t motor_y_ch)
{
	return MotorDrive.err[motor_y_ch].outtimestate;
}

uint8_t MotorDrive_GeOTStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.err[motor_y_ch].outtimestate&0x00000001<<motor_x_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_GetErrStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	uint32_t state;
	state=MotorDrive.state.errsta;
	if(state)
		return 0x01;
	else
		return 0x00;
}
//获取运行故障
uint8_t MotorDrive_GetRunErrState(void)
{
	return MotorDrive.state.errsta;
}

uint8_t MotorDrive_ReadMotorMode(void)
{
	return MotorDrive.state.motormod;
}

uint8_t MotorDrive_ReadPositErr(void)
{
	return MotorDrive.state.positerr;
}

//空闲状态检测
void MotorDrive_LinkSignalCollect(void)
{
	static uint8_t timecount=0;
	static uint8_t ch_x_count=0;
	static uint8_t ch_y_count=0;
	uint32_t linkstate,poststate,fallstate,risingstate;
	uint8_t i;
	
	if(MotorDrive.motorset.runeneable)
	{
		timecount=0;
		ch_x_count=0;
		ch_y_count=0;
		return;
	}
	if(timecount<MOTOR_SIGNAL_COLLECTTIME)
	{
		timecount++;
		MotorGpio_Set_X(ch_x_count);
	}
	
	if(timecount==MOTOR_SIGNAL_COLLECTTIME)
	{
		uint32_t signalstate;
		
		if(DigitalSignal_GetSignalLevelBit(2,ch_y_count))
		{
			MotorDrive.link[ch_y_count].linkstate
				|=(0x00000001<<ch_x_count);
		}
		else
		{
			MotorDrive.link[ch_y_count].linkstate
				&=~(0x00000001<<ch_x_count);
		}
		
		if(DigitalSignal_GetSignalLevelBit(1,ch_y_count))
		{
			MotorDrive.position[ch_y_count].positionstate
				|=(0x00000001<<ch_x_count);
		}
		else
		{
			MotorDrive.position[ch_y_count].positionstate
				&=~(0x00000001<<ch_x_count);
		}
		
		if(DigitalSignal_GetSignalRisingBit(1,ch_y_count))
		{
			MotorDrive.position[ch_y_count].risingstate
				|=(0x00000001<<ch_x_count);
		}
		
		if(DigitalSignal_GetSignalFallingBit(1,ch_y_count))
		{
			MotorDrive.position[ch_y_count].fallingstate
				|=(0x00000001<<ch_x_count);
		}
					
		timecount=0;
		ch_y_count++;
		if(ch_y_count==MOTOR_Y_MAX)
		{
			ch_y_count=0;
			ch_x_count++;
			if(ch_x_count==MOTOR_X_MAX)
			{
				ch_x_count=0;
			}
		}
	}
	
	MotorDrive.motorcurrent=MotorGpio_GetMotorCurrent();
}

//位置信号检测
void MotorDrive_PositSignalCollect(void)
{
	uint32_t linkstate,poststate,fallstate,risingstate;
	uint8_t x,y;
	
	if(MotorDrive.motorset.runeneable==0
		||MotorDrive.state.runstate==0)
	  return;
	
	x=MotorDrive.motorset.motor_x;
	y=MotorDrive.motorset.motor_y;

	MotorGpio_Set_X(x);
	
	if(DigitalSignal_GetSignalLevelBit(1,y))
	{
		MotorDrive.position[y].positionstate
			|=(0x00000001<<x);
	}
	else
	{
		MotorDrive.position[y].positionstate
			&=~(0x00000001<<x);
	}
	
	if(DigitalSignal_GetSignalRisingBit(1,y))
	{
		MotorDrive.position[y].risingstate
			|=(0x00000001<<x);
	}
	if(DigitalSignal_GetSignalFallingBit(1,y))
	{
		MotorDrive.position[y].fallingstate
			|=(0x00000001<<x);
	}
	
	MotorDrive.position[y].hightleveltime[x] = DigitalSignal_GetHightLevelTime(1,y);
	MotorDrive.position[y].lowleveltime[x]   = DigitalSignal_GetLowLevelTime(1,y);
	
	MotorDrive.motorcurrent=MotorGpio_GetMotorCurrent();
}

//10ms 调用一次
void MotorDrive_TimeTask(void)
{
	MotorDrive_LinkSignalCollect();
	MotorDrive_PositSignalCollect();
}
//循环调用一次
void MotorDrive_Task(void)
{
	uint8_t i;
	uint32_t Bit1=0x00000001;
	uint32_t BitNum;                   //获取信号状态
	
	MotorDrive_LinkSignalCollect();    //连接信号采集
	MotorDrive_PositSignalCollect();   //位置信号采集
	
	if((MotorDrive.motorset.runeneable==0)
		&&(MotorDrive.state.runstate==0))
		return;
	
	if(MotorDrive.motorset.runeneable==0)//关闭电机
	{
		MotorDrive.state.runstate=0;
		MotorGpio_RestAll_X();
		MotorGpio_RestAll_Y();
	}
	else
	{
		if(MotorDrive.state.runstate)//运行计时
			MotorDrive.runtime++;
		
		if(MotorDrive.state.runstate==0)
		{
			MotorDrive.maxtime=D_MOTOR_OUTTIME;
			MotorDrive.state.runstate=0x01;
			MotorDrive.runtime=0;       		//运行时间置0
			MotorDrive.triggertime=0;			
			MotorDrive.state.errsta=0x00;		
            MotorDrive.blocktime=0x00;
			MotorDrive.state.motormod=0x00;
			
			MotorGpio_Set_X(MotorDrive.motorset.motor_x);//设置电机x轴电机电平信号
			MotorGpio_Set_Y(MotorDrive.motorset.motor_y);//启动电机
		}
		else if(MotorDrive.runtime==MOTOR_STAR_DELAY)//启动检测货道异常
		{
			MotorDrive_GetFallingStateBit(MotorDrive.motorset.motor_x,MotorDrive.motorset.motor_y);
			MotorDrive_GetRisingStateBit(MotorDrive.motorset.motor_x,MotorDrive.motorset.motor_y);
			
			if(MotorDrive_GetPositionStateBit(MotorDrive.motorset.motor_x,MotorDrive.motorset.motor_y))//检测电机位置是否正常
				MotorDrive.state.positerr=0x01;//异常状态
			else
				MotorDrive.state.positerr=0x00;//正常状态
			
			MotorDrive.state.runstate=0x02; //完成货道异常检测
		}
		else if(MotorDrive.runtime>MOTOR_STAR_DELAY)
		{
			if(MotorDrive.triggertime)//检测电机是否达到触发条件
			{
				if((MotorDrive.runtime-MotorDrive.triggertime)>MOTOR_STOP_DELAY)
				{
					uint8_t x,y;
					x=MotorDrive.motorset.motor_x;
					y=MotorDrive.motorset.motor_y;
					BitNum=Bit1<<MotorDrive.motorset.motor_x;
					MotorDrive.err[MotorDrive.motorset.motor_y].outtimestate&=(~BitNum);
					MotorDrive.err[MotorDrive.motorset.motor_y].blockstate&=(~BitNum);
					MotorDrive.triggertime=0x00;
					
					MotorDrive.motorset.runeneable=0;//复位使能位
					MotorDrive.state.runstate  =0;//复位状态位
					MotorGpio_RestAll_X();
					MotorGpio_RestAll_Y();
				}
			}
			else if(MotorDrive_GetFallingStateBit(MotorDrive.motorset.motor_x,MotorDrive.motorset.motor_y))//检测位置开关是否弹开，上升沿信号
			{
				uint8_t x,y;
				x=MotorDrive.motorset.motor_x;
				y=MotorDrive.motorset.motor_y;
				if(MotorDrive_GetPositionSignal_HightLevelTime(x,y)>MOTOR_SIGLIFTER_TIME)
				{
					if(MotorDrive_GetPositionSignal_HightLevelTime(x,y)>COIL_SIGLIFTER_TIME)//弹簧货道
					{
						BitNum=Bit1<<MotorDrive.motorset.motor_x;
						MotorDrive.state.motormod=MOTOR_COILMODE;
						MotorDrive.err[MotorDrive.motorset.motor_y].outtimestate&=(~BitNum);
						MotorDrive.err[MotorDrive.motorset.motor_y].blockstate&=(~BitNum);
						MotorDrive.triggertime=0x00;
						MotorDrive.motorset.runeneable=0;//复位使能位
						MotorDrive.state.runstate  =0;//复位状态位
						MotorGpio_RestAll_X();
						MotorGpio_RestAll_Y();
					}
					else if(MotorDrive_GetPositionSignal_HightLevelTime(x,y)>CONVEYER_SIGLIFTER_TIME)//履带或链带货道
					{
						MotorDrive.state.motormod=MOTOR_CONVEYERMODE;
						MotorDrive.triggertime=MotorDrive.runtime; 
					}
			  }
			}
			else if(MotorDrive.runtime==MotorDrive.maxtime)//电机超时
			{ 
				BitNum=Bit1<<MotorDrive.motorset.motor_x;
				MotorDrive.err[MotorDrive.motorset.motor_y].outtimestate|=BitNum;
				MotorDrive.state.errsta=0x01;
				MotorDrive.motorset.runeneable=0;//复位使能位
				MotorDrive.state.runstate  =0;//复位状态位
				MotorGpio_RestAll_X();
				MotorGpio_RestAll_Y();
			}
			else if(MotorDrive_GetMotorCurrent()>MOTOR_MOTORCURRENT_MAX)
			{
				if(MotorDrive.blocktime<MOTOR_BLOCKTIME)
					MotorDrive.blocktime++;
				else
				{
					BitNum=Bit1<<MotorDrive.motorset.motor_x;
					MotorDrive.err[MotorDrive.motorset.motor_y].blockstate|=BitNum;
					MotorDrive.state.errsta=0x02;
					MotorDrive.motorset.runeneable=0;//复位使能位
					MotorDrive.state.runstate  =0;//复位状态位
					MotorGpio_RestAll_X();
					MotorGpio_RestAll_Y();
				}
			}
			else if(MotorDrive.runtime==MOTOR_CHECKMODE_TIME)
			{
				if(MotorDrive_GetPositionStateBit(MotorDrive.motorset.motor_x,MotorDrive.motorset.motor_y))
				{
					MotorDrive.state.motormod=MOTOR_COILMODE;
				}
				else
					MotorDrive.state.motormod=MOTOR_CONVEYERMODE;
			}
		}
   }
}

