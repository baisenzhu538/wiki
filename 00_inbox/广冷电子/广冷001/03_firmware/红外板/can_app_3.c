#include "can_app.h"
#include "task_manage.h"

//控制器资源节点初始化
void CanApp_ControllerSourceInit(void)
{
	 //LED
	 sIndexTable_AddSource(0x00,0x04,RW,&(LED_Control.en),0x01);
	 sIndexTable_SetStateSync(0x00,0x04);
	
	 //配置货道电机工作参数	
	 sIndexTable_AddSource(0x00,0x80,RW,&(MotorDrive.motorset),0x04);
	 sIndexTable_AddSource(0x00,0x81,RO,&(MotorDrive.state),0x04);	
	 sIndexTable_SetStateSync(0x00,0x80);
	 sIndexTable_SetStateSync(0x00,0x81);
	 
	 sIndexTable_AddSource(0x00,0x82,RO,&(MotorDrive.link[0]),0x04*8);
//	 sIndexTable_AddSource(0x00,0x82,RO,&(MotorDrive.link[0]),0x04);
//	 sIndexTable_AddSource(0x00,0x83,RO,&(MotorDrive.link[1]),0x04);
//	 sIndexTable_AddSource(0x00,0x84,RO,&(MotorDrive.link[2]),0x04);
//	 sIndexTable_AddSource(0x00,0x85,RO,&(MotorDrive.link[3]),0x04);
//	 sIndexTable_AddSource(0x00,0x86,RO,&(MotorDrive.link[4]),0x04);
//	 sIndexTable_AddSource(0x00,0x87,RO,&(MotorDrive.link[5]),0x04);
//	 sIndexTable_AddSource(0x00,0x88,RO,&(MotorDrive.link[6]),0x04);
//	 sIndexTable_AddSource(0x00,0x89,RO,&(MotorDrive.link[7]),0x04);
	 sIndexTable_SetCycSync(0x00,0x82,100);//1s定时发送
//	 sIndexTable_SetStateSync(0x00,0x82);
//	 sIndexTable_SetStateSync(0x00,0x83);
//	 sIndexTable_SetStateSync(0x00,0x84);
//	 sIndexTable_SetStateSync(0x00,0x85);
//	 sIndexTable_SetStateSync(0x00,0x86);
//	 sIndexTable_SetStateSync(0x00,0x87);
//	 sIndexTable_SetStateSync(0x00,0x88);
//	 sIndexTable_SetStateSync(0x00,0x89);
	 //配置压缩机工作参数
	 sIndexTable_AddSource(0x00,0x96,RW,&(CryogenDriveInfo.set),0x04);
   sIndexTable_AddSource(0x00,0x97,RO,&(CryogenDriveState.runsta),0x04); 
   sIndexTable_SetStateSync(0x00,0x96);
   sIndexTable_SetStateSync(0x00,0x97);
	 
	 //设置传感器状态位索引地址与资源表同步方式
   sIndexTable_AddSource(0x00,0x98,RO,&(SignalManage.siggroup[2].sigstate),0x04);
   sIndexTable_SetStateSync(0x00,0x98);
}
//二级终端资源节点初始化
void CanApp_SecondLevelSourceInit(void)
{
	
}

//137控制板资源映射表
void CanApp_137Source(uint8_t num)
{
	mIndexTable_AddSource(0x0137,num,0x04,RW,&(LED[num].en),0x01);
	mIndexTable_SetStateSync(0x0137,num,0x04);
	
	mIndexTable_AddSource(0x0137,num,0x80,RW,&(MotorDrive_RegisterMap[num].motorset),0x04);
	mIndexTable_AddSource(0x0137,num,0x81,RO,&(MotorDrive_RegisterMap[num].state),0x04);
	mIndexTable_SetStateSync(0x0137,num,0x80);
	mIndexTable_SetStateSync(0x0137,num,0x81);
	
 mIndexTable_AddSource(0x0137,num,0x82,RO,&(MotorDrive_RegisterMap[num].link[0]),0x04*8);
// mIndexTable_AddSource(0x0137,num,0x82,RO,&(MotorDrive_RegisterMap[num].link[0]),0x04);
// mIndexTable_AddSource(0x0137,num,0x83,RO,&(MotorDrive_RegisterMap[num].link[1]),0x04);
// mIndexTable_AddSource(0x0137,num,0x84,RO,&(MotorDrive_RegisterMap[num].link[2]),0x04);
// mIndexTable_AddSource(0x0137,num,0x85,RO,&(MotorDrive_RegisterMap[num].link[3]),0x04);
// mIndexTable_AddSource(0x0137,num,0x86,RO,&(MotorDrive_RegisterMap[num].link[4]),0x04);
// mIndexTable_AddSource(0x0137,num,0x87,RO,&(MotorDrive_RegisterMap[num].link[5]),0x04);
// mIndexTable_AddSource(0x0137,num,0x88,RO,&(MotorDrive_RegisterMap[num].link[6]),0x04);
// mIndexTable_AddSource(0x0137,num,0x89,RO,&(MotorDrive_RegisterMap[num].link[7]),0x04);
 mIndexTable_SetCycSync(0x0137,num,0x82,100);
// mIndexTable_SetStateSync(0x0137,num,0x82);
// mIndexTable_SetStateSync(0x0137,num,0x83);
// mIndexTable_SetStateSync(0x0137,num,0x84);
// mIndexTable_SetStateSync(0x0137,num,0x85);
// mIndexTable_SetStateSync(0x0137,num,0x86);
// mIndexTable_SetStateSync(0x0137,num,0x87);
// mIndexTable_SetStateSync(0x0137,num,0x88);
// mIndexTable_SetStateSync(0x0137,num,0x89);

 //制冷控制
 mIndexTable_AddSource(0x0137,num,0x96,RW,&CryogenControl[num].CryogenSet,0x04);
 mIndexTable_AddSource(0x0137,num,0x97,RO,&CryogenControl[num].CryogenState,0x04);
 mIndexTable_SetStateSync(0x0137,num,0x96);
 mIndexTable_SetStateSync(0x0137,num,0x97);
 
//设置传感器状态位索引地址与资源表同步方式 
 mIndexTable_AddSource(0x0137,num,0x98,RO,&SensorGroup[num].s,0x04);
 mIndexTable_SetStateSync(0x0137,num,0x98);
}
//一级终端资源节点初始化
void CanApp_FirstLevelSourceInit(void)
{
 CanApp_137Source(0x01);
 CanApp_137Source(0x02);
 CanApp_137Source(0x03);
}

void CanApp_SysInit(void)
{
	 NodeDiscernTypeDef NodeDiscern;
 	 NodeDiscern.can_nodeid=(DigitalSignal_ReadCodeId()&0x07);        //设置节点MACID为0x01
	 NodeDiscern.devicenum =(DigitalSignal_ReadCodeId()&0x07);        //设置设备编号为0x01
	
	 NodeDiscern.deviceid_0=*(__IO u32 *)(0X1FFFF7E8);
	 NodeDiscern.deviceid_1=*(__IO u32 *)(0X1FFFF7EC);
	 NodeDiscern.deviceid_2=*(__IO u32 *)(0X1FFFF7F0);
	
	 if(DigitalSignal_ReadCodeId()==0x00)                      //一级终端模式
	 {
	  NodeDiscern.devicetype=NODE_DEV_TYPE|NODE_FIRSTLEVEL_DEVICE;                             
	  NodeDiscern.dvr       =NODE_FIRSTLEVEL_DEVICE_VER;
	 }
	 else if(DigitalSignal_ReadCodeId()&0x08)                 //二级终端
	 {
		 NodeDiscern.devicetype=NODE_DEV_TYPE|NODE_SECONDLEVEL_DEVICE;                             
	   NodeDiscern.dvr       =NODE_SECONDLEVEL_DEVICE_VER;
	 }
	 else                                                     //控制器模式
	 {
		 NodeDiscern.devicetype=NODE_DEV_TYPE|NODE_CONTROLLER_DEVICE;                             
	   NodeDiscern.dvr       =NODE_CONTROLLER_DEVICE_VER;
	 }
	 NodeDiscernInit(&NodeDiscern);                            //初始化设备识别参数
	 
	 if(NodeDiscern.devicetype&NODE_FIRSTLEVEL_DEVICE)
	 {
    MasteProtoco_Init();                                      //协议栈初始化
	  CanApp_FirstLevelSourceInit();
	  TaskManage_AddTasks(TimeTask_TaskRun,5,10,0x00);    //创建CAN定时器任务
  	TaskManage_AddTasks(CanMaste_RollRun,0,0,0x01);     //创建CAN循环扫描任务
	 }
	 else if(NodeDiscern.devicetype&NODE_SECONDLEVEL_DEVICE)
	 {
		ProtocoStack_Init();
		CanApp_SecondLevelSourceInit();
		TaskManage_AddTasks(TimeTask_TaskRun,5,10,0x00);        //创建CAN定时器任务
  	TaskManage_AddTasks(ProtocoStack_RollRun,0,0,0x01);     //创建CAN循环扫描任务
	 }
	 else
	 {
		ProtocoStack_Init();
		CanApp_ControllerSourceInit();
		TaskManage_AddTasks(TimeTask_TaskRun,5,10,0x00);        //创建CAN定时器任务
  	TaskManage_AddTasks(ProtocoStack_RollRun,0,0,0x01);     //创建CAN循环扫描任务
	 }
}


