#include "lock_app.h"
#include "protocol_app.h"
#include "cloud_protocol.h"
ElcLockAppTypeDef ElcLockApp;
ElcLockStateTypeDef ElcLockState;


void LockApp_ResportSta(uint8_t cmd)
{
	ElcLockResportStateTypeDef ElcLockResportState;
	ElcLockResportState.elclock_num=0x03;
	ElcLockResportState.State[0].contain=0x00;
	ElcLockResportState.State[0].sta=0x01;
	ElcLockResportState.State[1].contain=0x01;
	ElcLockResportState.State[1].sta=0x01;
	ElcLockResportState.State[2].contain=0x2;
	ElcLockResportState.State[2].sta=0x01;
	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&ElcLockResportState,sizeof(ElcLockResportStateTypeDef));
}
void LockApp_Init(void)
{
 ElcLock_GpioInit();
}
void LockApp_OpenDoor(uint8_t contain)
{
	ElcLockStateTypeDef ElcLockState;
	ElcLockApp.en=0x01;
	ElcLockApp.contain=contain;
}

void LockApp_Test(void)
{
	if(Sensor_Get_KeyRt(2)||Sensor_Get_KeyFt(2))
		LockApp_OpenDoor(0);
}

//10ms‘À––
void LockApp_TaskRun(void)
{
	LockApp_Test();
	ElcLock_TaskRun();
	ElcLockState.sta=ElcLock_ReadLockState();
	if(ElcLockApp.en==0x00&&ElcLockApp.sta==0x00)
		return;
	if(ElcLockApp.en==0x00)
	{
		ElcLock_ResetEnable();
		ElcLockApp.sta=0x00;
	}
	else
	{
		switch(ElcLockApp.sta)
		{
			case 0x00:
				ElcLock_SetEnable();
			  ElcLockApp.sta=0x01;
				break;
			case 0x01:
				if(ElcLock_ReadEnableSta()==0x00)
				{
					if(ElcLock_ReadLockErr())
					{
						ElcLockState.contain=ElcLockApp.contain;
						ElcLockState.err=0x01;
						ElcLockState.sta=ElcLock_ReadLockState();
						DeviceProtocol_TxResportMsg(0x18,(uint8_t*)&ElcLockState,sizeof(ElcLockStateTypeDef));
						
					}
					else
					{
						ElcLockState.contain=ElcLockApp.contain;
						ElcLockState.err=0x00;
						ElcLockState.sta=ElcLock_ReadLockState();
						DeviceProtocol_TxResportMsg(0x18,(uint8_t*)&ElcLockState,sizeof(ElcLockStateTypeDef));
					}
//					CloudProtocol_ResponseLockStaMessage(&ElcLockState);
					ElcLockApp.sta=0x00;
					ElcLockApp.en =0x00;
				}
				break;
		}
	}
}
