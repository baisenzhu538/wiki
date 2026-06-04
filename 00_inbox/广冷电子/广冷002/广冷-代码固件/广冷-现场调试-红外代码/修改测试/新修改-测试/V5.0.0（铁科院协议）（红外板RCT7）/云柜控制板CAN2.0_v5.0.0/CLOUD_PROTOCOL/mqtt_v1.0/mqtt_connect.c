#include "mqtt_connect.h"


MqttDownPara_TypeDef	MqttDownPara;

MQTT_ConnectManage_TypeDef	MQTT_ConnectManage = {0x01,0x00,0x00,0x01,MQTT_SESSION_RETAIN_TIME * 100};

uint8_t MQTT_Get_Start_Status(void)
{
	return MQTT_ConnectManage.Link;
}

//10ms定时任务
void MQTT_Session_Task(void)
{
	if(MQTT_ConnectManage.Link)
	{
		MQTT_ConnectManage.DeadlineTime = 0;
		MQTT_ConnectManage.SessionState = 0x00;
	}
	else
	{
		if(MQTT_ConnectManage.DeadlineTime < MQTT_SESSION_RETAIN_TIME * 100)	
		{
			MQTT_ConnectManage.DeadlineTime++;
			MQTT_ConnectManage.SessionState = 0x00;	//离线时长未超过会话保留时长,下次连接不重新订阅
		}
		else
		{
			MQTT_ConnectManage.SessionState = 0x01;	//离线时长超过会话保留时长，下次连接时重新订阅
		}
	}
}


void MQTT_Down_Set(MqttDownPara_TypeDef	* pMqttDownPara)
{
	MqttDownPara.DownEn = pMqttDownPara->DownEn;
	MqttDownPara.DownTime = pMqttDownPara->DownTime;
	MqttDownPara.DownMaxTime = pMqttDownPara->DownMaxTime;
}
//10ms任务
void MQTT_Down_Task(void)
{
	if(MqttDownPara.DownEn)
	{		
		if(MqttDownPara.DownTime > 10*100)
			MQTT_ConnectManage.enable = 0x00;	
		if(MqttDownPara.DownTime < (MqttDownPara.DownMaxTime+10)*100)
			MqttDownPara.DownTime++;
		else
		{
			MqttDownPara.DownEn = 0;
			MQTT_ConnectManage.enable = 0x01;	
			MqttDownPara.DownTime = 0;
			Iap_SysReset();//系统复位
		}
	}
}

void MQTT_Add_Subcribe(uint8_t * Topic, uint8_t TopicLen, uint8_t Qos)
{
	MQTT_TopicUint_TypeDef topic_uint;
	topic_uint.topic_qos = Qos;
	topic_uint.topic_lenth = TopicLen;
	SysMem_copy(topic_uint.topic_string, Topic, TopicLen);
	MQTT_SubscribeTopicTable_AddUint(&topic_uint);
}


void MQTT_CleanSession_Flag(void)
{
	MQTT_ConnectManage.DeadlineTime = MQTT_SESSION_RETAIN_TIME * 100;
	MQTT_ConnectManage.SessionState = 0x01;
}

void MQTT_Start_Reset(void)
{
	MQTT_ConnectManage.Link = 0x00;
	MQTT_ConnectManage.step = 0x00;
	MQTT_ReciveStatus.Connack.ConnackFlag = 0x00;
	MQTT_ReciveStatus.Connack.ConnackSn = 0x00;
	MQTT_ReciveStatus.PingResp.PingRespFlag = 0x00;
	MQTT_ReciveStatus.PingResp.PingRespSn = 0x00;
	MQTT_ReciveStatus.Suback.SubackFlag = 0x00;
	MQTT_ReciveStatus.Suback.SubackSn = 0x00;	
}

void MQTT_Strat_Reboot(void)
{
	MQTT_CleanSession_Flag();
	MQTT_Start_Reset();
}

void MQTT_Start_Enable(void)
{
	MQTT_ConnectManage.enable = 0x01;
}

void MQTT_Start_Disable(void)
{
	MQTT_ConnectManage.enable = 0x00;
}


//10ms 秒定时任务
void MQTT_Start_Task(void)
{
	static uint32_t wait_time = 0;
	static uint8_t reply_num = 0;
	
	if(MQTT_ConnectManage.enable == 0x00)
		return;

	switch(MQTT_ConnectManage.step)
	{
		case 0x00://等待通信模块就绪
		{
			 if(WirelessModule_ReadRunStaus())	
			 {
				//去发送连接申请 
				MQTT_ConnectManage.step = 0x02;
			 }
		}
		break;
		case 0x12://等待连接断开
		{
			if(wait_time < MQTT_DISCONNECT_WAIT_TIME*100)
				wait_time++;
			else
			{
				wait_time = 0;
				MQTT_ConnectManage.step = 0x02;
			}
			if(MQTT_ReciveStatus.Connack.ConnackFlag)
				MQTT_ConnectManage.step = 0x03;
		}
		break;
		case 0x02://发送连接申请
		{					
			MQTT_Send_Connect();
//			MQTT_Send_CleanSession();
			MQTT_ConnectManage.step = 0x03;
		}
		break;
		case 0x03://等待连接应答
		{
			
			if(MQTT_ReciveStatus.Connack.ConnackFlag)
			{
				if(MQTT_ConnectManage.SessionState)
				{
					MQTT_ConnectManage.step = 0x04;
				}
				else
				{
					MQTT_ConnectManage.step = 0x06;
					MQTT_ConnectManage.Link = 0x01;
				}
				wait_time = 0;
				reply_num = 0;
			}
			else
			{
				if(wait_time < MQTT_CONNECT_WAIT_TIME*100)
				{
					wait_time++;
				}
				else
				{
					wait_time = 0;
					if(reply_num < MQTT_SEND_CONNECT_MAX_NUM)
					{
						reply_num++;
//						if(WirelessModuleInit.TypeNum == 0x01)	
//						{
//							MQTT_Send_DisConnect();
//							MQTT_ConnectManage.step = 0x12;							
//						}
//						else
//						{
							MQTT_ConnectManage.step = 0x02;
//						}
					}
					else
					{
						reply_num = 0;
						MQTT_ConnectManage.step = 0x08;
					}
				}
			}
		}
		break;	
		case 0x04://发送订阅申请
		{
			MQTT_Send_Subscribe();
			MQTT_ConnectManage.step = 0x05;
		}
		break;
		case 0x05://等待订阅应答
		{
			if(MQTT_ReciveStatus.Suback.SubackFlag)
			{
				MQTT_ConnectManage.Link = 0x01;
				MQTT_ConnectManage.step = 0x06;
				wait_time = 0;
				reply_num = 0;
			}
			else
			{
				if(wait_time < MQTT_SUBSCRIBE_WAIT_TIME*100)
				{
					wait_time++;
				}
				else
				{
					wait_time = 0;
					if(reply_num < MQTT_SEND_SUBSCRIBE_MAX_NUM)
					{
						reply_num++;
						MQTT_ConnectManage.step = 0x04;
					}
					else
					{
						MQTT_ReciveStatus.Connack.ConnackFlag = 0x00;
						MQTT_ConnectManage.step = 0x02;
						reply_num = 0;
					}
				}
			}										
		}
		break;
		case 0x06://发送心跳申请
		{
			MQTT_Send_PingReq();
			MQTT_ConnectManage.step = 0x07;
		}
		break;
		case 0x07:	//心跳维持
		{		
			if(wait_time < MQTT_HEART_WAIT_TIME*100)
			{
				wait_time++;
			}
			else
			{
				wait_time = 0;
				if(MQTT_ReciveStatus.PingResp.PingRespFlag)
				{
					reply_num = 0;
					MQTT_ReciveStatus.PingResp.PingRespFlag = 0x00;
					MQTT_ConnectManage.step = 0x06;
				}
				else
				{
					if(reply_num < MQTT_SEND_HEART_MAX_NUM)
					{
						reply_num++;
						MQTT_ConnectManage.step = 0x06;
					}
					else
					{
						MQTT_ReciveStatus.Connack.ConnackFlag = 0x00;
						MQTT_ReciveStatus.Suback.SubackFlag = 0x00;
						MQTT_ConnectManage.Link = 0x00;
						reply_num = 0;
//						if(WirelessModuleInit.TypeNum == 0x01)	
//						{
//							MQTT_Send_DisConnect();
//							MQTT_ConnectManage.step = 0x12;							
//						}
//						else
//						{
							MQTT_ConnectManage.step = 0x1F;
//						}
					}
				}
			}				
		}
		break;	
		case 0x08://清理会话
		{
			MQTT_Send_CleanSession();
			MQTT_ConnectManage.step = 0x09;
			MQTT_ConnectManage.DeadlineTime = MQTT_SESSION_RETAIN_TIME * 100;
			MQTT_ConnectManage.SessionState = 0x01;
		}
		break;
		case 0x09://等待清理会话
		{
			if(MQTT_ReciveStatus.Connack.ConnackFlag)
			{
				wait_time = 0;
				reply_num = 0;
				MQTT_ReciveStatus.Connack.ConnackFlag = 0x00;
				MQTT_ConnectManage.step = 0x02;
			}
			else
			{
				if(wait_time < MQTT_CLEAN_SESSION_WAIT_TIME*100)
				{
					wait_time++;
				}
				else
				{
					wait_time = 0;
					if(reply_num < MQTT_SEND_CLEAN_SESSION_MAX_NUM)
					{
						reply_num++;
						MQTT_ConnectManage.step = 0x08;
					}
					else
					{
						reply_num = 0;
						MQTT_ConnectManage.step = 0x1F;
						return;
					}
				}
			}
		}
		break;
		case 0x1F: //重连，并复位4G模块
		{
			CloudProtol_Manage_Struct_Clear();
			MQTT_Start_Reset();
			ESP32_Remove_All_SendData();
			WirelessModule_ResetModule();			
			
			MQTT_ConnectManage.step = 0x00;		
		}
		break;
	}
}


void MQTT_Connect_Task(void)
{
	MQTT_Session_Task();
	MQTT_Down_Task();
	MQTT_Start_Task();
}
