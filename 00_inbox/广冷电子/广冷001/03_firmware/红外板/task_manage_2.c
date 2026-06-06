#include "task_manage.h"

sTask SystemTask[SYSTEM_MAX_TASKS];


void TaskManage_ClockInit(void)
{
	SysTick_CLKSourceConfig(SysTick_CLKSource_HCLK_Div8);
	SysTick->CTRL|=SysTick_CTRL_TICKINT_Msk;   	//开启SYSTICK中断
	SysTick->LOAD=9000; 						            //每1ms定时
	SysTick->CTRL|=SysTick_CTRL_ENABLE_Msk;   	//开启SYSTICK    
}

uint8_t TaskManage_AddTasks(void (*pFuntion)(void),uint32_t delay,uint32_t period,uint8_t mod)
{
	uint8_t i_index;
	for(i_index=0;i_index<SYSTEM_MAX_TASKS;i_index++)
	{
		if(SystemTask[i_index].pTask==NULL)
		{
			SystemTask[i_index].pTask=pFuntion;
			SystemTask[i_index].enable=0x01;
			SystemTask[i_index].delay=delay;
			SystemTask[i_index].period=period;
			SystemTask[i_index].runmod=mod;
			SystemTask[i_index].runme=0;
			return i_index;
		}
	}
	return 0xFF;
}

void TaskManage_DeleteTasks(uint8_t index)
{
  SystemTask[index].pTask=NULL;
	SystemTask[index].enable=0;
	SystemTask[index].delay=0;
	SystemTask[index].period=0;
	SystemTask[index].runmod=0;
	SystemTask[index].runme=0;
}

void TaskManage_Updata(void)
{
	uint8_t i_index;
	for(i_index=0;i_index<SYSTEM_MAX_TASKS;i_index++)
	{
		if((SystemTask[i_index].runmod==0x00)&&(SystemTask[i_index].enable==0x01))
		{
			if(SystemTask[i_index].runme==0)
			{
				if(SystemTask[i_index].delay>0)
				 SystemTask[i_index].delay--;
				if(SystemTask[i_index].delay==0)
				{
					SystemTask[i_index].runme=0x01;
					if(SystemTask[i_index].period)
					{
						SystemTask[i_index].delay=SystemTask[i_index].period;
					}
				}

		  }
		}
	}
}

void TaskManage_Tasks(void)
{
	uint8_t i_index;
	for(i_index=0;i_index<SYSTEM_MAX_TASKS;i_index++)
	{
		if((SystemTask[i_index].enable==0x01)&&(SystemTask[i_index].pTask!=NULL))
		{
			if(SystemTask[i_index].runmod==0x01)
			{
				(*SystemTask[i_index].pTask)();
			}
			else if(SystemTask[i_index].runmod==0x00)//时间运行模式
			{
				if(SystemTask[i_index].runme)
				{
					(*SystemTask[i_index].pTask)();
					SystemTask[i_index].runme=0x00;
					if(SystemTask[i_index].period==0)//单次运行，删除任务
					{
						TaskManage_DeleteTasks(i_index);
					}
				}
			}
		}
	}
}



void SysTick_Handler(void)
{
	TaskManage_Updata();
}
