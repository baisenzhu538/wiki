/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN报文接收队列
*	文件名称 : transport_queue.c
*	版    本 : V1.0
*	说    明 : 1.对接收的CAN报文入列出列操作
*            2.提供报文的接收缓冲
*通过该模块，从can接口接收到的报文通过本模块加入到队列中并将报文向协议层传递，驱动协议层
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "transport_queue.h"

RX_MsgQueueTypeDef Rx_MsgQueue;  //创建接收队列

/*************************************************************
函数：MsgQueue_Init
功能：初始化队列
参数：无
返回：无
*************************************************************/
void MsgQueue_Init(void)
{
	Rx_MsgQueue.head=0;
	Rx_MsgQueue.tail=0;
	Rx_MsgQueue.queuelen=RX_MSGQUEUE_SIZE;
}

/*************************************************************
函数：MsgQueue_GetQueueSize
功能：剩余获取队列空间
参数：queue_num 查询队列号
返回：返回剩余队列空间
*************************************************************/
uint16_t MsgQueue_GetQueueSize(void)
{
	uint16_t queuesize;
	 queuesize=Rx_MsgQueue.queuelen;
  return queuesize;
}

/*************************************************************
函数：MsgQueue_AddRxMsg
功能：消息加入队列
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t MsgQueue_AddRxMsg(TransportCanMsgTypeDef *pMsg)
{
	if((Rx_MsgQueue.tail==Rx_MsgQueue.head)&&(Rx_MsgQueue.queuelen==0))
	 return MSG_QUEUE_FULL;              //队列满
	Mem_copy((void*)(Rx_MsgQueue.rx_msgqueue+Rx_MsgQueue.tail),(void *)pMsg,sizeof(CanMsgTypeDef));
	Rx_MsgQueue.tail++;
	Rx_MsgQueue.queuelen--;
	if(Rx_MsgQueue.tail==RX_MSGQUEUE_SIZE)
		Rx_MsgQueue.tail=0;
	return MSG_QUEUE_ADD;
}
/*************************************************************
函数：MsgQueue_GetRxMsg
功能：从消息队列中获取数据
参数：msg 消息指针
返回：MSG_QUEUE_NULL 队列空
      MSG_QUEUE_GET  数据获取成功
*************************************************************/
uint8_t MsgQueue_GetRxMsg(TransportCanMsgTypeDef *pMsg)
{
	if((Rx_MsgQueue.tail==Rx_MsgQueue.head)&&(Rx_MsgQueue.queuelen==RX_MSGQUEUE_SIZE))
		return MSG_QUEUE_NULL;                                  //队列无数据
	Mem_copy((void *)pMsg,(void*)(Rx_MsgQueue.rx_msgqueue+Rx_MsgQueue.head),sizeof(CanMsgTypeDef));
	Rx_MsgQueue.head++;
	Rx_MsgQueue.queuelen++;
	if(Rx_MsgQueue.head==RX_MSGQUEUE_SIZE)
		Rx_MsgQueue.head=0;
	return MSG_QUEUE_GET;
}

