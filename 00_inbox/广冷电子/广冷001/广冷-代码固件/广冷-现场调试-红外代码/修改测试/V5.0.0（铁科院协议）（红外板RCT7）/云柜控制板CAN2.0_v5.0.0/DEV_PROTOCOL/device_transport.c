#include "device_transport.h"
#include "transport_api.h"

DeviceTransport_SnManageTypeDef     DeviceTransport_SnManage;//穿件sn码管理块
DeviceTransport_BuffQueueTypeDef    DeviceTransport_RxQueue={0,0,DEVICE_RXQUEUE_MAXLEN,DEVICE_RXQUEUE_MAXLEN};
DeviceTransport_BuffQueueTypeDef    DeviceTransport_TxQueue={0,0,DEVICE_TXQUEUE_MAXLEN,DEVICE_TXQUEUE_MAXLEN};

/*************************************************************
函数：DeviceTransport_CompareRxSn
功能：查找是否存在相同Sn码
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t DeviceTransport_CompareRxSn(uint16_t sn)
{
	uint8_t i;
	for(i=0;i<SN_TABLE_MAX;i++)
	{
		if(DeviceTransport_SnManage.rx_sn_table[i]==sn)
			return 0x00;//存在相同sn码
	}
	DeviceTransport_SnManage.rx_sn_table[DeviceTransport_SnManage.rx_sn_tabletail]=sn;
	DeviceTransport_SnManage.rx_sn_tabletail++;
	if(DeviceTransport_SnManage.rx_sn_tabletail==SN_TABLE_MAX)
		DeviceTransport_SnManage.rx_sn_tabletail=0;
	return 0xFF;
}
/*************************************************************
函数：MsgQueue_AddRxMsg
功能：消息加入队列
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint16_t DeviceTransport_GetTxSn(void)
{
	return DeviceTransport_SnManage.tx_sn++;
}
/*************************************************************
函数：DeviceTranspot_AddBuffQueue
功能：接收数据报文存入队列中
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t DeviceTranspot_AddBuffQueue(DeviceTransport_BuffQueueTypeDef *pQueue,DeviceTransport_ProtocolBuffTypeDef *pBuff)
{
	if((pQueue->tail==pQueue->head)&&(pQueue->queuelen==0))
	 return DEVICE_QUEUE_FULL;              //队列满
	pQueue->pRxBuff[pQueue->tail]=pBuff;
	pQueue->tail++;
	pQueue->queuelen--;
	if(pQueue->tail==pQueue->maxlen)
		pQueue->tail=0;
	return DEVICE_QUEUE_ADD;
}

/*************************************************************
函数：DeviceTranspot_GetBuffQueue
功能：从缓存队列中获取报文
参数：msg 消息指针
返回：MSG_QUEUE_NULL 队列空
      MSG_QUEUE_GET  数据获取成功
*************************************************************/
DeviceTransport_ProtocolBuffTypeDef * DeviceTranspot_GetBuffQueue(DeviceTransport_BuffQueueTypeDef *pQueue)
{
	DeviceTransport_ProtocolBuffTypeDef *pRxBuff;
	if((pQueue->tail==pQueue->head)&&(pQueue->queuelen==pQueue->maxlen))
		return NULL;                                  //队列无数据
	pRxBuff=pQueue->pRxBuff[pQueue->head];
	pQueue->head++;
	pQueue->queuelen++;
	if(pQueue->head==pQueue->maxlen)
		pQueue->head=0;
	return pRxBuff;
}

/*************************************************************
函数：DeviceTranspot_AddRxMsg
功能：接收数据报文存入队列中
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t DeviceTranspot_AddRxMsg(DeviceTransport_ProtocolBuffTypeDef *pRxBuff)
{
 return DeviceTranspot_AddBuffQueue(&DeviceTransport_RxQueue,pRxBuff);
}

/*************************************************************
函数：DeviceTranspot_GetRxMsg
功能：从缓存队列中获取报文
参数：msg 消息指针
返回：MSG_QUEUE_NULL 队列空
      MSG_QUEUE_GET  数据获取成功
*************************************************************/
DeviceTransport_ProtocolBuffTypeDef * DeviceTranspot_GetRxMsg(void)
{
	return DeviceTranspot_GetBuffQueue(&DeviceTransport_RxQueue);
}
/*************************************************************
函数：DeviceTranspot_AddTxMsg
功能：接收数据报文存入队列中
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t DeviceTranspot_AddTxMsg(DeviceTransport_ProtocolBuffTypeDef *pTxBuff)
{
 return DeviceTranspot_AddBuffQueue(&DeviceTransport_TxQueue,pTxBuff);
}

/*************************************************************
函数：DeviceTranspot_GetTxMsg
功能：从缓存队列中获取待发送报文
参数：void
返回：存放数据指针
*************************************************************/
DeviceTransport_ProtocolBuffTypeDef * DeviceTranspot_GetTxMsg(void)
{
	return DeviceTranspot_GetBuffQueue(&DeviceTransport_TxQueue);
}


void DeviceTransport_TxTask(void)
{
	static uint8_t runstate=0;
	static DeviceTransport_ProtocolBuffTypeDef *pProtocolBuff;
	switch(runstate)
	{
		case 0x00:
			pProtocolBuff=NULL;
			pProtocolBuff=DeviceTranspot_GetTxMsg();
		  if(pProtocolBuff!=NULL)
			 runstate=0x01;
			break;
		case 0x01:
			if(TransportApi_SendData(pProtocolBuff)==0xFF)
			{
			 SysMem_free(pProtocolBuff);
			 runstate=0x00;
			}
			break;
	}
}
