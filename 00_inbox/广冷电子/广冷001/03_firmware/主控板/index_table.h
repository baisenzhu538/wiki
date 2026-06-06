#ifndef __INDEX_TABLE_H
#define __INDEX_TABLE_H
#include "data_struct.h"
#include "malloc.h"
#include "funcid_define.h"
#include "transport_layer.h"
#include "node_info.h"

#define M_INDEXTABLE_TIMENUM 0x0A
#define S_INDEXTABLE_TIMENUM 0x03

//数据类型
#define RW 0x00
#define RO 0x01
#define NV 0x02 //非易失性

#define THRESHOLD_UP_STATE    0x01
#define THRESHOLD_LOW_STATE   0x00
#define THRESHOLD_RANGE_STATE 0x02

#define S_INDEXTABLE_MAX 256
#define M_INDEXTABLE_MAX 256

typedef struct 
{
	uint8_t  nodeid;             //节点id
	uint8_t  sourceid;           //资源节点地址
	uint16_t datalen;
	void *   data;
}SourceDataTypeDef;

typedef struct 
{
  uint8_t  type	         :4;           //数据类型
	uint8_t  cycleinit     :1;  //循环触发初始化0未初始化1初始化
	uint8_t  thresholdinit :1;  //阈值触发初始化状态位
	uint8_t  stateinit     :1;  //状态触发初始化状态位
	uint8_t  connectflag   :1;  //节点连接状态
	
	uint8_t  timeoverflag     :4;
	uint8_t  receive_enable   :1; //触发接收
	uint8_t  cycle_enable     :1; //定时触发
	uint8_t  threshold_enable :1; //阈值触发
	uint8_t  state_enable     :1; //状态触发
	
	
	
	uint16_t timecount;     //定时计数
	uint16_t time;          //定时时间
	
	uint8_t star_tx;        //启动一次发送，自动复位      
	uint8_t last_threshold;
	uint32_t last_state;    //最后保存变量值
	uint32_t upper_limit;
	uint32_t lower_limit; 
}SourceManageTypeDef;

typedef struct
{
	SourceDataTypeDef   SourceData;
	SourceManageTypeDef SourceManage;
}SourceInfoTypeDef;


typedef struct _IndexTableUint
{
	struct _IndexTableUint *prior;
	struct _IndexTableUint *next;
	SourceInfoTypeDef      Source;
}IndexTableUintTypeDef;

typedef struct 
{
 IndexTableUintTypeDef *head;
 IndexTableUintTypeDef *tail;
 uint16_t   maxsize;
 uint16_t   tablesize;
}IndexTableTypeDef;

typedef struct 
{
 IndexTableUintTypeDef *now;
 void (*Receive_CallBack)(SourceDataTypeDef*);
 void (*Trigger_CallBack)(SourceDataTypeDef*);
}IndexTableTaskTypeDef;

uint8_t mIndexTable_SetThresoldSync(uint8_t nodeid,uint8_t sourceid,uint32_t u_lim,uint32_t l_lim);
uint8_t sIndexTable_SetThresoldSync(uint8_t nodeid,uint8_t sourceid,uint32_t u_lim,uint32_t l_lim);
uint8_t mIndexTable_SetStateSync(uint8_t nodeid,uint8_t sourceid);
uint8_t sIndexTable_SetStateSync(uint8_t nodeid,uint8_t sourceid);
uint8_t mIndexTable_SetCycSync(uint8_t nodeid,uint8_t sourceid,uint16_t time);
uint8_t sIndexTable_SetCycSync(uint8_t nodeid,uint8_t sourceid,uint16_t time);

void mIndexTable_SetConnectFlag(uint8_t nodeid,uint8_t connectflag);
void sIndexTable_SetConnectFlag(uint8_t nodeid,uint8_t connectflag);

void mIndexTable_ReceiveTask(TransportCanMsgTypeDef *pRxMsg);
void sIndexTable_ReceiveTask(TransportCanMsgTypeDef *pRxMsg);

uint8_t sIndexTable_AddSource(uint8_t nodeid,uint8_t sourceid,uint8_t type,void *srcdr,uint16_t datalen);
uint8_t mIndexTable_AddSource(uint8_t nodeid,uint8_t sourceid,uint8_t type,void *srcdr,uint16_t datalen);

uint8_t sIndexTable_WriteData(uint8_t node_id,uint8_t index_num,void *srdata,uint16_t datalen);
uint8_t mIndexTable_WriteData(uint8_t node_id,uint8_t index_num,void *srdata,uint16_t datalen);
uint8_t sIndexTable_ReadData(uint8_t node_id,uint8_t index_num,void *drdata);
uint8_t mIndexTable_ReadData(uint8_t node_id,uint8_t index_num,void *drdata);
uint16_t mIndexTable_GetDataLen(uint8_t node_id,uint8_t index_num);
uint16_t sIndexTable_GetDataLen(uint8_t node_id,uint8_t index_num);

uint8_t sIndexTable_UpDataLate(uint8_t nodeid,uint8_t sourceid);//更新存放缓存值

void sIndexTable_SetStarTx(uint8_t nodeid,uint8_t sourceid);
void mIndexTable_SetStarTx(uint8_t nodeid,uint8_t sourceid);

void sIndexTable_SyncTaskRun(void);
void mIndexTable_SyncTaskRun(void);
void mIndexTable_Init(void);
void sIndexTable_Init(void);
#endif
