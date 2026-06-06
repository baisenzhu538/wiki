#ifndef	_MQTT_CONNECT_H_
#define	_MQTT_CONNECT_H_

#include "mqtt_recive.h"
#include "mqtt_send.h"

#define	MQTT_DISCONNECT_WAIT_TIME					10	//s,发送断连等待时间
#define	MQTT_SESSION_RETAIN_TIME					120	//s ,会话保留时间
#define	MQTT_DISCONNECT_WAIT_TIME					10	//s,发送断连等待时间
#define	MQTT_CONNECT_WAIT_TIME						10	//s,连接等待时间			
#define	MQTT_SEND_CONNECT_MAX_NUM					2	//连接最大次数
#define	MQTT_SUBSCRIBE_WAIT_TIME					10	//s,订阅等待时间
#define	MQTT_SEND_SUBSCRIBE_MAX_NUM					3	//订阅最大次数
#define	MQTT_HEART_WAIT_TIME						10	//心跳等待时间
#define	MQTT_SEND_HEART_MAX_NUM						6	//心跳最大次数	
#define	MQTT_CLEAN_SESSION_WAIT_TIME				10	//s，清除会话等待时间
#define	MQTT_SEND_CLEAN_SESSION_MAX_NUM				1	//清除会话最大次数

typedef	struct
{
	u8	DownEn;
	u16 DownTime;
	u16 DownMaxTime;
}MqttDownPara_TypeDef; 

typedef	struct
{
	uint8_t	enable;
	uint8_t	step;
	uint8_t	Link;
	uint8_t	SessionState;
	u32 DeadlineTime;
}MQTT_ConnectManage_TypeDef;

void MQTT_Down_Set(MqttDownPara_TypeDef	* pMqttDownPara);
void MQTT_Add_Subcribe(uint8_t * Topic, uint8_t TopicLen, uint8_t Qos);
void MQTT_Strat_Reboot(void);
void MQTT_Start_Enable(void);
void MQTT_Start_Disable(void);
void MQTT_Connect_Task(void);
uint8_t MQTT_Get_Start_Status(void);
void MQTT_Strat_Reboot(void);
void MQTT_Start_Reset(void);


#endif	/*_MQTT_CONNECT_H_*/