#ifndef __DEVICE_TRANSPORT_H
#define __DEVICE_TRANSPORT_H
#include "stm32f10x.h"
#include "sys_malloc.h"


#define ERR_RESEND_NUM 3//重发次数
#define SN_TABLE_MAX   32
#define DEVICETRANSPORT_BUFF_MAXSIZE 400
#define DEVICETRANSPORT_QUEUE_MAXLEN 20
typedef struct
{
	uint16_t tx_sn;          //发送报文sn滚码
	uint8_t  rx_sn_tablehead;//接收sn码记录表表头
	uint8_t  rx_sn_tabletail;//接收sn码记录表表尾
	uint16_t rx_sn_table[SN_TABLE_MAX];
}DeviceTransport_SnManageTypeDef;


typedef struct
{
 	uint16_t srcdev_type;
	uint16_t destdev_type;
	uint8_t  srcdev_no;
	uint8_t  destdev_no;
	uint8_t  func_id;
	uint8_t  command;
	uint16_t sn;
	uint16_t pakesize;
}ProtocolHeadTypeDef;

typedef struct 
{
  ProtocolHeadTypeDef protocolhead;
	uint8_t Data[DEVICETRANSPORT_BUFF_MAXSIZE];
}DeviceTransport_ProtocolBuffTypeDef;



#define DEVICE_RXQUEUE_MAXLEN 20
#define DEVICE_TXQUEUE_MAXLEN 20

#define DEVICE_QUEUE_FULL   0x01
#define DEVICE_QUEUE_NULL   0x01
#define DEVICE_QUEUE_ADD    0xFF
#define DEVICE_QUEUE_GET    0xFF


typedef struct 
{
 uint8_t head;
 uint8_t tail;
 uint8_t queuelen;
 uint8_t maxlen;
 DeviceTransport_ProtocolBuffTypeDef *pRxBuff[DEVICE_RXQUEUE_MAXLEN];
}DeviceTransport_BuffQueueTypeDef;

uint16_t DeviceTransport_GetTxSn(void);
uint8_t  DeviceTransport_CompareRxSn(uint16_t sn);

DeviceTransport_ProtocolBuffTypeDef * DeviceTranspot_GetRxMsg(void);
uint8_t DeviceTranspot_AddRxMsg(DeviceTransport_ProtocolBuffTypeDef *pRxBuff);
DeviceTransport_ProtocolBuffTypeDef * DeviceTranspot_GetTxMsg(void);
uint8_t DeviceTranspot_AddTxMsg(DeviceTransport_ProtocolBuffTypeDef *pTxBuff);

void DeviceTransport_TxTask(void);

#endif
