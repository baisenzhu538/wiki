#ifndef __DEVICE_MANAGE_H
#define __DEVICE_MANAGE_H
#include "data_struct.h"
#include "malloc.h"
#include "time_task.h"
#include "funcid_define.h"
#include "transport_layer.h"
#include "node_info.h"
#include "index_table.h"

#define DEVICE_MAXNUM              20                 //可接入最大设备数量
#define CONTROLLER_MAXNUM          20
#define ASKTASK_MAXNUM             CAN_ACKTASK_MAXNUM //每个节点最多有20个响应任务
#define DEVICEBLOCK_MAXNUM         CAN_DEVICE_MAXNUM  //每个总线中最多可以有64个节点

#define SLAVEHEART_OVERTIME        CAN_MASTERHEART_OVERTIME//2s超时
#define ASK_LIFETIME               CAN_DEVICEMANAGE_LIFETIME //100ms,已响应报文存活时间

#define DEVICEMANAGE_TASK_TIMENUM  0x09

#define DeviceManage_GetNodeId(p)       (p->nodefilter.can_nodeid)
#define DeviceManage_ResetHeartTime(p)  (p->LinkManage.hearttime=0)
#define DeviceManage_GetConnectFlag(p)  (p->LinkManage.connectflag)
#define DeviceManage_SetConnectFlag(p)  (p->LinkManage.connectflag=0x01)
#define DeviceManage_ResetConnectFlag(p)  (p->LinkManage.connectflag=0x00)


typedef struct
{
	uint8_t  funcid;     //资源节点操作功能码
	uint8_t  sourceid;   //资源节点id
	uint8_t  askfuncid;  //响应功能码
	uint8_t  errid;      //响应类型
	uint8_t  lifetime;   //循环周期次数
	uint8_t  lifeover;   //生存时间结束
	uint8_t  reserve2;
	uint8_t  reserve3;
	TransportMsgDataTypeDef devicedata;
}AskTaskTypeDef;

typedef struct _AskNode
{
	struct _AskNode  *prior;
	struct _AskNode  *next;
	AskTaskTypeDef   DeviceAskTask;
}AskTaskBlockTypeDef;

typedef struct
{
	AskTaskBlockTypeDef *head;
	AskTaskBlockTypeDef *tail;
	uint32_t tablelen;
}AskTaskTableTypeDef;

typedef struct
{
	uint8_t  heartflag;   //节点心跳
	uint8_t  connectflag; //节点连接
	uint16_t hearttime;   //心跳计时
	uint8_t  heartover;   //心跳超时标志
	uint8_t  reserve1;
	uint8_t  reserve2;
  uint8_t  reserve3;
}DeviceLinkManageTypeDef;

typedef struct
{
	NodeDiscernTypeDef      nodefilter;  //设备识别
	DeviceLinkManageTypeDef   LinkManage;  //连接管理
	AskTaskTableTypeDef       AskTaskTable;//响应任务表
}DeviceManageTypeDef;

typedef struct _DeviceManageBlock
{
	struct _DeviceManageBlock *prior;
	struct _DeviceManageBlock *next;
	DeviceManageTypeDef       DeviceManage;
}DeviceManageBlockTypeDef;

typedef struct
{
	DeviceManageBlockTypeDef *head;
  DeviceManageBlockTypeDef *tail;
	uint32_t tablelen;
}DeviceManageTableTypeDef;





uint8_t DeviceManage_AddDevice(NodeDiscernTypeDef *pFilter);

AskTaskTypeDef *DeviceManage_GetAskTask(AskTaskTableTypeDef *pAskTable,uint8_t sourceid,uint8_t Funcid);
void DeviceManage_RemoveAllAskTask(AskTaskTableTypeDef *pAskTaskTable);
void DeviceManage_TaskInit(void);
AskTaskBlockTypeDef *DeviceManage_GetAskTaskBlock(AskTaskTableTypeDef *pAskTable,uint8_t sourceid,uint8_t Funcid);
uint8_t DeviceManage_AddAskTask(AskTaskTableTypeDef *pAskTable,AskTaskTypeDef *pAskTask);
uint8_t DeviceManage_RemoveAskTask(AskTaskTableTypeDef *pAskTable,AskTaskTypeDef *pAskTask);

void DeviceManage_CallBack(NodeDiscernTypeDef *pNodeDiscern,DeviceLinkManageTypeDef* pLinkManage);

DeviceManageTypeDef *DeviceManage_GetDeviceManage(uint8_t nodeid);
DeviceManageTypeDef *DeviceManage_GetDeviceManage2(uint8_t devicenum,uint16_t devicetype);

/*外部调用接口*/
uint8_t DeviceManage_ReadPort(uint8_t nodeid,uint8_t sounrcid,void *data);
uint8_t DeviceManage_WritePort(uint8_t nodeid,uint8_t sounrcid,void *data,uint8_t datasize);
uint8_t DeviceManage_GetLinkFlag(uint8_t devicenum,uint16_t devicetype);
uint8_t DeviceManage_GetLinkFlag2(uint8_t nodeid);
uint8_t DeviceManage_GetDeviceID(uint8_t devicenum,uint16_t devicetype);
uint8_t DeviceManage_AssignDeviceId(DeviceMarkTypeDef *pDeviceMark);
uint8_t DeviceManage_AssignControllerId(DeviceMarkTypeDef *pDeviceMark);
void DeviceManage_SetConnectCallBack(void(*p)(NodeDiscernTypeDef*,DeviceLinkManageTypeDef*));//设置连接回调函数
#endif


