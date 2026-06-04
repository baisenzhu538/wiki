#ifndef	_SELL_HISTORY_H_
#define	_SELL_HISTORY_H_

#include "time_stamp.h"
#include "sell_app.h"
#include "sys.h"
#include "sys_config.h"
#include <string.h>
#include "debug.h"
#include "sys_config.h"


void SellHistory_Init(void);
//出货日志字符串生成（时间段1）
u32 SellHistory_CreatLogStringForTimeRange1(Time_TypeDef *pTime,u8 * Buffer);
//出货日志字符串生成（时间段2）
u32 SellHistory_CreatLogStringForTimeRange2(Time_TypeDef *pTime1,Time_TypeDef *pTime2,u8 * Buffer);
//出货日志新增
void SellHistory_AddLog(HistoryUintTypeDef * pUint);
//出货日志修改出货状态(根据出货码)
void SellHistory_FixLogStateForCode(int code,int state);
//出货日志获取出货状态
int SellHistory_GetLogStateForCode(int code);

int SellHistory_CheckLogCodeForCode(int code);

void SellHistory_Test(void);

void History_PrintfTask(void);

#endif	/*_SELL_HISTORY_H_*/

