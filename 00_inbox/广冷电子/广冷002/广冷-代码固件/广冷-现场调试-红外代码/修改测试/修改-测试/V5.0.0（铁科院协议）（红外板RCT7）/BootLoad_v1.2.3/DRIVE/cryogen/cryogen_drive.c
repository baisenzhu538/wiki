#include "cryogen_drive.h"
CryogenDriveStateTypeDef CryogenDriveState;
CryogenDriveInfoTypeDef  CryogenDriveInfo;



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
	CryogenDriveState.runsta.current_temp=TempSensor_GetTempVaule(0x00);//读取温度值
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
	if((CryogenDriveState.runsta.state_bit.cryogen_state)&&(CryogenDriveState.runsta.state_bit.comp_state==0)&&(CryogenDriveState.runsta.state_bit.temp_state==1))//压缩机停止工作后冷凝器风扇循环
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
	if((CryogenDriveState.cStartTime==CryogenDriveInfo.starttime)&&(CryogenDriveState.runsta.state_bit.temp_state==0))//达到启动时间且温度未达到设定值，开启冷凝器风扇和压缩机
	{
		CryogenDrive_SetComp(ENABLE);
		CryogenDrive_SetFan(ENABLE);
		CryogenDriveState.cStartTime=0;
		CryogenDriveState.cRunTime=0;     //清0计数
		CryogenDriveState.cRecoveTime=0;
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
		if(CryogenDriveState.cRunTime<CryogenDriveInfo.longtime)
		 CryogenDriveState.cRunTime++;
		else
		{
			if(CryogenDriveState.cRecoveTime<CryogenDriveInfo.recovetime)
			 CryogenDriveState.cRecoveTime++;
			else
			 CryogenDrive_CryogenStart();    //启动压缩机
		}
		
		if((CryogenDriveState.cRunTime==CryogenDriveInfo.longtime)||(CryogenDriveState.runsta.state_bit.temp_state==1))//达到最高运行时间或者达到设定温度停止压缩机
		{
			CryogenDrive_SetComp(DISABLE);
		}
  }
	else
	{
    CryogenDrive_CryogenStart();          //启动机组
  }
}

void CryogenDrive_CryogenControl(void)
{
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
	CryogenDriveInfo.set.temp=4;
	CryogenDriveInfo.set.mode=CRYOGEN_COLDMODE;
	CryogenDriveInfo.set.enable_bit.cryogen_en=ENABLE;
	CryogenDriveInfo.cycletime =CRYOGEN_CYCLETIME;
	CryogenDriveInfo.longtime  =CRYOGEN_LONGTIME;
	CryogenDriveInfo.recovetime=CRYOGEN_RECOVETIME;
	CryogenDriveInfo.fwv_ahead =FWV_AHEADTTIME;
	CryogenDriveInfo.starttime =CRYOGEN_STARTTIME;
	CompressorControl_init();
	TempSensor_Init();
}

//1ms调用一次
void CryogenDrive_IoDrive(void)
{
	if(CryogenDriveInfo.set.enable_bit.comp_en!=CryogenDriveState.runsta.state_bit.comp_state)
	{
		CryogenDriveState.runsta.state_bit.comp_state=CryogenDriveInfo.set.enable_bit.comp_en;
		CompressorControl_SetComp(CryogenDriveInfo.set.enable_bit.comp_en);
	}
	if(CryogenDriveInfo.set.enable_bit.fan_en!=CryogenDriveState.runsta.state_bit.fan_state)
	{
		CryogenDriveState.runsta.state_bit.fan_state=CryogenDriveInfo.set.enable_bit.fan_en;
		CompressorControl_SetFan(CryogenDriveInfo.set.enable_bit.fan_en);
	}
	if(CryogenDriveInfo.set.enable_bit.fwv_en!=CryogenDriveState.runsta.state_bit.fwv_state)
	{
		CryogenDriveState.runsta.state_bit.fwv_state=CryogenDriveInfo.set.enable_bit.fwv_en;
		CompressorControl_SetFwv(CryogenDriveInfo.set.enable_bit.fwv_en);
	}
	if(CryogenDriveInfo.set.enable_bit.spare_en!=CryogenDriveState.runsta.state_bit.spare_state)
	{
		CryogenDriveState.runsta.state_bit.spare_state=CryogenDriveInfo.set.enable_bit.spare_en;
		CompressorControl_SetSpare(CryogenDriveInfo.set.enable_bit.spare_en);
	}
}
//1s定时一次
//制冷系统任务
void CryogenDrive_TaskRun(void)
{
	CryogenDrive_TempScan();
	CryogenDrive_FanControl();
	CryogenDrive_CryogenControl();
//	CryogenDrive_IoDrive();
}




