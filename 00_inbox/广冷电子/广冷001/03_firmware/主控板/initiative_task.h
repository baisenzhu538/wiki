#ifndef __INITIATIVE_TASK_H
#define __INITIATIVE_TASK_H
#include "can_stdint.h"
#include "malloc.h"
#include "time_task.h"
#include "transport_queue.h"
#include "slave_protoco.h"

#define INITIATIVETASK_TIMENUM    0x03
#define INITIATIVETASK_TASKMAXSIZE CAN_TRGGERTASK_MAXNUM

#define INITIATIVETASK_CYCLECLASS     0x00
#define INITIATIVETASK_THRESHOLDCLASS 0x01
#define INITIATIVETASK_STATECLASS     0x02

#define INITIATIVETASK_TRIGGERACK     0x00//状态触发与阈值触发是否响应，响应该值为0，不响应为1
typedef struct
{
	uint8_t  cycle_enable;
	uint8_t  threshold_enable;
	uint8_t  state_enable;
	
	uint8_t  overtimeflag:4;//超市标志
	uint8_t  cycleinit:1;
	uint8_t  thresholdinit:1;
	uint8_t  stateinit:1;
	uint8_t  receve :1;
	
	uint16_t timecount;     //定时计数
	uint16_t time;          //定时时间
	uint32_t last;          //最后保存变量值
	uint32_t upper_limit;
	uint32_t lower_limit;                      
}TriggerManageTypeDef;

typedef struct
{
 MsgFilterTypeDef      InitiativeTaskFilter;
 TriggerManageTypeDef  TriggerManage;                
}InitiativeTaskTypeDef;

typedef struct _InitiativeTaskBlockTypeDef
{
	struct _InitiativeTaskBlockTypeDef *prior;
	struct _InitiativeTaskBlockTypeDef *next;
  InitiativeTaskTypeDef InitiativeTask;
}InitiativeTask_BlockTypeDef;


typedef struct _InitiativeTask_LinkesListTypeDef                     //链表管理模块
{
	InitiativeTask_BlockTypeDef *head;     
	InitiativeTask_BlockTypeDef *tail;
	uint16_t linkdelist_len;
	uint16_t taskstate;
}InitiativeTask_LinkesListTypeDef;


typedef struct
{
 void (*InitiativeTask_CycleCallBack)(InitiativeTaskTypeDef*);
 void (*InitiativeTask_ThresholdCallBack)(InitiativeTaskTypeDef*);
 void (*InitiativeTask_StateCallBack)(InitiativeTaskTypeDef*);
}InitiativeTask_CallBackTypeDef;

//InitiativeTask_BlockTypeDef *InitiativeTask_GetAddr(MsgFilterTypeDef *pInitiativeTaskFilter);
//uint8_t InitiativeTask_Add(InitiativeTaskTypeDef *pInitiativeTask);
//uint8_t InitiativeTask_Remove(MsgFilterTypeDef *pInitiativeTaskFilter);

void InitiativeTask_LinkesListInit(InitiativeTask_CallBackTypeDef *pInitiativeTask_CallBack);
void InitiativeTask_TaskRun(NodeLinkTypeDef *pLinkManage);
void InitiativeTask_TimeRun(uint8_t timetasknum);
void InitiativeTask_RestInitFlag(void);
uint8_t InitiativeTask_SetState(uint8_t SourceID);
uint8_t InitiativeTask_SetThreshold(uint8_t SourceID,uint32_t low,uint32_t up);
uint8_t InitiativeTask_SetCycle(uint8_t SourceID,uint16_t time);
void InitiativeTask_RenewTable(void);
void InitiativeTask_UpdataLast(uint8_t SourceID);
#endif
