#include "can_app.h"

NodeDiscernTypeDef NodeDiscern;

void CanApp_HardwareInit(void)
{
	Can_DriveInit(NodeDiscern.can_nodeid);
}

void CanApp_SourceInit(void)
{
 sIndexTable_AddSource(0x00,0x80,RW,&(CryogenDriveInfo.set),0x04);           //温度设置参数
 sIndexTable_AddSource(0x00,0x81,RO,&(CryogenDriveState.runsta),0x04);     //压缩机控制状态位
	
 sIndexTable_SetStateSync(0x00,0x80);
 sIndexTable_SetStateSync(0x00,0x81);
}


void CanApp_SysInit(void)
{
	 NodeDiscern.can_nodeid=0x30+SignalGpio_ReadCode();        //设置节点MACID为0x01
	 NodeDiscern.devicenum =SignalGpio_ReadCode();             //设置设备编号为0x01
	 NodeDiscern.devicetype=0x02;                              //设置设备类型号为0x02
	 NodeDiscern.version   =0x12345678;                        //设置设备版本号
	 NodeDiscernInit(&NodeDiscern);                            //初始化设备识别参数
	 ProtocoStack_Init();                                      //协议栈初始化
	 CanApp_HardwareInit();
	 CanApp_SourceInit();
}


