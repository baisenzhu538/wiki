#ifndef __TRANSPORT_API_H
#define __TRANSPORT_API_H
#include "stm32f10x.h"
#include "device_transport.h"
#include "rs232drive.h"

uint8_t TransportApi_SendData(DeviceTransport_ProtocolBuffTypeDef *pBuff);

uint8_t TransportApi_ReceiveData(uint8_t *Data,uint16_t size);
#endif
