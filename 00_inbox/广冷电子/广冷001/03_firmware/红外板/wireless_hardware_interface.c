#include "wireless_hardware_interface.h"




//模块复位、电源引脚初始化
void WierlessHarware_ModuleInit(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;
		
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE);	 //使能PB,PE端口时钟
	
	GPIO_InitStructure.GPIO_Pin  = GPIO_Pin_1;				 //LED0-->PB.5 端口配置
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	GPIO_Init(GPIOC, &GPIO_InitStructure);					 //根据设定参数初始化GPIOB.5
	
	GPIO_ResetBits(GPIOC, GPIO_Pin_1);	
}

//模块复位、电源引脚初始化
//串口初始化
void WierlessHarware_InterfaceInit(void)
{
	WierlessHarware_ModuleInit();
	SerialDevice_Init(COM3);
}


//串口发送数据
uint8_t WierlessHarware_SendData(uint8_t *pData,uint32_t len)
{
	return Uart_SendData(COM3,pData,len);
}

//串口发送数据（带确认发完成、超时）
uint8_t WierlessOuttime_SendData(uint8_t *pData,uint32_t len, uint32_t outtime)
{
	WierlessHarware_SendData(pData, len);
	while(Uart_GetTxSate(COM3) && outtime--);
}

//串口获取接收数据的长度
uint16_t WierlessHarware_GetDataLen(void)
{
	return Uart_GetSate(COM3);
}

//串口获取接收数据指针
uint8_t WierlessHarware_GetData(uint8_t *pDataBuf)
{
	return Uart_GetData(COM3,pDataBuf);
}

//串口发送命令
uint8_t WirelesModule_sendcmd(char *cmd,char *res,uint32_t timeOut)
{
	static uint8_t sta=0;
	static uint32_t time;
	
	switch(sta)
	{
		case 0x00:
			{
				time=timeOut;
				WierlessHarware_SendData((unsigned char *)cmd, strlen((const char *)cmd));
				sta=0x01;
			}
			return 0x00;
			break;
		case 0x01:
			{
				//有接收数据
				if(WierlessHarware_GetDataLen())
				{
					char *p;
					
					//为接收到的数据分配内存
					p=SysMem_malloc(WierlessHarware_GetDataLen());
					if(p!=NULL)
					{						
						WierlessHarware_GetData((uint8_t *)p);
						sta=0x00;
						
						//比较指令应答
						if(strstr((const char *)p, res) != NULL)
						{
							SysMem_free(p);
							return 0xFF;//接收完成
						}
						SysMem_free(p);
					}
					return 0x00;  //接收未完成
				}
				else	//没有接收到数据
				{
					if(time)
					{
						time--;
					}
					else
					{
						sta=0x00;
						return 0xEE;//接收失败
					}
			   }
		   }
			return 0x00;      //接收未完成
			break;
	}
}




