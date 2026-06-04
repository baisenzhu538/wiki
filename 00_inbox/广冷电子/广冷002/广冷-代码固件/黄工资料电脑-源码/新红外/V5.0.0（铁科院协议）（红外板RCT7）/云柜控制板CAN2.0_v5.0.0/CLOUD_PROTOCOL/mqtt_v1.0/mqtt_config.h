#ifndef	_MQTT_CONFIG_H_
#define	_MQTT_CONFIG_H_

#include "stm32f10x.h"
#include "sys_malloc.h"
#include <string.h>
#include "time_stamp.h"
#include "sys_config.h"

#define	MQTT_QOS0	0x00
#define	MQTT_QOS1	0x01
#define	MQTT_QOS2	0x02

#define	MQTT_PROTOCOL_LEVEL_1	0x01
#define	MQTT_PROTOCOL_LEVEL_2	0x02
#define	MQTT_PROTOCOL_LEVEL_3	0x03
#define	MQTT_PROTOCOL_LEVEL_4	0x04

//MQTT 协议名
#define	MQTT_PROTOCOL_NAME				"MQTT"

//MQTT 协议名长度
#define	MQTT_PROTOCOL_NAME_LENTH		4

#define	MQTT_PROTOCOL_LEVEL				MQTT_PROTOCOL_LEVEL_4

//MQTT ClientID 长度
#define	MQTT_CLIENT_ID_LENTH			24	

//MQTT 遗嘱主题
#define	MQTT_WILL_TOPIC					"terminal_msg"			

//MQTT 遗嘱主题长度
#define	MQTT_WILL_TOPIC_LENTH			12							

//MQTT 遗嘱报文最大长度
#define	MQTT_WILL_MESSAGE_MAX_LENTH		256			

//MQTT 用户名
#define	MQTT_USER_NAME					"terminal"		

//MQTT 用户名长度
#define	MQTT_USER_NAME_LENTH			8						

//MQTT 密码
#define	MQTT_PASSWORD					"vending12306"					

//MQTT 密码长度
#define	MQTT_PASSWORD_LENTH				12					

//MQTT 订阅主题1
#define	MQTT_SUBSCRIBE_TOPIC_1			"controller_msg/"

//MQTT 订阅主题1拼接位置
#define	MQTT_SUBSCRIBE_TOPIC_1_OFFSET	15

#define	MQTT_SUBSCRIBE_TOPIC_1_MASK_LENTH	24

//MQTT 订阅主题1主题长度
#define	MQTT_SUBSCRIBE_TOPIC_1_LENTH	39

//MQTT 订阅主题1消息等级
#define	MQTT_SUBSCRIBE_TOPIC_1_QOS		0x01

//MQTT 订阅主题2
#define	MQTT_SUBSCRIBE_TOPIC_2			"jumiSingleChip/00000000000000000000000000000000"

//MQTT 订阅主题2拼接位置
#define	MQTT_SUBSCRIBE_TOPIC_2_OFFSET	15

#define	MQTT_SUBSCRIBE_TOPIC_2_MASK_LENTH	32

//MQTT 订阅主题2主题长度
#define	MQTT_SUBSCRIBE_TOPIC_2_LENTH	47

//MQTT 订阅主题2消息等级
#define	MQTT_SUBSCRIBE_TOPIC_2_QOS		0x01


//MQTT 订阅主题最大数量
#define	MQTT_SUBSCRIBE_TOPIC_MAX_NUM	1

//MQTT 订阅主题最大长度
#define	MQTT_SUBSCRIBE_TOPIC_MAX_LENTH	64

#define	MQTT_PROTOCOL_NAME_MAX_LENTH	4

#define	MQTT_CLIENT_ID_MAX_LENTH		36

#define	MQTT_USER_NAME_MAX_LENTH		10

#define	MQTT_PASSWORD_MAX_LENTH			12

#define	MQTT_WILL_TOPIC_MAX_LENTH		32

#define	MQTT_WILL_MESSAGE_MAX_LENTH		256

#define	MQTT_KEEPALIVE_TIME_S			60

typedef	struct
{
	u16 topic_lenth;
	u8 topic_qos;
	u8 topic_string[MQTT_SUBSCRIBE_TOPIC_MAX_LENTH];
}MQTT_TopicUint_TypeDef;

typedef	struct	_MQTT_TopicBlock_TypeDef
{
	struct _MQTT_TopicBlock_TypeDef	*proir;
	struct _MQTT_TopicBlock_TypeDef	*next;
	MQTT_TopicUint_TypeDef	uint;
}MQTT_TopicBlock_TypeDef;

typedef	struct
{
	MQTT_TopicBlock_TypeDef	*head;
	MQTT_TopicBlock_TypeDef	*tail;
	u8 table_lenth;
}MQTT_TopicTable_TypeDef;

typedef	struct
{
	u8	Reserved:1;
	u8	CleanSession:1;
	u8	WillFlag:1;
	u8	WillQos:2;
	u8	WillRetain:1;
	u8	PasswordFlag:1;
	u8	UserNameFlag:1;
}MQTT_ConnectFlag_TypeDef;

typedef	struct
{
	u16	KeepAlive;
	u8	ProtocolLevel;
	MQTT_ConnectFlag_TypeDef	ConnectFlag;
	u16 WillTopic_Lenth;
	u8	WillTopic_String[MQTT_WILL_TOPIC_MAX_LENTH];
	u16	WillMessage_Lenth;	
	u8	WillMessage_String[MQTT_WILL_MESSAGE_MAX_LENTH];
	u16 ProtocolName_Lenth;
	u8 ProtocolName_String[MQTT_PROTOCOL_NAME_MAX_LENTH];
	u16 ClientId_Lenth;
	u8	ClientId_String[MQTT_CLIENT_ID_MAX_LENTH];
	u16	UserName_Lenth;
	u8	UserName_String[MQTT_USER_NAME_MAX_LENTH];
	u16	Password_Lenth;
	u8	Password_String[MQTT_PASSWORD_MAX_LENTH];
}MQTT_Connect_Config_TypeDef;

extern MQTT_Connect_Config_TypeDef	MQTT_Connect_Config;
extern MQTT_TopicTable_TypeDef	SubscribeTopicTable;
int MQTT_SubscribeTopicTable_AddUint(MQTT_TopicUint_TypeDef * topic_uint);
int MQTT_SubscribeTopicTable_DeleteUint(u8 * topic_string);
u8 MQTT_SubscribeTopicTable_Get_TableLenth(void);

int MQTT_Config_Init(u8 * DeviceId);
int MQTT_WillMessage_Update(void);
void MQTT_Connect_Config_Will_Disable(void);
void MQTT_Connect_Config_Will_Enable(void);
void MQTT_Connect_Config_Write_KeepAlive(u16 keepalive);
void MQTT_Connect_Config_Write_ProtocolLevel(u8 level);
void MQTT_Connect_Config_CleanSession_Enable(void);
void MQTT_Connect_Config_CleanSession_Disable(void);
void MQTT_Connect_Config_PasswordFlag_Disable(void);
void MQTT_Connect_Config_PasswordFlag_Enable(void);
void MQTT_Connect_Config_UserNameFlag_Disable(void);
void MQTT_Connect_Config_UserNameFlag_Enable(void);


#endif	/*_MQTT_CONFIG_H_*/

