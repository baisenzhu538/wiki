#ifndef __TASK_MANAGE_H
#define __TASK_MANAGE_H
#include "stm32f10x.h"
#include "sys_malloc.h"

#define SYSTEM_MAX_TASKS 20
typedef struct
{
	void (*pTask)(void);
	uint32_t delay;     //
	uint32_t period;    //任务间隔时间
	uint32_t runme;
	uint8_t runmod;    //0定时运行 1循环运行
	uint8_t enable;
	uint8_t receve1;
	uint8_t receve2;
}sTask;


#define NULL 0

void TaskManage_Tasks(void);
uint8_t TaskManage_AddTasks(void (*pFuntion)(void),uint32_t delay,uint32_t period,uint8_t mod);
void TaskManage_DeleteTasks(uint8_t index);
void TaskManage_ClockInit(void);
#endif

