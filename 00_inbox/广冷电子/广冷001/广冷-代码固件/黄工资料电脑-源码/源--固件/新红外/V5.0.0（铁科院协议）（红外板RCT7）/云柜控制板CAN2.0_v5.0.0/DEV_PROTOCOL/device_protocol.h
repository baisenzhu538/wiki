#ifndef __DEVICE_PROTOCOL_H
#define __DEVICE_PROTOCOL_H
#include "device_transport.h"
#include "maste_protoco.h"

#define DEVICE_SN_MAXLEN    16
#define DEVICE_ID_MAXLEN    12
#define DEVICE_HEARTOUTTIME 600 //心跳超时时间，6s定时
#define DEVICE_HEARTTIME    200 //心跳时间,2s定时
#define DEVICE_LINKTIME     400 //连接定时，4s定时

typedef struct
{
	uint16_t dev_typ;
	uint8_t  dev_no;
	uint8_t  receve;
	uint32_t ver;
	uint8_t  dev_id[DEVICE_ID_MAXLEN];
	uint8_t  dev_sn[DEVICE_SN_MAXLEN];
}DeviceInfoTypeDef;

typedef struct
{
	uint8_t  link_flag;    //连接标志位
	uint8_t  heart_flag;    //心跳标志位
	uint16_t heart_time;    //心跳计时
  uint16_t heart_outtime; //心跳超时
	uint16_t link_time;    //连接报文时间
}DeviceLinkInfoTypeDef;//设备连接信息

//typedef struct
//{
//	uint16_t Pack_Num;
//	uint16_t Pack_Size;
//  uint32_t CheckSum;
//	uint8_t  *Data;
//}DeviceFwDataTypeDef;

uint8_t mDeviceProtocol_ForwardTxMsg(uint8_t *data,uint16_t size);
uint8_t DeviceProtocol_TxResportMsg(uint8_t cmd,uint8_t *data,uint16_t size);
uint8_t DeviceProtocol_TxTriggerMsg(uint8_t cmd,uint8_t *data,uint16_t size);

void DeviceProtocol_SetUserCallBackFun(uint8_t (*pfFun)(uint8_t,uint8_t*,uint16_t));
void DeviceProtocol_SetDeviceInfo(DeviceInfoTypeDef *Info);
void DeviceProtocol_TaskRun(void);
void DeviceProtocol_TimeTask(void);
#endif
