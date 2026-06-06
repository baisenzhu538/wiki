#ifndef __NODE_INFO_H
#define __NODE_INFO_H
#include "data_struct.h"
#include "malloc.h"
#include "drive_api.h"

//#define NODE_CANPROTOCOL_VER      0x00020201 // 2.2.1
#define NODE_CANPROTOCOL_VER      0x00020202 // 2.2.2 修改index_table.c 2019-01-16 



#define NODE_CONTROLLER_DEVICE    0x0000   //控制器
#define NODE_FIRSTLEVEL_DEVICE    0x1000   //一级设备
#define NODE_SECONDLEVEL_DEVICE   0x2000   //二级设备


#define NODE_DEVICEADDR_STAR      0x60//设备地址起始位
#define NODE_DEVICEADDR_END       0xFD//设备地址结束位

#define NODEINFONUM    3

typedef struct
{
 NodeDiscernTypeDef  NodeDiscern;	
 NodeResourceTypeDef NodeResource;
 NodeLinkTypeDef     NodeLink;
} NodeInfoTypeDef;

extern NodeInfoTypeDef NodeInfo;


uint16_t             GetInfoSize(uint8_t index);
NodeLinkTypeDef*     GetLinkInfoAddr(void);
NodeResourceTypeDef* GetResourceInfoAddr(void);
NodeDiscernTypeDef*  GetDiscernInfoAddr(void);
NodeInfoTypeDef*     GrtNodeInfoAddr(void);

void NodeDiscernInit(NodeDiscernTypeDef *pNodeDiscern);
void InfoTable_Init(void);

//外部调用接口
uint8_t NodeInfo_GetMastId(void);
uint8_t ReadNodeInfo(uint8_t index_num,void *pinfo);
uint8_t NodeInfo_GetConnectFlag(void);
uint8_t NodeInfo_GetIdCheckFlag(void);
uint8_t NodeInfo_GetNodeId(void);
uint8_t NodeInfo_GetDeviceNum(void);
uint16_t NodeInfo_GetDeviceType(void);
void NodeInfo_SetNodeId(uint8_t nodeid);
uint8_t NodeInfo_GetDeviceGrade(void);
#endif
