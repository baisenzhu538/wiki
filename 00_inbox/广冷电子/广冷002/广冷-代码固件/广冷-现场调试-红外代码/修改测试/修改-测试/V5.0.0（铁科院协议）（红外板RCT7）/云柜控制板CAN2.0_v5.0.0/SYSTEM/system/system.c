#include "system.h"

void test(void)
{
	uint32_t * ptr=NULL;
	*ptr=0x00;
}

void System_Init(void)
{
	TaskManage_ClockInit();	  	//任务管理定时器初始化	
	Ir_Init();
//	WatchDog_Init(3,1875);	//看门狗初始化，1.5秒溢出
			
	TaskManage_AddTasks(Ir_Scan_Task,10,10,0x01);
	


	


}



void System_TaskRun(void)
{
	//任务调度
	TaskManage_Tasks();
	
	//喂狗
//	WatchDog_Drive();
}



