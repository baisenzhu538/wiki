#ifndef __RS232DRIVE_H
#define __RS232DRIVE_H
#include "stm32f10x.h"
#include "sys_malloc.h"
#include "rs232api.h"

#define RS232DRIVE_PACKQUEUE_MAXLEN  20
#define RS232DRIVE_DATAPACK_MAXSIZE  512
#define RS232DRIVE_RES_OUTTIMENUM    3    //应答超时次数
#define RS232DRIVE_RES_OUTTIME       100   //100ms超时应答
#define RS232DRIVE_TXTABLE_MAXLEN    125

#define RS232_RXQUEUE_FULL    0x01
#define RS232_RXQUEUE_NULL    0x01
#define RS232_RXQUEUE_ADD     0xFF
#define RS232_RXQUEUE_GET     0xFF
#define RS232_RXQUEUE_MEMFULL 0x00

#define BigtoLittle32(A)                ((((uint32_t)(A)&0xff000000) >> 24)|(((uint32_t)(A)&0x00ff0000) >> 8)|(((uint32_t)(A)&0x0000ff00) << 8)|(((uint32_t)(A)&0x000000ff) << 24))
#define BigtoLittle16(A)                ((((uint16_t)(A)&0xff00)>>8)|(((uint16_t)(A)&0x00ff)<<8))   

typedef struct
{
	uint8_t  AA;
	uint8_t  BB;
	uint16_t datalen;
	uint32_t checksum;
}Rs232DataHeadTypeDef;

typedef struct
{
	Rs232DataHeadTypeDef Head;
	uint32_t             SN;
	uint8_t              Data[RS232DRIVE_DATAPACK_MAXSIZE];
}Rs232DataPackTypeDef;

typedef struct
{
	uint32_t             SN;
}Rs232SnManageTypeDef;

typedef struct
{
 uint8_t head;
 uint8_t tail;
 uint16_t queuelen;
 Rs232DataPackTypeDef *pDataPack[RS232DRIVE_PACKQUEUE_MAXLEN];
}Rs232RxQueueTypeDef;
typedef struct
{
	uint8_t               ack;      //应答位，0无需应答，1需应答
	uint8_t               txsta;    //发送标志位，1发送完成 0待发送
	uint8_t               outime;   //超时计时
	uint8_t               outtimenum;   //超时次数
	uint32_t              sn;
	Rs232DataPackTypeDef  *DataPack;     //待发送数据地址
}Rs232TxUintTypeDef; //串口发送单元

typedef struct _Rs232TxControlBlockTypeDef
{
	struct _Rs232TxControlBlockTypeDef *proir;
	struct _Rs232TxControlBlockTypeDef *next;
	Rs232TxUintTypeDef TxUint;
}Rs232TxControlBlockTypeDef;


typedef struct 
{
 Rs232TxControlBlockTypeDef *head;
 Rs232TxControlBlockTypeDef *tail;
  uint32_t table_len;                         //任务表长度
}Rs232TxControlTableTypeDef;


#define Rs232Drive_SetTxState(p)    p->txsta=0x01
#define Rs232Drive_ResetTxState(p)  p->txsta=0x00
#define Rs232Drive_GetAckFlag(p)    p->ack

void Rs232Drive_Init(void);
void Rs232Drive_TaskRun(void);
void Rs232Drive_TimeTask(void);
uint8_t Rs232Drive_SendData(uint8_t *Data,uint16_t size);
void Rs232Drive_SetUserReceiveFun(uint8_t (*pFun)(uint8_t*,uint16_t));
#endif
