#include "mqtt_qos1.h"


MQTT_RecivePubackPackId_TypeDef	PubackPackId;

MQTT_RecivePublishPackId_Queue_TypeDef  PublishPackId_Queue = {0,0,PUBLISH_PACK_ID_QUEUE_MAXLEN,{0}};

void MQTT_RecivePubackPackId_Update(u16 PackId)
{
	PubackPackId.packid = PackId;
}

MQTT_RecivePublishPackId_TypeDef * MQTT_RecivePublishPackId_Get_Queue(void)
{
	MQTT_RecivePublishPackId_TypeDef *pPublishPackId;
	
	if((PublishPackId_Queue.tail==PublishPackId_Queue.head)
		&&(PublishPackId_Queue.queuelen==PUBLISH_PACK_ID_QUEUE_MAXLEN))
		return 0;	//队列无数据
	pPublishPackId=PublishPackId_Queue.PublishPackId[PublishPackId_Queue.head];
	PublishPackId_Queue.PublishPackId[PublishPackId_Queue.head]=0;
	PublishPackId_Queue.head++;
	PublishPackId_Queue.queuelen++;
	if(PublishPackId_Queue.head==PUBLISH_PACK_ID_QUEUE_MAXLEN)
		PublishPackId_Queue.head=0;
	return pPublishPackId;
}

uint8_t MQTT_RecivePublishPackId_Add_Queue(MQTT_RecivePublishPackId_TypeDef *pPublishPackId)
{
	MQTT_RecivePublishPackId_TypeDef * ppPublishPackId=NULL;
	if((PublishPackId_Queue.tail==PublishPackId_Queue.head)
		&&(PublishPackId_Queue.queuelen==0))
	{
		ppPublishPackId = MQTT_RecivePublishPackId_Get_Queue();
		if(ppPublishPackId)
			SysMem_free(ppPublishPackId);
	}
	PublishPackId_Queue.PublishPackId[PublishPackId_Queue.tail]=pPublishPackId;
	PublishPackId_Queue.tail++;
	PublishPackId_Queue.queuelen--;
	if(PublishPackId_Queue.tail==PUBLISH_PACK_ID_QUEUE_MAXLEN)
		PublishPackId_Queue.tail=0;
	return 0x01;
}

MQTT_Msg_Queue_TypeDef Msg_Queue = {0,0,MSG_QUEUE_MAXLEN,{0}};


MQTT_Msg_TypeDef * MQTT_Msg_Get_Queue(void)
{
	MQTT_Msg_TypeDef *pMsg;
	if((Msg_Queue.tail==Msg_Queue.head)
		&&(Msg_Queue.queuelen==MSG_QUEUE_MAXLEN))
		return 0;	//队列无数据
	pMsg=Msg_Queue.pMsg[Msg_Queue.head];
	Msg_Queue.pMsg[Msg_Queue.head]=0;
	Msg_Queue.head++;
	Msg_Queue.queuelen++;
	if(Msg_Queue.head==MSG_QUEUE_MAXLEN)
		Msg_Queue.head=0;
	return pMsg;
}

uint8_t MQTT_Msg_Add_Queue(MQTT_Msg_TypeDef *pMsg)
{
	MQTT_Msg_TypeDef *ppMsg=NULL;
	if((Msg_Queue.tail==Msg_Queue.head)&&(Msg_Queue.queuelen==0))
	{
		ppMsg = MQTT_Msg_Get_Queue();
		if(ppMsg)
		{
			if(ppMsg->Data)
				SysMem_free(ppMsg->Data);		
			SysMem_free(ppMsg);
		}
	}
	Msg_Queue.pMsg[Msg_Queue.tail]=pMsg;
	Msg_Queue.tail++;
	Msg_Queue.queuelen--;
	if(Msg_Queue.tail==MSG_QUEUE_MAXLEN)
		Msg_Queue.tail=0;
	return 0x01;
}




MQTT_Msg_TypeDef * MQTT_Msg_Read_Queue(void)
{
	MQTT_Msg_TypeDef *pMsg;
	if((Msg_Queue.tail==Msg_Queue.head)
		&&(Msg_Queue.queuelen==MSG_QUEUE_MAXLEN))
		return NULL;	//队列无数据
	pMsg=Msg_Queue.pMsg[Msg_Queue.head];
	return pMsg;
}

//10ms
void MQTT_Publish_QOS1_Task(void)
{
	static u32 cycle_time = 0;
	MQTT_Msg_TypeDef * pMsg = NULL;
	
	if(cycle_time < 5*100)
	{
		cycle_time++;
		return;
	}
	else
	{
		cycle_time = 0;
	}
	pMsg = MQTT_Msg_Read_Queue();	//读取队头报文。
	if(pMsg != NULL)
	{
		if(PubackPackId.packid == pMsg->packid)	//收到发布确认
		{
			pMsg = MQTT_Msg_Get_Queue();		//删除消息
			if(pMsg)
			{	
				if(pMsg->Data)
					SysMem_free(pMsg->Data);
				SysMem_free(pMsg);
			}
			return ;
		}
		else
		{
			if(CloudProtocol_ReadLink())		//通信正常时，发送
			{
				MQTT_Send_Publish(pMsg);	//发布消息
				pMsg->SendSn++;
			}
		}
		
		if(pMsg->SendSn > 20)			//重发超过20次
		{
			pMsg = MQTT_Msg_Get_Queue();		//删除消息
			if(pMsg)
			{	
				if(pMsg->Data)
					SysMem_free(pMsg->Data);
				SysMem_free(pMsg);
			}
			return ;
		}
		
		if(pMsg->qos != MQTT_QOS1 
			|| pMsg->Topic == NULL 
			|| pMsg->TopicSize == 0x00 
			|| pMsg->Data == NULL)	//报文错误
		{
			pMsg = MQTT_Msg_Get_Queue();		//删除消息
			if(pMsg)
			{	
				if(pMsg->Data)
					SysMem_free(pMsg->Data);
				SysMem_free(pMsg);
			}
			return ;
		}
	}
}


//QOS1	发布应答任务  10ms
void MQTT_Puback_Task(void)
{
	MQTT_RecivePublishPackId_TypeDef * pPublishPackId = NULL;//不加限制，只要能发出就发，避免数据堆积
	pPublishPackId = MQTT_RecivePublishPackId_Get_Queue();	//从队列中取出报文ID，发关服务器，本报文已消费，停止重发。
	if(pPublishPackId != NULL)
	{
		MQTT_Send_Puback(pPublishPackId->packid);
		SysMem_free(pPublishPackId);	//释放内存
	}
}

void MQTT_QOS1_Task(void)
{
	MQTT_Publish_QOS1_Task();
	MQTT_Puback_Task();
}

