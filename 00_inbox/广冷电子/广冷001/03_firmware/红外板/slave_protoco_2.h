#ifndef __SLAVE_PROTOCO_H
#define __SLAVE_PROTOCO_H

#include "transport_layer.h"
#include "time_task.h"
#include "response_task.h"
#include "funcid_define.h"
#include "index_table.h"

#define HEART_OVERTIME_TIMENUM          0x04
#define HEART_SENDTIME_TIMENUM          0x05
//#define CONNECT_SENDTIME_TIMENUM        0x06 
//#define IDCHECK_SENDTIME_TIMENUM        0x07

#define HEART_OVERTIME                  CAN_SLAVEHEART_OVERTIME//3s超时
#define HEART_SENDTIME                  CAN_SLAVEHEART_TXTIME//1s发送一个心跳
//#define CONNECT_SENDTIME                100//1s发送一个连接申请报文
//#define IDCHECK_SENDTIME                10// 0.1s发送一个ID检测报文

//#define IDCHECK_MAXNUM               2

void ProtocoStack_Init(void);
void ProtocoStack_RollRun(void);
void ProtocoStack_SendMsg(uint8_t DestMacID,uint8_t FuncID,uint8_t SourceID,uint8_t ask);
void SlaveProtoco_SetCallBack(void (*p)(TransportCanMsgTypeDef *));
#endif
