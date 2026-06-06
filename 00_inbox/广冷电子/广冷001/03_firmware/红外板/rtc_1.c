#include "rtc.h"
#include "sys_config.h"

_calendar_obj	calendar;



void RTC_NVIC_Config(void)
{
	NVIC_InitTypeDef NVIC_InitStructure;
	NVIC_InitStructure.NVIC_IRQChannel = RTC_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 1;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;
	NVIC_Init(&NVIC_InitStructure);
}

//判断是否为闰年
u8 Is_Leap_Year(u16 year)
{
	if((year % 4 == 0 && year % 100 != 0) || year % 400)
		return 0x01;
	else
		return 0x00;
}

u8 RTC_Get_Week(u16 year,u8 month,u8 day)
{
	u8 week = 0;
	u8 dayCode = day;
	u8 monthCode = 0;
	u8 yearCode = 0;
	u8 sumCode = 0;
	u8 temp1 = 0;
	u8 temp2 = 0;
	u8 temp3 = 0;
	if(Is_Leap_Year(year))
	{
		switch(month)
		{
			case 1:monthCode = 5;break;
			case 2:monthCode = 1;break;
			case 3:monthCode = 2;break;
			case 4:monthCode = 5;break;
			case 5:monthCode = 0;break;
			case 6:monthCode = 3;break;
			case 7:monthCode = 5;break;
			case 8:monthCode = 1;break;
			case 9:monthCode = 4;break;
			case 10:monthCode = 6;break;
			case 11:monthCode = 2;break;
			case 12:monthCode = 4;break;
			default:return 0;
		}
	}
	else
	{
		switch(month)
		{
			case 1:monthCode = 6;break;
			case 2:monthCode = 2;break;
			case 3:monthCode = 2;break;
			case 4:monthCode = 5;break;
			case 5:monthCode = 0;break;
			case 6:monthCode = 3;break;
			case 7:monthCode = 5;break;
			case 8:monthCode = 1;break;
			case 9:monthCode = 4;break;
			case 10:monthCode = 6;break;
			case 11:monthCode = 2;break;
			case 12:monthCode = 4;break;
			default:return 0;
		}
	}
	temp1 = year % 100;
	temp2 = temp1 / 4;
	temp3 = temp1 + temp2;
	yearCode = temp3 % 7;
	sumCode = yearCode + monthCode + dayCode;
	if(sumCode < 7)
		week = sumCode;
	else
		week = sumCode % 7;
	return week;
}






//月份数据表
u8 const table_week[12]={0,3,3,6,1,4,6,2,5,0,3,5}; //月修正数据表
//平年的月份日期表
const u8 mon_table[12]={31,28,31,30,31,30,31,31,30,31,30,31};

u8 RTC_Set(u16 syear,u8 smon,u8 sday,u8 hour,u8 min,u8 sec)
{
	u16 t;
	u32 seccount=0;
	if(syear<1970||syear>2099)return 1;
	for(t=1970;t<syear;t++) //把所有年份的秒钟相加
	{ 
		if(Is_Leap_Year(t))
			seccount+=31622400;//闰年的秒钟数
		else 
			seccount+=31536000; //平年的秒钟数
	}
	smon-=1;
	for(t=0;t<smon;t++) //把前面月份的秒钟数相加
	{ 
		seccount+=(u32)mon_table[t]*86400; //月份秒钟数相加
		if(Is_Leap_Year(syear)&&t==1)
			seccount+=86400;//闰年 2 月份增加一天的秒钟数
	}
	seccount+=(u32)(sday-1)*86400; //把前面日期的秒钟数相加
	seccount+=(u32)hour*3600; //小时秒钟数
	seccount+=(u32)min*60; //分钟秒钟数
	seccount+=sec; //最后的秒钟加上去
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR |
	RCC_APB1Periph_BKP, ENABLE); //使能 PWR 和 BKP 外设时钟
	PWR_BackupAccessCmd(ENABLE); //使能 RTC 和后备寄存器访问
	RTC_SetCounter(seccount); //设置 RTC 计数器的值
	RTC_WaitForLastTask(); //等待最近一次对 RTC 寄存器的写操作完成
	return 0;
}



u8 RTC_Get(void)
{ 
	static u16 daycnt=0;
	u32 timecount=0;
	u32 temp=0;
	u16 temp1=0;
	timecount=RTC->CNTH; //得到计数器中的值(秒钟数)
	timecount<<=16;
	timecount+=RTC->CNTL;
	temp=timecount/86400; //得到天数(秒钟数对应的)
	if(daycnt!=temp) //超过一天了
	{
		daycnt=temp;
		temp1=1970; //从 1970 年开始
		while(temp>=365)
		{
			if(Is_Leap_Year(temp1)) //是闰年
			{
			if(temp>=366)
				temp-=366; //闰年的秒钟数
			else 
				break;
			}
			else 
				temp-=365; //平年
			temp1++;
		}
		calendar.w_year=temp1; //得到年份
		temp1=0;
		while(temp>=28) //超过了一个月
		{
			if(Is_Leap_Year(calendar.w_year)&&temp1==1)//当年是不是闰年/2 月份
			{
			if(temp>=29)
				temp-=29;//闰年的秒钟数
			else break;
			}
			else
			{ 
				if(temp>=mon_table[temp1])
					temp-=mon_table[temp1];//平年
				else 
					break;
			}
			temp1++;
		}
		calendar.w_month=temp1+1; //得到月份
		calendar.w_date=temp+1; //得到日期
	}
	temp=timecount%86400; //得到秒钟数
	calendar.hour=temp/3600; //小时
	calendar.min=(temp%3600)/60; //分钟
	calendar.sec=(temp%3600)%60; //秒钟
	calendar.week=RTC_Get_Week(calendar.w_year,calendar.w_month,calendar.w_date);
	//获取星期
	return 0;
}


u8 RTC_Sync(u16 year,u8 month,u8 day,u8 hour,u8 min,u8 sec)
{
	RTC_EnterConfigMode(); // 允许配置
	RTC_WaitForLastTask(); //等待最近一次对 RTC 寄存器的写操作完成
	RTC_Set(year,month,day,hour,min,sec); //设置时间
	RTC_ExitConfigMode(); //退出配置模式
}

u8 RTC_Copy(_calendar_obj * pcalendar)
{
	pcalendar->w_year = calendar.w_year;
	pcalendar->w_month = calendar.w_month;
	pcalendar->w_date = calendar.w_date;
	pcalendar->week = calendar.week;
	pcalendar->hour = calendar.hour;
	pcalendar->min = calendar.min;
	pcalendar->sec = calendar.sec;
}

u8 RTC_Init(void)
{
	u8 temp=0;
	//检查是不是第一次配置时钟
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR |
	RCC_APB1Periph_BKP, ENABLE); //①使能 PWR 和 BKP 外设时钟
	PWR_BackupAccessCmd(ENABLE); //②使能后备寄存器访问
//	if (AuxConfig_GetRtcDisableWriteFlag() != 0x5050) //从指定的后备寄存器中
//	//读出数据:读出了与写入的指定数据不相乎
//	{
		BKP_DeInit(); //③复位备份区域
		RCC_RTCCLKConfig(RCC_RTCCLKSource_HSE_Div128); //设置 RTC 时钟	-- HSE / 128
		//(RTCCLK),选择 HSE 作为 RTC 时钟
		
		RCC_RTCCLKCmd(ENABLE); 	//使能 RTC 时钟
		RTC_WaitForLastTask(); 	//等待最近一次对 RTC 寄存器的写操作完成
		RTC_WaitForSynchro(); 	//等待 RTC 寄存器同步
		RTC_ITConfig(RTC_IT_SEC, ENABLE); //使能 RTC 秒中断
		RTC_WaitForLastTask(); //等待最近一次对 RTC 寄存器的写操作完成
		RTC_EnterConfigMode(); // 允许配置
		RTC_SetPrescaler(62500); //设置 RTC 预分频的值
		RTC_WaitForLastTask(); //等待最近一次对 RTC 寄存器的写操作完成
		RTC_Set(0,0,0,0,00,00); //设置时间
		RTC_ExitConfigMode(); //退出配置模式
//		AuxConfig_UpRtcDisableWriteFlag(0X5050); //向指定的后备寄存器中
//		//写入用户程序数据 0x5050
//	}
//	else//系统继续计时
//	{
//		RTC_WaitForSynchro(); //等待最近一次对 RTC 寄存器的写操作完成
//		RTC_ITConfig(RTC_IT_SEC, ENABLE); //使能 RTC 秒中断
//		RTC_WaitForLastTask(); //等待最近一次对 RTC 寄存器的写操作完成
//	}
	RTC_NVIC_Config(); //RCT 中断分组设置
	RTC_Get(); //更新时间
	return 0; //ok
}

void RTC_IRQHandler(void)
{
	if (RTC_GetITStatus(RTC_IT_SEC) != RESET) //秒钟中断
	{
		RTC_Get(); //更新时间		
	}
	if(RTC_GetITStatus(RTC_IT_ALR)!= RESET) //闹钟中断
	{
		RTC_ClearITPendingBit(RTC_IT_ALR); //清闹钟中断
		RTC_Get(); //更新时间
//		printf("Alarm Time:%d-%d-%d %d:%d:%d\n",calendar.w_year,calendar.w_month,
//		calendar.w_date,calendar.hour,calendar.min,calendar.sec);//输出闹铃时间
	}
	RTC_ClearITPendingBit(RTC_IT_SEC|RTC_IT_OW); //清闹钟中断
	RTC_WaitForLastTask();
}