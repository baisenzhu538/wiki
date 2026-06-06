#include "rs232api.h"
#include "usart.h"

void (*pRs232Api_GetApiData)(uint8_t* Data,uint16_t size)=NULL;

void Rs232Api_SetReceiveCallBackFun(void (*pFun)(uint8_t* Data,uint16_t size))
{
	pRs232Api_GetApiData=pFun;
}



uint8_t DataPackBuf[sizeof(Rs232DataPackTypeDef)];
uint16_t DataPackBufSize=0;
void Rs232Api_ReceiveByte(uint8_t Data)
{
	Rs232DataPackTypeDef *pDataPack;
	if(DataPackBufSize<0x02)
  {
		if(Data==0xAA)
		{
			DataPackBufSize=0x00;
			DataPackBuf[DataPackBufSize++]=Data;
		}
		else if(DataPackBufSize==0x01)
		{
		 if(Data==0xBB)
			DataPackBuf[DataPackBufSize++]=Data;
		 else//数据包头错误，清除数据包头
			DataPackBufSize=0x00;
	  }
	}
  else
	{
		DataPackBuf[DataPackBufSize++]=Data;
		pDataPack=(Rs232DataPackTypeDef *)DataPackBuf;
		if(DataPackBufSize>0x03)
		{
			if(pDataPack->Head.datalen>RS232DRIVE_DATAPACK_MAXSIZE)
			{
				DataPackBufSize=0x00;//接收数据异常
				return;
			}
			if((pDataPack->Head.datalen+12)==DataPackBufSize)
			 {
				 if(pRs232Api_GetApiData)
					pRs232Api_GetApiData(DataPackBuf,DataPackBufSize);
				 DataPackBufSize=0x00;
			 }
	  }
	}		
}

void Rs232Api_ReceiveFrame(uint8_t *Data,uint16_t size)
{
	uint16_t i;
	for(i=0;i<size;i++)
	{
		Rs232Api_ReceiveByte(Data[i]);
	}
}

//10ms定时器任务
void Rs232Api_TimeTask(void)
{
//Usart_TimeTask(COM3);
}

uint8_t Rs232Api_SendData(uint8_t *Data,uint16_t size)
{
  return Uart_SendData(COM3,Data,size);
}

void Rs232Api_UartInit(void)
{
	SerialDevice_Init(COM3);
	SerialDevice_SetReceiveFrameCallBack(COM3,Rs232Api_ReceiveFrame);
}