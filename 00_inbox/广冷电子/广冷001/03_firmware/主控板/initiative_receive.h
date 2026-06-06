#ifndef __INITIATIVE_RECEIVE_H
#define __INITIATIVE_RECEIVE_H
#include "data_struct.h"
#include "malloc.h"
#include "transport_layer.h"
#include "funcid_define.h"
#include "node_info.h"

#define INITIATIVERECEIVE_MAXSIZE CAN_TRGGERRECEVICE_MAXNUM
#define INITIATIVERECEIVE_TIMENUM   0x0A

typedef struct
{
	uint8_t  can_nodeid;  //节点id
	uint8_t  sourceid;    //资源节点地址
	
	uint8_t  cycleinit     :1;  //循环触发初始化0未初始化1初始化
	uint8_t  thresholdinit :1;  //阈值触发初始化状态位
	uint8_t  stateinit     :1;  //状态触发初始化状态位
	uint8_t  connectflag   :1;  //节点连接状态
	uint8_t  receve        :4;  //保留位
	
	uint8_t  timeoverflag;
	
	uint8_t  trigger_receive;  //触发接收
	uint8_t  cycle_enable;     //定时触发
	uint8_t  threshold_enable; //阈值触发
	uint8_t  state_enable;     //状态触发
	
	uint16_t timecount;     //定时计数
	uint16_t time;          //定时时间
	uint32_t last;          //最后保存变量值
	uint32_t upper_limit;
	uint32_t lower_limit; 

  void *   data;
}InitiativeReceiveTypeDef;



typedef struct _InitiativeReceiveBlockTypeDef
{
 struct _InitiativeReceiveBlockTypeDef *prior;
 struct _InitiativeReceiveBlockTypeDef *next;
 InitiativeReceiveTypeDef              ReceiveInfo;
}InitiativeReceiveBlockTypeDef;

typedef struct 
{
 InitiativeReceiveBlockTypeDef *head;
 InitiativeReceiveBlockTypeDef *tail;
 uint32_t   tablesize;
}InitiativeReceiveTableTypeDef;

void InitiativeReceive_TableInit(void);
void InitiativeReceive_ReceiveTask(TransportCanMsgTypeDef *pRxMsg);
uint8_t InitiativeReceive_SetTrigeerRecive(uint8_t nodeid,uint8_t sourceid,void *addr);
void InitiativeReceive_TaskRun(void);

/*外部调用接口*/
void InitiativeReceive_SetConnectFlag(uint8_t nodeid,uint8_t connectflag);
void InitiativeReceive_SetCallBack(void (*p)(TransportCanMsgTypeDef *));  //设置回调函数
uint8_t InitiativeReceive_SetCycleTrigeer(uint8_t nodeid,uint8_t sourceid,uint16_t time,void *addr);
uint8_t InitiativeReceive_SetStateTrigeer(uint8_t nodeid,uint8_t sourceid,void *addr);
uint8_t InitiativeReceive_SetThresholdTrigeer(uint8_t nodeid,
                                              uint8_t sourceid,
                                              uint32_t low,
                                              uint32_t up, 
                                              void *addr);

																								

#endif
