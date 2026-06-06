#ifndef __NODE_INFO_H
#define __NODE_INFO_H
#include "data_struct.h"
#include "malloc.h"
#define NODEINFONUM    3

typedef struct
{
 NodeDiscernTypeDef  NodeDiscern;	
 NodeResourceTypeDef NodeResource;
 NodeLinkTypeDef     NodeLink;
} NodeInfoTypeDef;

extern NodeInfoTypeDef NodeInfo;


uint16_t GetInfoSize(uint8_t index);
NodeLinkTypeDef* GetLinkInfoAddr(void);
NodeResourceTypeDef* GetResourceInfoAddr(void);
NodeDiscernTypeDef* GetDiscernInfoAddr(void);
NodeInfoTypeDef* GrtNodeInfoAddr(void);

void NodeDiscernInit(NodeDiscernTypeDef *pNodeDiscern);
void InfoTable_Init(void);

//外部调用接口
uint8_t ReadNodeInfo(uint8_t index_num,void *pinfo);
uint8_t NodeInfo_GetConnectFlag(void);
uint8_t NodeInfo_GetIdCheckFlag(void);
uint8_t NodeInfo_GetNodeId(void);
#endif
