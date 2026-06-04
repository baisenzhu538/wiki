#ifndef __DRIVE_API_H
#define __DRIVE_API_H	 
#include "data_struct.h"
#include "can_drive.h"
#include "transport_layer.h"

void Can_DriveInit(void);
void Can_MsgFilterSet(uint8_t LocalMacID,uint8_t FilterNum);
void Can_ReceiveMsg(CanRxMsg *pRxMessage);
uint8_t Can_SendMsag(CanMsgTypeDef *pMessage);
void Can_Receive(void);
#endif
