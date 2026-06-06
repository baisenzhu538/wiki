#include "sell_app.h"

Sell_TypeDef Sell;

//出货应用任务初始化
void SellApp_Init(void)
{
	Sell.cargo_rn=0;
	Sell.cargo_s=0;
	Sell.sell_delay=SELL_DELAY;
	Sell.sell_flag=0;
	Sell.sell_fail  =0;
	Sell.task_state =0;
	Sell.sell_state=0;
	Sell.SellTask.q_head=0;
	Sell.SellTask.q_tail=0;
	Sell.SellTask.q_len =SELLTASK_QUEULEN;
}

uint8_t SellApp_AddTask(SellTaskTypeDef *pSellTask)
{
	uint8_t i;
	if(Sell.SellTask.q_len==0)
	 return 0x00;
  if((Sell.SellTask.q_head==Sell.SellTask.q_tail)&&(Sell.SellTask.q_head>Sell.SellTask.q_tail))
	{
		for(i=Sell.SellTask.q_head;i<SELLTASK_QUEULEN;i++)
		{
			if(*((uint32_t*)(&Sell.SellTask.selltask[Sell.SellTask.q_tail]))==*((uint32_t*)pSellTask))
			{
				return 0x01;//已存在相同任务
			}
		}
		for(i=0;i<Sell.SellTask.q_tail;i++)
		{
			if(*((uint32_t*)(&Sell.SellTask.selltask[Sell.SellTask.q_tail]))==*((uint32_t*)pSellTask))
			{
				return 0x01;//已存在相同任务
			}
		}
	}
	else
	{
		for(i=Sell.SellTask.q_head;i<Sell.SellTask.q_tail;i++)
		{
			if(*((uint32_t*)(&Sell.SellTask.selltask[Sell.SellTask.q_tail]))==*((uint32_t*)pSellTask))
			{
				return 0x01;//已存在相同任务
			}
		}
	}
	
	*((uint32_t*)(&Sell.SellTask.selltask[Sell.SellTask.q_tail]))=*((uint32_t*)pSellTask);
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
	Procotol_Memcopy((uint8_t*)ptask,(uint8_t*)&Sell.SellTask.selltask[Sell.SellTask.q_head],sizeof(SellTaskTypeDef));
	Sell.SellTask.q_head++;
	Sell.SellTask.q_len++;
	if(Sell.SellTask.q_head==SELLTASK_QUEULEN)
		Sell.SellTask.q_tail=0;
	return 0x01;
}

void SellApp_SetTaskState(uint8_t runstate)
{
	Sell.task_state=runstate;
}
//出货应用定时任务
void SellApp_TimeTask(void)
{
	if(Sell.cargo_s==0x02)
	{
		if(Sell.sell_delay>0)
		 Sell.sell_delay--;
	}
}
//弹簧货道出货任务
void SellApp_Coil(SellTaskTypeDef *pTask)
{
	if(MotorDrive_GetEnStateBit(pTask->cargo_no-1)==0)
	{
		if(MotorDrive_GetErrStateBit(pTask->cargo_no-1)==0)//电机工作正常,完成出货过程
		{
			Sell.cargo_s    =0x02;                     //出货完成
			if(Sensor_GetGoodsIr1FT())              //出货成功
			{
				pTask->cargo_num--;
				SellApp_SetTaskState(0x03);
			}
			else if(Sell.sell_delay==0)
			{
				if(Sell.cargo_rn)                     //重新出货
				{
					if(MotorDrive_SetBit(pTask->cargo_no-1)==0xFF)
					 {
						 Sell.cargo_s    =0x01;
						 Sell.sell_delay=SELL_DELAY;
					 }
					Sell.cargo_rn--;
				}
				else//未检到货物
				{
					SellApp_SetTaskState(0x04);
				}
			}
		}
		else//电机工作异常
		{
			if(MotorDrive_GeOTStateBit(pTask->cargo_no-1)==0)//电机超时
			{
				if(Sensor_GetGoodsIr1FT())              //出货成功
				{
					pTask->cargo_num--;
				}
				SellApp_SetTaskState(0x05);
			}
			if(MotorDrive_GetBlockStateBit(pTask->cargo_no-1)==0)//电机堵转，只有弹簧货道有该模式
			{
				if(Sensor_GetGoodsIr1FT())              //出货成功
				{
					pTask->cargo_num--;
				}
				SellApp_SetTaskState(0x06);
			}
		}
	}
}

uint8_t SellApp_GetSellState(void)
{
	return Sell.task_state;
}
//履带货道出货任务
void SellApp_Comveyer(SellTaskTypeDef *pTask)
{
	if(MotorDrive_GetEnStateBit(pTask->cargo_no-1)==0)
	{
		if(MotorDrive_GetErrStateBit(pTask->cargo_no-1)==0)
		{
			Sell.cargo_s    =0x02;                     //出货完成
			if(Sensor_GetGoodsIr1FT())              //出货成功
			{
				pTask->cargo_num--;
				SellApp_SetTaskState(0x03);
			}
			else if(Sell.sell_delay==0)
			{
				if(Sell.cargo_rn)                     //重新出货
				{
					if(MotorDrive_SetBit(pTask->cargo_no-1)==0xFF)
					 {
						 Sell.cargo_s    =0x01;
						 Sell.sell_delay=SELL_DELAY;
					 }
					Sell.cargo_rn--;
				}
				else//未检到货物
				{
					SellApp_SetTaskState(0x04);
				}
			}
	  }
	  else
		{
			if(MotorDrive_GeOTStateBit(pTask->cargo_no-1)==0)//电机超时
			{
				if(Sensor_GetGoodsIr1FT())              //出货成功
				{
					pTask->cargo_num--;
				}
				SellApp_SetTaskState(0x05);
			}
		}
	}
	else if(Sensor_GetGoodsIr1FT())              //出货成功
	{
		pTask->cargo_num--;
		MotorDrive_ResetBit(pTask->cargo_no-1);//关闭电机
		SellApp_SetTaskState(0x08);
	}
}

//出货应用程序
void SellApp_Task(void)
{
	static SellTaskTypeDef Task;
	uint8_t data[2];
	uint8_t motor_state;
	switch(Sell.task_state)
	{
		case 0x00:
			if(SellApp_GetTask(&Task))
			{
				Sell.sell_state=0x01;
				SellApp_SetTaskState(0x01);
			}
			else
				Sell.sell_state=0x00;
			break;
		case 0x01:
			 motor_state=MotorDrive_SetBit(Task.cargo_no-1);
		   Sensor_GetGoodsIr1FT();//清除红外标志位
		   switch(motor_state)
			 {
				 case 0x00://电机未连接
					 SellApp_SetTaskState(0x07);
					 break;
				 case 0x01://电机堵转
					 SellApp_SetTaskState(0x05);
					 break;
				 case 0x02://电机超时
					 SellApp_SetTaskState(0x06);
					 break;
				 case 0xFF:
				   Sell.sell_delay=SELL_DELAY;
				   if(MotorDrive_GetPositionStateBit(Task.cargo_no-1))//检测电机位置是否在初始位置
				    Sell.cargo_rn  =0;
				   else
					  Sell.cargo_rn  =SELLERR_RUNNUM;
				   SellApp_SetTaskState(0x02);
					 break;
				 default:break;
			 }
			break;
		case 0x02:
			if(MotorDrive_ReadMotorMode()==MOTOR_COILMODE)
			 SellApp_Coil(&Task);//调用弹簧货道出货程序
			else if(MotorDrive_ReadMotorMode()==MOTOR_CONVEYERMODE)
			 SellApp_Comveyer(&Task);//调用履带货道出货程序
		break;
		case 0x03://出货成功
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x05,Task.sn,data,2))
			{
				if(Task.cargo_num)
				{
					SellApp_SetTaskState(0x01);
				}
				else
				 SellApp_SetTaskState(0x00);
			}
		 break;
		case 0x04://红外未检测到货物
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x06,Task.sn,data,2))
		   SellApp_SetTaskState(0x00);
		 break;
		case 0x05://电机运行超时
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x08,Task.sn,data,2))
		   SellApp_SetTaskState(0x00);
		 break;
		case 0x06://电机堵转
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x07,Task.sn,data,2))
		   SellApp_SetTaskState(0x00);
		 break;
		case 0x07://电机未连接
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x09,Task.sn,data,2))
		   SellApp_SetTaskState(0x00);
			break;
		case 0x08://履带位置检测未检测到
			data[0]=Task.cargo_no;
			data[1]=Task.cargo_num;
			if(SerialProcotol_SendCmd(0x04,0x00,0x0C,Task.sn,data,2))
		   SellApp_SetTaskState(0x00);
			break;
	}
}
