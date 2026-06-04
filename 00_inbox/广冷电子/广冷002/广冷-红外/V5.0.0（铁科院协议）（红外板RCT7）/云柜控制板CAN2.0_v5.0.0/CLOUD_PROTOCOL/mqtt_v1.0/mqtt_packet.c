#include "mqtt_packet.h"

uint16_t MQTT_Get_PackId(void)
{
	static uint16_t Sn = 0;
	Sn++;
	return Sn;
}

static void MQTT_Get_Pack_TotalLen(uint16_t TotalLenSum, TotalLen_TypeDef * TotalLen)
{
	uint8_t a = 0,b = 0,c = 0,d = 0;
	
	a = TotalLenSum / 128;		//确定第2个字节
	b = a / 128;				//确定第3个字节
	c = b / 128;				//确定第4个字节
	d = TotalLenSum % 128;		//确定第1个字节
	
	if(c >= 1)	//长度达到4个字节
	{		
		TotalLen->TotalLen[0] = 0x80 | d;
		TotalLen->TotalLen[1] = 0x80 | a;
		TotalLen->TotalLen[2] = 0x80 | b;	
		TotalLen->TotalLen[3] = c;
		TotalLen->TotalLenLen = 4;
	}
	else if(b >= 1)	//长度达到3个字节
	{
		TotalLen->TotalLen[0] = 0x80 | d;
		TotalLen->TotalLen[1] = 0x80 | a;
		TotalLen->TotalLen[2] = b;
		TotalLen->TotalLenLen = 3;
	}
	else if (a >= 1) //长度达到2个字节
	{
		TotalLen->TotalLen[0] = 0x80 | d;
		TotalLen->TotalLen[1] = a;
		TotalLen->TotalLenLen = 2;
	}
	else //长度达到1个字节
	{
		TotalLen->TotalLen[0] = TotalLenSum;		
		TotalLen->TotalLenLen = 1;
	}	
}



static uint16_t	MQTT_Get_ConnectPack_TotalLenSum(void)
{
	uint16_t TotalLenSum = 0;
	
	TotalLenSum = sizeof(MQTT_Connect_Config.ProtocolName_Lenth)
					+ MQTT_Connect_Config.ProtocolName_Lenth
					+ sizeof(MQTT_Connect_Config.ProtocolLevel)
					+ sizeof(MQTT_Connect_Config.ConnectFlag)
					+ sizeof(MQTT_Connect_Config.KeepAlive)
					+ sizeof(MQTT_Connect_Config.ClientId_Lenth)
					+ MQTT_Connect_Config.ClientId_Lenth;
	if(MQTT_Connect_Config.ConnectFlag.WillFlag)
		TotalLenSum += sizeof(MQTT_Connect_Config.WillTopic_Lenth)
						+ MQTT_Connect_Config.WillTopic_Lenth
						+ sizeof(MQTT_Connect_Config.WillMessage_Lenth)
						+ MQTT_Connect_Config.WillMessage_Lenth;
	if(MQTT_Connect_Config.ConnectFlag.UserNameFlag)
		TotalLenSum += sizeof(MQTT_Connect_Config.UserName_Lenth)
						+ MQTT_Connect_Config.UserName_Lenth;
	if(MQTT_Connect_Config.ConnectFlag.PasswordFlag)
		TotalLenSum += sizeof(MQTT_Connect_Config.Password_Lenth)
						+ MQTT_Connect_Config.Password_Lenth;
	return TotalLenSum;
}

static void MQTT_Get_ConnectPack_TotalLen(TotalLen_TypeDef * TotalLen)
{
	MQTT_Get_Pack_TotalLen(MQTT_Get_ConnectPack_TotalLenSum(), TotalLen);
}

uint16_t MQTT_Get_ConnectPack_Lenth(void)
{
	TotalLen_TypeDef TotalLen;
	uint16_t ConnectPackLenth = 0;
	
	MQTT_Get_ConnectPack_TotalLen(&TotalLen);
	ConnectPackLenth = 1 + TotalLen.TotalLenLen + MQTT_Get_ConnectPack_TotalLenSum();
	
	return ConnectPackLenth;
}

uint16_t MQTT_ConnectPack_Creat(uint8_t * ConnectPackBuffer)
{
	uint8_t i;
	uint16_t Index = 0;	
	TotalLen_TypeDef TotalLen;
	
	ConnectPackBuffer[Index] = MQTT_CONNECT;
	Index++;
	
	MQTT_Get_ConnectPack_TotalLen(&TotalLen);
	for(i = 0; i < TotalLen.TotalLenLen; i++)
	{
		ConnectPackBuffer[Index] = TotalLen.TotalLen[i];
		Index++;
	}
	ConnectPackBuffer[Index] = MQTT_Connect_Config.ProtocolName_Lenth / 256;
	Index++;
	ConnectPackBuffer[Index] = MQTT_Connect_Config.ProtocolName_Lenth % 256;
	Index++;
	SysMem_copy(&ConnectPackBuffer[Index], 
				MQTT_Connect_Config.ProtocolName_String, 
				MQTT_Connect_Config.ProtocolName_Lenth);
	Index += MQTT_Connect_Config.ProtocolName_Lenth;
	ConnectPackBuffer[Index] = MQTT_Connect_Config.ProtocolLevel;
	Index++;
	SysMem_copy(&ConnectPackBuffer[Index], 
				&MQTT_Connect_Config.ConnectFlag, 
				sizeof(MQTT_Connect_Config.ConnectFlag));
	Index += sizeof(MQTT_Connect_Config.ConnectFlag);
	ConnectPackBuffer[Index] = MQTT_Connect_Config.KeepAlive / 256;
	Index++;
	ConnectPackBuffer[Index] = MQTT_Connect_Config.KeepAlive % 256;
	Index++;
	ConnectPackBuffer[Index] = MQTT_Connect_Config.ClientId_Lenth / 256;
	Index++;
	ConnectPackBuffer[Index] = MQTT_Connect_Config.ClientId_Lenth % 256;
	Index++;
	SysMem_copy(&ConnectPackBuffer[Index],
				MQTT_Connect_Config.ClientId_String,
				MQTT_Connect_Config.ClientId_Lenth);
	Index += MQTT_Connect_Config.ClientId_Lenth;
	
	if(MQTT_Connect_Config.ConnectFlag.WillFlag)
	{
		
		ConnectPackBuffer[Index] = MQTT_Connect_Config.WillTopic_Lenth / 256;
		Index++;
		ConnectPackBuffer[Index] = MQTT_Connect_Config.WillTopic_Lenth % 256;
		Index++;
		SysMem_copy(&ConnectPackBuffer[Index], 
					MQTT_Connect_Config.WillTopic_String,
					MQTT_Connect_Config.WillTopic_Lenth);
		Index += MQTT_Connect_Config.WillTopic_Lenth;
		
		ConnectPackBuffer[Index] = MQTT_Connect_Config.WillMessage_Lenth / 256;
		Index++;
		ConnectPackBuffer[Index] = MQTT_Connect_Config.WillMessage_Lenth % 256;
		Index++;
		SysMem_copy(&ConnectPackBuffer[Index], 
					MQTT_Connect_Config.WillMessage_String,
					MQTT_Connect_Config.WillMessage_Lenth);
		Index += MQTT_Connect_Config.WillMessage_Lenth;
	}
		
	if(MQTT_Connect_Config.ConnectFlag.UserNameFlag)
	{
		ConnectPackBuffer[Index] = MQTT_Connect_Config.UserName_Lenth / 256;
		Index++;
		ConnectPackBuffer[Index] = MQTT_Connect_Config.UserName_Lenth % 256;
		Index++;
		SysMem_copy(&ConnectPackBuffer[Index], 
					MQTT_Connect_Config.UserName_String,
					MQTT_Connect_Config.UserName_Lenth);
		Index += MQTT_Connect_Config.UserName_Lenth;
	}
	
	if(MQTT_Connect_Config.ConnectFlag.PasswordFlag)
	{
		ConnectPackBuffer[Index] = MQTT_Connect_Config.Password_Lenth / 256;
		Index++;
		ConnectPackBuffer[Index] = MQTT_Connect_Config.Password_Lenth % 256;
		Index++;
		SysMem_copy(&ConnectPackBuffer[Index], 
					MQTT_Connect_Config.Password_String,
					MQTT_Connect_Config.Password_Lenth);
		Index += MQTT_Connect_Config.Password_Lenth;
	}
	return Index;
}

uint16_t MQTT_Get_PubackPack_Lenth(void)
{
	return 0x04;
}

uint16_t MQTT_PubackPack_Creat(uint8_t * PubackPackBuffer, uint16_t PackId)
{
	uint16_t Index = 0;	
	
	PubackPackBuffer[Index] = MQTT_PUBACK;
	Index++;
	PubackPackBuffer[Index] = 0x02;
	Index++;
	PubackPackBuffer[Index] = PackId / 256;
	Index++;
	PubackPackBuffer[Index] = PackId % 256;
	Index++;
	
	return Index;
}



static uint16_t MQTT_Get_PublishPack_TotalLenSum(MQTT_Msg_TypeDef * pMsg)
{
	uint16_t TotalLenSum = 0;
	
	TotalLenSum = sizeof(pMsg->TopicSize)
					+ pMsg->TopicSize
					+ pMsg->DataSize;
	if(pMsg->qos > MQTT_QOS0)
		TotalLenSum += sizeof(pMsg->packid);
	
	return TotalLenSum;
}

static uint16_t MQTT_Get_PublishPack_TotalLen(MQTT_Msg_TypeDef * pMsg, TotalLen_TypeDef * TotalLen)
{
	MQTT_Get_Pack_TotalLen(MQTT_Get_PublishPack_TotalLenSum(pMsg),
							TotalLen);
}

uint16_t MQTT_Get_PublishPack_Lenth(MQTT_Msg_TypeDef * pMsg)
{
	TotalLen_TypeDef TotalLen;
	uint16_t PublishPackLenth;
	
	MQTT_Get_PublishPack_TotalLen(pMsg,&TotalLen);
	PublishPackLenth = 1 + TotalLen.TotalLenLen + MQTT_Get_PublishPack_TotalLenSum(pMsg);
	
	return PublishPackLenth;
}

uint16_t MQTT_PublishPack_Creat(MQTT_Msg_TypeDef * pMsg, uint8_t * PublishPackBuffer)
{
	uint8_t i = 0;
	uint16_t Index = 0;	
	TotalLen_TypeDef TotalLen;

	
	MQTT_Get_PublishPack_TotalLen(pMsg,&TotalLen);
	PublishPackBuffer[Index] = MQTT_PUBLISH;
	if(pMsg->qos == 0x01)
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_QOS1_BIT;
	}
	else if(pMsg->qos == 0x02)
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_QOS2_BIT;
	}
	else
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_QOS0_BIT;
	}
	if(pMsg->dup == 0x01)
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_DUP1_BIT;
	}
	else
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_DUP0_BIT;
	}
	if(pMsg->retain == 0x01)
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_RETAIN1_BIT;
	}
	else
	{
		PublishPackBuffer[Index] |= MQTT_PUBLISH_RETAIN0_BIT;
	}
	Index++;
	for(i = 0; i < TotalLen.TotalLenLen; i++)
	{
		PublishPackBuffer[Index] = TotalLen.TotalLen[i];
		Index++;
	}
	PublishPackBuffer[Index] = pMsg->TopicSize / 256;
	Index++;
	PublishPackBuffer[Index] = pMsg->TopicSize % 256;
	Index++;
	SysMem_copy(&PublishPackBuffer[Index],
				pMsg->Topic,
				pMsg->TopicSize);
	Index += pMsg->TopicSize;
	if(pMsg->qos)
	{
		PublishPackBuffer[Index] = pMsg->packid / 256;
		Index++;
		PublishPackBuffer[Index] = pMsg->packid % 256;
		Index++;
	}
	SysMem_copy(&PublishPackBuffer[Index],
				pMsg->Data,
				pMsg->DataSize);
	Index += pMsg->DataSize;
	
	return Index;
}



static uint16_t MQTT_Get_SubscribePack_TotalLenSum(void)
{
	uint8_t i;
	uint16_t TotalLenSum = 0;
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	
	pTopicBlock = SubscribeTopicTable.head;
	TotalLenSum = sizeof(uint16_t);
	
	while(pTopicBlock)
	{
		TotalLenSum += sizeof(uint16_t)
						+ pTopicBlock->uint.topic_lenth
						+ sizeof(uint8_t);
		pTopicBlock = pTopicBlock->next;
	}
	return TotalLenSum;
}

static void MQTT_Get_SubscribePack_TotalLen(TotalLen_TypeDef * TotalLen)
{
	MQTT_Get_Pack_TotalLen(MQTT_Get_SubscribePack_TotalLenSum(), 
							TotalLen);
}

uint16_t MQTT_Get_SubscribePack_Lenth(void)
{
	uint16_t SubscribePackLenth = 0;
	TotalLen_TypeDef TotalLen;
	
	MQTT_Get_SubscribePack_TotalLen(&TotalLen);
	SubscribePackLenth = 1 + TotalLen.TotalLenLen 
							+ MQTT_Get_SubscribePack_TotalLenSum();
	
	return SubscribePackLenth;
}

uint16_t MQTT_SubscribePack_Creat(uint8_t * SubscribePackBuffer)
{
	uint16_t Index = 0;
	uint8_t i;
	TotalLen_TypeDef TotalLen;
	uint16_t packid;
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	
	pTopicBlock = SubscribeTopicTable.head;
	packid = MQTT_Get_PackId();
	
	MQTT_Get_SubscribePack_TotalLen(&TotalLen);
	
	SubscribePackBuffer[Index] = MQTT_SUBSCRIBE;
	Index++;
	for(i = 0; i < TotalLen.TotalLenLen; i++)
	{
		SubscribePackBuffer[Index] = TotalLen.TotalLen[i];
		Index++;
	}
	SubscribePackBuffer[Index] = packid / 256;
	Index++;
	SubscribePackBuffer[Index] = packid % 256;
	Index++;
	while(pTopicBlock)
	{
		SubscribePackBuffer[Index] = pTopicBlock->uint.topic_lenth / 256;
		Index++;
		SubscribePackBuffer[Index] = pTopicBlock->uint.topic_lenth % 256;
		Index++;
		SysMem_copy(&SubscribePackBuffer[Index],
					pTopicBlock->uint.topic_string,
					pTopicBlock->uint.topic_lenth);
		Index += pTopicBlock->uint.topic_lenth;
		SubscribePackBuffer[Index] = pTopicBlock->uint.topic_qos;
		Index++;
		pTopicBlock = pTopicBlock->next;
	}
	return Index;
}


















