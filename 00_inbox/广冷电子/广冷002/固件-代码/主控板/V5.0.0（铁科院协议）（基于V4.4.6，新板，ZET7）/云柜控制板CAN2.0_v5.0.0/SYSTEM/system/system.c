#include "system.h"

void test(void)
{
	uint32_t * ptr=NULL;
	*ptr=0x00;
}

void System_Init(void)
{
	TaskManage_ClockInit();	  	//任务管理定时器初始化	
//	Debug_Init();
	ElcLock_GpioInit();       	//初始化电子锁控制程序	
	BasicGateMotor_Init();	  	//初始闸门控制
	LED_Init();				  	//板载LED、出货提示灯初始化
	Miscs_Init();				//照明灯初始化
	Sensor_Init();				//信号扫描初始化
	MotorDrive_Init();     		//货道电机驱动初始化
	CryogenDrive_Init();   		//制冷控制初始化
	TempControl_Init();    		//温控初始化
	
	SysConfig_Init();			//FLASH参数初始化
	AuxConfig_Init();			//FLASH参数初始化
	SellHistory_Init();			//出货日志初始化
	SellApp_Init();				//出货控制初始化
	
	DgusApp_Init();				//屏幕控制初始化
	CloudProtocol_Init();  		//云通信协议初始化
	RTC_Init();					//时钟初始化
	MQTT_Config_Init(CloudProtocol_Read_DeviceId());	//MQTT配置初始化
		
	WatchDog_Init(3,1875);	//看门狗初始化，1.5秒溢出
	
	/*传感器信号采集，任务创建*/
	TaskManage_AddTasks(Sensor_InfoColle,10,10,0x01);
		
	/*货道电机驱动，任务创建*/
	TaskManage_AddTasks(MotorDrive_Task,10,10,0x00);       
	
	/*出货任务，任务创建*/
	TaskManage_AddTasks(SellApp_TimeTask,5,10,0x00);        
	TaskManage_AddTasks(SellApp_Task,5,0,0x01);             
	
	/*板载LED、取货指示灯，任务创建*/
	TaskManage_AddTasks(LED_Drive,8,100,0x00);

	/*制冷任务，任务创建*/
	TaskManage_AddTasks(CryogenDrive_TaskRun,5,1000,0x00);       

	/*电控锁任务，任务创建*/
	TaskManage_AddTasks(ElcLock_TaskRun,10,10,0x00);     

	/*保温门任务，任务创建*/
	TaskManage_AddTasks(BasicGateMotor_Task,10,10,0);
	
	/*串口屏任务，任务创建*/
	TaskManage_AddTasks(DgusApp_Task,10,10,0);

	/*网络任务，任务创建*/
	TaskManage_AddTasks(MQTT_QOS1_Task,10,10,0x00);
	TaskManage_AddTasks(MQTT_Connect_Task,10,10,0x00);
//	TaskManage_AddTasks(otaTask,100,1000,0x00);			//OTA任务	
	TaskManage_AddTasks(WirelessModule_ResetTask,0,100,0x00);
	TaskManage_AddTasks(NetworkModule_InitTask,0,10,0x00);
	TaskManage_AddTasks(CloudProtocol_TimeTask,5,10,0x00);
	TaskManage_AddTasks(CloudProtocol_Task,5,0,0x01);	
	
	/*日志打印，任务创建*/
	TaskManage_AddTasks(History_PrintfTask,2000,10,0x00);
	
	/*自检任务，任务创建*/
	TaskManage_AddTasks(MotorTest_Task,10,10,0x00);	

//	TaskManage_AddTasks(Debug_Test,10,1000,0);

}



void System_TaskRun(void)
{
	//任务调度
	TaskManage_Tasks();
	
	//喂狗
	WatchDog_Drive();
}



