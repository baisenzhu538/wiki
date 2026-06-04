#include "transport_api.h"


uint8_t TransportApi_SendData(DeviceTransport_ProtocolBuffTypeDef *pBuff)
{
	if(Rs232Drive_SendData((uint8_t*)pBuff,pBuff->protocolhead.pakesize+sizeof(ProtocolHeadTypeDef))==0xFF)
		return 0xFF;
	return 0x00;
}


uint8_t TransportApi_ReceiveData(uint8_t *Data,uint16_t size)
{
	DeviceTransport_ProtocolBuffTypeDef *pRxBuff;
	if(size<sizeof(ProtocolHeadTypeDef))
		return 00;
	else
	{ 
		pRxBuff=SysMem_malloc(size);
		if(pRxBuff!=NULL)
		{
		 SysMem_copy((void*)pRxBuff,Data,size);
	   if(DeviceTranspot_AddRxMsg(pRxBuff)==DEVICE_QUEUE_FULL)
		 {
			 SysMem_free(pRxBuff);
			 return 0x01;
		 }
		 else
			return 0xFF;
		}
		return 0x02;
	}
}










