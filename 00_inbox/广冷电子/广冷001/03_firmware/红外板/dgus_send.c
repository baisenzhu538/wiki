#include "dgus_send.h"


DgusDataPack_TypeDef	DgusDataSendPack;
u8 DgusDataSendPackBuffer[DGUS_DATA_BUFFER_MAX_SIZE];


static void Dgus_UartSend(DgusDataPack_TypeDef * pDgusDataPack)
{
	u8	i;
	u8 index = 0;
			
	DgusDataSendPackBuffer[index] = pDgusDataPack->FixHead/256;
	index++;
	
	DgusDataSendPackBuffer[index] = pDgusDataPack->FixHead%256;
	index++;
	
	DgusDataSendPackBuffer[index] = pDgusDataPack->DataLenth;
	index++;
	
	DgusDataSendPackBuffer[index] = pDgusDataPack->Cmd;
	index++;
	
	for(i=0;i<(pDgusDataPack->DataLenth-3);i++)
	{
		DgusDataSendPackBuffer[index] = pDgusDataPack->Data[i];
		index++;
	}
	
	DgusDataSendPackBuffer[index] = pDgusDataPack->Crc16/256;
	index++;
	
	DgusDataSendPackBuffer[index] = pDgusDataPack->Crc16%256;
	index++;
	
	Uart_SendData(COM2,DgusDataSendPackBuffer,index);
}

static void Dgus_Cmd_Send(u8 cmd,u8 * data,u16 datasize)
{
	u8 i;
	
	DgusDataSendPack.FixHead = DGUS_FIX_HEAD;
	DgusDataSendPack.DataLenth = datasize+3;	//+3
	DgusDataSendPack.Cmd = cmd;
		
	for(i=0;i<datasize;i++)
	{
		DgusDataSendPack.Data[i] = *(data+i);
	}
	 
	DgusDataSendPack.Crc16 = CRC16_Toggle(&DgusDataSendPack.Cmd,(DgusDataSendPack.DataLenth-2));
	
	Dgus_UartSend(&DgusDataSendPack);	
}

void Dgus_83ReadCmd_Send(u8 * data,u16 datasize)
{
	DgusRecive_Set_82Ack(*data+*(data+1));	
	Dgus_Cmd_Send(DGUS_READ_CMD,data,datasize);
}

void Dgus_82WriteCmd_Send(u8 * data,u16 datasize)
{
	DgusRecive_Set_82Ack(*data+*(data+1));
	Dgus_Cmd_Send(DGUS_WRITE_CMD,data,datasize);
}

