#ifndef	_DGUS_CONTROL_H_
#define	_DGUS_CONTROL_H_

#include "dgus_recive.h"
#include "dgus_send.h"

void DgusControl_ShowQRCode(u8 * qrcode,u8 size);
void DgusControl_ShowNetSta(u8 sta);
void DgusControl_ShowTemp(u8 temp);
void DgusControl_UpTime(u8 year,u8 month,u8 day,u8 week,u8 hour,u8 min,u8 sec);
void DgusControl_GotoPage(u8 page_no);
void DgusControl_ClearText(u16 addr,u8 byte_num);
void DgusControl_ShowDeviceId(u8 * DeviceId);
void DgusControl_Init(void);
void DgusControl_ShowGoodsHistory(u16 addr,
									u16 year,
									u8 month,
									u8 day,
									u8 hour,
									u8 min,
									u8 sec,
									u8 contain_no,
									u8 shelf_no,
									u8 cargo_no,
									u8 sta,
									u32 err1,
									u32 err2);

extern void DgusControl_ShowErrorInfo(u8 contain_no,u8 shelf_no,u8 motor_no,u32 err1,u32 err2);
void DgusControl_ShowStoreSta(u8 sta);


void DgusControl_ShowSellErrorInfo(int state);
void DgusControl_ShowSystemErrorInfo(int state);
void DgusControl_ShowSellLogo(char * orderId);
void DgusControl_ShowTemp2(u8 temp);
void DgusControl_ShowSellTest(u8 row,u8 list,u8	motor_err);
void DgusControl_ShowSellColor(u8 row,u8 list,u8 motor_err);
void DgusControl_ShowSellReset(u8 row,u8 list);
void DgusControl_ShowIrCheckColor(u8 sta);
void DgusControl_ShowIrCheck(u8 sta);
void DgusControl_ClearIrCheck(void);
void DgusControl_ShowMotorCheckColor(u8 sta);
void DgusControl_ShowMotorCheck(u8 sta);
void DgusControl_ClearMotorCheck(void);

#endif	/*_DGUS_CONTROL_H_*/

