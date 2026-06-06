#ifndef __TIME_TASK_H
#define __TIME_TASK_H
#include "can_stdint.h"
#include "malloc.h"
#define TIMEMODE_AUTOREST     0x00
#define TIMEMODE_NONAUTOREST  0x01

#define TIMETASK_TASKMAXSIZE  CAN_TIMETASK_MAXNUM

typedef struct                            //定时器管理器
{
	uint16_t time_value;  //定时器定时值
  uint16_t count_vaule; //定时器计数值
	uint8_t  overflow;    //溢出状态位
  uint8_t  time_mode;   //工作模式
	uint8_t  callback;
	uint8_t  enable;
	void (*TimeTack_CallBack)(uint8_t);
}TimeTaskTypeDef;

typedef struct _TimeTask_TaskBlockTypeDef//定时器任务块
{
	struct _TimeTask_TaskBlockTypeDef *prior;
	struct _TimeTask_TaskBlockTypeDef *next;
	uint32_t blocknum;
	TimeTaskTypeDef TimeTask;
}TimeTask_TaskBlockTypeDef;

typedef struct                            //定时器链表管理模块
{
	TimeTask_TaskBlockTypeDef *head;     
	TimeTask_TaskBlockTypeDef *tail;
	uint16_t linkdelist_len;
}TimeTask_LinkesListTypeDef;

void TimeTask_Init(void);
uint8_t TimeTask_Cmd(uint8_t timetasknum,uint8_t enable);
uint8_t TimeTask_Add(uint8_t timetasknum,TimeTaskTypeDef *TimeTask);
uint8_t TimeTask_Remove(uint8_t timetasknum);
uint8_t TimeTask_ReadOverflowFlag(uint8_t timetasknum);
uint8_t TimeTask_RestCount(uint8_t timetasknum);
void TimeTask_TaskRun(void);
uint8_t TimeTask_Revamp(uint8_t timetasknum,TimeTaskTypeDef *pTimeTask);

#endif
