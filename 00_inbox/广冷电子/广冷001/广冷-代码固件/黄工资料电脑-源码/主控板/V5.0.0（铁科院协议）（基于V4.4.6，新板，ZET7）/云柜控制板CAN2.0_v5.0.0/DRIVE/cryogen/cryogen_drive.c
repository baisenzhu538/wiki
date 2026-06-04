/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 压缩机制冷驱动模块
*	文件名称 : crygen_drive.c
*	版    本 : V1.0
*	说    明 : 1.实现对压缩机和蒸发器风扇的逻辑控制
*            2.实现制冷加热模式的切换
* 
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2019-03-18  Waves    修复以往bug，正式发布
*   V1.1    2019-04-02  Waves    修复达到设定温度后需等待运行周期结束才启动制冷问题
                                 增加int8_t CryogenDrive_GetDevTemp(void) 获取当前温度
																 增加void CryogenDrive_SetDriveInfo(uint8_t ensta,uint8_t mode,uint8_t temp) 设置制冷工作参数
		V1.2    2019-04-13  Waves    增加湿度采集
*********************************************************************************************************
*/
#include "cryogen_drive.h"
#include "dgus_app.h"
#include "motor_test.h"

CryogenDriveStateTypeDef CryogenDriveState;
CryogenDriveInfoTypeDef  CryogenDriveInfo;

uint8_t CryogenDrive_GetDevHumid(void)
{
	return CryogenDriveState.runsta.current_humid;
}
int8_t CryogenDrive_GetDevTemp(void)
{
	return CryogenDriveState.runsta.current_temp;
}
void CryogenDrive_SetDriveInfo(uint8_t ensta,uint8_t mode,uint8_t temp)
{
	CryogenDriveInfo.set.enable_bit.cryogen_en=ensta;
	CryogenDriveInfo.set.mode      =mode;
	CryogenDriveInfo.set.temp      =temp;
}

void CryogenDrive_SetComp(FunctionalState NewState)
{
	CryogenDriveInfo.set.enable_bit.comp_en=NewState;
	CryogenDriveState.runsta.state_bit.comp_state=CryogenDriveInfo.set.enable_bit.comp_en;
	CompressorControl_SetComp(CryogenDriveInfo.set.enable_bit.comp_en);
}
void CryogenDrive_SetFan(FunctionalState NewState)
{
	CryogenDriveInfo.set.enable_bit.fan_en=NewState;
	CryogenDriveState.runsta.state_bit.fan_state=CryogenDriveInfo.set.enable_bit.fan_en;
	CompressorControl_SetFan(CryogenDriveInfo.set.enable_bit.fan_en);
}
void CryogenDrive_SetFwv(FunctionalState NewState)
{
	CryogenDriveInfo.set.enable_bit.fwv_en=NewState;
	CryogenDriveState.runsta.state_bit.fwv_state=CryogenDriveInfo.set.enable_bit.fwv_en;
	CompressorControl_SetFwv(CryogenDriveInfo.set.enable_bit.fwv_en);
}
void CryogenDrive_SetSpare(FunctionalState NewState)
{
	CryogenDriveInfo.set.enable_bit.spare_en=NewState;
	CryogenDriveState.runsta.state_bit.spare_state=CryogenDriveInfo.set.enable_bit.spare_en;
	CompressorControl_SetSpare(CryogenDriveInfo.set.enable_bit.spare_en);
}

//循环读取温度值
void CryogenDrive_TempScan(void)
{
	CryogenDriveState.runsta.current_humid=Sensor_GetHumid();//读取温度值
	if(CryogenDriveState.runsta.current_humid>100||CryogenDriveState.runsta.current_humid<5)
	{
		CryogenDriveState.runsta.err|=0x02;
	}
	else
	{
		if(CryogenDriveState.runsta.current_humid)
		CryogenDriveState.runsta.err&=(~0x02);
	}
	
	if(Sensor_GetTemp()==0xFF)//传感器故障
	{
		CryogenDriveState.runsta.err|=0x01;
	 if(CryogenDriveInfo.set.mode==CRYOGEN_COLDMODE)
		CryogenDriveState.runsta.current_temp=0;
	 else
		CryogenDriveState.runsta.current_temp=0xFF;
	}
	else
	{
	 CryogenDriveState.runsta.err&=(~0x01);
	 CryogenDriveState.runsta.current_temp=Sensor_GetTemp();//读取温度值
	}
	
	if(CryogenDriveInfo.set.mode==0x00)
	{
		if((CryogenDriveState.runsta.current_temp<CryogenDriveInfo.set.temp)||(CryogenDriveState.runsta.current_temp==CryogenDriveInfo.set.temp))//温度达到设定值
		{
			CryogenDriveState.runsta.state_bit.temp_state=0x01;
		}
		else if(CryogenDriveState.runsta.current_temp>(CryogenDriveInfo.set.temp+TEMP_DEVIATION))
		{
			CryogenDriveState.runsta.state_bit.temp_state=0x00;
		}
	}
	else
	{
		if((CryogenDriveState.runsta.current_temp>CryogenDriveInfo.set.temp)||(CryogenDriveState.runsta.current_temp==CryogenDriveInfo.set.temp))
		{
			CryogenDriveState.runsta.state_bit.temp_state=0x01;
		}
		else if(CryogenDriveState.runsta.current_temp<(CryogenDriveInfo.set.temp-TEMP_DEVIATION))
		{
			CryogenDriveState.runsta.state_bit.temp_state=0x00;
		}
	}
}

void CryogenDrive_FanControl(void)
{
	if((CryogenDriveState.runsta.state_bit.cryogen_state)
		 &&(CryogenDriveState.runsta.state_bit.comp_state==0)
	   &&(CryogenDriveState.runsta.state_bit.temp_state==1)
	  )//压缩机停止工作后冷凝器风扇循环,温度达到压缩机停止，风扇循环工作，如压缩机停止温度未达到，风扇持续工作
	{
		if(CryogenDriveState.cFanTime<CryogenDriveInfo.cycletime)
		 CryogenDriveState.cFanTime++;
		else
		{
			CryogenDriveState.cFanTime=0;
			if(CryogenDriveState.runsta.state_bit.fan_state)
				CryogenDrive_SetFan(DISABLE);
			else
				CryogenDrive_SetFan(ENABLE);
		}
	}
}
//制冷启动
void CryogenDrive_CryogenStart(void)
{
	if(CryogenDriveState.cStartTime<CryogenDriveInfo.starttime)
	 CryogenDriveState.cStartTime++;
	if((CryogenDriveState.cStartTime==CryogenDriveInfo.starttime)
		 &&(CryogenDriveState.runsta.state_bit.temp_state==0)
	  )//达到启动时间且温度未达到设定值，开启冷凝器风扇和压缩机
	{
		CryogenDrive_SetComp(ENABLE);
		CryogenDrive_SetFan(ENABLE);
		CryogenDriveState.cStartTime=0;
		CryogenDriveState.cRunTime=0;     //清0计数
		CryogenDriveState.cRecoveTime=0;
		CryogenDriveState.cFanTime   =0;
		CryogenDriveState.runsta.state_bit.forst_staste=0; //清楚化霜标志位
		CryogenDriveState.runsta.state_bit.cryogen_state=1;//置位机组工作状态
	}
	else if(CryogenDriveState.cStartTime==(CryogenDriveInfo.starttime-CryogenDriveInfo.fwv_ahead))
	{
		if(CryogenDriveInfo.set.mode)
		{
		 CryogenDrive_SetSpare(DISABLE);//关闭门加热功能
		 CryogenDrive_SetFwv(ENABLE);//提前开启四通阀
		}
		else
		{
		 CryogenDrive_SetSpare(ENABLE);//打开门加热功能
		 CryogenDrive_SetFwv(DISABLE);
		}
	}
}

//制冷控制程序，内部调用
void CryogenDrive_ColdAndHotTask(void)
{
	if(CryogenDriveState.runsta.state_bit.cryogen_state)//机组已经在工作状态中
	{
		if(CryogenDriveState.runsta.state_bit.temp_state==0)//未达到设定温度
		{
			if(CryogenDriveState.runsta.state_bit.comp_state||CryogenDriveState.runsta.state_bit.forst_staste)//检测压缩机为启动状态或者化霜中
			{
				if(CryogenDriveState.cRunTime<CryogenDriveInfo.longtime)
				{
				 CryogenDriveState.cRunTime++;
				}
				else if(CryogenDriveState.cRunTime==CryogenDriveInfo.longtime
					      &&CryogenDriveState.runsta.state_bit.forst_staste==0)//工作超时，关闭压缩机进入化霜周期
				{
					CryogenDrive_SetComp(DISABLE);
					CryogenDriveState.cRecoveTime=0;
					CryogenDriveState.runsta.state_bit.forst_staste=1;//置位化霜标志
				}
				else//进入化霜周期
				{
					if(CryogenDriveState.cRecoveTime<CryogenDriveInfo.recovetime)
					 CryogenDriveState.cRecoveTime++;
					else
					 CryogenDrive_CryogenStart();    //启动压缩机
				}
		  }
			else
			{
				CryogenDrive_CryogenStart();    //启动压缩机
			}
	  }
		else //达到设定温度
		{
			CryogenDriveState.runsta.state_bit.forst_staste=0x00;//清除化霜标志位
			CryogenDrive_SetComp(DISABLE);//关闭压缩机
		}
  }
	else//制冷机组未启动，执行启动程序
	{
    CryogenDrive_CryogenStart();          //启动机组
  }
}

void CryogenDrive_CryogenControl(void)
{
	if(ElcLock_ReadLockState()||(MotorTest_Get_Mode() == 1))
		CryogenDriveInfo.set.enable_bit.cryogen_en = 1;
	else
		CryogenDriveInfo.set.enable_bit.cryogen_en = 0;
	
	if(CryogenDriveInfo.set.enable_bit.cryogen_en)//制冷工作使能位
	{ 
		if(CryogenDriveInfo.set.mode!=CryogenDriveState.runsta.currrent_mode)//模式切换
		{
			CryogenDriveState.runsta.currrent_mode=CryogenDriveInfo.set.mode;
			CryogenDriveState.cStartTime=0;
			CryogenDriveState.runsta.state_bit.cryogen_state=0;//机组停止工作
			CryogenDrive_SetComp(DISABLE);    //关闭压缩机
			CryogenDrive_SetFan(DISABLE);
		}
		else
		{
			CryogenDrive_ColdAndHotTask();
		}
	}
	else
	{
		if(CryogenDriveState.runsta.state_bit.cryogen_state)//开启状态切换到关闭状态，关闭压缩机，关闭冷凝器风扇
		{
			CryogenDriveState.cStartTime=0;
			CryogenDriveState.runsta.state_bit.cryogen_state=0;
			CryogenDrive_SetComp(DISABLE);
			CryogenDrive_SetFan(DISABLE);
			CryogenDrive_SetSpare(DISABLE);//关闭门加热功能
		}
	}
}

void CryogenDrive_Init(void)
{
	CryogenDriveInfo.set.temp=8;
	CryogenDriveInfo.set.mode=CRYOGEN_COLDMODE;
	CryogenDriveInfo.set.enable_bit.cryogen_en=ENABLE;
	CryogenDriveInfo.cycletime =CRYOGEN_CYCLETIME;
	CryogenDriveInfo.longtime  =CRYOGEN_LONGTIME;
	CryogenDriveInfo.recovetime=CRYOGEN_RECOVETIME;
	CryogenDriveInfo.fwv_ahead =FWV_AHEADTTIME;
	CryogenDriveInfo.starttime =CRYOGEN_STARTTIME;
	CompressorControl_init();
}

void CryogenDrive_ShowTemp(void)
{
	static u8 cnt = 0;
	static u8 last_temp=0;
	static u8 last_temp2=0;	
	static u8 last_err=0;
	static int	last_devicesta=0;
	
	
	if(cnt<10)
	{
		cnt++;
	}
	else
	{
		cnt = 0;		
		
		
		
		if(last_temp != Sensor_GetTemp()
			|| last_temp2 != Sensor_GetTemp2()
			|| last_devicesta != CloudProtocol_Get_DeviceState())
		{
			last_devicesta = CloudProtocol_Get_DeviceState();
			last_temp = Sensor_GetTemp();
			last_temp2 = Sensor_GetTemp2();
			
			if(Sensor_GetTemp() == 0xFF)
			{
				DgusApp_Set_Temp(0);
				
				if(Sensor_GetTemp2() == 0xFF)
				{
					DgusApp_Set_Temp2(0);
					
					if(CloudProtocol_Get_DeviceState() == 0)
					{
						DgusApp_Set_ShowSystemErrorInfo(154);
					}
				}
				else
				{
					DgusApp_Set_Temp2(Sensor_GetTemp2());
					
					if(CloudProtocol_Get_DeviceState() == 0)
					{
						DgusApp_Set_ShowSystemErrorInfo(152);
					}
				}
			}
			else
			{
				DgusApp_Set_Temp(Sensor_GetTemp());
				
				if(Sensor_GetTemp2() == 0xFF)
				{
					DgusApp_Set_Temp2(0);
					
					if(CloudProtocol_Get_DeviceState() == 0)
					{
						DgusApp_Set_ShowSystemErrorInfo(153);
					}
				}
				else
				{
					DgusApp_Set_Temp2(Sensor_GetTemp2());
					
					if(CloudProtocol_Get_DeviceState() == 0)
					{
						DgusApp_Set_ShowSystemErrorInfo(151);
					}
				}
			}
		}
		
	}
}

//1s定时一次
//制冷系统任务
void CryogenDrive_TaskRun(void)
{
	CryogenDrive_TempScan();
	CryogenDrive_FanControl();
	CryogenDrive_CryogenControl();
	CryogenDrive_ShowTemp();
}


