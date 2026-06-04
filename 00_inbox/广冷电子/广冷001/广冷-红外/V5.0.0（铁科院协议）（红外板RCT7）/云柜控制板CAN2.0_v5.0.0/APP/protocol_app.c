#include "protocol_app.h"
#include "transport_api.h"
uint8_t ProtocolApp_UserCmd(uint8_t Cmd,uint8_t *Data,uint16_t size);
DeviceInfoTypeDef Info;

void ProtocolApp_Init(void)
{
	SysConfig_GetDevInfoConfig(&Info);//获取flash中存储的设备信息
	
	Info.dev_typ=DEV_LEVEL|DEV_TYPE;
	Info.dev_no =0x01;
	Info.ver    =DEV_VER;
	
	SysMem_copy(Info.dev_id,(uint8_t*)((__IO u32 *)(0X1FFFF7E8)),12);
	
	DeviceProtocol_SetDeviceInfo(&Info);//设置设备信息
	DeviceProtocol_SetUserCallBackFun(ProtocolApp_UserCmd);//设置指令回调函数
	
	Rs232Drive_Init();//初始化串口驱动
	Rs232Drive_SetUserReceiveFun(TransportApi_ReceiveData);
	
	ProtocolApp_ReadDeviceCode();
}

uint8_t ProtocolApp_ReadDeviceCode(void)
{
	uint16_t device_code=0x00000;
	device_code|=Info.dev_sn[0];
	device_code=(device_code<<4)|((Info.dev_sn[1]>>4)&0x0F);

	switch(device_code)
	{
		case 0x0000:
		case 0x0137:
			return 0x01;
			break;
		case 0x0115:
			return 0x02;
			break;
		default:return 0x01;
	}
}
//10ms定时调用
void ProtocolApp_TimeTask(void)
{
	Rs232Drive_TimeTask();
	DeviceProtocol_TimeTask();
}

void ProtocolApp_TaskRun(void)
{
	Rs232Drive_TaskRun();
	DeviceProtocol_TaskRun();
}

void AndriodApp_Set_MiscGpio_Callback(uint8_t cmd,void *pData,uint16_t size,uint64_t sn)
{
	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)pData,size);
}

void ProtocolApp_SellAppCallBack(uint8_t cmd,void *pData,uint16_t size,uint64_t sn)
{
	DeviceProtocol_TxResportMsg(0x11,(uint8_t*)pData,size);
}

void ProtocolApp_CargoTestCallBack(CargoMotorTaskTestCmdTypeDef *pCargoMotorTaskTestCmd)
{
	DeviceProtocol_TxResportMsg(0x1F,(uint8_t*)pCargoMotorTaskTestCmd,sizeof(CargoMotorTaskTestCmdTypeDef));
}

uint8_t ProtocolApp_UserCmd(uint8_t Cmd,uint8_t *Data,uint16_t size)
{
	switch(Cmd)
	{
		case 0x10:
			break;
		case 0x11: 
			{				
				SellApp_SetSellTask(Cmd,
									Data,
									NULL,
									ProtocolApp_SellAppCallBack);
			}
		  return 0x00;
		case 0x12://读取设备状态
			sysSta_SendDeviceSta(Cmd);
			return 0x00;
		case 0x13://人体检测传感器状态
//			sysSta_SendBodySta(Cmd);
			return 0x00;
		case 0x14://红外状态
//			sysSta_SendIrSta(Cmd);
			return 0x00;
		case 0x15://升降平台状态
//			sysSta_SendLiftSta(Cmd);
			return 0x00;
		case 0x16://读取货道状态
			SellApp_ResportShelfStyle(Cmd);
			break;
		case 0x17://读取门状态
//			LockApp_ResportSta(Cmd);
			break;
		case 0x18://打开电子锁
			LockApp_OpenDoor(Data[0]);
			return 0x00;
		case 0x19://设置机柜温度
			TempControl_CmdSet(Cmd,(CryogenCmdTypeDef*)Data);
			return 0x00;
		case 0x1A://保存当前升降平台位置
//			SellApp_ConfigCmd(Cmd,(Sell_ConfigCmdTypeDef*)Data);
			return 0x00;
		case 0x1D:
//			SellApp_ResportConfig(Cmd);
			break;
		case 0x1E://设置设备信息
			SysConfig_UpDevInfoConfig((DeviceInfoTypeDef*)Data);
		  DeviceProtocol_TxResportMsg(Cmd,NULL,NULL);         //返回响应
			return 0x00;
		case 0x1F://货道测试
//			CargoMotor_TestSet((CargoMotorTestCmdTypeDef*)Data,ProtocolApp_CargoTestCallBack);
			break;
		case 0x4C://开关量输出
		{			
			AndroidApp_Set_Miscs(Cmd,Data,size,NULL,AndriodApp_Set_MiscGpio_Callback);
		}
		break;
		default: return 0x02;
	}
	return 0x00;
}

