#ifndef	_TIME_STAMP_H_
#define	_TIME_STAMP_H_

#include "sys.h"

/*****************************                         时间管理相关             ***********************************/
typedef struct
{
	u16	year;
	u8	month;
	u8	day;
	u8	hour;
	u8	min;
	u8	sec;
	u8  receve;
}Time_TypeDef;

int TimeStamp_Get_TimeStamp(Time_TypeDef * pTimeStamp);		//生成时间戳
int TimeStamp_Init(void);									//时间管理初始化 & 1ms定时器初始化 
int TimeStamp_UpData(Time_TypeDef * pOther_Time);			//更新同步时间
int TimeStamp_Task(void);									//1ms时间回调任务
u32 TimeStamp_Subtract(Time_TypeDef * TimeStamp1,Time_TypeDef * TimeStamp2);
int TimeStamp_Compare(Time_TypeDef * TimeStamp1,Time_TypeDef * TimeStamp2);
int TimeStamp_Check(Time_TypeDef * TimeStamp);
int TimeStamp_CheckRtcReset(void);

#endif	/*_TIME_STAMP_H_*/

