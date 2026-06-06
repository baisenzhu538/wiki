#ifndef	_MQTT_QOS1_H_
#define	_MQTT_QOS1_H_

#include "mqtt_recive.h"
#include "mqtt_send.h"

#define	PUBLISH_PACK_ID_QUEUE_MAXLEN	20
#define	MSG_QUEUE_MAXLEN	20

typedef	struct
{
	u16 packid;
}MQTT_RecivePubackPackId_TypeDef;

typedef	struct
{
	u16 packid;
}MQTT_RecivePublishPackId_TypeDef;

typedef struct
{
	uint8_t head;
	uint8_t tail;
	uint16_t queuelen;
	MQTT_RecivePublishPackId_TypeDef *PublishPackId[PUBLISH_PACK_ID_QUEUE_MAXLEN];
}MQTT_RecivePublishPackId_Queue_TypeDef;






typedef struct
{
	uint8_t head;
	uint8_t tail;
	uint16_t queuelen;
	MQTT_Msg_TypeDef *pMsg[MSG_QUEUE_MAXLEN];
}MQTT_Msg_Queue_TypeDef;

MQTT_RecivePublishPackId_TypeDef * MQTT_RecivePublishPackId_Get_Queue(void);
uint8_t MQTT_RecivePublishPackId_Add_Queue(MQTT_RecivePublishPackId_TypeDef *pPublishPackId);
uint8_t MQTT_Msg_Add_Queue(MQTT_Msg_TypeDef *pMsg);
void MQTT_RecivePubackPackId_Update(u16 PackId);
void MQTT_QOS1_Task(void);


#endif	/*_MQTT_QOS1_H_*/

