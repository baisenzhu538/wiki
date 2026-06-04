#ifndef	_MQTT_RECIVE_H_
#define	_MQTT_RECIVE_H_

#include "mqtt_packet.h"
#include "wireless_module_init.h"
#include "mqtt_ota_if.h"

#define	MQTT_SUBSCRIBE_FAILURE	0x80
#define	JSON_DATAPACK_MAXSIZE		512						//JSON数据包最大长度
#define	JSON_QUEUE_MAXLEN			32						//JSON队列最大长度

typedef struct
{
	uint8_t    Data[JSON_DATAPACK_MAXSIZE];
}JSON_DataPack_TypeDef;		//串口数据包结构

typedef struct
{
	uint8_t head;
	uint8_t tail;
	uint16_t queuelen;
	JSON_DataPack_TypeDef *pDataPack[JSON_QUEUE_MAXLEN];
}JSON_Queue_TypeDef;

typedef	struct
{
	u8 PackType;
	u8 TotalLen;
	u8 SP:1;
	u8 Reserved:7;
	u8 ReturnCode;
}MQTT_ConnackPack_TypeDef;



typedef struct
{
	u8 ConnackFlag;
	u16 ConnackSn;
	u8 SessionPresent;
	u8 ReturnCode;
}MQTT_ConnackStatus_TypeDef;

typedef	struct
{
	u8 PackType;
	u8 TotalLen;
	u8 PackId_H;
	u8 PackId_L;
}MQTT_PubackPack_TypeDef;

typedef	struct
{
	u16 PubackSn;
	u16 PackId;
}MQTT_PubackStatus_TypeDef;

typedef	struct
{
	u8	PackType;
	u8	TotalLen;
	u8	PackId_H;
	u8	PackId_L;
	u8	ReturnCode[MQTT_SUBSCRIBE_TOPIC_MAX_NUM];
}MQTT_SubackPack_TypeDef;

typedef	struct
{
	u8	SubackFlag;
	u16 SubackSn;
	u16 PackId;
	u8	ReturnCode[MQTT_SUBSCRIBE_TOPIC_MAX_NUM];
}MQTT_SubackStatus_TypeDef;

typedef	struct
{
	u8	PingRespFlag;
	u16  PingRespSn;
}MQTT_PingRespStatus_TypeDef;

typedef	struct
{
	MQTT_ConnackStatus_TypeDef	Connack;
	MQTT_PubackStatus_TypeDef	Puback;
	MQTT_SubackStatus_TypeDef	Suback;
	MQTT_PingRespStatus_TypeDef	PingResp;
}MQTT_ReciveStatus_TypeDef;

extern MQTT_ReciveStatus_TypeDef	MQTT_ReciveStatus;

JSON_DataPack_TypeDef * Mqtt_Get_Json(void);
int MQTT_Pack_Json_Cut(uint8_t * InData, uint16_t Size);


#endif	/*_MQTT_RECIVE_H_*/


