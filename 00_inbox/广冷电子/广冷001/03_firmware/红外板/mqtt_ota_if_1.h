#ifndef	_MQTT_OTA_IF_H_
#define	_MQTT_OTA_IF_H_

#include "cloud_protocol.h"
#include "ota.h"
#include "mqtt_packet.h"
#include "mqtt_send.h"

typedef struct
{
	u8 PubTopic[30];	//发布主题
	u8 SubTopic[30];	//订阅主题  
	u8 Host[30];		//请求域名
	u8 URL[100];		//请求文件路径
	u8 FwVer[30];		//固件版本
	u32 FwSize;			//固件大小
	u8 FwMD5[30];		//固件MD5
}FwUpdataManage_TypeDef;

typedef struct
{
	u8 PubTopic[64];	//发布主题
	u8 SubTopic[64];	//订阅主题  
	u8 PubTopicSize;
	u8 SubTopicSize;
}FwUpdataTopic_TypeDef;

extern FwUpdataTopic_TypeDef	FwUpdataTopic;

void FwUpdata_Recive_Data_Parsing(char * data, u16 size);
char FwUpdata_Send_Data(char * data, int size);



#endif	/*_MQTT_OTA_IF_H_*/

