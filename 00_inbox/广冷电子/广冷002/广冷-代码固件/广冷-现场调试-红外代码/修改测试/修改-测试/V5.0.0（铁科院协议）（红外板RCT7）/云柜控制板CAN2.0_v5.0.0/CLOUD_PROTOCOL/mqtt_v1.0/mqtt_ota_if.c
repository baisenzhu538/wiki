#include "mqtt_ota_if.h"


FwUpdataTopic_TypeDef	FwUpdataTopic={"","",0,0};


//发送数据
char FwUpdata_Send_Data(char * data, int size)
{
//	MQTT_Msg_TypeDef * pMsg;
//	
//	pMsg = (MQTT_Msg_TypeDef*)SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
//	if(pMsg == NULL)
//	{
//		return 0x00;
//	}
//	pMsg->qos = 0;
//	pMsg->dup = 0;
//	pMsg->packid = MQTT_Get_PackId();
//	pMsg->retain = 0;
//	pMsg->TopicSize = strlen((char*)FwUpdataTopic.PubTopic);
//	SysMem_copy(pMsg->Topic, FwUpdataTopic.PubTopic, strlen((char*)FwUpdataTopic.PubTopic));
//	pMsg->DataSize = size;
//	pMsg->Data = (u8*)SysMem_malloc(pMsg->DataSize);
//	if(pMsg->Data == NULL)
//	{
//		SysMem_free(pMsg);
//	}
//	SysMem_copy(pMsg->Data,data,size);
//	MQTT_Send_Publish(pMsg);
//	SysMem_free(pMsg->Data);
//	SysMem_free(pMsg);
	
}

//接收数据解释
void FwUpdata_Recive_Data_Parsing(char * data, u16 size)
{
//	Ota_Receive(data,(int)size);
}

