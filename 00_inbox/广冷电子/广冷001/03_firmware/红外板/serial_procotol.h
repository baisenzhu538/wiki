#ifndef __SERIAL_PROCOTOL_H
#define __SERIAL_PROCOTOL_H
#include "usart.h"
#include "sell_app.h"

#define PCK_HEAD_LEN  8
#define PCK_BUFF_NUM  3
#define PCK_TX_NUM    2//重复发送次数
#define PCK_RESP_TIME 10//响应超时10ms*5
#define CYC_TX_TIME   100 //10ms*100
typedef struct 
{
	uint8_t  funcid;
	uint8_t  resid;
	uint8_t  command;
	uint8_t  receve;
	uint16_t sn;         //流水码
	uint16_t packet_size;
}SerialPacketHeadTypeDef;

typedef struct
{
	uint32_t m_errstate;
	uint8_t  body_s;
  uint8_t  body_e;
  uint8_t  ir1_e;
  uint8_t  ir2_e;
  uint8_t  door_s;
  uint8_t  door_e;
  uint8_t  sell_s;
  uint8_t  receve2;	
}Device_SysStateTypedef;

typedef struct 
{
  SerialPacketHeadTypeDef   pckhead;
	uint8_t databuf[512];
}SerialPacketTypeDef;

typedef struct 
{
 SerialPacketTypeDef PackBuf;
 uint8_t BufState;//状态位位
 uint8_t Ack;     //响应位
 uint8_t txnum;   //重复发送次数
 uint8_t RespTime;//响应超时时间
 uint8_t resperr;
}SerialTxBufTypeDef;

typedef struct 
{
 uint8_t TaskRunState;//任务运行状态
 uint8_t CycTxTime;   //循环任务时间
 uint8_t CycTimeCount;//循环任务计时10ms一周期
 uint8_t receve;
}SerialTaskTypeDef;

void SerialProcotol_Init(void);
void SerialProcotol_TaskRun(void);
void SerialProcotol_TimeTask(void);
void Procotol_Memcopy(uint8_t* pd_data,uint8_t* ps_data,uint16_t datalen);
uint8_t SerialProcotol_SendCmd(uint8_t funcid,uint8_t errid,uint8_t cmd,uint16_t sn,uint8_t *data,uint16_t datasize);

#endif
