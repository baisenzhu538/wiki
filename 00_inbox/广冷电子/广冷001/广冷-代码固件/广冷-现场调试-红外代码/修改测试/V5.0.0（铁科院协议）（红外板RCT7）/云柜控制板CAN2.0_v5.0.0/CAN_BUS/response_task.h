#ifndef __RESPONSE_TASK_H
#define __RESPONSE_TASK_H
#include "can_stdint.h"
#include "malloc.h"
#include "transport_layer.h"
#include "time_task.h"
#include "funcid_define.h"



//#define RESPONSETASK_MAXSIZE         128
//#define RESPONSETASK_OVERTIME        20  //200ms超时

#define RESPONSETASK_OVERTIMENUM     2   //超时次数重发次数RESPONSETASK_OVERTIMENUM-1
#define RESPONSETASK_ERRNUM          2


void ResponseTask_TaskRun(NodeLinkTypeDef *pLink);
void ResponseTask_TimeCallBack(uint8_t timenum);
void ResponseTask_MsgParsing(TransportCanMsgTypeDef *pRxMsg);
void ResponseTask_SetAskCallBack(void(*pCallBack)(TransportCanMsgTypeDef *pRxMsg));
void ResponseTask_SetExceptionsCallBack(void(*pCallBack)(TransportTaskTypeDef *pTransportTask,uint8_t));
#endif
