#ifndef __TRANSPORT_LAYER_H
#define __TRANSPORT_LAYER_H
#include "transport_layer.h"
#include "data_struct.h"
#include "drive_api.h"
#include "transport_queue.h"
#include "malloc.h"
#include "time_task.h"
#include "transport_linkeslist.h"

#define TRANSPORT_TIMETASKNUM_0  0x00
#define TRANSPORT_TIMETASKNUM_1  0x01

#define MSG_MAXBYTESIZE             7

#define RX_SECTIONMSG_BUFFSIZE      CAN_RX_SECTIONMSG_NUM

#define STATE_SECTIONMSG_BUFFOCCUPY 0x01
#define STATE_SECTIONMSG_BUFFFREE   0x00

#define MSG_RX_NONSECTION     0x00
#define MSG_RX_FIRSTSECTION   0x01
#define MSG_RX_MIDDLESECTION  0x02
#define MSG_RX_LASTSECTION    0x03


#define MSG_TX_GETQUEUE       0x00
#define MSG_TX_NONSECTION     0x01
#define MSG_TX_SECTION        0x02
#define MSG_TX_FINISH         0x03
#define MSG_TX_FREEMEM        0x04

#define TX_SECTION_GETMSG     0x00
#define TX_SECTION_CONVERT    0x01
#define TX_SECTION_MIDDLE     0x02
#define TX_SECTION_LAST       0x03
#define TX_SECTION_FINISH     0xFF

#define TX_SING_GETMSG        0x00
#define TX_SING_SEND          0x01
#define TX_SING_FINNISH       0xFF
typedef struct
{
	uint8_t state;
	MsgFilterTypeDef SectionMsgFilter;
	
	uint8_t ErrID;
	uint8_t SegNum;
	
	uint16_t DataSize;
	uint8_t Data[512];
} SectionMsgTypeDef;

typedef struct
{
	uint8_t TaskState;
	uint8_t TxSectionState;
	uint8_t TxSingleState;
	TransportTaskTypeDef *pTransportTask;
}TxTaskManageTypeDef;

void TransportLayer_TaskRun(void);
void TransportLayer_Init(void (*p)(MsgFilterTypeDef *));
void TransportLayer_ReceiveQueue(CanMsgTypeDef *pMsg);
uint8_t TransportLayer_TxMsg(TransportCanMsgTypeDef *pMsgBuff);
uint8_t TransportLayer_RxMsg(TransportCanMsgTypeDef *pMsgBuff);
void TransportLayer_CancelAllSend(void);

#endif

