#ifndef	_DGUS_RECIVE_H_
#define	_DGUS_RECIVE_H_

#include "dgus_crc16.h"
#include "usart.h"
#include "dgus_struct.h"

typedef	struct
{
	u16	VariableAddr;
	u8	AckFlag;
}DgusReciveAck_TypeDef;

void Dgus_Recive_Init(void);
u8	DgusRecive_Get_82Ack(void);
void DgusRecive_Reset_82Ack(void);
void DgusRecive_Set_82Ack(u16 VariableAddr);
u8	DgusRecive_Get_83Ack(void);
void DgusRecive_Reset_83Ack(void);
void DgusRecive_Set_83Ack(u16 VariableAddr);
void DgusRecive_Set_DeviceManageIdCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceManagePwdCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceManageLoginCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceManageFixIdCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceManageFixPwdCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceManageFixCallback(void (*pfun)(u8*,u8));
void DgusRecive_Set_DeviceIdFix_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_DeviceIdFixOk_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_WifiSsidFix_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_WifiPwdFix_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_WifiFixOk_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_TcpIpFix_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_TcpPortFix_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_TcpFixOk_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_OpenLock_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_ShowHistoryStart_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_ShowHistoryNext_Callback(void (pfun)(u8*,u8));
void DgusRecive_Set_ShowHistoryLast_Callback(void (pfun)(u8*,u8));


#endif	/*_DGUS_RECIVE_H_*/

