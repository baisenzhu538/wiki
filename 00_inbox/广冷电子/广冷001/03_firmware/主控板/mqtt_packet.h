#ifndef	_MQTT_PACKET_H_
#define	_MQTT_PACKET_H_

#include "mqtt_config.h"


//报文类型列表
	
	//连接相关
		//连接申请
		#define MQTT_CONNECT			0x10	
		
		//连接应答
		#define MQTT_CONNACK			0x20	

	//发布相关
		//QOS0消息发布
		#define MQTT_PUBLISH					0x30
		
		#define	MQTT_PUBLISH_QOS0_BIT			0x00
		#define	MQTT_PUBLISH_QOS1_BIT			0x02
		#define	MQTT_PUBLISH_QOS2_BIT			0x04
		#define	MQTT_PUBLISH_DUP0_BIT			0x00
		#define	MQTT_PUBLISH_DUP1_BIT			0x08
		#define	MQTT_PUBLISH_RETAIN0_BIT		0x00
		#define	MQTT_PUBLISH_RETAIN1_BIT		0x01
		
		//QOS1消息首次发布（关闭保留）
		#define MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_0	0x32
		
		//QOS1消息首次发布（开启保留）
		#define	MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_1	0x33
		
		//QOS1消息重复发布（关闭保留）
		#define MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_0	0x3A 
		
		//QOS1消息重复发布（开启保留）
		#define	MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_1	0x3B	
		
		//发布应答
		#define	MQTT_PUBACK				0x40	
	
	//订阅
	#define	MQTT_SUBSCRIBE			0x82
	
	//订阅应答
	#define MQTT_SUBACK				0x90	
	
	//取消订阅
	#define	MQTT_UNSUBSCRIBE		0xA0	
	
	//取消订阅应答
	#define	MQTT_UNSUBACK			0xB0	
	
	//心跳请求
	#define	MQTT_PINGREQ			0xC0	
	
	//心跳响应
	#define	MQTT_PINGRESP			0xD0	
	
	//断开连接
	#define	MQTT_DISCONNECT			0xE0	

#define	MQTT_TOTAL_MAX_LENTH	4


typedef	struct
{
	uint8_t TotalLen[MQTT_TOTAL_MAX_LENTH];
	uint8_t TotalLenLen;
}TotalLen_TypeDef;

typedef	struct
{
	uint8_t qos;
	uint8_t retain;
	uint8_t dup;
	uint8_t SendSn;
	u16 packid;	
	u16 TopicSize;
    uint8_t  Topic[64];		
	u16 DataSize;
	uint8_t * Data;
}MQTT_Msg_TypeDef;

uint16_t MQTT_Get_PackId(void);
uint16_t MQTT_Get_ConnectPack_Lenth(void);
uint16_t Mqtt_ConnectPack_Creat(uint8_t * ConnectPackBuffer);
uint16_t MQTT_Get_PubackPack_Lenth(void);
uint16_t MQTT_PubackPack_Creat(uint8_t * PubackPackBuffer, u16 PackId);
uint16_t MQTT_Get_PublishPack_Lenth(MQTT_Msg_TypeDef * pMsg);
uint16_t MQTT_PublishPack_Creat(MQTT_Msg_TypeDef * pMsg, uint8_t * PublishPackBuffer);
uint16_t MQTT_Get_SubscribePack_Lenth(void);
uint16_t MQTT_SubscribePack_Creat(uint8_t * SubscribePackBuffer);


#endif	/*_MQTT_PACKET_H_*/

