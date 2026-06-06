#ifndef __MASTE_PROTOCO_H
#define __MASTE_PROTOCO_H
#include "transport_layer.h"
#include "funcid_define.h"
#include "device_manage.h"
#include "data_struct.h"
#include "response_task.h"
#include "node_info.h"
#include "index_table.h"

#define MASTEHEART_SENDFTIME_TIMENUM 0x08
#define MASTEHEART_SENDTIME          CAN_MASTERHEART_TXTIME  //心跳发送定时


void MasteProtoco_Init(void);
void CanMaste_RollRun(void);

uint8_t MasteProtoco_ReadPort(uint8_t nodeid,uint8_t sounrcid,void *data);
uint8_t MasteProtoco_WritePort(uint8_t nodeid,uint8_t sounrcid,void *data,uint8_t datasize);

uint8_t MasteProtoco_WriteSerialPort(uint8_t devicenum,uint16_t devicetype,uint8_t sounrcid,void *data,uint8_t datasize);

#endif

