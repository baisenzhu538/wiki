#include "sell_history.h"


int SellHistory_CheckLogCodeForCode(int code)
{
	u32 lenth;
	u32 i;
	HistoryUintTypeDef	Uint;
	
	lenth = History_Get_TableLenth();
		
	for(i=0;i<lenth;i++)
	{
		History_Get_TableUint(i,&Uint);
		if(Uint.code == code)
			return 1;
	}	
	return 0;
}

//出货日志获取出货状态
int SellHistory_GetLogStateForCode(int code)
{
	u32 lenth;
	u32 i;
	HistoryUintTypeDef	Uint;
	
	lenth = History_Get_TableLenth();
		
	for(i=0;i<lenth;i++)
	{
		History_Get_TableUint(i,&Uint);
		if(Uint.code == code)
			return Uint.state;
	}	
	return 2;//其他
}

//出货日志修改出货状态(根据出货码)
void SellHistory_FixLogStateForCode(int code,int state)
{
	u32 lenth;	
	u32 i;		
	HistoryUintTypeDef	Uint;
	
	lenth = History_Get_TableLenth();
		
	for(i=0;i<lenth;i++)
	{
		History_Get_TableUint(i,&Uint);
		if(Uint.code == code)
		{
			Uint.state = state;
			History_Add_TableUint(i,&Uint);
			break;
		}
	}	
}

//出货日志新增
void SellHistory_AddLog(HistoryUintTypeDef * pUint)
{
	u16 lenth;
	u16	head;
	u16	tail;
	HistoryUintTypeDef Uint;
	
	SysMem_copy(&Uint,pUint,sizeof(HistoryUintTypeDef));
		
	lenth = History_Get_TableLenth();
	head = History_Get_TableHead();
	tail = History_Get_TableTail();
		
	Uint.index = tail;
	History_Add_TableUint(tail,&Uint);
		
	if(lenth<(HISTORY_UINT_MAX_NUM))
	{
		lenth++;
		
		if(tail<(HISTORY_UINT_MAX_NUM-1))
		{
			tail++;
		}
		else
		{
			tail=0;
		}
	}
	else
	{		
		if(tail<(HISTORY_UINT_MAX_NUM-1))
		{
			tail++;
		}
		else
		{
			tail=0;
		}
		
		if(head<(HISTORY_UINT_MAX_NUM-1))
		{
			head++;
		}
		else
		{
			head=0;
		}
	}
	
	History_Set_TableLenth(lenth);
	History_Set_TableHead(head);
	History_Set_TableTail(tail);
	
}

//出货日志字符串生成（时间段2）
u32 SellHistory_CreatLogStringForTimeRange2(Time_TypeDef *pTime1,Time_TypeDef *pTime2,u8 * Buffer)
{
	u32 lenth;
	u32 i;
	u16	BufferLenth=0;
	u32	Time1Sum,Time2Sum,UintTimeSum;
	u32	log_num=0;
	HistoryUintTypeDef	Uint;
	char TempLog[33];
		
	Time1Sum = pTime1->year*10000000000
				+pTime1->month*100000000
				+pTime1->day*1000000
				+pTime1->hour*10000
				+pTime1->min*100
				+pTime1->sec;
	
	Time2Sum = pTime2->year*10000000000
				+pTime2->month*100000000
				+pTime2->day*1000000
				+pTime2->hour*10000
				+pTime2->min*100
				+pTime2->sec;	
	
	lenth = History_Get_TableLenth();
		
	for(i=0;i<lenth;i++)
	{
		History_Get_TableUint(i,&Uint);
		
		UintTimeSum = Uint.time.year*10000000000
						+Uint.time.month*100000000
						+Uint.time.day*1000000
						+Uint.time.hour*10000
						+Uint.time.min*100
						+Uint.time.sec;	
		
		if(UintTimeSum>=Time1Sum && UintTimeSum<=Time2Sum)
		{			
			if(BufferLenth>(1024-33))
				break;
			
			log_num++;
			
			sprintf(TempLog,
					"%4d%2d%2d%2d%2d%2d/%d/%d/%d/%d#",
					Uint.time.year,
					Uint.time.month,
					Uint.time.day,
					Uint.time.hour,
					Uint.time.min,			
					Uint.time.sec,
					Uint.code,
					Uint.row,
					Uint.list,
					Uint.state);	
			if(Buffer)
				strcat(Buffer,TempLog);
		}
	}	
	return log_num;
}

//出货日志字符串生成（时间段1）
u32 SellHistory_CreatLogStringForTimeRange1(Time_TypeDef *pTime,u8 * Buffer)
{
	u32 lenth;
	u32 i;
	u16	BufferLenth=0;
	u32 log_num=0;
	HistoryUintTypeDef	Uint;
	char TempLog[33];

	
	lenth = History_Get_TableLenth();
		
	for(i=0;i<lenth;i++)
	{
		History_Get_TableUint(i,&Uint);
		if(Uint.time.year == pTime->year
			&&Uint.time.month == pTime->month
			&&Uint.time.day == pTime->day)
		{			
			if(BufferLenth>(1024*6-33))
				break;
		
			log_num++;
			sprintf(TempLog,
					"%04d%02d%02d%02d%02d%02d/%d/%d/%d/%d#",
					Uint.time.year,
					Uint.time.month,
					Uint.time.day,
					Uint.time.hour,
					Uint.time.min,			
					Uint.time.sec,
					Uint.code,
					Uint.row,
					Uint.list,
					Uint.state);		
			if(Buffer)
				strcat(Buffer,TempLog);
		}
	}
	
	return log_num;
}


//日志初始化
void SellHistory_Init(void)
{
	u16	init=0;
	
	init = History_Get_TableInit();
	
	if(init != 0x0001)
	{
		History_Set_TableLenth(0x0000);
		History_Set_TableHead(0x0000);
		History_Set_TableTail(0x0000);		
		History_Set_TableInit(0x0001);
	}
	else
		while(0);
}



void SellHistory_Test(void)
{
	int state;
	u32 i;
	HistoryUintTypeDef	Uint;
	
	for(i=0;i<4000;i++)
	{
		Uint.code = i;
		Uint.state = 1;		
		if(i==72)
			while(0);
		SellHistory_AddLog(&Uint);
		Uint.state = SellHistory_GetLogStateForCode(i);
		if(Uint.state != 1)
		{
			while(1);
		}		
	}
	while(1);
}
//创建1条日志
//提取1条日志
//当提取的日志与

typedef	struct
{
	u8	enable;
	u8	step;
	u8	num;
}HistoryPrintf_TypeDef;

HistoryPrintf_TypeDef	HistoryPrintf;

u8	temp[64];

void History_PrintfTask(void)
{
	u32	i = 0;
	u32	lenth=0;
	u8 * buffer = NULL;
	Time_TypeDef	Time;
	WifiApPara_TypeDef	WifiApPara;
	HistoryUintTypeDef	Uint;
	
	if(Sensor_Get_KeyRt(3))
	{
		HistoryPrintf.enable = 1;
	}
	
	if(HistoryPrintf.enable)
	{
		switch(HistoryPrintf.step)
		{
			case 0:
			{
				//打印设备ID
				SysConfig_Get_DeviceId(temp);
				printf("\r\n\r\n设备ID:%s\r\n",temp);
				
				AuxConfig_Get_WifiApPara(&WifiApPara);
				
				//打印WIFI名称
				printf("WIFI名称:%s\r\n",WifiApPara.ssid);
				//打印WIFI密码
				printf("WIFI密码：%s\r\n\r\n",WifiApPara.pwd);
				
				HistoryPrintf.step = 1;
			}
			break;
			case 1:
			{
				lenth = History_Get_TableLenth();
		
				for(i=0;i<lenth;i++)
				{
					History_Get_TableUint(i,&Uint);
					
					printf("%04d%02d%02d%02d%02d%02d/%d/%d/%d/%d\r\n",
								Uint.time.year,
								Uint.time.month,
								Uint.time.day,
								Uint.time.hour,
								Uint.time.min,			
								Uint.time.sec,
								Uint.code,
								Uint.row,
								Uint.list,
								Uint.state);
				}
				
				HistoryPrintf.step = 0;
				HistoryPrintf.enable = 0;
			}
			break;
		}
	}
}

