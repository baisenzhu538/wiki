#include "sellmotor.h"

MotorDrive_RegisterMapTypedef  MotorDrive_RegisterMap[MOTOR_MANAGE_MAXNUN];


uint8_t SellMotor_SetStar(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	if(dri_no==0x00)
	 return MotorDrive_SetBit(motor_x_ch,motor_y_ch);
	if(MotorDrive_RegisterMap[dri_no].state.runstate)//检测电机运行状态
		return 0x00;
	MotorDrive_RegisterMap[dri_no].motorset.runeneable=0x01;
	MotorDrive_RegisterMap[dri_no].motorset.motor_x   =motor_x_ch;
	MotorDrive_RegisterMap[dri_no].motorset.motor_y   =motor_y_ch;
	 return 0xFF;//电机连接，设置驱动位成功
}

void SellMotor_SetStop(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch)
{

	if(dri_no==0x00)
	{
	  MotorDrive_ResetBit(motor_x_ch,motor_y_ch);
		return;
	}
	MotorDrive_RegisterMap[dri_no].motorset.runeneable=0x00;
}


uint32_t SellMotor_GetLinkState(uint8_t dri_no,uint8_t motor_y_ch)
{

	if(dri_no==0x00)
	 return MotorDrive_GetLinkState(motor_y_ch);
	return MotorDrive_RegisterMap[dri_no].link[motor_y_ch].linkstate;
}

uint8_t SellMotor_GetLinkStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	if(dri_no==0x00)
		MotorDrive_RegisterMap[dri_no].link[motor_y_ch].linkstate=SellMotor_GetLinkState(dri_no,motor_y_ch);
	
	if(MotorDrive_RegisterMap[dri_no].link[motor_y_ch].linkstate&(0x00000001<<motor_x_ch))
	  return 0x01;
	else
		return 0x00;
}


uint32_t SellMotor_GetBlockState(uint8_t dri_no,uint8_t motor_y_ch)
{
	return MotorDrive_RegisterMap[dri_no].err[motor_y_ch].blockstate;
}

uint32_t SellMotor_GetErrState(uint8_t dri_no,uint8_t motor_y_ch)
{
	return MotorDrive_RegisterMap[dri_no].state.errsta;
}

uint8_t SellMotor_GetBlockStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	
	if(dri_no==0x00)	
	  MotorDrive_RegisterMap[dri_no].err[motor_y_ch].blockstate=SellMotor_GetBlockState(dri_no,motor_y_ch);
	
	if(MotorDrive_RegisterMap[dri_no].err[motor_y_ch].blockstate&0x00000001<<motor_x_ch)
		return 0x01;
	else
		return 0x00;
}

uint32_t SellMotor_GeOTState(uint8_t dri_no,uint8_t motor_y_ch)
{
	uint32_t state;
	if(dri_no==0x00)
	 return MotorDrive_GeOTState(motor_y_ch);
	return MotorDrive_RegisterMap[dri_no].err[motor_y_ch].outtimestate;
}

uint8_t SellMotor_GeOTStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch)
{
	if(dri_no==0x00)
		MotorDrive_RegisterMap[dri_no].err[motor_y_ch].outtimestate=SellMotor_GeOTState(dri_no,motor_y_ch);

	if(MotorDrive_RegisterMap[dri_no].err[motor_y_ch].outtimestate&0x00000001<<motor_x_ch)
		return 0x01;
	else
		return 0x00;
}

uint8_t SellMotor_GetRunErrState(uint8_t dri_no)
{
	if(dri_no==0x00)
		return MotorDrive_GetRunErrState();
	return MotorDrive_RegisterMap[dri_no].state.errsta;
}

uint8_t SellMotor_ReadMotorMode(uint8_t dri_no)
{
	if(dri_no==0x00)
		return MotorDrive_ReadMotorMode();
	return MotorDrive_RegisterMap[dri_no].state.motormod;
}

uint8_t SellMotor_ReadPositErr(uint8_t dri_no)
{
	if(dri_no==0x00)
	 return MotorDrive_ReadPositErr();	
	return MotorDrive_RegisterMap[dri_no].state.positerr;
}

uint8_t SellMotor_GetRunState(uint8_t dri_no)
{
	if(dri_no==0x00)
 	 return MotorDrive_GetRunState();
	return MotorDrive_RegisterMap[dri_no].state.runstate;
}



