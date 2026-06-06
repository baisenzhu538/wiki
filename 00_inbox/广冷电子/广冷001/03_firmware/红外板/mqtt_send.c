#include "mqtt_send.h"


void MQTT_Send_PingReq(void)
{
	uint8_t PingReqPackBuffer[2] = {MQTT_PINGREQ,0x00};
	
//	WierlessHarware_SendData(PingReqPackBuffer, 2);
	WirelessModule_SendData(PingReqPackBuffer, 2);	
}

void MQTT_Send_DisConnect(void)
{
	uint8_t DisConnectPackBuffer[2] = {MQTT_DISCONNECT, 0x00};
//	WierlessHarware_SendData(DisConnectPackBuffer, 2);	
	WirelessModule_SendData(DisConnectPackBuffer, 2);	
}

void MQTT_Send_CleanSession(void)
{
	uint8_t * ConnectPackBuffer = NULL;
	uint16_t ConnectPackLenth = 0;
	
	if(MQTT_Connect_Config.ConnectFlag.WillFlag)
		MQTT_WillMessage_Update();
	ConnectPackLenth = MQTT_Get_ConnectPack_Lenth();
	ConnectPackBuffer = (uint8_t*)SysMem_malloc(ConnectPackLenth);
	if(ConnectPackBuffer == NULL)
		return ;
	MQTT_Connect_Config_CleanSession_Enable();
	MQTT_ConnectPack_Creat(ConnectPackBuffer);
//	WierlessHarware_SendData(ConnectPackBuffer, 
//								ConnectPackLenth);		
	WirelessModule_SendData(ConnectPackBuffer, 
								ConnectPackLenth);	
	SysMem_free(ConnectPackBuffer);	
}

void MQTT_Send_Connect(void)
{
	uint8_t * ConnectPackBuffer = NULL;
	uint16_t ConnectPackLenth = 0;
	
	MQTT_Connect_Config_CleanSession_Disable();
	if(MQTT_Connect_Config.ConnectFlag.WillFlag)
		MQTT_WillMessage_Update();
	ConnectPackLenth = MQTT_Get_ConnectPack_Lenth();
	ConnectPackBuffer = (uint8_t*)SysMem_malloc(ConnectPackLenth);
	if(ConnectPackBuffer == NULL)
		return ;
	
	MQTT_ConnectPack_Creat(ConnectPackBuffer);
//	WierlessHarware_SendData(ConnectPackBuffer, 
//								ConnectPackLenth);		
	WirelessModule_SendData(ConnectPackBuffer, 
								ConnectPackLenth);	
	SysMem_free(ConnectPackBuffer);
}

void MQTT_Send_Subscribe(void)
{
	uint8_t * SubscribePackBuffer = NULL;
	uint16_t SubscribePackLenth = 0;
	
	SubscribePackLenth = MQTT_Get_SubscribePack_Lenth();
	SubscribePackBuffer = (uint8_t*)SysMem_malloc(SubscribePackLenth);
	if(SubscribePackBuffer == NULL)
		return ;
	MQTT_SubscribePack_Creat(SubscribePackBuffer);
//	WierlessHarware_SendData(SubscribePackBuffer, 
//								SubscribePackLenth);	
	WirelessModule_SendData(SubscribePackBuffer, 
								SubscribePackLenth);	
	SysMem_free(SubscribePackBuffer);
}

void MQTT_Send_Publish(MQTT_Msg_TypeDef * pMsg)
{
	uint8_t * PublishPackBuffer = NULL;
	uint16_t PublishPackLenth = 0;	
	
	PublishPackLenth = MQTT_Get_PublishPack_Lenth(pMsg);
	PublishPackBuffer = (uint8_t*)SysMem_malloc(PublishPackLenth);
	if(PublishPackBuffer == NULL)
		return ;
	MQTT_PublishPack_Creat(pMsg, PublishPackBuffer);
//	WierlessHarware_SendData(PublishPackBuffer, 
//								PublishPackLenth);		
	WirelessModule_SendData(PublishPackBuffer, PublishPackLenth);
	SysMem_free(PublishPackBuffer);	
}

void MQTT_Send_Puback(uint16_t PackId)
{
	uint8_t * PubackPackBuffer = NULL;
	uint16_t PubackPackLenth = 0;	
	
	PubackPackLenth = MQTT_Get_PubackPack_Lenth();
	PubackPackBuffer = (uint8_t*)SysMem_malloc(PubackPackLenth);
	if(PubackPackBuffer == NULL)
		return ;
	MQTT_PubackPack_Creat(PubackPackBuffer, PackId);
//	WierlessHarware_SendData(PubackPackBuffer, 
//								PubackPackLenth);		
	WirelessModule_SendData(PubackPackBuffer, PubackPackLenth);
	SysMem_free(PubackPackBuffer);	
}

