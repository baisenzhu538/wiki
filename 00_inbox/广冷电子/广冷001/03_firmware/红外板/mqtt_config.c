#include "mqtt_config.h"


MQTT_Connect_Config_TypeDef	MQTT_Connect_Config;
MQTT_TopicTable_TypeDef	SubscribeTopicTable = {NULL,NULL,0};


uint8_t MQTT_SubscribeTopicTable_Get_TableLenth(void)
{
	return SubscribeTopicTable.table_lenth;
}

MQTT_TopicBlock_TypeDef * MQTT_SubscribeTopicTable_TraverseBlock(uint8_t * topic_string)
{
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	
	pTopicBlock = SubscribeTopicTable.head;
	while(pTopicBlock)
	{
		if(strcmp((char*)pTopicBlock->uint.topic_string, (char*)topic_string) == 0x00)
			return pTopicBlock;
		pTopicBlock = pTopicBlock->next;
	}
	return NULL;
}

MQTT_TopicUint_TypeDef * MQTT_SubscribeTopicTable_TraverseUint(uint8_t * topic_string)
{
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	
	pTopicBlock = MQTT_SubscribeTopicTable_TraverseBlock(topic_string);
	if(pTopicBlock == NULL)
		return NULL;
	else
		return &pTopicBlock->uint;
}

int MQTT_SubscribeTopicTable_AddUint(MQTT_TopicUint_TypeDef * topic_uint)
{
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	MQTT_TopicUint_TypeDef * pTopicUint;
	
	if(topic_uint == NULL
		|| topic_uint->topic_lenth == 0
		|| topic_uint->topic_qos > MQTT_QOS2
		|| topic_uint->topic_string == NULL)
	{
		//形参不合法
		while(0);
		return -1;
	}
	if(SubscribeTopicTable.table_lenth >= MQTT_SUBSCRIBE_TOPIC_MAX_NUM)
	{
		//列表满
		while(0);
		return -2;
	}
	pTopicUint = MQTT_SubscribeTopicTable_TraverseUint(topic_uint->topic_string);
	if(pTopicUint)
	{
		//覆盖原QOS
		pTopicUint->topic_qos = topic_uint->topic_qos;
		return -3;
	}
	pTopicBlock = (MQTT_TopicBlock_TypeDef*)SysMem_malloc(sizeof(MQTT_TopicBlock_TypeDef));
	if(pTopicBlock == NULL)
	{
		//内存分配失败
		while(0);
		return -4;
	}
	SysMem_copy((uint8_t*)&pTopicBlock->uint, (uint8_t*)topic_uint, sizeof(MQTT_TopicUint_TypeDef));
	if(SubscribeTopicTable.head == NULL)
	{
		pTopicBlock->next = NULL;
		pTopicBlock->proir = NULL;
		SubscribeTopicTable.head = pTopicBlock;
		SubscribeTopicTable.tail = pTopicBlock;
		SubscribeTopicTable.table_lenth++;
	}
	else
	{
		pTopicBlock->next = NULL;
		SubscribeTopicTable.tail->next = pTopicBlock;
		pTopicBlock->proir = SubscribeTopicTable.tail;
		SubscribeTopicTable.tail = pTopicBlock;
		SubscribeTopicTable.table_lenth++;
	}
	return 0xFF;
}

int MQTT_SubscribeTopicTable_DeleteUint(uint8_t * topic_string)
{
	MQTT_TopicBlock_TypeDef	* pTopicBlock;
	
	pTopicBlock = MQTT_SubscribeTopicTable_TraverseBlock(topic_string);
	if(pTopicBlock == NULL)
	{
		while(0);
		return -1;	
	}
	//只剩1个
	if(SubscribeTopicTable.table_lenth == 1 
		&& SubscribeTopicTable.head == SubscribeTopicTable.tail)
	{
		SubscribeTopicTable.head = NULL;
		SubscribeTopicTable.tail = NULL;
	}
	//头
	else if(pTopicBlock == SubscribeTopicTable.head)
	{
		SubscribeTopicTable.head = pTopicBlock->next;
		SubscribeTopicTable.head->proir = NULL;
	}
	//尾
	else if(pTopicBlock == SubscribeTopicTable.tail)
	{
		SubscribeTopicTable.tail = pTopicBlock->proir;
		SubscribeTopicTable.tail->next = NULL; 
	}
	//中间
	else
	{
		pTopicBlock->proir->next = pTopicBlock->next;
		pTopicBlock->next->proir = pTopicBlock->proir;
	}
	SubscribeTopicTable.table_lenth--;
	SysMem_free(pTopicBlock);
	return 0xFF;
}


int MQTT_SubscribeTopicTable_Init(uint8_t * DeviceId)
{
	int ret = 0;
	MQTT_TopicUint_TypeDef * pTopicUint;
	
	pTopicUint = (MQTT_TopicUint_TypeDef*)SysMem_malloc(sizeof(MQTT_TopicUint_TypeDef));
	if(pTopicUint == NULL)
	{
		return -1;
	}
	
	//填充订阅主题
	SysMem_copy(pTopicUint->topic_string, MQTT_SUBSCRIBE_TOPIC_1, MQTT_SUBSCRIBE_TOPIC_1_LENTH);
	//"controller_msg/"
	
	SysMem_copy(pTopicUint->topic_string+MQTT_SUBSCRIBE_TOPIC_1_OFFSET, DeviceId, MQTT_SUBSCRIBE_TOPIC_1_MASK_LENTH);
	//"controller_msg/xxxxx"	//拼接设备ID
	
	//主题长度
	pTopicUint->topic_lenth = MQTT_SUBSCRIBE_TOPIC_1_LENTH;
	
	//服务质量要求
	pTopicUint->topic_qos = MQTT_SUBSCRIBE_TOPIC_1_QOS;
	
	//增加到订阅主题队列
	ret = MQTT_SubscribeTopicTable_AddUint(pTopicUint);
	if(ret < 0)
	{
		SysMem_free(pTopicUint);
		return -2;
	}
//	SysMem_copy(pTopicUint->topic_string, MQTT_SUBSCRIBE_TOPIC_2, MQTT_SUBSCRIBE_TOPIC_2_LENTH);
//	SysMem_copy(pTopicUint->topic_string+MQTT_SUBSCRIBE_TOPIC_2_OFFSET, DeviceId, MQTT_SUBSCRIBE_TOPIC_2_MASK_LENTH);
//	pTopicUint->topic_lenth = MQTT_SUBSCRIBE_TOPIC_2_LENTH;
//	pTopicUint->topic_qos = MQTT_SUBSCRIBE_TOPIC_2_QOS;
//	ret = MQTT_SubscribeTopicTable_AddUint(pTopicUint);	
//	SysMem_free(pTopicUint);
//	if(ret < 0)
//	{
//		return -2;
//	}
	return 0xFF;
}



static void MQTT_Cofig_HexNumbleToString_LittleEnd(uint8_t *pString,uint8_t *pNumble,uint8_t ByteNum)
{
	static char HexChar[16]={"0123456789ABCDEF"};
	uint8_t i;
	for(i=0;i<ByteNum;i++)
	{
		pString[i*2]    =HexChar[(pNumble[ByteNum-i-1]>>4)&0x0F];
		pString[(i*2)+1]=HexChar[pNumble[ByteNum-i-1]&0x0F];
	}
}

static uint64_t MQTT_WillMessage_Get_Sn(void)
{
	static uint64_t	sn = 0;
	sn++;
	return	sn;
}
int MQTT_WillMessage_Update(void)
{
	uint8_t Sn[]  ="FFFFFFFFFFFFFFFF";
	uint64_t sn = MQTT_WillMessage_Get_Sn();
	
	Time_TypeDef NowTime;
	TimeStamp_Get_TimeStamp(&NowTime);	//获取时间戳
	MQTT_Cofig_HexNumbleToString_LittleEnd(Sn, (uint8_t*)&sn, sizeof(uint64_t));
	MQTT_Connect_Config.WillMessage_Lenth = 0;
	memset(MQTT_Connect_Config.WillMessage_String,0,MQTT_WILL_MESSAGE_MAX_LENTH);
	sprintf((char*)MQTT_Connect_Config.WillMessage_String,
	"{"
		"\"ID\":\"%s\","
		"\"SN\":\"%s\","
		"\"Cmd\":\"21\","
		"\"Ack\":\"00\","
		"\"Time\":{"
					"\"year\":%d,"
					"\"month\":%d,"
					"\"day\":%d,"
					"\"hour\":%d,"
					"\"minute\":%d,"
					"\"second\":%d"
					"}"
	"}",
	MQTT_Connect_Config.ClientId_String,
	Sn,
	NowTime.year,
	NowTime.month,
	NowTime.day,
	NowTime.hour,
	NowTime.min,
	NowTime.sec);
	
	MQTT_Connect_Config.WillMessage_Lenth = strlen((char*)MQTT_Connect_Config.WillMessage_String);
	
	return 0xFF;
}

int MQTT_Connect_Config_Init(uint8_t * DeviceId)
{
	int ret = 0;
	
	MQTT_Connect_Config.KeepAlive = MQTT_KEEPALIVE_TIME_S;
	MQTT_Connect_Config.ConnectFlag.CleanSession = 0x01;
	
	MQTT_Connect_Config.ProtocolLevel = MQTT_PROTOCOL_LEVEL;
	MQTT_Connect_Config.ProtocolName_Lenth = MQTT_PROTOCOL_NAME_LENTH;
	SysMem_copy(MQTT_Connect_Config.ProtocolName_String,
				MQTT_PROTOCOL_NAME,MQTT_PROTOCOL_NAME_LENTH);
	
	MQTT_Connect_Config.ClientId_Lenth = MQTT_CLIENT_ID_LENTH;
//	SysMem_copy(MQTT_Connect_Config.ClientId_String, 
//				DeviceId, MQTT_CLIENT_ID_LENTH);
	
	SysConfig_Get_DeviceId((char*)MQTT_Connect_Config.ClientId_String);

	MQTT_Connect_Config.ConnectFlag.UserNameFlag = 0x01;	
	MQTT_Connect_Config.UserName_Lenth = MQTT_USER_NAME_LENTH;
	SysMem_copy(MQTT_Connect_Config.UserName_String,
				MQTT_USER_NAME,	MQTT_USER_NAME_LENTH);

	MQTT_Connect_Config.ConnectFlag.PasswordFlag = 0x01;	
	MQTT_Connect_Config.Password_Lenth = MQTT_PASSWORD_LENTH;
	SysMem_copy(MQTT_Connect_Config.Password_String,
				MQTT_PASSWORD, MQTT_PASSWORD_LENTH);

	MQTT_Connect_Config.ConnectFlag.WillFlag = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillQos = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillRetain = 0x00;
	
	MQTT_Connect_Config.WillTopic_Lenth = MQTT_WILL_TOPIC_LENTH;
	SysMem_copy(MQTT_Connect_Config.WillTopic_String,
				MQTT_WILL_TOPIC,MQTT_WILL_TOPIC_LENTH);
}	


void MQTT_Connect_Config_Will_Disable(void)
{
	MQTT_Connect_Config.WillMessage_Lenth = 0x00;
	memset(MQTT_Connect_Config.WillMessage_String,0,MQTT_WILL_MESSAGE_MAX_LENTH);
	MQTT_Connect_Config.ConnectFlag.WillQos = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillRetain = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillFlag = 0x00;
}

void MQTT_Connect_Config_Will_Enable(void)
{
	MQTT_WillMessage_Update();
	MQTT_Connect_Config.ConnectFlag.WillQos = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillRetain = 0x00;
	MQTT_Connect_Config.ConnectFlag.WillFlag = 0x01;
}

void MQTT_Connect_Config_Write_KeepAlive(uint16_t keepalive)
{
	MQTT_Connect_Config.KeepAlive = keepalive;
}

void MQTT_Connect_Config_Write_ProtocolLevel(uint8_t level)
{
	MQTT_Connect_Config.ProtocolLevel = level;
}

void MQTT_Connect_Config_CleanSession_Enable(void)
{
	MQTT_Connect_Config.ConnectFlag.CleanSession = 0x01;
}

void MQTT_Connect_Config_CleanSession_Disable(void)
{
	MQTT_Connect_Config.ConnectFlag.CleanSession = 0x00;	
}

void MQTT_Connect_Config_PasswordFlag_Disable(void)
{
	MQTT_Connect_Config.ConnectFlag.PasswordFlag = 0x00;
}

void MQTT_Connect_Config_PasswordFlag_Enable(void)
{
	MQTT_Connect_Config.ConnectFlag.PasswordFlag = 0x01;
}

void MQTT_Connect_Config_UserNameFlag_Disable(void)
{
	MQTT_Connect_Config.ConnectFlag.UserNameFlag = 0x00;
}

void MQTT_Connect_Config_UserNameFlag_Enable(void)
{
	MQTT_Connect_Config.ConnectFlag.UserNameFlag = 0x01;
}

int MQTT_Config_Init(uint8_t * DeviceId)
{
	MQTT_SubscribeTopicTable_Init(DeviceId);
	MQTT_Connect_Config_Init(DeviceId);
}




