/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 设备节点信息
*	文件名称 : node_info.c
*	版    本 : V1.0
*	说    明 : 1.实现内存的动态管理
*            2.实现内存的分配释放
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "node_info.h"

NodeInfoTypeDef NodeInfo;

void*    NodeInfoTable[NODEINFONUM+1];
uint16_t InfoDataSize[NODEINFONUM+1];
void InfoTable_Init(void)
{
	NodeInfoTable[0]=NULL;                      InfoDataSize[0]=0;
	NodeInfoTable[1]=&NodeInfo.NodeDiscern;     InfoDataSize[1]=sizeof(NodeDiscernTypeDef);
	NodeInfoTable[2]=&NodeInfo.NodeResource;    InfoDataSize[2]=sizeof(NodeResourceTypeDef);
	NodeInfoTable[3]=&NodeInfo.NodeLink;        InfoDataSize[3]=sizeof(NodeLinkTypeDef);
}

void NodeDiscernInit(NodeDiscernTypeDef *pNodeDiscern)
{
	Mem_copy(&NodeInfo.NodeDiscern,pNodeDiscern,sizeof(NodeDiscernTypeDef));
	NodeInfo.NodeLink.LocalMACID=NodeInfo.NodeDiscern.can_nodeid;
}
uint16_t GetInfoSize(uint8_t index)
{
	if(index>NODEINFONUM&&index==0x00)
		return 0x00;
	return InfoDataSize[index];
}

void* GetInfoAddr(uint8_t index)
{
	if(index>NODEINFONUM&&index==0x00)
		return NULL;
	return NodeInfoTable[index];
}

uint8_t ReadNodeInfo(uint8_t index_num,void *pinfo)
{
	if(index_num>NODEINFONUM&&index_num==0x00)
		return NULL;
	Mem_copy(pinfo,NodeInfoTable[index_num],GetInfoSize(index_num));
	return 0xFF;
}

NodeLinkTypeDef* GetLinkInfoAddr(void)
{
	return &NodeInfo.NodeLink;
}

NodeResourceTypeDef* GetResourceInfoAddr(void)
{
	return &NodeInfo.NodeResource;
}

NodeDiscernTypeDef* GetDiscernInfoAddr(void)
{
	return &NodeInfo.NodeDiscern;
}

NodeInfoTypeDef* GrtNodeInfoAddr(void)
{
	return &NodeInfo;
}

uint8_t NodeInfo_GetConnectFlag(void)
{
	return NodeInfo.NodeLink.ConnectFlag;
}

uint8_t NodeInfo_GetIdCheckFlag(void)
{
	return NodeInfo.NodeLink.IDTest;
}

uint8_t NodeInfo_GetNodeId(void)
{
	return NodeInfo.NodeDiscern.can_nodeid;
}
