
/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 升降平台电机驱动模块
*	文件名称 : sell_app.c
*	版    本 : V1.1
*	说    明 : 1.实现电机的控制与电机位置信号采集
*
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-12-14  欧阳     
*   V1.1    2018-06-13  欧阳     修改履带电机控制接口，新增速度调整
*********************************************************************************************************
*/	

#include "sell_app.h"
//#include "sys_config.h"
#include "led.h"
#include "protocol_app.h"
#include "basic_gate_motor.h"

Sell_TypeDef Sell;
Sell_ConfigTypeDef SellConfig={
	                             {
																 {
																   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
																 },//0号机柜升降平台出货口位置
																 {
																	 0x00000907,//0
																	 0x00002713,//1
																	 0x00004434,//2
																	 0x00006140,//3
																	 0x00008964,//4
																	 0x0000A809,//5
																	 0x0000C302,//6
																	 0x0000E32B,//7
																	 0x0001156E,//8
																	 0x00012C1A,//9
																	 0x000152E1,//A
																	 0x0000D2A9,//B
																	 0x0000D2A9,//C
																	 0x0000D2A9,//D
																	 0x0000D2A9,//E
																	 0x0000D2A9 //F
																 },//1号升降平台出货口位置                                  
																 {
																	 0x000152E1,//0
																	 0x00013D61,//1
																	 0x000114D1,//2
																	 0x0000779B,//3
																	 0x0000F32D,//4
																	 0x0000779B,//5
																	 0x0000D90A,//6
																	 0x0000779B,//7
																	 0x0000BDB3,//8
																	 0x0000779B,//9
																	 0x0000A087,//A
																	 0x0000779B,//B
																	 0x00006A86,//C
																	 0x0000779B,//D
																	 0x00003E3E,//E
																	 0x0000181E,//F
																 }//2号升降平台出货口位置
															 },                                     
															 {
															  0,
															  0x0000D6F5,
															  0x00007EB3
															 }//机柜出货口升降平台位置
                              };

															//返回货道样式
typedef __packed struct
{
	uint8_t  contain_num;
	uint16_t link_sta1[16];
	uint16_t link_sta2[16];
	uint16_t link_sta3[16];
}ShelfStyleTypeDef;

ShelfStyleTypeDef ShelfStyle={0x03,{0}};
void SellApp_ResportShelfStyle(uint8_t cmd)
{
	uint8_t i;
	for(i=0;i<MOTOR_Y_MAX;i++)
	{
		ShelfStyle.link_sta1[i]=SellMotor_GetLinkState(0,i);
	}
	for(i=0;i<MOTOR_Y_MAX;i++)
	{
		ShelfStyle.link_sta2[i]=SellMotor_GetLinkState(1,i);
	}
	for(i=0;i<MOTOR_Y_MAX;i++)
	{
		ShelfStyle.link_sta3[i]=SellMotor_GetLinkState(2,i);
	}
//	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&ShelfStyle,sizeof(ShelfStyleTypeDef));
}

//貨道连接状态扫描
void SellApp_ShelfLinkScan(void)
{
//	uint8_t i,flag=0x00;
//	for(i=0;i<16;i++)
//	{
//		if(ShelfStyle.link_sta1[i]!=MotorDrive_GetLinkState(0x00,i))
//		{
//		 ShelfStyle.link_sta1[i]=MotorDrive_GetLinkState(0x00,i);
//		 flag=0x01;
//		}
//	}
//	for(i=0;i<16;i++)
//	{
//		if(ShelfStyle.link_sta2[i]!=MotorDrive_GetLinkState(0x01,i))
//		{
//		 ShelfStyle.link_sta2[i]=MotorDrive_GetLinkState(0x01,i);
//		 flag=0x01;
//		}
//	}
//	for(i=0;i<16;i++)
//	{
//		if(ShelfStyle.link_sta3[i]!=MotorDrive_GetLinkState(0x02,i))
//		{
//		 ShelfStyle.link_sta3[i]=MotorDrive_GetLinkState(0x02,i);
//		 flag=0x01;
//		}
//	}
//	if(flag==0x01)
//	 DeviceProtocol_TxTriggerMsg(0x16,(uint8_t*)&ShelfStyle,sizeof(ShelfStyleTypeDef));
}
//出货应用任务初始化
void SellApp_Init(void)
{
	Sell.cargo_rn=0;
	Sell.cargo_s=0;
	
	Sell.sell_delay=SELL_DELAY;
	Sell.cargo_outtime=0;
	Sell.lift_outtimr=0;
	Sell.tarck_outtime=0;
	
	Sell.liftrest_flag=1;
	Sell.sell_flag =0;
	Sell.task_state=0;
	Sell.sell_state=0;
	
	Sell.sell_ir_errnum=0;
	
	Sell.SellTask.q_head=0;
	Sell.SellTask.q_tail=0;
	Sell.SellTask.q_len =SELLTASK_QUEULEN;
}

//接收配置指令,保存当前位置为制定层架位置
void SellApp_ConfigCmd(uint8_t cmd,Sell_ConfigCmdTypeDef *pConfigCmd)
{

}

void SellApp_ResportConfig(uint8_t cmd)
{

}

//获取出货任务队列剩余长度
uint8_t SellApp_GetSellTaskQueueOverLenth(void)
{
	return Sell.SellTask.q_len;
}

uint8_t SellApp_AddTask(SellTaskTypeDef *pSellTask)
{
	if(Sell.SellTask.q_len==0)
	 return 0x00;
	SysMem_copy(&Sell.SellTask.selltask[Sell.SellTask.q_tail],pSellTask,sizeof(SellTaskTypeDef));
	Sell.SellTask.q_tail++;
	Sell.SellTask.q_len--;
	if(Sell.SellTask.q_tail==SELLTASK_QUEULEN)
		Sell.SellTask.q_tail=0;
	return 0xFF;
}



uint8_t SellApp_GetTask(SellTaskTypeDef *ptask)
{
	if(Sell.SellTask.q_len==SELLTASK_QUEULEN)
	 return 0x00;
	SysMem_copy((uint8_t*)ptask,(uint8_t*)&Sell.SellTask.selltask[Sell.SellTask.q_head],sizeof(SellTaskTypeDef));
	Sell.SellTask.q_head++;
	Sell.SellTask.q_len++;
	if(Sell.SellTask.q_head==SELLTASK_QUEULEN)
		Sell.SellTask.q_head=0;
	return 0x01;
}

uint8_t SellApp_SetSellTask2(int code,int shelf_no,int cargo_no,void (*pFun)(int,int))
{
	SellTaskTypeDef SellTask;
	
	SellTask.SellId.cargo_no =cargo_no;
	SellTask.SellId.cargo_num =0;
	SellTask.SellId.contain_no=0;
	SellTask.SellId.shelf_no  =shelf_no;
	SellTask.SellId.code = code;
	SellTask.pTaskFinishCallBack2=pFun;
	SellTask.SN                 =0;
	SellTask.Cmd                =0;
	return SellApp_AddTask(&SellTask);
}


uint8_t SellApp_SetSellTask(uint8_t cmd,void* pData,uint64_t sn,void (*pFun)(uint8_t,void*,uint16_t,uint64_t))
{
	SellTaskTypeDef SellTask;
	SellIdTypeDef   *pSellId;
	pSellId=pData;
	SellTask.SellId.cargo_no =pSellId->cargo_no;
	SellTask.SellId.cargo_num =pSellId->cargo_num;
	SellTask.SellId.contain_no=pSellId->contain_no;
	SellTask.SellId.shelf_no  =pSellId->shelf_no;
	SellTask.pTaskFinishCallBack=pFun;
	SellTask.SN                 =sn;
	SellTask.Cmd                =cmd;
	return SellApp_AddTask(&SellTask);
}

void SellApp_SetTaskState(uint8_t runstate)
{
	Sell.task_state=runstate;
}

uint8_t SellApp_GetSellState(void)
{
	return Sell.task_state;
}

//出货电机控制,内部调用
static uint8_t SellApp_MotorControl(SellTaskTypeDef *pTask)
{
	if(SellMotor_GetRunState(pTask->SellId.contain_no)==0)//检测电机运行状态
	{
		Sell.cargo_s    =0x02;//电机停止出货
		if(SellMotor_GetRunErrState(pTask->SellId.contain_no)==0)//运行正常
		{
			if(Sell.sell_delay<300)
			{
				if(Sensor_Get_GoodsIrFT(pTask->SellId.contain_no)||Sensor_Get_GoodsIrRT(pTask->SellId.contain_no))//出货成功 //出货成功
				{ 
					pTask->SellId.cargo_num--;
					return 0x01;
				}
				else if(Sell.sell_delay==0)//出货超时
				{
					if(Sell.cargo_rn)                     //重新出货
					{
	//					if(SellMotor_SetStar(pTask->SellId.contain_no,pTask->SellId.cargo_no,pTask->SellId.shelf_no)==0xFF)
	//					 {
							 Sell.cargo_s=0x01;
	//						 Sell.sell_delay=SELL_DELAY;
	//					 }
						Sell.cargo_rn--;
						return 0x02;//重新出货
					}
					else//未检到货物
					{
						return 0x03;//重新出货结束
					}
				}
			}
		}
		else
		{
			uint8_t sta;
			sta=SellMotor_GetRunErrState(pTask->SellId.contain_no);
			if(sta==0x01)//超时故障
			{				
				if(Sensor_Get_GoodsIrFT(pTask->SellId.contain_no)||Sensor_Get_GoodsIrRT(pTask->SellId.contain_no))//出货成功              //超时出货成功
				{
					pTask->SellId.cargo_num--;
					return 0x05;
				}
				return 0x04;                           //超时出货失败
		  }
			else//堵转故障
			{
				return 0x06;
			}
		}
	}
	else if((SellMotor_ReadPositErr(pTask->SellId.contain_no)==0x01))// ||(MotorDrive_ReadMotorMode()==MOTOR_CONVEYERMODE))//位置异常或为履带货道
	{
		if(Sensor_Get_GoodsIrFT(pTask->SellId.contain_no)||Sensor_Get_GoodsIrRT(pTask->SellId.contain_no)) //检测货物出货
		{
			pTask->SellId.cargo_num--;
			SellMotor_SetStop(pTask->SellId.contain_no,pTask->SellId.cargo_no,pTask->SellId.shelf_no);//关闭电机
			return 0x01;
		}
	}
	return 0x00;
}

//出货电机控制，内部调用
static uint8_t SellApp_CargoMotor(SellTaskTypeDef *pTask)
{
	static uint8_t runstate=0x00;
	uint8_t motorstate,cargostate=0x00;
	switch(runstate)
	{
		case 0x00:
			Sell.cargo_s=0x00;
		  runstate=0x01;
		  Sell.cargo_outtime=SELL_CARGO_OUTTIME*50;
			break;
		case 0x01:
			if(SellMotor_SetStar(pTask->SellId.contain_no,pTask->SellId.cargo_no,pTask->SellId.shelf_no))//检查设置是否成功
			{
				Sensor_Get_GoodsIrFT(pTask->SellId.contain_no);//清除红外标志位
				Sensor_Get_GoodsIrRT(pTask->SellId.contain_no);//清除红外标志位
				Sell.sell_delay=SELL_DELAY;
				runstate=0x02;
				Sell.cargo_outtime=SELL_CARGO_OUTTIME;
			}
			break;
		case 0x02://检测电机是否启动
			if(SellMotor_GetRunState(pTask->SellId.contain_no)==0X02)
			{
				Sensor_Get_GoodsIrFT(pTask->SellId.contain_no);//清除红外标志位
				Sensor_Get_GoodsIrRT(pTask->SellId.contain_no);//清除红外标志位
				if((MotorDrive_ReadPositErr()==0x00)||(Sell.cargo_s==0x01))//检测电机位置是否异常,或为重复出货
					Sell.cargo_rn  =0;
				 else
					Sell.cargo_rn  =SELLERR_RUNNUM;
				Sell.cargo_s=0x01;//出货中
				runstate=0x03;
				Sell.cargo_outtime=SELL_CARGO_OUTTIME*50;
				 Sell.sell_delay=SELL_DELAY;
			}
			break;
		case 0x03://检测出货是否完成
			motorstate=SellApp_MotorControl(pTask);
			switch(motorstate)
			{
				case 0x00:break;
				case 0x01:
					cargostate=0xFF;//出货完成
				  runstate=0x00;
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME;
					break;
				case 0x02:
					runstate=0x01;//重新出货
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME*50;
					break;
				case 0x03://未检测到货物
					cargostate=0x03;
				  runstate=0x00;
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME;
					break;
				case 0x04://超时出货失败
					if(SellMotor_GetLinkStateBit(pTask->SellId.contain_no,pTask->SellId.cargo_no,pTask->SellId.shelf_no))
					 cargostate=0x04;
					else
					 cargostate=0x01;
				  runstate=0x00;
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME;
					break;
				case 0x05://超时出货成功
					cargostate=0x05;
				  runstate=0x00;
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME;
					break;
				case 0x06://堵转出货
					cargostate=0x02;
					runstate=0x00;
				  Sell.cargo_outtime=SELL_CARGO_OUTTIME;
					break;
			}
			break;
	}
	if(Sell.cargo_outtime==0x00)//检测操作是否超时
	{
		cargostate=0x0E;
		runstate=0x00;
	}
	return cargostate;
}
//出货应用定时任务
void SellApp_TimeTask(void)
{
	if(Sell.cargo_s==0x02)
	{
		if(Sell.sell_delay>0)
		 Sell.sell_delay--;
	}
	if(Sell.shelsantime<SELL_SHELFSCAN_TIME)
		Sell.shelsantime++;
	else
	{
		SellApp_ShelfLinkScan();
		Sell.shelsantime=0;
	}
	if(Sell.cargo_outtime>0)
	 Sell.cargo_outtime--;
	if(Sell.lift_outtimr>0)
	 Sell.lift_outtimr--;
	if(Sell.tarck_outtime>0)
	 Sell.tarck_outtime--;
	if(Sell.liftrest_time>0)
	 Sell.liftrest_time--;
	if(Sell.taskwait_time>0)
		Sell.taskwait_time--;
	if(Sell.gaterest_time>0)
		Sell.gaterest_time--;	
	if(Sell.sellsta_time>0)
		Sell.sellsta_time--;
}

void SellApp_AddErrCodeToTaskSta(SellTaskStaTypeDef *pTaskSta,uint32_t err_code)
{
	pTaskSta->err[pTaskSta->err_num]=err_code;
	pTaskSta->err_num++;
}

int SellApp_ReadTaskStaSize(SellTaskStaTypeDef *pTaskSta)
{
	return (sizeof(pTaskSta->SellId)+2+(pTaskSta->err_num*4));
}

//出货应用程序
void SellApp_Task(void)
{
	Time_TypeDef	Time;
	static SellTaskTypeDef    Task;
	static SellTaskStaTypeDef TaskSta;
	uint8_t motor_state;
	
	switch(Sell.task_state)
	{
		case SELL_STATE_GETTASK://获取出货任务
			{
				if(SellApp_GetTask(&Task))
				{
					Sell.sell_state=0x01;
					TaskSta.SellId.cargo_no=Task.SellId.cargo_no;
					TaskSta.SellId.cargo_num=Task.SellId.cargo_num;
					TaskSta.SellId.contain_no=Task.SellId.contain_no;
					TaskSta.SellId.shelf_no=Task.SellId.shelf_no;
					TaskSta.SellId.code=Task.SellId.code;
					TaskSta.err_num=0;
					TaskSta.sta = OPERATE_FAIL;
					TaskSta.state = 1;
					
					SellApp_SetTaskState(SELL_STATE_START_ROUTE);
				}
				else
				{
//					if(Sell.gaterest_flag)
//					{
//						if(Sell.gaterest_time==0)
//						{
//							SellApp_SetTaskState(SELL_STATE_STOP_CLOSEGATE);
//							Sell.gaterest_flag = 0;
//						}
//					}
					if(Sell.sellsta_flag)
					{
						if(!Sell.sellsta_time)
						{
							Sell.sellsta_flag = 0;							
							if(MQTT_Get_Start_Status())
							{			
								if(SysConfig_Get_StoreState())
								{
									if(WirelessModule_ReadRssiSta())
									{
										DgusApp_Set_GotoPage(2);
									}
									else
									{
										DgusApp_Set_GotoPage(3);
									}
								}
								else
								{
									if(SysConfig_Get_QrCodeSize())
									{
										DgusApp_Set_GotoPage(5);
									}
									else
									{
										DgusApp_Set_GotoPage(4);
									}
								}
							}
							else
							{
								DgusApp_Set_GotoPage(0);
							}
						}
					}
				}
			}
			break;			
		case SELL_STATE_START_ROUTE://出货前路由步骤
			{
//				if(TaskSta.SellId.shelf_no < 2)
//				{
//					//0，1层，先开门，后出货
//					SellApp_SetTaskState(SELL_STATE_START_OPENGATE);
//				}
//				else if(TaskSta.SellId.shelf_no == 2)
//				{
//					//2层，先关门，后出货
//					SellApp_SetTaskState(SELL_STATE_START_CLOSEGATE);
//				}
//				else
//				{
					//其他层，直接出货
					SellApp_SetTaskState(SELL_STATE_DRIVECARGO);
//				}				
			}
			break;
		case SELL_STATE_START_OPENGATE://出货前，打开保温门
			{
				BasicGateMotor_Set(0,1,100,7000);
				SellApp_SetTaskState(SELL_STATE_START_OPENGATE_WAIT);
			}
			break;
		case SELL_STATE_START_OPENGATE_WAIT://等待保温门打开
			{
				if(!BasicGateMotor_Get_Enable(0))
				{
					if(!BasicGateMotor_Get_ErrStaCom(0))
					{
						//开门成功，下一步
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_NORMAL);
						SellApp_SetTaskState(SELL_STATE_DRIVECARGO);
					}
					else
					{
						//开门失败，结束任务
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_UNOPEN);
						
						if(Task.pTaskFinishCallBack2)
							Task.pTaskFinishCallBack2(TaskSta.SellId.code,TaskSta.state);								
												
						SellHistory_FixLogStateForCode(TaskSta.SellId.code,TaskSta.state);
						
						SellApp_SetTaskState(SELL_STATE_GETTASK);
					}
				}
			}
			break;
		case SELL_STATE_START_CLOSEGATE://出货前，关闭保温门
			{
				BasicGateMotor_Set(0,0,100,7000);
				SellApp_SetTaskState(SELL_STATE_START_CLOSEGATE_WAIT);
			}
			break;
		case SELL_STATE_START_CLOSEGATE_WAIT://等待保温门关闭
			{
				if(!BasicGateMotor_Get_Enable(0))
				{
					if(!BasicGateMotor_Get_ErrStaCom(0))
					{
						//关门成功，下一步
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_NORMAL);
						SellApp_SetTaskState(SELL_STATE_DRIVECARGO);
					}
					else
					{
						//关门失败，结束任务
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_UNCLOSE);
						
						if(Task.pTaskFinishCallBack2)
							Task.pTaskFinishCallBack2(TaskSta.SellId.code,TaskSta.state);		

						SellHistory_FixLogStateForCode(TaskSta.SellId.code,TaskSta.state);
						
						SellApp_SetTaskState(SELL_STATE_GETTASK);
					}
				}
			}
			break;			
		case SELL_STATE_DRIVECARGO://执行货道出货任务
			{
				motor_state=SellApp_CargoMotor(&Task);
				switch(motor_state)
				{
					case 0x00:break;
					case 0x01://电机未连接
							{
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_LINKERR);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_UNDETECT);
//								TaskSta.sta = OPERATE_FAIL;
								DgusApp_Set_GotoPage(8);			
								TaskSta.state = 302;
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;				
					case 0x02://电机堵转	
							{
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_BLOCK);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_UNDETECT);
//								TaskSta.sta = OPERATE_FAIL;
								DgusApp_Set_GotoPage(8);			
								TaskSta.state = 304;								
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;					
					case 0x03://未检测到货物
							{
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_NORMAL);
//								
//								TaskSta.sta = OPERATE_FAIL;
//								
//								Sell.sell_ir_errnum++;
//								if(Sell.sell_ir_errnum>SELL_IR_ERRNUM
//									||Sensor_Get_GoodsIrErr(Task.SellId.contain_no))
//								{
//									SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_ERR);
//								}
//								else
//								{
//									SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_UNDETECT);
//								}
								DgusApp_Set_GotoPage(8);			
								TaskSta.state = 301;
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);	
							}					
							break;					
					case 0x04://超时出货失败
							{
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_OUTIME);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_UNDETECT);
//								TaskSta.sta = OPERATE_FAIL;
								DgusApp_Set_GotoPage(8);			
								TaskSta.state = 302;								
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;
					case 0x05://电机超时出货成功
							{
//								Sell.sell_ir_errnum=0;
//								
								LED_Set(TaskSta.SellId.contain_no);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_OUTIME);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_NORMAL);
//								TaskSta.sta = OPERATE_SUCCESS;
								DgusApp_Set_GotoPage(7);	
								TaskSta.state = 2;									
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;
					case 0x0E://操作超时
							{
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_CONTROL_LINKERR);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_UNDETECT);
//								TaskSta.sta = OPERATE_FAIL;
								DgusApp_Set_GotoPage(8);			
								TaskSta.state = 302;
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;
					case 0xFF://出货成功
							{
								LED_Set(TaskSta.SellId.contain_no);
								
//								Sell.sell_ir_errnum=0;
//								
//								SellApp_AddErrCodeToTaskSta(&TaskSta,CARGO_MOTOR_NORMAL);
//								SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_IR_NORMAL);
//								TaskSta.sta=OPERATE_SUCCESS;								
								DgusApp_Set_GotoPage(7);	
								TaskSta.state = 2;
								SellApp_SetTaskState(SELL_STATE_STOP_ROUTE);
							}
							break;
				}
			}
			break;
		case SELL_STATE_STOP_ROUTE://根据所在层路由下一步
			{
//				if(TaskSta.SellId.shelf_no<2)
//				{
//					//0，1层，出货后，要关闭保温门
//					Sell.gaterest_flag = 1;
//					Sell.gaterest_time = SELL_GATEREST_TIME;
//					SellApp_SetTaskState(SELL_STATE_GETTASK);
//					
//				}
//				else
//				{
					//其他层，结束出货任务
					//显示出货故障信息
					if(Task.pTaskFinishCallBack2)
							Task.pTaskFinishCallBack2(TaskSta.SellId.code,TaskSta.state);		
					
					//更新出货LOG
//					DgusApp_Set_ShowSellLog(NULL);
										
					//更新系统故障
					if(TaskSta.SellId.code,TaskSta.state == 301)
					{
						if(Sell.sell_ir_errnum<2)
						{
							Sell.sell_ir_errnum++;
							
						}
						else
						{
							if(CloudProtocol_Get_DeviceState() == 104)
							{
								CloudProtocol_Set_DeviceState(106);
							}
							else if(CloudProtocol_Get_DeviceState() == 0)
							{
								CloudProtocol_Set_DeviceState(102);
							}
						}						
					}
					else if(TaskSta.SellId.code,TaskSta.state == 2)
					{
						Sell.sell_ir_errnum = 0;
						
						if(CloudProtocol_Get_DeviceState() == 106)
						{
							CloudProtocol_Set_DeviceState(104);
						}
						else if(CloudProtocol_Get_DeviceState() == 102)
						{
							CloudProtocol_Set_DeviceState(0);
						}
					}
					
					SellHistory_FixLogStateForCode(TaskSta.SellId.code,TaskSta.state);
										
					SellApp_SetTaskState(SELL_STATE_GETTASK);
										
					Sell.sellsta_flag = 1;
					Sell.sellsta_time = 500;
//				}			
			}
			break;			
			
		case SELL_STATE_STOP_CLOSEGATE://出货后，关闭保温门
			{
				BasicGateMotor_Set(0,0,100,7000);
				SellApp_SetTaskState(SELL_STATE_STOP_CLOSEGATE_WAIT);
			}
			break;
		case SELL_STATE_STOP_CLOSEGATE_WAIT://等待保温门关闭
			{
				if(!BasicGateMotor_Get_Enable(0))
				{
					if(!BasicGateMotor_Get_ErrStaCom(0))
					{
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_NORMAL);					
					}
					else
					{
						SellApp_AddErrCodeToTaskSta(&TaskSta,GOODS_INNERGATE_UNCLOSE);										
					}
					
					//任务结束
					if(Task.pTaskFinishCallBack)
							Task.pTaskFinishCallBack(Task.Cmd,&TaskSta,SellApp_ReadTaskStaSize(&TaskSta),Task.SN);			
					
					SellHistory_FixLogStateForCode(TaskSta.SellId.code,TaskSta.state);
					
					SellApp_SetTaskState(SELL_STATE_GETTASK);
				}
			}
			break;
		default:break;				
	}
}
