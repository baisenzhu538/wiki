#ifndef	_DGUS_APP_H_
#define	_DGUS_APP_H_

#include "dgus_send.h"
#include "dgus_recive.h"
#include "dgus_control.h"
#include <string.h>
#include "cloud_protocol.h"
#include "sys_config.h"
#include "sell_history.h"

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u8	DeviceId[32];
}DgusApp_ShowDeviceId_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u16	year;
	u8	month;
	u8	day;
	u8	week;
	u8	hour;
	u8	min;
	u8	sec;
}DgusAppUpTime_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u8	qrcode[256];
	u8	qrcode_size;
}DgusApp_ShowQRCode_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	sta;
	u8	retry_cnt;
	u16	runtime;
}DgusApp_ShowNetSta_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	sta;
	u8	retry_cnt;
	u16	runtime;
}DgusApp_ShowStoreSta_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	temp;
	u8	retry_cnt;
	u16	runtime;
}DgusApp_ShowTemp_TypeDef;

typedef	struct
{
	u8	enable;
	u8	page_no;
	u8	step;
	u8	retry_cnt;
	u16	runtime;		
}DgusAppGotoPage_TypeDef;

typedef	struct
{	
	DgusLoginPara_TypeDef	src;
	DgusLoginPara_TypeDef	input;
	u8	login_flag;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
}DgusAppDeviceManageLogin_TypeDef;

typedef	struct
{
	WifiApPara_TypeDef	wifi;
}DgusAppWifiPara_TypeDef;

typedef	struct
{
	NetworkPara_TypeDef	net;
}DgusAppTcpPara_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u16	addr;
	u16	year;
	u8	month;
	u8	day;
	u8	hour;
	u8	min;
	u8	sec;
	u8	contain_no;
	u8	shelf_no;
	u8	cargo_no;
	u8	sta;
	u32	err1;
	u32	err2;
}DgusAppShowHistory_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;
	u16	offset;
	u16	cnt;
	u8	page_no;
	u16	lenth;
	u16	head;
	u16	tail;
	u8	area_no;
}DgusAppShowHistoryManage_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;	
	u8	clear;
	char orderId[24];
}DgusAppShowSellLog_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;	
	int	state;
}DgusAppShowSellErrorInfo_TypeDef;

typedef	struct
{
	u8	enable;
	u8	step;
	u8	retry_cnt;
	u16	runtime;	
	int	state;	
}DgusAppShowSystemErrorInfo_TypeDef;

void DgusApp_Set_Time(u8 year,u8 month,u8 day,u8 week,u8 hour,u8 min,u8 sec);
void DgusApp_Set_Temp(u8 temp);
void DgusApp_Set_QRCode(u8 * qrcode,u8 size);
void DgusApp_Set_GotoPage(u8 page_no);
void DgusApp_Set_DeviceId(u8 * DeviceId);
void DgusApp_SetShowHistory(u16 addr,u16 year,u8 month,u8 day,u8 hour,u8 min,u8 sec,u8 contain_no,u8 shelf_no,u8 cargo_no,u8 sta,u8 err1,u8 err2);
u8 DgusApp_GetShowHistory_Enable(void);
void DgusApp_Set_StoreSta(u8 sta);
void DgusApp_Set_ShowSellLog(char * orderId);
void DgusApp_Set_ShowSellErrorInfo(int state);
void DgusApp_Set_ShowSystemErrorInfo(int state);
void DgusApp_Set_Temp2(u8 temp);
void DgusApp_Set_ShowSellTest(u8 row,u8 list,u8 motor_err);
void DgusApp_Set_ShowSellReset(void);
void DgusApp_Set_ShowIrCheck(u8 sta);
void DgusApp_Set_ClearIrCheck(void);
void DgusApp_Set_ShowMotorCheck(u8 sta);
void DgusApp_Set_ClearMotorCheck(void);



void DgusApp_Init(void);
void DgusApp_Task(void);


#endif	/*_DGUS_APP_H_*/

