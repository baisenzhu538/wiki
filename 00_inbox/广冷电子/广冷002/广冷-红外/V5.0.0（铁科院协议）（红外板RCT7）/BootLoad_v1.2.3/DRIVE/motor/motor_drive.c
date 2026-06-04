#include "motor_drive.h"

MotorDrive_MotorManageTypedef MotorDrive_MotorManage;

void MotorDrive_Init(void)
{
	MotorDrive_MotorManage.motormaxnum=MOTOR_MAXNUM;
	MotorDrive_MotorManage.motormod   =MOTOR_COILMODE;
	MotorDrive_MotorManage.position.positionstate=0x00000000;
	MotorDrive_MotorManage.link.linkstate        =0x00000000;
	MotorGpio_GpioInit();//初始化IO

}

void MotorDrive_RestPosit(void)
{
	MotorDrive_MotorManage.drive.runeneable|=((~MotorDrive_MotorManage.position.positionstate)&0x00001FFF);
}

uint8_t MotorDrive_SetBit(uint8_t motor_ch)
{
	if((MotorDrive_MotorManage.link.linkstate&0x00000001<<motor_ch)==0)
	 return 0x00;//电机未连接
	if(MotorDrive_MotorManage.drive.blockstate&0x00000001<<motor_ch)
	 return 0x01;                                                  //电机堵转
	if(MotorDrive_MotorManage.drive.outtimestate&0x00000001<<motor_ch)
	 return 0x02;                                                   //运作超时
	MotorDrive_MotorManage.drive.runeneable|=0x00000001<<motor_ch;
	 return 0xFF;//电机连接，设置驱动位成功
}

void MotorDrive_ResetBit(uint8_t motor_ch)
{
	MotorDrive_MotorManage.drive.runeneable&=~(0x00000001<<motor_ch);
	MotorGpio_ResetStar(motor_ch);//停止电机转动
}

uint32_t MotorDrive_GetLinkState(void)
{
	return MotorDrive_MotorManage.link.linkstate;
}

uint8_t MotorDrive_GetLinkStateBit(uint8_t motor_ch)
{
	if(MotorDrive_MotorManage.link.linkstate&(0x00000001<<motor_ch))
	  return 0x01;
	else
		return 0x00;
}

uint32_t MotorDrive_GetBlockState(void)
{
	return MotorDrive_MotorManage.drive.blockstate;
}

uint32_t MotorDrive_GetErrState(void)
{
	return MotorDrive_MotorManage.drive.errstate;
}

uint8_t MotorDrive_GetBlockStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.drive.blockstate&0x00000001<<motor_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_GetRisingStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.position.risingstate&0x00000001<<motor_ch;
	if(state)
	{
		MotorDrive_MotorManage.position.risingstate&=(~state);
		return 0x01;
	}
	else
		return 0x00;
	
}
uint8_t MotorDrive_GetFallingStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.position.fallingstate&0x00000001<<motor_ch;
	if(state)
	{
		MotorDrive_MotorManage.position.fallingstate&=(~state);
		return 0x01;
	}
	else
		return 0x00;
}

uint8_t MotorDrive_GetPositionStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.position.positionstate&0x00000001<<motor_ch;
	if(state)
	 return 0x01;
	else
	 return 0x00;
}

uint8_t MotorDrive_GetRunStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.drive.runstate&0x00000001<<motor_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}
uint8_t MotorDrive_GetEnStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.drive.runeneable&0x00000001<<motor_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_GeOTStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.drive.outtimestate&0x00000001<<motor_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_GetErrStateBit(uint8_t motor_ch)
{
	uint32_t state;
	state=MotorDrive_MotorManage.drive.errstate&0x00000001<<motor_ch;
	if(state)
		return 0x01;
	else
		return 0x00;
}

uint8_t MotorDrive_ReadMotorMode(void)
{
	return MotorDrive_MotorManage.motormod;
}

//电机信号采集，1ms定时循环扫描
void MotorDrive_SignalCollect(void)
{
	if(MotorDrive_MotorManage.drive.runeneable==0x00000000)
	 MotorDrive_MotorManage.link.linkstate=((~DigitalSignal_GetSignalLevel3())&0x00001FFF);
	
	MotorDrive_MotorManage.position.positionstate=DigitalSignal_GetSignalLevel2();
	MotorDrive_MotorManage.position.fallingstate|=DigitalSignal_GetSignalFalling2();
	MotorDrive_MotorManage.position.risingstate |=DigitalSignal_GetSignalRising2();
}
//10ms调用一次
void MotorDrive_Task(void)
{
	uint8_t i;
	uint32_t Bit1=0x00000001;
	uint32_t BitNum;
	MotorDrive_SignalCollect();                    //获取信号状态
	if(MotorDrive_MotorManage.drive.runeneable==0)
		return;
	for(i=0;i<MotorDrive_MotorManage.motormaxnum;i++)
	{
		BitNum=Bit1<<i;
		if(MotorDrive_MotorManage.drive.runeneable&BitNum)
		{
			if((MotorDrive_MotorManage.drive.runstate&BitNum)==0)
			{
				if(MotorDrive_MotorManage.position.positionstate&BitNum)//检测电机是否在初始位置上，以设置不同的超时时间
				{
					MotorDrive_MotorManage.drive.maxtime[i]=D_MOTOR_OUTTIME;
				}
				else
				{
					MotorDrive_MotorManage.drive.maxtime[i]=E_MOTOR_OUTTIME;
				}
				MotorDrive_MotorManage.drive.runstate|=BitNum;
				MotorDrive_MotorManage.position.risingstate&=~(BitNum);
				MotorDrive_MotorManage.position.fallingstate&=~(BitNum);
				MotorDrive_MotorManage.drive.runtime[i]=0;       //运行时间置0
				MotorGpio_SetStar(i);
			}
			else
			{
				MotorDrive_MotorManage.drive.runtime[i]++;
				if(MotorDrive_MotorManage.position.risingstate&BitNum)//检测位置开关是否弹开，上升沿信号
				{
					MotorDrive_MotorManage.drive.runeneable&=~BitNum;//复位使能位
					MotorDrive_MotorManage.drive.runstate  &=~BitNum;//复位状态位
					MotorGpio_ResetStar(i);
				}
				else if((MotorDrive_MotorManage.drive.runtime[i]==MOTOR_BLOCKTIME)&&(MotorDrive_MotorManage.motormod==MOTOR_COILMODE))//检测堵转超时,履带货道不支持堵转检测
				{
				 if(MotorDrive_MotorManage.position.positionstate&BitNum)          //检测位置开关是否下压
					{
						MotorDrive_MotorManage.drive.blockstate|=BitNum; //置位为堵转
						MotorDrive_MotorManage.drive.errstate|=BitNum;
						MotorDrive_MotorManage.drive.runeneable&=~BitNum;//复位使能位
						MotorDrive_MotorManage.drive.runstate  &=~BitNum;//复位状态位
						MotorGpio_ResetStar(i);//关闭电机
					}
				}
				else if(MotorDrive_MotorManage.drive.runtime[i]==MotorDrive_MotorManage.drive.maxtime[i])
				{
					MotorDrive_MotorManage.drive.outtimestate|=BitNum;
					MotorDrive_MotorManage.drive.errstate|=BitNum;
					MotorDrive_MotorManage.drive.runeneable&=~BitNum;//复位使能位
					MotorDrive_MotorManage.drive.runstate  &=~BitNum;//复位状态位
					MotorGpio_ResetStar(i);//关闭电机
				}
			}
		}
	}
}

