#include "sys_sta.h"
#include "sensor.h"

SysState_DeviceStaTypeDef     SysState_DeviceSta;
SysState_BodyAndIrStaTypeDef  SysState_BodySta;
SysState_IrStaTypeDef         SysState_IrSta;
SysState_InitTypeDef          SysState_Init={0x00,0x00,0x00};




void SysSta_SetInit(void)
{
	SysState_Init.initset=0x01;
}
void SysSta_ResetInit(void)
{
	SysState_Init.initset=0x00;
}
void SysSta_InitTask(void)
{
//	if(SysState_Init.initset==0x00&&SysState_Init.initsta==0x00)
//	 return;
//	if(SysState_Init.initset==0x00)
//	{
//		SysState_Init.initsta=0x00;
//		SysState_Init.inittime=0;
//	}
//	else
//	{
//		switch(SysState_Init.initsta)
//		{
//			case 0x00:
//				if(SysState_Init.inittime<SYSINIT_STARTIME)
//				 SysState_Init.inittime++;
//				else
//				{
//         //设置关闭闸门
//				 SpeedMotor_LimitMotorStar(0x00,0x01,0x01,1000,99);
//				 SpeedMotor_LimitMotorStar(0x00,0x02,0x01,1000,99);
//				 SpeedMotor_LimitMotorStar(0x00,0x03,0x01,1000,99);
//				 //设置升降平台自检测试
//				 LiftMotor_LiftMotorTestStar(0x01);
//				 SysState_Init.inittime=0x00;
//				 SysState_Init.initsta=0x01;
//				}
//				break;
//			case 0x01:
//				if(LiftMotor_ReadLiftMotorTest(0x01)==0x00)
//				{
//					SysState_Init.initset =0x00;
//					SysState_Init.inittime=0x00;
//				  SysState_Init.initsta =0x00;
//				}
//				else if(SysState_Init.inittime<SYSINIT_OUTTIME)
//				{
//					SysState_Init.inittime++;
//				}
//        else//初始化超时
//        {
//					SysState_Init.initset =0x00;
//					SysState_Init.inittime=0x00;
//				  SysState_Init.initsta =0x00;
//					SysState_Init.initerr =0x01;
//				}					
//				break;
//		}
//	}
}


SysState_ElcLockStaTypeDef    SysState_ElcLockSta;
//2s钟后执行
void SysSta_Task(void)
{
//	if(Sensor_GetDoorSW1State()&&Sensor_GetDoorSW2State())
//	{
//		if(SysState_ElcLockSta.sta==0x00)
//		{
//			SysState_ElcLockSta.sta=0x01;
//			LiftMotor_LiftMotorDriEn(0x01);
//			SysSta_SetInit();//重现初始化升降平台
//		}
//	}
//	else
//	{
//		if(SysState_ElcLockSta.sta==0x01)
//		{
//			SysState_ElcLockSta.sta=0x00;
//			LiftMotor_LiftMotorDriDisable(0x01);
//			SysSta_ResetInit();
//		}
//	}
//	SysSta_InitTask();
}




void sysSta_SendDeviceSta(uint8_t cmd)
{
	
	SysState_DeviceSta.SysState_ModeSta.mode_num=5;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[0].Contain =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[0].link    =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[0].modetype=(uint16_t)(101);
	SysState_DeviceSta.SysState_ModeSta.ModeSta[1].Contain =0x02;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[1].link    =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[1].modetype=(uint16_t)(101);
	SysState_DeviceSta.SysState_ModeSta.ModeSta[2].Contain =0x00;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[2].link    =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[2].modetype=(uint16_t)(102);
	SysState_DeviceSta.SysState_ModeSta.ModeSta[3].Contain =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[3].link    =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[3].modetype=(uint16_t)(102);
	SysState_DeviceSta.SysState_ModeSta.ModeSta[4].Contain =0x02;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[4].link    =0x01;
	SysState_DeviceSta.SysState_ModeSta.ModeSta[4].modetype=(uint16_t)(102);
	
	SysState_DeviceSta.SysState_DoorSta.Door_num=3;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[0].contain=0x00;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[0].sta    =0x01;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[1].contain=0x01;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[1].sta    =0x01;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[2].contain=0x02;
	SysState_DeviceSta.SysState_DoorSta.DoorSta[2].sta    =0x01;
	
	SysState_DeviceSta.SysState_TempSysSta.Door_num       =0x01;
	SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].contain=0x00;
	SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].sta    =0x01;
	SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].temp   =TempControl_GetTemp(SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].contain);
	SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].mode   =0x00;
	SysState_DeviceSta.SysState_TempSysSta.DoorSta[0].config =0x00;
	
	SysState_DeviceSta.SysState_LiftSysSta.lift_num=0x02;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[0].contain=0x01;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[0].lift_sta=0x01;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[0].lift_posit=0x00015678;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[0].tarck_sta =0x01;
	
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[1].contain=0x02;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[1].lift_sta=0x01;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[1].lift_posit=0x00015678;
	SysState_DeviceSta.SysState_LiftSysSta.liftsta[1].tarck_sta =0x01;
	
	SysState_DeviceSta.SysState_IrSensor.sensor_num=5;
	SysState_DeviceSta.SysState_IrSensor.IrSta[0].contain_no=0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[0].sensor_no =0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[0].sta       =0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[1].contain_no=0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[1].sensor_no =0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[1].sta       =0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[2].contain_no=0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[2].sensor_no =0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[2].sta       =0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[3].contain_no=0x02;
	SysState_DeviceSta.SysState_IrSensor.IrSta[3].sensor_no =0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[3].sta       =0x01;
	SysState_DeviceSta.SysState_IrSensor.IrSta[4].contain_no=0x02;
	SysState_DeviceSta.SysState_IrSensor.IrSta[4].sensor_no =0x00;
	SysState_DeviceSta.SysState_IrSensor.IrSta[4].sta       =0x01;
	
	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&SysState_DeviceSta,sizeof(SysState_DeviceStaTypeDef));
}

void sysSta_SendBodySta(uint8_t cmd)
{
	SysState_IrSta.sensor_num=0x04;
	SysState_IrSta.IrSta[0].contain_no=0x00;
	SysState_IrSta.IrSta[0].err=0x00;
	SysState_IrSta.IrSta[0].sensor_no=0x00;
	SysState_IrSta.IrSta[0].sta      =0x01;
	
	SysState_IrSta.IrSta[1].contain_no=0x00;
	SysState_IrSta.IrSta[1].err=0x00;
	SysState_IrSta.IrSta[1].sensor_no=0x01;
	SysState_IrSta.IrSta[1].sta      =0x01;
	
	SysState_IrSta.IrSta[2].contain_no=0x01;
	SysState_IrSta.IrSta[2].err=0x00;
	SysState_IrSta.IrSta[2].sensor_no=0x00;
	SysState_IrSta.IrSta[2].sta      =0x01;
	
	SysState_IrSta.IrSta[3].contain_no=0x02;
	SysState_IrSta.IrSta[3].err=0x00;
	SysState_IrSta.IrSta[3].sensor_no=0x00;
	SysState_IrSta.IrSta[3].sta      =0x01;
	
	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&SysState_IrSta,sizeof(SysState_BodyAndIrStaTypeDef));
}

void sysSta_SendIrSta(uint8_t cmd)
{
	SysState_IrSta.sensor_num=0x05;
	SysState_IrSta.IrSta[0].contain_no=0x00;
	SysState_IrSta.IrSta[0].err=0x00;
	SysState_IrSta.IrSta[0].sensor_no=0x00;
	SysState_IrSta.IrSta[0].sta      =0x01;
	
	SysState_IrSta.IrSta[1].contain_no=0x01;
	SysState_IrSta.IrSta[1].err=0x00;
	SysState_IrSta.IrSta[1].sensor_no=0x01;
	SysState_IrSta.IrSta[1].sta      =0x01;
	
	SysState_IrSta.IrSta[2].contain_no=0x01;
	SysState_IrSta.IrSta[2].err=0x00;
	SysState_IrSta.IrSta[2].sensor_no=0x00;
	SysState_IrSta.IrSta[2].sta      =0x01;
	
	SysState_IrSta.IrSta[3].contain_no=0x02;
	SysState_IrSta.IrSta[3].err=0x00;
	SysState_IrSta.IrSta[3].sensor_no=0x00;
	SysState_IrSta.IrSta[3].sta      =0x01;
	
	SysState_IrSta.IrSta[3].contain_no=0x02;
	SysState_IrSta.IrSta[3].err=0x00;
	SysState_IrSta.IrSta[3].sensor_no=0x00;
	SysState_IrSta.IrSta[3].sta      =0x01;
	
	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&SysState_IrSta,sizeof(SysState_BodyAndIrStaTypeDef));
}

void sysSta_SendLiftSta(uint8_t cmd)
{
	SysState_LiftSysTypeDef liftsys_sta;
	liftsys_sta.lift_num=0x02;
	liftsys_sta.liftsta[0].contain=0x01;
	liftsys_sta.liftsta[0].lift_sta=0x01;
	liftsys_sta.liftsta[0].tarck_sta=0x01;
	liftsys_sta.liftsta[0].lift_posit=0x00012340;
	
	liftsys_sta.liftsta[1].contain=0x02;
	liftsys_sta.liftsta[1].lift_sta=0x01;
	liftsys_sta.liftsta[1].tarck_sta=0x01;
	liftsys_sta.liftsta[1].lift_posit=0x00012340;
	
	DeviceProtocol_TxResportMsg(0x15,(uint8_t*)&liftsys_sta,sizeof(SysState_LiftSysTypeDef));
}








