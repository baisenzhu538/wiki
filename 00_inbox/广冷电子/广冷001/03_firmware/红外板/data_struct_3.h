#ifndef __DATA_STRUCT_H
#define __DATA_STRUCT_H
#include "can_stdint.h"

#define CAN_MSG_MAXFRAMELEN  0x07


typedef struct      //4字节
{
	uint8_t  SourceID;
	uint8_t  DestMacID;
	uint8_t  SrcMacID;
	uint8_t  FuncID:4;
	uint8_t  Ack   :4;
}MsgFilterTypeDef;

typedef struct       //8字节
{
 uint8_t DataSize;
 uint8_t Data[CAN_MSG_MAXFRAMELEN];
}MsgDataTypeDef;

typedef struct      //4字节
{
	uint8_t ErrID;
	uint8_t ErrFunc;
	uint8_t SegPolo;
	uint8_t SegNum;
}MsgManageTypeDef;


typedef struct
{
	MsgFilterTypeDef MsgFilter;
	MsgDataTypeDef   MsgData;
	MsgManageTypeDef MsgManage;
} CanMsgTypeDef;

typedef struct       //8字节
{
 uint32_t DataSize;
 uint8_t  *Data;
}TransportMsgDataTypeDef;

typedef struct       //8字节
{
 MsgFilterTypeDef          TransportMsgFilter;//4字节
 MsgManageTypeDef          TransportMsgManage;//4字节
 TransportMsgDataTypeDef   TransportMsgData;  //8字节
}TransportCanMsgTypeDef;


typedef struct
{
	uint8_t  can_nodeid;  //节点id
	uint8_t  devicenum;   //设备编号
	uint16_t devicetype;  //设备类型
	uint32_t dvr;         //设备版本号
	uint32_t ver;         //通讯版本
	uint32_t deviceid_0;  //96位设备唯一ID
	uint32_t deviceid_1;
	uint32_t deviceid_2;
}NodeDiscernTypeDef;

typedef struct
{
 uint8_t  CycleNum;     //循环发送数量
 uint8_t  ThresholdNum; //触发发送数量
 uint8_t  StateNum;     //状态发送数量
 uint8_t  SourceNum;    //使用资源节点数量
 uint8_t  RxQueueSize;  //接收队列大小
 uint8_t  RxQueueFree;  //剩余队列大小
 uint8_t  TxTaskNum;    //待发送数据包
 uint8_t  reserve;
 uint16_t MemBaseSize;  //可分配内存大小
 uint16_t MemUsageSize; //使用内存大小
}NodeResourceTypeDef;



typedef struct
{
	uint8_t MasterMACID;                       
  uint8_t LocalMACID;
	uint8_t ConnectFlag;     //连接标志位 1：为已建立连接 0：未连接 2:删除连接
	uint8_t IDTest;          //ID检测 1：正在检测中 0：未进行检测 2:检测通过 3.检测不通过
	uint8_t IDTestNum;       //ID检测次数
	uint8_t HeartbeatFlag;   //总线是否心跳标识
  uint8_t HeartbeatCounter;//心跳计数
	uint8_t HeartbeatTime;   //心跳时间
	uint8_t SysOutTime;      //同步超时时间
	uint8_t SysCounter;      //主机同步超时计数
	uint8_t Sysflag;         //检测同步信号标志位	
	uint8_t reserve;
} NodeLinkTypeDef;

typedef struct
{
	uint8_t  can_nodeid;  //节点id
	uint8_t  devicenum;   //设备编号
	uint16_t devicetype;  //设备类型
}DeviceMarkTypeDef;//设备标志

#endif
