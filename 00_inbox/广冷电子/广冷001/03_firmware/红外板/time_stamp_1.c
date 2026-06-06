#include "time_stamp.h"
#include "rtc.h"

//Time_TypeDef	HostTime;

int TimeStamp_Get_TimeStamp(Time_TypeDef * pTimeStamp)	//生成时间戳
{
//	pTimeStamp->sec = HostTime.sec;
//	pTimeStamp->min = HostTime.min;
//	pTimeStamp->hour = HostTime.hour;
//	pTimeStamp->day = HostTime.day;
//	pTimeStamp->month = HostTime.month;
//	pTimeStamp->year = HostTime.year;
	_calendar_obj xcalendar;
	
	RTC_Copy(&xcalendar);
	pTimeStamp->sec = xcalendar.sec;
	pTimeStamp->min = xcalendar.min;
	pTimeStamp->hour = xcalendar.hour;
	pTimeStamp->day = xcalendar.w_date;
	pTimeStamp->month = xcalendar.w_month;
	pTimeStamp->year = xcalendar.w_year;
	return 0;
}
//int TimeStamp_Init(void)										//时间管理初始化 & 1ms定时器初始化 
//{
//	HostTime.year = 2019;
//	HostTime.month = 1;
//	HostTime.day = 1;
//	HostTime.hour = 0;
//	HostTime.min = 0;
//	HostTime.sec = 0;
//}
int TimeStamp_UpData(Time_TypeDef * pOther_Time)			//更新同步时间
{
//	HostTime.year = pOther_Time->year;
//	HostTime.month = pOther_Time->month;
//	HostTime.day = pOther_Time->day;
//	HostTime.hour = pOther_Time->hour;
//	HostTime.min = pOther_Time->min;
//	HostTime.sec = pOther_Time->sec;	
	
	RTC_Sync(pOther_Time->year,
			pOther_Time->month,
			pOther_Time->day,
			pOther_Time->hour,
			pOther_Time->min,
			pOther_Time->sec);	//时间同步

	return 0;
}

//int Time_Check_LeapYear(u16 year)
//{
//	if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
//		return 0;
//	else
//		return -1;
//}



u32 TimeStamp_Subtract(Time_TypeDef * TimeStamp1,Time_TypeDef * TimeStamp2)
{
	Time_TypeDef SubTime;
	u32 sec = 0;
	
	if(TimeStamp1->sec >= TimeStamp2->sec)	//当前时间秒大
		SubTime.sec = TimeStamp1->sec - TimeStamp2->sec;
	else									//当前时间秒小
	{	
		SubTime.sec = 60 - TimeStamp2->sec + TimeStamp1->sec;
		TimeStamp1->min -= 1;	//借1分钟
	}
	
	if(TimeStamp1->min >= TimeStamp2->min)
		SubTime.min = TimeStamp1->min - TimeStamp2->min;
	else
	{
		SubTime.min = 60 - TimeStamp2->min + TimeStamp1->min;
		TimeStamp1->hour -= 1;
	}
	
	if(TimeStamp1->hour >= TimeStamp2->hour)
		SubTime.hour = TimeStamp1->hour - TimeStamp2->hour;
	else
		SubTime.hour = 24 - TimeStamp2->hour + TimeStamp1->hour;	
	
	sec = SubTime.hour * 60 * 60 + SubTime.min * 60 + SubTime.sec;
	return sec;
}


int TimeStamp_Compare(Time_TypeDef * TimeStamp1,Time_TypeDef * TimeStamp2)
{
	if(TimeStamp1->hour > TimeStamp2->hour)
	{
		return 1;
	}
	else if(TimeStamp1->hour < TimeStamp2->hour)
	{
		return -1;
	}
	else
	{
		if(TimeStamp1->min > TimeStamp2->min)
		{
			return 1;
		}
		else if(TimeStamp1->min < TimeStamp2->min)
		{
			return -1;
		}
		else
		{
			if(TimeStamp1->sec > TimeStamp2->sec)
			{
				return 1;
			}
			else if(TimeStamp1->sec < TimeStamp2->sec)
			{
				return -1;
			}
			else
			{
				return 0;
			}
		}
	}
}

int TimeStamp_Check(Time_TypeDef * TimeStamp)
{
	if(TimeStamp->year > 2100 || TimeStamp->year < 2019)
		return -1;
	else if(TimeStamp->month > 12 || TimeStamp->month < 1)
		return -1;
	else if(TimeStamp->day > 31 || TimeStamp->day < 1)
		return -1;
	else if(TimeStamp->hour > 23 || TimeStamp->hour < 0)
		return -1;
	else if(TimeStamp->min > 60 || TimeStamp->min < 0)
		return -1;
	else if(TimeStamp->sec > 60 || TimeStamp->sec < 0)
		return -1;
	else
		return 0;
}

////1ms调用 
//int TimeStamp_Task(void)
//{
//	static u16 ms = 0;
//	ms++;
//	if(ms > 1000)
//	{
//		ms = 0;
//		HostTime.sec++;
//		if(HostTime.sec >= 60)
//		{
//			HostTime.sec = 0;
//			HostTime.min++;
//			if(HostTime.min >= 60)
//			{
//				HostTime.min = 0;
//				HostTime.hour++;
//				if(HostTime.hour >= 24)
//				{
//					HostTime.hour = 0;
//				}
//			}
//		}
//	}
//}	


static Time_TypeDef NowTimeStamp;
int TimeStamp_CheckRtcReset(void)
{
	TimeStamp_Get_TimeStamp(&NowTimeStamp);
	if(NowTimeStamp.year < 2019)
		return 1;	
	else
		return 0;
}

