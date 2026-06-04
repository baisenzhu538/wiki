#ifndef __SELL_APP_H
#define __SELL_APP_H

#include "SellMotor.h"
#include "sensor.h"
#include "sys_malloc.h"
#include "lift_motor.h"
#include "device_protocol.h"
//#include "gate_control.h"
#include "err_code.h"
#include "time_stamp.h"

#define SELLERR_RUNNUM    1 //出货失败运行次数
#define SELLTASK_QUEULEN  20
#define SELL_DELAY        600//10ms一周期，共1s   //改2S

#define SELL_TARCK_OUTIME  20 //升降平台履带操作超时检测
#define SELL_CARGO_OUTTIME 30
#define SELL_LIFT_OUTTIME  20     //升降平台升降电机超时检测
#define SELL_LIFTREST_TIME 60*100 //60s无出货任务复位升降平台
#define	SELL_GATEREST_TIME	10*100	//10s无出货任务关闭闸门

#define SELL_SHELFSCAN_TIME 100   //10ms一周期,总计1s

#define SELL_IR_ERRNUM       2


#define SELL_STATE_GETTASK              0x00
#define SELL_STATE_DRIVELIFT_SHELF      0x01
#define SELL_STATE_DRIVECARGO           0x02
#define SELL_STATE_DRIVELIFT_PORT       0x03 //驱动升降平台到出货口
#define SELL_STATE_DRIVETARCK           0x04 //驱动升降平台履带
#define SELL_STATE_DRIVELIFT_ZERO       0x05
#define SELL_STATE_TARCKREVERSE         0x06

#define SELL_STATE_START_OPENGATE       0x07
#define SELL_STATE_START_CLOSEGATE      0x08
#define	SELL_STATE_STOP_CLOSEGATE		0x09

#define	SELL_STATE_START_OPENGATE_WAIT	0x0A
#define	SELL_STATE_START_CLOSEGATE_WAIT	0x0B
#define	SELL_STATE_STOP_CLOSEGATE_WAIT	0x0C

#define	SELL_STATE_STOP_ROUTE			0x0D
#define	SELL_STATE_START_ROUTE			0x0E

//#define SELL_STATE_ROUTE                0x09
//#define	SELL_STATE_WAIT					0x0A

//#define	SELL_STATE_OPENGATE_WAIT		0x0B
//#define	SELL_STATE_CLOSEGATE_WAIT		0x0C

typedef __packed struct 
{
	uint8_t contain_no;//货柜号
	uint8_t shelf_no;  //层架编号
	uint8_t cargo_no;  //货道编号
	uint8_t cargo_num;//出货次数
	int	code;
}SellIdTypeDef;

typedef  __packed struct 
{
	SellIdTypeDef SellId;
	uint8_t       sta;
	uint8_t       err_num;
	uint32_t      err[8];
	int	state;
}SellTaskStaTypeDef;


typedef void(*pTaskFinishCallBackTypeDef)(uint8_t,void*,uint16_t,uint64_t);
typedef	void(*pTaskFinishCallBack2TypeDef)(int,int);

typedef struct 
{
	uint8_t  Cmd;
	uint8_t  receve;
	uint64_t SN;
	SellIdTypeDef SellId;
	pTaskFinishCallBackTypeDef pTaskFinishCallBack;
	pTaskFinishCallBack2TypeDef	pTaskFinishCallBack2;
}SellTaskTypeDef;

typedef struct 
{
	SellTaskTypeDef  selltask[SELLTASK_QUEULEN];
	uint8_t  q_tail;
	uint8_t  q_head;
	uint8_t  q_len;
}SellTaskQueueTypeDef;

typedef struct
{
	SellTaskQueueTypeDef SellTask;
	uint8_t sell_flag;      //出货标志，0为未出货，1为已经出货
  uint8_t sell_state;     //出货状态，0空闲，1出货中
	uint8_t liftrest_flag;  //升降平台复位标志
	uint8_t gaterest_flag;
	
	uint16_t sell_delay;     //出货延时检测红外信号
	uint16_t tarck_outtime;  //履带操作超时
	uint16_t lift_outtimr;   //升降平台操作超时
	uint16_t cargo_outtime;  //货到出货超时
	uint16_t liftrest_time;  //升降电机复位时间
	uint16_t shelsantime;    //貨道扫描时间
	uint16_t taskwait_time;
	uint16_t gaterest_time;	//闸门复位时间
	uint16_t sellsta_time;
	uint16_t sellsta_flag;
	uint8_t cargo_s;        //货道状态，0空闲，1出货中，2出货完成
	uint8_t cargo_rn;       //货道出货次数
	uint8_t task_state;     //任务状态
	
	uint8_t sell_ir_errnum;    //连续出货错误次数
}Sell_TypeDef;

typedef struct
{
 uint8_t  contain_no;//货柜号
 uint8_t  shelf_no;  //层架编号
 uint16_t receve;
}Sell_ConfigCmdTypeDef;

typedef struct
{
 int32_t shelf_posit[3][16];
 int32_t port_posit[3];	
}Sell_ConfigTypeDef;

typedef struct 
{
	uint8_t  contain_num;
	uint8_t  receve1;
	uint16_t receve2;
	Sell_ConfigTypeDef sellconfig;
}Sell_ConfigResportTypeDef;

void SellApp_ResportShelfStyle(uint8_t cmd);
void SellApp_Init(void);
void SellApp_Task(void);
void SellApp_TimeTask(void);//10ms调用一次
uint8_t SellApp_SetSellTask(uint8_t cmd,void* pData,uint64_t sn,void (*pFun)(uint8_t,void*,uint16_t,uint64_t));
uint8_t SellApp_GetSellState(void);
void SellApp_ConfigCmd(uint8_t cmd,Sell_ConfigCmdTypeDef *pConfigCmd);
void SellApp_ResportConfig(uint8_t cmd);
uint8_t SellApp_GetSellTaskQueueOverLenth(void);

extern void SellHistory_Add(Time_TypeDef *pTime,SellTaskStaTypeDef * pTaskSta);
uint8_t SellApp_SetSellTask2(int code,int shelf_no,int cargo_no,void (*pFun)(int,int));


#endif
