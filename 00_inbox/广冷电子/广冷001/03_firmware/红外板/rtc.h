#ifndef	_RTC_H_
#define	_RTC_H_

#include "sys.h"
#include "stm32f10x.h"
#include "misc.h"
#include "stm32f10x_rtc.h"
#include "stm32f10x_bkp.h"

typedef struct
{
	vu8 hour;
	vu8 min;
	vu8 sec;
	//公历日月年周
	vu16 w_year;
	vu8 w_month;
	vu8 w_date;
	vu8 week;
}_calendar_obj;

u8 RTC_Init(void);
u8 RTC_Sync(u16 year,u8 month,u8 day,u8 hour,u8 min,u8 sec);	//时间同步
u8 RTC_Copy(_calendar_obj * pcalendar);	//时间复制


#endif	/*_RTC_H_*/

