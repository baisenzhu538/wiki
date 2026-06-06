#ifndef __TRANSPORT_LINKESLIST_H
#define __TRANSPORT_LINKESLIST_H

#include "can_stdint.h"
#include "data_struct.h"
#include "malloc.h"
#include "time_task.h"
#include "canbus_config.h"

#define TRANSPORT_CALLBACKTIME      1//10模式调用
#define TRANSPORT_CALLBACKTIMENUM   0x02

#define TRANSPORT_LINKES_MAXLEN     CAN_TX_LINKLEN
#define TRANSPORT_OUTTIME           CAN_RESPONSE_OUTTIME //100ms
#define TRANSPORT_OVERTIMENUM       2

#define TransportTask_GetTxMsgCancel(p)   (p->TransportTaskManage.TransportCancel)          //获取取消发送标志位
#define TransportTask_SetTxMsgCancel(p)   (p->TransportTaskManage.TransportCancel=0x01)
#define TransportTask_ResetTxMsgCancel(p) (p->TransportTaskManage.TransportCancel=0x00)
#define TransportTask_SetTxMsgReSend(p)   (p->TransportTaskManage.TransportCancel=0x02)
#define TransportTask_ResetTxMsgReSend(p)   (p->TransportTaskManage.TransportCancel=0x00)

#define TransportTask_GetTxMsgAsk(p)      (p->TxCanMsg.TransportMsgFilter.Ack)              //获取报文响应位

#define TransportTask_GetTxMsgState(p)    (p->TransportTaskManage.TransportState)
#define TransportTask_ResetTxMsgState(p)  (p->TransportTaskManage.TransportState=0x00)      //设置传输状态位为0x00，此时为发送结束
#define TransportTask_SetTxMsgState(p)    (p->TransportTaskManage.TransportState=0x01)      //设置传输状态位为0x01，此时为待发送状态

#define TransportTask_GetTxMsgDataAddr(p) (p->TxCanMsg.TransportMsgData.Data)
#define TransportTask_GetTxMsgDataLen(p)  (p->TxCanMsg.TransportMsgData.DataSize)

#define TransportTask_GetOverTimeFlag(p)  (p->TransportTaskManage.OverTimeFlag)
#define TransportTask_SetOverTimeFlag(p)  (p->TransportTaskManage.OverTimeFlag=0x01)
#define TransportTask_ResetOverTimeFlag(p)(p->TransportTaskManage.OverTimeFlag=0x00)

#define TransportTask_GetOverTimeNum(p)   (p->TransportTaskManage.OverTimeNum)
#define TransportTask_GetErrNum(p)        (p->TransportTaskManage.ErrNum)
#define TransportTask_AddErrNum(p)        (p->TransportTaskManage.ErrNum++)

#define TransportTask_GetTxMsgFuncId(p)   (p->TxCanMsg.TransportMsgFilter.FuncID)

typedef struct 
{
  uint32_t TimeCount      :8;   
	uint32_t OverTimeNum    :8;//超时计时
	uint32_t ErrNum         :8;
	uint32_t OverTimeFlag   :4;//溢出标志位
	uint32_t TransportState :2;
	uint32_t TransportCancel:2;// 0x00本次发送正常 0x01 发送任务取消 0x02 本次发送取消，并重新发送 
}TransportTaskManageTypeDef;


typedef struct 
{
  TransportCanMsgTypeDef     TxCanMsg;
	TransportTaskManageTypeDef TransportTaskManage;
}TransportTaskTypeDef;


typedef struct _TransportTaskBlockTypeDef
{
	struct _TransportTaskBlockTypeDef *prior;
	struct _TransportTaskBlockTypeDef *next;
	TransportTaskTypeDef              TransportTask;
}TransportTaskBlockTypeDef;

typedef struct
{
	TransportTaskBlockTypeDef *head;
	TransportTaskBlockTypeDef *tail;
	uint32_t linkdelist_len;
}TransportTask_LinkesListTypeDef;




void TransportTask_LinkesListInit(void);
void TransportTask_BlockInit(TransportTaskBlockTypeDef *pTaskBlock);

uint8_t TransportTask_RemoveLinkedList(MsgFilterTypeDef *pTransportTaskFilter);
uint8_t TransportTask_AddLinkedList(TransportTaskTypeDef *pTransportTask);

void TransportTask_BlockInit(TransportTaskBlockTypeDef *pTaskBlock);
TransportTaskTypeDef  *TransportTask_GetTransportTask(void);
TransportTaskTypeDef  *TransportTask_GetOverTimeTask(void);
uint8_t TransportTask_RemoveTask(TransportTaskTypeDef *pTransportTask);
TransportTaskTypeDef *TransportTask_TraverseTaskAddr(MsgFilterTypeDef *pTransportTaskFilter);
TransportTaskBlockTypeDef *TransportTask_GetLinkesListHead(void);
void TransportTask_RemoveAllTask(void);
#endif
