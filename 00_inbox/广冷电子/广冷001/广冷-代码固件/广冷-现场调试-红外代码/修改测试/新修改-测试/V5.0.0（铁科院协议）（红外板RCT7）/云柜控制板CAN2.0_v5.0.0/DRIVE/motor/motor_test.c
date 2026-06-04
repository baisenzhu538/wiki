#include "motor_test.h"

//按键进入模式，切换页面
//启动出货任务
//等待出货任务完成
//将出货结果打印到屏幕
//按键退出模式

//连续按2下进入或退出

typedef	struct
{
	u8	mode;
	u8	enable;
	u8	step;
	u8	row;
	u8	list;
	u16	runtime;
	u8	motor_err;
	u8	ir_err;
	u8	reset_enable;
	u8	reset_step;
}MotorTest_TypeDef;

MotorTest_TypeDef	MotorTest;

uint8_t	MotorTest_Get_Mode(void)
{
	return MotorTest.mode;
}

static u8 ir_checkflag=0;
static u8 motor_checkflag=0;

void MotorTest_Test(void)
{
	static u32	time=0;
	
	if(MotorTest.mode == 1)	//自检模式
	{
		if(Sensor_Get_TestButtonSta())
		{
			if(time < 100)
			{
				Sensor_Get_TestButtonFt();
				time++;
			}
			else
			{				
				time = 0;
				
				MotorTest.mode = 3;
				MotorTest.enable = 0;
				MotorTest.step = 0;
				DgusApp_Set_ShowSellReset();
				DgusApp_Set_ClearIrCheck();
				DgusApp_Set_ClearMotorCheck();
				//切换回原页面
				if(CloudProtocol_Get_DeviceState_DoorState())
				{
					DgusApp_Set_GotoPage(9);
				}
				else
				{					
					if(MQTT_Get_Start_Status())
					{			
						if(SysConfig_Get_StoreState())
						{
							if(WirelessModule_ReadRssiSta())
							{
								DgusApp_Set_GotoPage(2);
							}
							else
							{
								DgusApp_Set_GotoPage(3);
							}
						}
						else
						{
							if(SysConfig_Get_QrCodeSize())
							{
								DgusApp_Set_GotoPage(5);
							}
							else
							{
								DgusApp_Set_GotoPage(4);
							}
						}
					}
					else
					{
						DgusApp_Set_GotoPage(0);
					}
					
				}
			}
		}
		else
		{
			time = 0;
		}
	}
	else if(MotorTest.mode == 0)
	{
		if(Sensor_Get_TestButtonSta())
		{
			if(time < 300)
			{
				Sensor_Get_TestButtonFt();
				time++;
			}
			else
			{				
				time = 0;
					
				MotorTest.mode = 2;
				MotorTest.enable = 1;
				MotorTest.step = 0;
				DgusApp_Set_GotoPage(18);
				Sensor_Get_GoodsIrFT(0);
				Sensor_Get_GoodsIrRT(0);				
				ir_checkflag = 0;
				motor_checkflag = 0;
			}
		}
		else
		{
			time = 0;
		}
	}
	else if(MotorTest.mode == 2)
	{
		if(Sensor_Get_TestButtonFt())
		{
			MotorTest.mode = 1;
		}
	}
	else if(MotorTest.mode == 3)
	{
		if(Sensor_Get_TestButtonFt())
		{
			MotorTest.mode = 0;
		}
	}
	
}

//显示接口包含行列号，找到对应位置显示。


void MotorTest_Task(void)
{
		
	MotorTest_Test();
	
	if(MotorTest.enable)
	{
		if(!ir_checkflag)
		{
			if(Sensor_Read_GoodsIrRt(0)
				||Sensor_Read_GoodsIrFt(0))
			{
				DgusApp_Set_ShowIrCheck(1);
				ir_checkflag = 1;
			}
		}

		
		switch(MotorTest.step)
		{
			case 0:
			{
				MotorTest.list = 0;
				MotorTest.row = 0;
				MotorTest.step = 1;
			}
			break;
			case 1://执行货道动作
			{			
				if(MotorDrive_SetBit(MotorTest.list,MotorTest.row))
					MotorTest.step = 2;
			}
			break;
			case 2://等待电机启动
			{
				if(MotorDrive_GetRunState()==2)
				{
					MotorTest.step = 3;
				}
			}
			break;
			case 3://等待货道动作完成
			{
				if(MotorDrive_GetRunState() == 0)
				{
					if(MotorDrive_GetRunErrState())
					{
						MotorTest.motor_err = 1;
						MotorTest.step = 7;
					}
					else
					{
						if(MotorDrive_ReadPositErr())
						{
							MotorTest.step = 4;
						}
						else
						{
							MotorTest.motor_err = 0;
							DgusApp_Set_ShowMotorCheck(1);
							motor_checkflag = 1;
							MotorTest.step = 7;
						}
					}		
				}
			}
			break;
			case 4://
			{
				if(MotorDrive_SetBit(MotorTest.list,MotorTest.row))
					MotorTest.step = 5;
			}
			break;
			case 5://
			{
				if(MotorDrive_GetRunState()==2)
				{
					MotorTest.step = 6;
				}
			}
			break;
			case 6:
			{
				if(MotorDrive_GetRunState() == 0)
				{
					if(MotorDrive_GetRunErrState())
					{
						MotorTest.motor_err = 1;
						MotorTest.step = 7;
					}
					else
					{
						MotorTest.motor_err = 0;
						DgusApp_Set_ShowMotorCheck(1);
						motor_checkflag = 1;
						MotorTest.step = 7;
					}
				}
			}
			break;
			case 7://打印出货结果
			{
				DgusApp_Set_ShowSellTest(MotorTest.row,MotorTest.list,MotorTest.motor_err);
				MotorTest.step = 8;
			}
			break;
			case 8://确定要操作的货道
			{
				if(MotorTest.row == 0)
				{
					if(MotorTest.list<3)
					{
						MotorTest.list++;
					}
					else
					{
						MotorTest.list = 0;
						MotorTest.row++;
					}
					MotorTest.step = 1;
				}
				else if(MotorTest.row == 1)
				{
					if(MotorTest.list<10)
					{
						MotorTest.list++; 
					}
					else
					{
						MotorTest.list = 0;
						MotorTest.row++;
					}
					MotorTest.step = 1;
				}
				else if(MotorTest.row == 2)
				{
					if(MotorTest.list<10)
					{
						MotorTest.list++;
					}
					else
					{
						MotorTest.list = 0;
						MotorTest.row++;
					}
					MotorTest.step = 1;
				}
				else if(MotorTest.row == 3)
				{
					if(MotorTest.list<10)
					{
						MotorTest.list++;
					}
					else
					{
						MotorTest.list = 0;
						MotorTest.row++;
					}
					MotorTest.step = 1;
				}
				else if(MotorTest.row == 4)
				{
					if(MotorTest.list<5)
					{
						MotorTest.list++;
					}
					else
					{
						MotorTest.list = 0;
						MotorTest.row++;
					}
					MotorTest.step = 1;
				}
				else
				{
					
					if(!ir_checkflag)
					{
						DgusApp_Set_ShowIrCheck(0);
					}
					
					if(!motor_checkflag)
					{
						DgusApp_Set_ShowMotorCheck(0);
					}
					MotorTest.row = 0;
					MotorTest.list = 0;
					MotorTest.step = 0;
					MotorTest.enable = 0;
				}
			}
			break;
		}
	}
	else
	{
		MotorTest.row = 0;
		MotorTest.list = 0;
		MotorTest.step = 0;
	}
}