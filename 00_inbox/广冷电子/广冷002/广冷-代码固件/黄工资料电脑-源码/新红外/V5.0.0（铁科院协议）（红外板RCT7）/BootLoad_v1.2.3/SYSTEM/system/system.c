#include "system.h"

void System_Init(void)
{
	TaskManage_ClockInit();//任务管理定时器初始化

	CryogenDrive_Init();   //初始化压缩机驱动
  CanApp_SysInit();      //CAN总线初始化

	TaskManage_AddTasks(TimeTask_TaskRun,5,10,0x00);    //创建CAN定时器任务
	TaskManage_AddTasks(ProtocoStack_RollRun,0,0,0x01); //创建CAN循环扫描任务
	
	TaskManage_AddTasks(CryogenDrive_TaskRun,8,1000,0x00); //压缩机控制任务1s钟执行一次
//	TaskManage_AddTasks(CryogenDrive_IoDrive,0,0,0x01);    //IO输出驱动任务
}



void System_TaskRun(void)
{
	TaskManage_Tasks();
}
