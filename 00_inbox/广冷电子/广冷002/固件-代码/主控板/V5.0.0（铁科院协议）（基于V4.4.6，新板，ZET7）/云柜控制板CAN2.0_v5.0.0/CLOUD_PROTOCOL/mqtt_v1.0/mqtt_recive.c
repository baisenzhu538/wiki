#include "mqtt_recive.h"
#include "mqtt_qos1.h"



MQTT_ReciveStatus_TypeDef	MQTT_ReciveStatus;
JSON_Queue_TypeDef JSON_Queue = {0,0,JSON_QUEUE_MAXLEN,{NULL}};


int MQTT_ConnackPack_Parsing(uint8_t * PackData, uint8_t Size)
{
	MQTT_ConnackPack_TypeDef * ConnackPack = (MQTT_ConnackPack_TypeDef *)PackData;
	if(Size < sizeof(MQTT_ConnackPack_TypeDef)
		|| ConnackPack->Reserved)		
		return -1;
	MQTT_ReciveStatus.Connack.SessionPresent = ConnackPack->SP;
	MQTT_ReciveStatus.Connack.ReturnCode = ConnackPack->ReturnCode;
	if(ConnackPack->ReturnCode != 0x00)		//连接返回码报错
		return -2;
	MQTT_ReciveStatus.Connack.ConnackFlag = 0x01;
	return 0xFF;
}

int MQTT_PubackPack_Parsing(uint8_t * PackData, uint8_t Size)
{
	MQTT_PubackPack_TypeDef * PubackPack = (MQTT_PubackPack_TypeDef * )PackData;
	if(Size < sizeof(MQTT_PubackPack_TypeDef))	//长度不符合
		return 0x01;
	MQTT_ReciveStatus.Puback.PubackSn++;
	MQTT_ReciveStatus.Puback.PackId = PubackPack->PackId_H * 256 + PubackPack->PackId_L;
	
	//此处执行回调函数
	MQTT_RecivePubackPackId_Update(MQTT_ReciveStatus.Puback.PackId);
	
	return 0xFF;
}

int MQTT_SubackPack_Parsing(uint8_t * PackData, uint8_t Size)
{
	uint8_t i;
	MQTT_SubackPack_TypeDef * SubackPack = (MQTT_SubackPack_TypeDef * )PackData;
	uint8_t SubscribeTopicNum = MQTT_SubscribeTopicTable_Get_TableLenth();
	if(Size < (sizeof(MQTT_SubackPack_TypeDef)-MQTT_SUBSCRIBE_TOPIC_MAX_NUM+SubscribeTopicNum))
		return -1;
	MQTT_ReciveStatus.Suback.SubackSn++;
	MQTT_ReciveStatus.Suback.PackId = SubackPack->PackId_H * 256 + SubackPack->PackId_L;
	for(i = 0; i < SubscribeTopicNum; i++)
	{
		MQTT_ReciveStatus.Suback.ReturnCode[i] = SubackPack->ReturnCode[i];
		if(SubackPack->ReturnCode[i] == MQTT_SUBSCRIBE_FAILURE)
			return -2;
	}
	MQTT_ReciveStatus.Suback.SubackFlag = 0x01;
	return 0xFF;
}

int MQTT_PingRespPack_Parsing(uint8_t * PackData, uint8_t Size)
{
	if(Size < 0x02)	//长度不符合
		return -1;
	if(PackData[1] != 0x00)		//不是心跳响应
		return -2;
	MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
	MQTT_ReciveStatus.PingResp.PingRespSn++;
	return 0xFF;
}

uint8_t MQTT_Pack_Parsing(uint8_t * InData, uint8_t InSize)
{
	switch(InData[0])
	{
		case MQTT_CONNACK:	//连接应答
		{
			if(MQTT_ConnackPack_Parsing(InData, InSize)>0)
			{
				return MQTT_CONNACK;
			}
		}
		break;
		case MQTT_PUBACK:		//发布应答	//Qos 0 无应答
		{
			if(MQTT_PubackPack_Parsing(InData, InSize)>0)
			{
				return MQTT_PUBACK;
			}
		}
		break;
		case MQTT_SUBACK:		//订阅应答
		{
			if(MQTT_SubackPack_Parsing(InData, InSize)>0)
			{
				return MQTT_SUBACK;
			}
		}
		break;
		case MQTT_PINGRESP:	//心跳响应
		{
			if(MQTT_PingRespPack_Parsing(InData, InSize)>0)
			{
				return MQTT_PINGRESP;
			}
		}
		break;	
		//“订阅主题”有新消息到达
		case MQTT_PUBLISH:			//QOS 0
		{
			MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
			return MQTT_PUBLISH;
		}
		break;
		case MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_0:		//QOS 1 首发	 
		{ 
			MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
			return MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_0;	
		}
		break;
		case MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_0:		//QOS 1 重发	
		{
			MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
			return MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_0;
		}
		break;
		case MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_1:
		{
			MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
			return MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_1;
		}
		break;
		case MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_1:
		{
			MQTT_ReciveStatus.PingResp.PingRespFlag = 0x01;
			return MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_1;
		}
		break;
		default:return 0x00;
	}
	return 0x00;
}

//求包可变长度
uint16_t Mqtt_Pack_Get_LenSum(uint8_t * InData)
{
	uint16_t Index = 0;		//索引
	uint16_t LenSum = 0;		//数据包总长
	uint8_t LenLen = 0;		//可变长度字节数据
	
	Index++;		//跳过包类型
	if(InData[Index] & 0x80)		//第一个字节最高位是 1 
	{
		LenSum += InData[Index] & 0x7F;		
		Index++;
		if(InData[Index] & 0x80)	//第二个字节最高位是 1 
		{
			LenSum += (InData[Index] & 0x7F) * 0x80;	
			Index++;
			if(InData[Index] & 0x80)	//第三个字节最高位是 1
			{
				LenSum += (InData[Index] & 0x7F) * 0x80 * 0x80;	
				Index++;
				LenSum += (InData[Index] & 0x7F) * 0x80 * 0x80 * 0x80;		//第四个字节 
				LenLen = 4;
			}
			else
			{
				LenLen = 3;
				LenSum += InData[Index] * 0x80 * 0x80;
			}
		}
		else
		{
			LenLen = 2;
			LenSum += InData[Index] * 0x80;
		}
	}
	else	//第一个字节最高位是 0
	{
		LenLen = 1;
		LenSum = InData[Index];
	}
	return LenSum;
}

uint8_t Mqtt_Pack_Get_LenLen(uint8_t * InData)
{
	uint16_t Index = 0;		//索引
	uint8_t LenLen = 0;		//可变长度字节数
	
	Index++;		//路过包类型
	if(InData[Index] & 0x80)		//第一个字节最高位是 1 
	{
		Index++;
		if(InData[Index] & 0x80)	//第二个字节最高位是 1 
		{
			Index++;
			if(InData[Index] & 0x80)	//第三个字节最高位是 1
			{
				Index++;
				LenLen = 4;
			}
			else
			{
				LenLen = 3;
			}
		}
		else
		{
			LenLen = 2;
		}
	}
	else	//第一个字节最高位是 0
	{
		LenLen = 1;
	}
	return LenLen;	
}

uint8_t Mqtt_Pack_MessageTypeCheck(uint8_t * SubTopic, uint16_t SubTopicLen, uint8_t * InData)
{
	uint16_t i = 0;
	uint8_t LenLen = 0;
	uint16_t TopicLen = 0;	
	
	LenLen = Mqtt_Pack_Get_LenLen(InData);	//求可变长度所占的字节数据
	if(LenLen > 4)
		return 0x01;
	TopicLen =  *(InData + 1 + LenLen) * 256 + *(InData + 1 + LenLen + 1);	//求主题长度
	if(TopicLen != SubTopicLen)				//长度不符合
		return 0x02;
	for(i = 0; i < TopicLen; i++)
	{
		if(*(SubTopic+i) != *(InData+1+LenLen+2+i))	//主题不符
			return 0x03;
	}
	return 0x00;
}

uint8_t * Mqtt_Pack_Get_Data_Head(uint8_t Qos, uint8_t * InData)
{
	MQTT_RecivePublishPackId_TypeDef * pPublishPackId;
	uint8_t LenLen = 0;
	uint8_t TopicLen = 0;
	LenLen = Mqtt_Pack_Get_LenLen(InData);	//求可变长度所占的字节数据
	if(LenLen > 4)
		return NULL;
	TopicLen =  *(InData + 1 + LenLen) * 256 + *(InData + 1 + LenLen + 1);	//求主题长度
	
	if(Qos == 0x01)//获取报文ID
	{
		{
			//将报文ID存入队列，后续用于比较发送消息的报文ID
			pPublishPackId = (MQTT_RecivePublishPackId_TypeDef*)SysMem_malloc(sizeof(MQTT_RecivePublishPackId_TypeDef));
			if(pPublishPackId != NULL)
			{
				pPublishPackId->packid = *(InData + 1 + LenLen + 2 +TopicLen) *256 + *(InData + 1 + LenLen + 2 +TopicLen + 1);
				MQTT_RecivePublishPackId_Add_Queue(pPublishPackId);
			}
		}
		InData += 1 + LenLen + 2 + TopicLen + 2;
	}
	else
	{
		InData += 1 + LenLen + 2 + TopicLen;
	}
	return InData;
}

//添加JSON字符串到队列
/*
	功能：
		添加JSON数据包到队列
	形参：
		JSON数据包首地址
	返回：
		0XFF	队列已满
		0X01	已入队
*/
uint8_t JSON_AddDataQueue(JSON_DataPack_TypeDef *pRxPack)
{
	if((JSON_Queue.tail==JSON_Queue.head)&&(JSON_Queue.queuelen==0))
	 return 0xFF;              //队列满
	JSON_Queue.pDataPack[JSON_Queue.tail]=pRxPack;
	JSON_Queue.tail++;
	JSON_Queue.queuelen--;
	if(JSON_Queue.tail==JSON_QUEUE_MAXLEN)
		JSON_Queue.tail=0;
	return 0x01;
}

//从队列中获取字符串
/*
	功能：
		从队列中获取JSON数据包
	返回：
		NULL	失败
		数据包缓存首地址
*/
JSON_DataPack_TypeDef * JSON_GetDataQueue(void)
{
	JSON_DataPack_TypeDef *pRxPack;
	if((JSON_Queue.tail==JSON_Queue.head)&&(JSON_Queue.queuelen==JSON_QUEUE_MAXLEN))
		return NULL;	//队列无数据
	pRxPack=JSON_Queue.pDataPack[JSON_Queue.head];
	JSON_Queue.pDataPack[JSON_Queue.head]=NULL;
	JSON_Queue.head++;
	JSON_Queue.queuelen++;
	if(JSON_Queue.head==JSON_QUEUE_MAXLEN)
		JSON_Queue.head=0;
	return pRxPack;
}
JSON_DataPack_TypeDef * Mqtt_Get_Json(void)
{
	return JSON_GetDataQueue();
}
uint8_t Mqtt_Json_In_Queue(uint8_t * InData)
{
	char * string_buffer = NULL;
	uint8_t res = 0;
	
	{			
		string_buffer = SysMem_malloc(strlen(InData));				//为字符串分配内存				
		if(string_buffer == NULL)										//内存分配失败
			return 0x01;
		
		SysMem_copy(string_buffer,InData, strlen(InData));					//内存拷贝
		
		res = JSON_AddDataQueue((JSON_DataPack_TypeDef *)string_buffer);	//加入队列				
		if(res == 0xFF)														//加入队列失败
		{
			if(string_buffer)
				SysMem_free(string_buffer);									//释放字符串内存		
			return 0x02;
		}				
	}	
	return 0x00;
}


uint16_t Mqtt_Pack_Get_TopicLen(uint8_t * InData)
{
	u8 LenLen = 0;
	u8 TopicLen = 0;
	LenLen = Mqtt_Pack_Get_LenLen(InData);	//求可变长度所占的字节数据
	if(LenLen > 4)
		return 0x00;
	TopicLen =  *(InData + 1 + LenLen) * 256 + *(InData + 1 + LenLen + 1);	//求主题长度
	return TopicLen;
}

uint16_t Mqtt_Pack_Get_Payload_Size(uint8_t Qos, uint8_t * InData)
{
	uint16_t Payload_Size = 0;
	uint16_t LenSum = 0;
	uint16_t TopicLen = 0;
	
	LenSum = Mqtt_Pack_Get_LenSum(InData);
	TopicLen = Mqtt_Pack_Get_TopicLen(InData);
	if(Qos == 0x00)
	{
		Payload_Size = LenSum - (2 + TopicLen);
	}
	else
	{
		Payload_Size = LenSum - (2 + TopicLen + 2);
	}
	return Payload_Size;
}

//串口包拆包
int MQTT_Pack_Json_Cut(uint8_t * InData, uint16_t Size)
{
	uint8_t PackNum = 0;
	char * pJson = NULL;
	uint16_t LenSum = 0;
	uint8_t 	LenLen = 0;
	uint16_t PackLenSum = 0;
	uint8_t packType = 0;
	uint8_t res = 0;
	uint8_t	debug_res=0;
	
	//等待4G模块连接服务器
	if(WirelessModule_ReadRunStaus() == 0x00)	
		return 0;
	while(1)	//拆包
	{
		if(Size <= 0)
		{
			//空包
			return PackNum;
		}
		
		LenSum = Mqtt_Pack_Get_LenSum(InData);
		LenLen = Mqtt_Pack_Get_LenLen(InData);
		if(LenLen > 4)
		{
			//可变长度不合法
			InData++;
			Size--;
			continue;
		}
		//求报文总长
		PackLenSum = 1 + LenLen + LenSum;	
		if(PackLenSum > Size)
		{
			//报文不完整
			InData++;
			Size--;
			continue;
		}
		
		//MQTT 包解释
		{
			packType = MQTT_Pack_Parsing((uint8_t*)InData, Size);
			switch(packType)
			{
				case MQTT_CONNACK:break;
				case MQTT_PUBACK:break;
				case MQTT_SUBACK:break;
				case MQTT_UNSUBACK:break;
				case MQTT_PINGRESP:break;
					
				case MQTT_PUBLISH:
				{
					debug_res = Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->uint.topic_string,
													SubscribeTopicTable.head->uint.topic_lenth,
													InData);
					
					if(Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->uint.topic_string,
													SubscribeTopicTable.head->uint.topic_lenth,
													InData) == 0x00)		//主题筛选
					{	
						
						
						pJson = Mqtt_Pack_Get_Data_Head(MQTT_QOS0, InData);	//获取JSON头				
						if(pJson == NULL)		//获取JSON头失败
							return 0x02;

						res = Mqtt_Json_In_Queue(pJson);
						if(res != 0x00)
							return 0x03;		//数包入队列发生错误
						PackNum++;
					}
					else if(Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->next->uint.topic_string,
														SubscribeTopicTable.head->next->uint.topic_lenth,
														InData) == 0x00)
					{
						pJson = Mqtt_Pack_Get_Data_Head(MQTT_QOS0, InData);	//获取JSON头				
						if(pJson == NULL)		//获取JSON头失败
							return 0x02;

						res = Mqtt_Json_In_Queue(pJson);
						if(res != 0x00)
							return 0x03;		//数包入队列发生错误
						PackNum++;
					}
					else if(Mqtt_Pack_MessageTypeCheck((uint8_t*)FwUpdataTopic.SubTopic,
														strlen((char*)FwUpdataTopic.SubTopic),
														InData) == 0x00)	//远程升级主题
					{	
						FwUpdata_Recive_Data_Parsing(Mqtt_Pack_Get_Data_Head(MQTT_QOS0, InData), 
														Mqtt_Pack_Get_Payload_Size(MQTT_QOS0, InData));	
					}
					else
					{
						InData++;
						Size--;
						continue;
					}
				}
				break;
				case MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_0:
				case MQTT_PUBLISH_QOS_1_DUP_0_RETAIN_1:
				case MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_0:
				case MQTT_PUBLISH_QOS_1_DUP_1_RETAIN_1:
				{
					debug_res = Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->uint.topic_string,
													SubscribeTopicTable.head->uint.topic_lenth,
													InData);
					
					if(Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->uint.topic_string,
													SubscribeTopicTable.head->uint.topic_lenth,
													InData) == 0x00)		//主题筛选
					{	
						pJson = Mqtt_Pack_Get_Data_Head(MQTT_QOS1, InData);	//获取JSON头				
						if(pJson == NULL)		//获取JSON头失败
							return 0x02;

						res = Mqtt_Json_In_Queue(pJson);
						if(res != 0x00)
							return 0x03;		//数包入队列发生错误
						PackNum++;
					}
					else if(Mqtt_Pack_MessageTypeCheck(SubscribeTopicTable.head->next->uint.topic_string,
														SubscribeTopicTable.head->next->uint.topic_lenth,
														InData) == 0x00)
					{
						pJson = Mqtt_Pack_Get_Data_Head(MQTT_QOS1, InData);	//获取JSON头				
						if(pJson == NULL)		//获取JSON头失败
							return 0x02;

						res = Mqtt_Json_In_Queue(pJson);
						if(res != 0x00)
							return 0x03;		//数包入队列发生错误
						PackNum++;
					}
					else if(Mqtt_Pack_MessageTypeCheck((uint8_t*)FwUpdataTopic.SubTopic,
														strlen((char*)FwUpdataTopic.SubTopic),
														InData) == 0x00)	//远程升级主题
					{	
						FwUpdata_Recive_Data_Parsing(Mqtt_Pack_Get_Data_Head(MQTT_QOS1, InData), 
														Mqtt_Pack_Get_Payload_Size(MQTT_QOS1, InData));	
					}
					else
					{
						InData++;
						Size--;
						continue;
					}
				}
				break;
				default:
				{
					if(Size > 0)
					{
						InData++;
						Size--;
						continue;
					}
				}
			}			
		}
		//越过一个报文长度
		InData += PackLenSum;	
		//总长减去一个报文长度
		Size -= PackLenSum;		
		LenSum = 0;
		LenLen = 0;
		PackLenSum = 0;
	}		
}
