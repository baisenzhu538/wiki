#ifndef __TRANSPORT_QUEUE__
#define __TRANSPORT_QUEUE__
#include "data_struct.h"
#include "malloc.h"
#include "canbus_config.h"


#define RX_MSGQUEUE_SIZE CAN_RX_QUEUELEN


#define MSG_QUEUE_FULL   0x01
#define MSG_QUEUE_NULL   0x01
#define MSG_QUEUE_GET    0xFF
#define MSG_QUEUE_ADD    0xFF

typedef struct
{
	uint8_t head;
	uint8_t tail;
	uint16_t queuelen;
	TransportCanMsgTypeDef rx_msgqueue[RX_MSGQUEUE_SIZE];
}RX_MsgQueueTypeDef;


void MsgQueue_Init(void);
uint16_t MsgQueue_GetQueueSize(void);
uint8_t MsgQueue_GetRxMsg(TransportCanMsgTypeDef *pMsg);
uint8_t MsgQueue_AddRxMsg(TransportCanMsgTypeDef *pMsg);

#endif
