#include "gate_control.h"
GateControlTypeDef GateControl={0x01};

uint8_t GateControl_GetDoorOpenSta(void)
{
	return SpeedMotor_ReadLimitMotorUp(0x00);
}

uint8_t GateControl_GetDoorCloseSta(void)
{
	return SpeedMotor_ReadLimitMotorDown(0x00);
}

void GateControl_GateDoorTestTask(void)
{
	if(GateControl.en_test==0x00&&GateControl.test_sta==0x00)
		return;
	if(GateControl.en_test==0x00)
	{
		SpeedMotor_MotorLimitDriveStor(0x00);
		GateControl.test_sta=0x00;
	}
	else
	{
		switch(GateControl.test_sta)
		{
			case 0x00:
				if(GateControl_GetDoorOpenSta()==0x01)//检测防盗门是否开启
				{
					SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATECLOSE,300,90);//关闭防盗门
					GateControl.test_sta=0x02;
				}
				else
				{
					SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATEOPEN,300,90);//开启防盗门
					GateControl.test_sta=0x01;
				}
				break;
			case 0x01://等待防盗门开启
				if(SpeedMotor_ReadLimitMotorEnState(0x00)==0x00)//检测电机停止
				{
          if(GateControl_GetDoorOpenSta())
					{
						GateControl.err&=(~0x01);
					}
					else//防盗门有故障
					{				
						GateControl.err|=0x01;
						GateControl.test_openerr_num++;
					}
					GateControl.test_sta=0x02;
					SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATECLOSE,300,90);//关闭防盗门
				}
				break;
			case 0x02://关闭防盗门
				if(SpeedMotor_ReadLimitMotorEnState(0x00)==0x00)
				{
					if(GateControl_GetDoorCloseSta())//检测是否关闭
					{
						if(GateControl.err&0x01)//防盗门打开存在故障
						{
							if(GateControl.test_openerr_num<2)
								GateControl.test_sta=0x00;
						}
						else
						{
							GateControl.en_test =0x00;
							GateControl.test_sta=0x00;
						}
						GateControl.err&=(~0x02);
					}
					else//防盗门故障
					{
						GateControl.test_sta=0x01;
						GateControl.err|=0x02;
						GateControl.test_closerr_num++;
						if(GateControl.test_closerr_num<2)
						 SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATEOPEN,300,90);//开启防盗门
						else
						{
							GateControl.en_test =0x00;
							GateControl.test_sta=0x00;
						}
					}
				}
				break;
		}
	}
}


uint8_t GateControl_StarOpenDoor(void)
{
	switch(GateControl.sta)
	{
		case 0x00:
			if(GateControl_GetDoorOpenSta())
				return 0xFF;//已经打开
			else
			{
				GateControl.sta=0x01;
				SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATEOPEN,300,90);//开启防盗门
			}
			break;
		case 0x01:
			if(SpeedMotor_ReadLimitMotorEnState(0x00)==0x00)//检测电机停止
			{
				if(GateControl_GetDoorOpenSta())
				{
					GateControl.sta=0x00;
					GateControl.err&=(~0x01);
					return 0xFF;
				}
				else//防盗门有故障
				{	
					GateControl.sta=0x00;
					GateControl.err|=0x01;
          if(GateControl_GetDoorCloseSta())
						return 0xEE;//防盗门未开启
					else
						return 0xFE;//防盗门半开					
				}
			}
			break;
	}
  return GateControl.sta;
}

uint8_t GateControl_StarCloseDoor(void)
{
	switch(GateControl.sta)
	{
		case 0x00:
			if(GateControl_GetDoorCloseSta())
				return 0xFF;//关闭
			else
			{
				GateControl.sta=0x01;
				SpeedMotor_MotorLimitDriveStar(0x00,GATECONTROL_GATECLOSE,300,90);//关闭防盗门
			}
			break;
		case 0x01:
		  if(SpeedMotor_ReadLimitMotorEnState(0x00)==0x00)//检测电机停止
			{
				if(GateControl_GetDoorCloseSta())
				{
					GateControl.sta=0x00;
					GateControl.err&=(~0x02);
					return 0xFF;
				}
				else//防盗门有故障
				{	
					GateControl.sta=0x00;
					GateControl.err|=0x02;
          if(GateControl_GetDoorOpenSta())
						return 0xEE;//防盗门未关闭
					else
						return 0xFE;//防盗门半开					
				}
			}
			break;
	}
	return GateControl.sta;
}