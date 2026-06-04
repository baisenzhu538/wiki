#include "esp32.h"



u8 ESP32RssiSta=0;

u8 ESP32Harware_ReadRssiSta(void)
{
	return ESP32RssiSta;
}

u8 ESP32Harware_ResetModule(void)
{
	return 0xFF;
}

u8 ESP32Harware_PowerReset(void)
{
	static u16 count = 0;
	static u8 mode = 0;
	switch(mode)
	{
		case 0x00:
			{
				count = 0;
				ESP32_PWR_CTL = 0;
				mode = 1;
			}
			break;
		case 0x01:
			{
				count++;
				if(count > 200)
				{
					count = 0;
					mode = 2;
				}
			}
			break;
		case 0x02:
			{
				ESP32_PWR_CTL = 1;
				mode = 3;
			}
			break;
		case 0x03:
			{
				count++;
				if(count > 200)
				{
					count = 0;
					mode = 0;
					return 0xFF;
				}
			}
			break;
	}
	return 0x00;
}


NetworkPara_TypeDef	ESP32NetworkPara = {"39.96.10.250","11883","TCP"};
u8 ESP32_CIPSTART_AT_CMD[100];

WifiApPara_TypeDef	ESP32WifiApPara = {"crgtVending","123456789"};
u8 ESP32_CWJAP_AT_CMD[100];


u8	utf8_buf[32];
u8 ESP32_Init(void)
{
	static u8 res1 = 0;
	static u8 res2 = 0;
	static u8 first_flag = 1;
	
	if(first_flag)
	{
		first_flag = 0;
		AuxConfig_GetNetWorkPara(&ESP32NetworkPara);
		memset((char*)ESP32_CIPSTART_AT_CMD,0,100);
//		sprintf((char*)ESP32_CIPSTART_AT_CMD,
//				"AT+CIPSTART=\"TCP\",\"%s\",%s\r\n",
//				(char*)ESP32NetworkPara.IPaddress, 
//				(char*)ESP32NetworkPara.port);
		sprintf((char*)ESP32_CIPSTART_AT_CMD,
				"AT+CIPSTART=\"TCP\",\"%s\",%s\r\n",
				(char*)"39.96.10.250", 
				(char*)"11883");
		
		
		AuxConfig_Get_WifiApPara(&ESP32WifiApPara);
				
		wifiSsid_GB2312_TO_UTF8(utf8_buf,ESP32WifiApPara.ssid,strlen(ESP32WifiApPara.ssid));
				
		memset((char*)ESP32_CWJAP_AT_CMD,0,100);		
		sprintf((char*)ESP32_CWJAP_AT_CMD,
				"AT+CWJAP=\"%s\",\"%s\"\r\n",
				(char*)utf8_buf, 
				(char*)ESP32WifiApPara.pwd);		
	}
	if(ESP32Harware_PowerReset())
	{
		res2 = 0xFF;
	}
	if(res2 == 0xFF)
	{
		res2 = 0;
		return 0xFF;
	}
	return 0x00;
}


u8 ESP32_ConfigModule(void)
{
	static u8 step  = 0;
	static u8 reply_num = 0;
	static u8 reply_num2 = 0;	
	static u16 wait_time = 0;
	static u8 reset_mode;
	u8 res = 0;
	
	switch(step)
	{
		case 0x00://查WIFI模式
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CWMODE?\r\n",strlen("AT+CWMODE?\r\n"));
			step = 0x01;
		}
		break;
		case 0x01:
		{
			if(strstr((char*)Uart3_RxBuf,"+CWMODE"))
			{
				if(strstr((char*)Uart3_RxBuf,"+CWMODE:1"))
				{	
					step = 0x04;
					wait_time = 0;
					reply_num = 0;
				}
				else
				{
					step = 0x02;
					wait_time = 0;
					reply_num = 0;
				}
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x00;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x02://发送AT+CWMODE=1,设置WIFI模式为station
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CWMODE=1\r\n",strlen("AT+CWMODE=1\r\n"));
			step = 0x03;
		}
		break;
		case 0x03://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x04;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x02;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x04://查AP连接
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CWJAP?\r\n",strlen("AT+CWJAP?\r\n"));
			step = 0x05;
		}
		break;
		case 0x05:
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				if(strstr((char*)Uart3_RxBuf,"+CWJAP:"))
				{
					step = 0x09;	
				}
				else
				{
					step = 0x06;	
				}
				
				wait_time = 0;
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x04;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x06://发送AT+CWJAP，连接到AP
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)ESP32_CWJAP_AT_CMD,strlen((char*)ESP32_CWJAP_AT_CMD));
			step = 0x07;
		}
		break;
		case 0x07://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"WIFI CONNECTED"))	//收到
			{
				step = 0x08;	
				wait_time = 0;	
				reply_num = 0;
			}
			else
			{
				wait_time++;
				if(wait_time > 5*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x06;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		
		case 0x08://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x09;	
				wait_time = 0;	
				reply_num = 0;
			}				
			else
			{
				wait_time++;
				if(wait_time > 5*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x09;	
				}
			}
		}
		break;
		
		case 0x09://配置SNTP
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIPSNTPCFG=1,-8,\"ntp.aliyun.com\"\r\n",
									strlen("AT+CIPSNTPCFG=1,-8,\"ntp.aliyun.com\"\r\n"));
			step = 0x0A;	
		}
		break;
		case 0x0A://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x0B;	
				wait_time = 0;	
				reply_num = 0;
			}				
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x09;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		
		case 0x0B://关闭TCP连接
		{
//			memset((char*)Uart3_RxBuf,0,512);
//			WierlessHarware_SendData((u8*)"AT+CIPCLOSE\r\n",
//									strlen("AT+CIPCLOSE\r\n"));
			step = 0x0C;	
		}
		break;
		case 0x0C:
		{
//			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
//			{
				step = 0x0D;	
//				wait_time = 0;	
//				reply_num = 0;
//			}				
//			else
//			{
//				wait_time++;
//				if(wait_time > 3*100)	//3秒重试
//				{
//					wait_time = 0;		
//					step = 0x0B;	
//					reply_num++;
//					if(reply_num > 3)	//重试5次
//					{
//						reply_num = 0;
//						step = 0xEE;
//					}
//				}
//			}
		}
		break;
		
		case 0x0D://发送AT+CIPSTART,连接到TCP
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)ESP32_CIPSTART_AT_CMD,
										strlen((char*)ESP32_CIPSTART_AT_CMD));
			step = 0x0E;
		}
		break;
		case 0x0E://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"CONNECT")
				|| strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x00;	
				wait_time = 0;	
				reply_num = 0;
				reply_num2 = 0;
				return 0xFF;
			}
			else if(strstr((char*)Uart3_RxBuf,"ERROR"))
			{
				if(reply_num2<3)
				{
					reply_num2++;
					wait_time = 0;		
					reply_num = 0;
					step = 0x0F;	//去复位
				}
				else
				{
					wait_time = 0;		
					reply_num = 0;
					reply_num2 = 0;
					step = 0xEE;	//去复位
				}			
			}
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x0D;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;	//去复位
					}
				}
			}
		}
		break;
		case 0x0F://关闭TCP连接
		{
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+CIPCLOSE\r\n",
									strlen("AT+CIPCLOSE\r\n"));
			step = 0x10;	
		}
		break;
		case 0x10:
		{
			if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
			{
				step = 0x0D;	
				wait_time = 0;	
				reply_num = 0;
			}				
			else
			{
				wait_time++;
				if(wait_time > 3*100)	//3秒重试
				{
					wait_time = 0;		
					step = 0x0F;	
					reply_num++;
					if(reply_num > 3)	//重试5次
					{
						reply_num = 0;
						step = 0xEE;
					}
				}
			}
		}
		break;
		default://复位模块 0xEE
		{
			switch(reset_mode)
			{
				case 0:
					{
//						res = ESP32Harware_ResetModule();		//硬件复位
//						if(res == 0xFF)
							reset_mode = 1;
					}
					break;
				case 1:
					{
						res = ESP32Harware_PowerReset();		//掉电
						if(res == 0xFF)
						{
							wait_time=0;
							reset_mode = 2;
						}
					}
					break;
				case 2:
					{
						if(wait_time<1000)
						{
							wait_time++;
						}
						else
						{
							wait_time = 0;
							step = 0x00;
							reset_mode = 0;
						}
					}
					break;
			}	
		}
		break;
		
	}
	return 0x00;
}

u8 ESP32_CheckModule(void)
{
	static u8 mode = 0;
	static u16 reply_num = 0;
	static u16 wait_time = 0;
		
	switch(mode)
	{
		case 0://查模块型号
		{	
			memset((char*)Uart3_RxBuf,0,512);
			WierlessHarware_SendData((u8*)"AT+GMR\r\n",strlen("AT+GMR\r\n"));
			mode = 1;
		}
		break;
		case 1://等待响应
		{
			if(strstr((char*)Uart3_RxBuf,"WROOM-32"))	//收到
			{
				mode = 0;	//
				wait_time = 0;	
				reply_num = 0;
				return 0xFF;
			}
			else
			{
				wait_time++;
				if(wait_time > 1*100)	//3秒重试
				{
					wait_time = 0;		
					mode = 0;	
					reply_num++;
					if(reply_num > 5)	//重试5次
					{
						reply_num = 0;
						mode = 0;	
						return 0xEE;
					}
				}
			}
		}
		break;
		default:return 0xEE;
	}
	return 0x00;	
}



char ESP32_ReciveParsing(u8 * data,u16 size)
{
	static u8 step = 0x00;
	char * p = NULL;
	char * rdata;
	u16 rsize;
	switch(step)
	{
		case 0x00:
		{
			p = strstr((char*)Uart3_RxBuf, "+IPD,");			
			if(p)
			{
				rdata = strstr((char*)p,":")+1;
				p = strstr((char*)Uart3_RxBuf, "+IPD,");
				if(p)
				{
					rsize = atoi(p+strlen("+IPD,"));
					MQTT_Pack_Json_Cut((u8*)rdata,rsize);
//					memset((char*)Uart3_RxBuf,0,512);
					while(0);
				}
				
			}
		}
		break;
	}
	return NULL;	
}






char ESP32_ReadAtSta(void)
{
	return NULL;
}


ESP32TxControlTableTypeDef	ESP32TxControlTable = {NULL,NULL,NULL};

//添加数据到队列
u8 ESP32_Add_SendData(u8 * data, u16 size)
{
	ESP32TxControlBlockTypeDef * pTxBlock;
	if(ESP32TxControlTable.table_len == ESP32_TXTABLE_MAXLEN)
		return 0x00;
	
	pTxBlock = (ESP32TxControlBlockTypeDef*)SysMem_malloc(sizeof(ESP32TxControlBlockTypeDef));
	if(pTxBlock == NULL)
		return 0x00;
	pTxBlock->TxUint.lenth = size;
	SysMem_copy((u8*)&pTxBlock->TxUint.data, data, size);
	if(ESP32TxControlTable.head == NULL)
	{
		pTxBlock->next = NULL;
		pTxBlock->proir = NULL;
		ESP32TxControlTable.head = pTxBlock;
		ESP32TxControlTable.tail = pTxBlock;
		ESP32TxControlTable.table_len++;
	}
	else
	{
		pTxBlock->next = NULL;
		ESP32TxControlTable.tail->next = pTxBlock;
		pTxBlock->proir = ESP32TxControlTable.tail;
		ESP32TxControlTable.tail = pTxBlock;
		ESP32TxControlTable.table_len++;
	}
	return 0xFF;
}

//从队列中获取数据
ESP32TxUintTypeDef * ESP32_Get_SendData(void)
{
	if(ESP32TxControlTable.head == NULL)
		return NULL;
	return &ESP32TxControlTable.head->TxUint;
}

//从队列中删除数据
u8 ESP32_Remove_SendData(void)
{
	ESP32TxControlBlockTypeDef * pTxBlock;
	
	if(ESP32TxControlTable.head == NULL)
		return NULL;
	pTxBlock = ESP32TxControlTable.head;
	if(ESP32TxControlTable.head->next)
		ESP32TxControlTable.head->next->proir = NULL;
	ESP32TxControlTable.head = ESP32TxControlTable.head->next;
	ESP32TxControlTable.table_len--;
	SysMem_free(pTxBlock);
	return 0xFF;
}

u8 ESP32_Remove_All_SendData(void)
{
	u8 i;
	for(i=0;i<10;i++)
	{
		if(!ESP32TxControlTable.table_len)
		{
			break;
		}
		else
		{
			ESP32_Remove_SendData();
		}
	}
}

char esp32_at_cmd_buffer[64];

//10ms

u8 esp32_send_enable=1;
void ESP32_SendData_Task(void)
{
	static u8 step;
	static u8 reply_num;
	static u16 wait_time;
	static ESP32TxUintTypeDef * pTxUint = NULL;
	
	if(!esp32_send_enable)
		return ;
	
	switch(step)
	{
		case 0x00://从队列中获取数据
		{
			pTxUint = ESP32_Get_SendData();
			if(pTxUint == NULL)
				return;
			step = 0x01;
		}
		break;
		case 0x01://请求发送数据
		{
			memset((char*)Uart3_RxBuf,0,512);
			memset((char*)Uart3_TxBuf,0,512);
			memset((char*)esp32_at_cmd_buffer,0,64);			
			sprintf(esp32_at_cmd_buffer,"AT+CIPSEND=%d\r\n",pTxUint->lenth);
			WierlessHarware_SendData((u8*)esp32_at_cmd_buffer,
										strlen(esp32_at_cmd_buffer));
			step = 0x02;
		}
		break;
		case 0x02://等待应答
		{
			if(strstr((char*)Uart3_RxBuf,">"))	//收到
			{
				step = 0x03;
				reply_num = 0;
				wait_time = 0;
			}
			else if(strstr((char*)Uart3_RxBuf,"ERROR"))
			{
				reply_num++;
				if(reply_num > 3)
				{
					reply_num = 0;
					CloudProtol_Manage_Struct_Clear();					
					MQTT_Start_Reset();
					ESP32_Remove_All_SendData();
					WirelessModule_ResetModule();
					step = 0xEE;
				}
			}
			else
			{
				if(wait_time < 100)
					wait_time++;
				else
				{
					wait_time = 0;
					reply_num = 0;
					step = 0x03;
//					reply_num++;
//					if(reply_num > 3)
//					{
//						reply_num = 0;
//						step = 0xEE;
//					}
//					else
//						step = 0x01;
				}
			}
		}
		break;
		case 0x03://发送数据内容
		{
			memset((char*)Uart3_RxBuf,0,512);
			memset((char*)Uart3_TxBuf,0,512);
			WierlessHarware_SendData(pTxUint->data,pTxUint->lenth);
			step = 0x04;
		}
		break;
		case 0x04://等待发送应答
		{
			if(strstr((char*)Uart3_RxBuf,"SEND OK"))	
			{
		
				step = 0xEE;
				reply_num = 0;
				wait_time = 0;
			}
			else
			{
				if(wait_time < 100)
					wait_time++;
				else
				{
					wait_time = 0;
//					reply_num++;
//					if(reply_num > 3)
//					{
//						reply_num = 0;
						step = 0xEE;
//					}
//					else
//						step = 0x03;
				}
			}
		}
		break;
		case 0xEE://从队列中删除
		{
			ESP32_Remove_SendData();
			step = 0x00;
		}
		default:while(0);
	}
}



char ESP32_Send_Data(u8 *data, u16 size)
{
	ESP32_Add_SendData(data, size);
	return 0xFF;
}

void ESP32_SNTP_Task(void)
{
	static u8 step;
	static u8 reply_num;
	static u16 wait_time;	
	static u32 cycle_time=40*100;
	u8 * pdata = NULL;
	Time_TypeDef ntpTime;
	
	if(cycle_time<60*100)
	{
		cycle_time++;
	}
	else
	{
		switch(step)
		{
			
			case 0:
			{
				esp32_send_enable = 0;				
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CWJAP?\r\n",
										strlen("AT+CWJAP?\r\n"));
				step = 1;
			}
			break;
			case 1:
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CWJAP:");
					if(pdata)
					{
						pdata = strstr((char*)Uart3_RxBuf,"-");
						if(pdata)
						{
							pdata += strlen("-"); 
							
							if(*pdata > 0x37)
							{
								ESP32RssiSta = 0;
							}
							else
							{
								ESP32RssiSta = 1;
							}
						}
					}
					
					step = 2;	
					wait_time = 0;	
					reply_num = 0;
				}				
				else
				{
					wait_time++;
					if(wait_time > 100)	//3秒重试
					{
						wait_time = 0;		
						step = 0;		
						reply_num = 0;
//						reply_num++;
//						if(reply_num > 3)	//重试5次
//						{
//							reply_num = 0;
//							step = 0;
							cycle_time = 0;
							esp32_send_enable = 1;
//						}
					}
				}
			}
			break;
			case 2://查SNTP时间
			{
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CIPSNTPTIME?\r\n",
										strlen("AT+CIPSNTPTIME?\r\n"));
				step = 3;
			}
			break;
			case 3://等待响应
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CIPSNTPTIME:");
					if(pdata)
					{
						pdata += strlen("+CIPSNTPTIME:Thu ");
						
						if(strstr((char*)Uart3_RxBuf,"Jan"))
						{
							ntpTime.month = 1;
						}
						else if(strstr((char*)Uart3_RxBuf,"Feb"))
						{
							ntpTime.month = 2;
						}
						else if(strstr((char*)Uart3_RxBuf,"Mar"))
						{
							ntpTime.month = 3;
						}
						else if(strstr((char*)Uart3_RxBuf,"Apr"))
						{
							ntpTime.month = 4;
						}
						else if(strstr((char*)Uart3_RxBuf,"May"))
						{
							ntpTime.month = 5;
						}
						else if(strstr((char*)Uart3_RxBuf,"Jun"))
						{
							ntpTime.month = 6;
						}
						else if(strstr((char*)Uart3_RxBuf,"Jul"))
						{
							ntpTime.month = 7;
						}
						else if(strstr((char*)Uart3_RxBuf,"Aug"))
						{
							ntpTime.month = 8;
						}
						else if(strstr((char*)Uart3_RxBuf,"Sept"))
						{
							ntpTime.month = 9;
						}
						else if(strstr((char*)Uart3_RxBuf,"Oct"))
						{
							ntpTime.month = 10;
						}
						else if(strstr((char*)Uart3_RxBuf,"Nov"))
						{
							ntpTime.month = 11;
						}
						else if(strstr((char*)Uart3_RxBuf,"Dec"))
						{
							ntpTime.month = 12;
						}
						if(ntpTime.month>12)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("May ");
						if(*pdata>=0x30&&*pdata<=0x39)
						{
							ntpTime.day = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%32;
							pdata += strlen("20 ");
						}
						else
						{
							pdata += strlen(" ");
							ntpTime.day = (*pdata-0x30);
							pdata += strlen("2 ");
						}
						
						if(ntpTime.day>31)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						ntpTime.hour = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%24;
						if(ntpTime.hour>23)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("11:");
						ntpTime.min = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%60;
						if(ntpTime.min>59)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("50:");
						ntpTime.sec = ((*pdata-0x30)*10+(*(pdata+1)-0x30))%60;
						if(ntpTime.sec>59)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						pdata += strlen("58 ");
						ntpTime.year = (*pdata-0x30)*1000+(*(pdata+1)-0x30)*100+(*(pdata+2)-0x30)*10+(*(pdata+3)-0x30)%10;
						if(ntpTime.year>2099)
						{
							wait_time = 0;		
							step = 0;	
							reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
								cycle_time = 0;
								esp32_send_enable = 1;
//							}
							return;
						}
						
						TimeStamp_UpData(&ntpTime);			//更新同步时间
						DgusApp_Set_Time(ntpTime.year%100,ntpTime.month,ntpTime.day,0,ntpTime.hour,ntpTime.min,ntpTime.sec);
					}
					
					reply_num = 0;
					step = 0;
					cycle_time = 0;
					esp32_send_enable = 1;
					
				}				
				else
				{
					wait_time++;
					if(wait_time > 100)	//3秒重试
					{
						wait_time = 0;		
						step = 0;	
						reply_num = 0;
//							reply_num++;
//							if(reply_num > 3)	//重试5次
//							{
//								reply_num = 0;
//								step = 0;
						cycle_time = 0;
						esp32_send_enable = 1;
//							}
						return;
					}
				}
			}
			break;
			default:break;
		}
	}
}

void ESP32_CheckCSQ_Task(void)
{
	static u8 step;
	static u8 reply_num;
	static u16 wait_time;	
	static u32 cycle_time=10*60*100;
	u8 * pdata = NULL;
	Time_TypeDef ntpTime;
	
	if(cycle_time<60*100)
	{
		cycle_time++;
	}
	else
	{
		switch(step)
		{
			case 0://查SNTP时间
			{
				esp32_send_enable = 0;
				memset((char*)Uart3_RxBuf,0,512);
				WierlessHarware_SendData((u8*)"AT+CWJAP?\r\n",
										strlen("AT+CWJAP?\r\n"));
				step = 1;
			}
			break;
			case 1://等待响应
			{
				if(strstr((char*)Uart3_RxBuf,"OK"))	//收到
				{
					pdata = strstr((char*)Uart3_RxBuf,"+CWJAP:");
					if(pdata)
					{
						pdata = strstr((char*)Uart3_RxBuf,",1,-");
						if(pdata)
						{
							pdata += strlen(",1,-"); 
							
							if(*pdata > 0x34)
							{
								ESP32RssiSta = 0;
							}
							else
							{
								ESP32RssiSta = 1;
							}
						}
					}
					
					step = 0;	
					wait_time = 0;	
					reply_num = 0;
					cycle_time = 0;
					esp32_send_enable = 1;
				}				
				else
				{
					wait_time++;
					if(wait_time > 3*100)	//3秒重试
					{
						wait_time = 0;		
						step = 0;	
						reply_num++;
						if(reply_num > 3)	//重试5次
						{
							reply_num = 0;
							step = 0;
							cycle_time = 0;
							esp32_send_enable = 1;
						}
					}
				}
			}
			break;
			default:break;
		}
	}	
}

void ESP32_TaskRun(void)
{
	ESP32_SendData_Task();
	if(WirelessModule_ReadRunStaus())
	{
		ESP32_SNTP_Task();
//		ESP32_CheckCSQ_Task();
	}
}