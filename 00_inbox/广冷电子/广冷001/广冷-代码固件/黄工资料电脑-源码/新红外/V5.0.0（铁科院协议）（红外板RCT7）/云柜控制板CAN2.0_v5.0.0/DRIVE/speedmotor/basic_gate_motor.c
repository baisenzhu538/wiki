#include "basic_gate_motor.h"

BasicGateMotor_Manage_TypeDef	BasicGateMotorManage[BASIC_GATE_MOTOR_MAX_NUM];

void BasicGateMotor_Init(void)
{
	SpeedMotorGpio_Init();
//	BasicGateMotor_Set(0,0,100,7000);
//	BasicGateMotor_Set(1,0,100,7000);
}

void BasicGateMotor_Set(uint8_t motor_no,uint8_t dir,uint8_t speed,uint16_t outtime)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return ;
	if(BasicGateMotorManage[motor_no].drive.enable)
		return ;
		
	BasicGateMotorManage[motor_no].drive.dir = dir;
	BasicGateMotorManage[motor_no].drive.speed = speed;
	BasicGateMotorManage[motor_no].drive.outtime = outtime;
	BasicGateMotorManage[motor_no].drive.enable = 0x01;
}

uint8_t BasicGateMotor_Get_Enable(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return BasicGateMotorManage[motor_no].drive.enable;
}

uint8_t BasicGateMotor_Get_State(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return BasicGateMotorManage[motor_no].state.state;
	
	
}

uint8_t BasicGateMotor_Get_ErrStaCom(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return 	BasicGateMotorManage[motor_no].state.errsta.com;
}

uint8_t BasicGateMotor_Get_ErrStaOuttime(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return BasicGateMotorManage[motor_no].state.errsta.outtime;
}

uint8_t BasicGateMotor_Get_ErrStaPosit(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return BasicGateMotorManage[motor_no].state.errsta.posit;
}

uint8_t BasicGateMotor_Get_LimiteDownSwSta(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;

	return BasicGateMotorManage[motor_no].state.limite.down_sw_sta;	
}

uint8_t BasicGateMotor_Get_LimiteUpSwSta(uint8_t motor_no)
{
	if(motor_no >= BASIC_GATE_MOTOR_MAX_NUM)
		return 0;
	
	return BasicGateMotorManage[motor_no].state.limite.up_sw_sta;	
}

void BasicGateMotor_RunTest(void)
{		
//	if(Sensor_Get_KeyRt(0))
//	{
//		BasicGateMotor_Set(0,0,100,7000);
//	}
//	else if(Sensor_Get_KeyFt(0))
//	{
//		BasicGateMotor_Set(0,1,100,7000);
//	}
//			
//	if(Sensor_Get_KeyRt(1))
//	{
//		BasicGateMotor_Set(1,0,100,7000);
//	}	
//	else if(Sensor_Get_KeyFt(1))
//	{
//		BasicGateMotor_Set(1,1,100,7000);
//	}
}

void BasicGateMotor_TIM_Task(void)
{
	uint8_t i;
	
	for(i=0;i<BASIC_GATE_MOTOR_MAX_NUM;i++)
		BasicGateMotorManage[i].step.runtime++;
}

void BasicGateMotor_Collect(void)
{
	uint8_t i;
	
	for(i=0;i<BASIC_GATE_MOTOR_MAX_NUM;i++)
	{	
		BasicGateMotorManage[i].state.limite.up_sw_sta = Sensor_Get_MotorUpSta(i);
		BasicGateMotorManage[i].state.limite.down_sw_sta = Sensor_Get_MotorDownSta(i);
	}
}

void BasicGateMotor_RunTask(void)
{
	static uint8_t i;
	static uint8_t jump_cnt;
		
	for(i=0;i<BASIC_GATE_MOTOR_MAX_NUM;i++)
	{
		if(BasicGateMotorManage[i].drive.enable)
		{
			switch(BasicGateMotorManage[i].step.step)
			{
				case 0://初始化
				{				
					
					BasicGateMotorManage[i].state.errsta.com = 0;
					BasicGateMotorManage[i].state.errsta.outtime = 0;
					BasicGateMotorManage[i].state.errsta.posit = 0;
					BasicGateMotorManage[i].state.state = 1;
					BasicGateMotorManage[i].step.runtime = 0;
					BasicGateMotorManage[i].step.step = 1;
				}
				break;
				case 1://判断当前位置
				{
					if(Sensor_Get_MotorUpSta(i)
						&& Sensor_Get_MotorDownSta(i))
					{									
						//位置异常
						BasicGateMotorManage[i].step.step = 0;
						BasicGateMotorManage[i].state.state = 0x02;									
						BasicGateMotorManage[i].state.errsta.com = 1;
						BasicGateMotorManage[i].state.errsta.posit = 1;
						BasicGateMotorManage[i].drive.enable = 0x00;						
					}
					else
					{
						if(BasicGateMotorManage[i].drive.dir == 0)
						{
							//关门
							if(Sensor_Get_MotorUpSta(i))
							{
								//已关门
								BasicGateMotorManage[i].step.step = 0;
								BasicGateMotorManage[i].state.state = 0x02;
								BasicGateMotorManage[i].drive.enable = 0x00;
							}
							else
							{
								//去关门
								BasicGateMotorManage[i].step.step = 2;						
							}
						}
						else
						{
							//开门
							if(Sensor_Get_MotorDownSta(i))
							{
								//已开门
								BasicGateMotorManage[i].step.step = 0;
								BasicGateMotorManage[i].state.state = 0x02;
								BasicGateMotorManage[i].drive.enable = 0x00;
							}
							else
							{
								//去开门
								BasicGateMotorManage[i].step.step = 2;						
							}							
						}	
					}																		
				}
				break;
				case 2://启动电机
				{
					if(BasicGateMotorManage[i].drive.dir == 0)
					{
						//关门
						Sensor_Get_MotorUpRt(i);						
						Sensor_Get_MotorUpFt(i);
						SpeedMotorGpio_Dir_Forward(i);
					}
					else
					{
						//开门
						Sensor_Get_MotorUpRt(i);
						Sensor_Get_MotorUpFt(i);
						SpeedMotorGpio_Dir_Reverse(i);
					}

					SpeedMotorGpio_PWM_Set(i,BasicGateMotorManage[i].drive.speed);
					SpeedMotorGpio_Power_Enable(i);
					BasicGateMotorManage[i].step.runtime = 0;
					BasicGateMotorManage[i].step.step = 3;
				}
				break;
				case 3://等待电机触发限位
				{
					if(Sensor_Get_MotorUpSta(i)
						&& Sensor_Get_MotorDownSta(i))
					{
						//位置异常
						SpeedMotorGpio_Power_Disable(i);
						SpeedMotorGpio_PWM_Set(i,0);
						SpeedMotorGpio_Dir_Brake(i);
						
						BasicGateMotorManage[i].step.step = 0;
						BasicGateMotorManage[i].state.state = 0x02;
						BasicGateMotorManage[i].state.errsta.com = 1;
						BasicGateMotorManage[i].state.errsta.posit = 1;
						BasicGateMotorManage[i].drive.enable = 0x00;
						return ;
					}
					
					if(BasicGateMotorManage[i].step.runtime<BasicGateMotorManage[i].drive.outtime)
					{									
						if(BasicGateMotorManage[i].drive.dir == 0)
						{					
							//关门
							if(Sensor_Get_MotorUpSta(i))
							{
								//已关门
								SpeedMotorGpio_Power_Disable(i);
								SpeedMotorGpio_PWM_Set(i,0);
								SpeedMotorGpio_Dir_Brake(i);
								
								BasicGateMotorManage[i].step.step = 0;
								BasicGateMotorManage[i].state.state = 0x02;
								BasicGateMotorManage[i].drive.enable = 0x00;
							}
						}
						else
						{
							//开门
							if(Sensor_Get_MotorDownSta(i))
							{
								//已开门								
								SpeedMotorGpio_Power_Disable(i);
								SpeedMotorGpio_PWM_Set(i,0);
								SpeedMotorGpio_Dir_Brake(i);
								
								if(i==0)
								{
//									if(Sensor_Get_MotorDownSta(1))
//									{
										//不动
										BasicGateMotorManage[i].step.step = 0;
										BasicGateMotorManage[i].state.state = 0x02;
										BasicGateMotorManage[i].drive.enable = 0x00;	
//									}
//									else
//									{
//										//动
//										BasicGateMotorManage[i].step.step = 4;
//									}
								}
								else
								{
//									if(Sensor_Get_MotorDownSta(0))
//									{
										//不动
										BasicGateMotorManage[i].step.step = 0;
										BasicGateMotorManage[i].state.state = 0x02;
										BasicGateMotorManage[i].drive.enable = 0x00;										
//									}
//									else
//									{
//										//动
//										BasicGateMotorManage[i].step.step = 4;
//									}
								}
								

							}
						}								
					}
					else
					{					
						SpeedMotorGpio_Power_Disable(i);
						SpeedMotorGpio_PWM_Set(i,0);
						SpeedMotorGpio_Dir_Brake(i);
						
						BasicGateMotorManage[i].step.step = 0;
						BasicGateMotorManage[i].state.errsta.com = 1;
						BasicGateMotorManage[i].state.errsta.outtime = 1;
						BasicGateMotorManage[i].state.state = 0x02;
						BasicGateMotorManage[i].drive.enable = 0x00;
					}
				}
				break;
				case 4://当上面操作为开门时，对面门抖几下
				{
					BasicGateMotorManage[i].step.runtime = 0;
					if(i==0)
					{						
						if(jump_cnt%2)
							SpeedMotorGpio_Dir_Reverse(1);							
						else
							SpeedMotorGpio_Dir_Forward(1);
						SpeedMotorGpio_PWM_Set(1,BasicGateMotorManage[i].drive.speed);
						SpeedMotorGpio_Power_Enable(1);		
					}
					else
					{						
						if(jump_cnt%2)
							SpeedMotorGpio_Dir_Reverse(0);							
						else
							SpeedMotorGpio_Dir_Forward(0);
						SpeedMotorGpio_PWM_Set(0,BasicGateMotorManage[i].drive.speed);
						SpeedMotorGpio_Power_Enable(0);		
					}
					BasicGateMotorManage[i].step.step = 5;
				}
				break;
				case 5:
				{
					if(BasicGateMotorManage[i].step.runtime>200)
					{
						SpeedMotorGpio_Power_Disable(0);
						SpeedMotorGpio_PWM_Set(0,0);
						SpeedMotorGpio_Dir_Brake(0);
						SpeedMotorGpio_Power_Disable(1);
						SpeedMotorGpio_PWM_Set(1,0);
						SpeedMotorGpio_Dir_Brake(1);
						BasicGateMotorManage[i].step.runtime = 0;
						
						if(jump_cnt<3)
						{
							jump_cnt++;
							BasicGateMotorManage[i].step.step = 4;
						}
						else
						{
							jump_cnt=0;
							BasicGateMotorManage[i].step.step = 6;
						}						
					}
				}
				break;
				case 6:
				{
					BasicGateMotorManage[i].step.runtime = 0;
					if(i==0)
					{						
						SpeedMotorGpio_Dir_Reverse(1);
						SpeedMotorGpio_PWM_Set(1,BasicGateMotorManage[i].drive.speed);
						SpeedMotorGpio_Power_Enable(1);		
					}
					else
					{						
						SpeedMotorGpio_Dir_Reverse(0);
						SpeedMotorGpio_PWM_Set(0,BasicGateMotorManage[i].drive.speed);
						SpeedMotorGpio_Power_Enable(0);		
					}
					BasicGateMotorManage[i].step.step = 7;
				}
				break;
				case 7:
				{
					if(BasicGateMotorManage[i].step.runtime>0)
					{
						SpeedMotorGpio_Power_Disable(0);
						SpeedMotorGpio_PWM_Set(0,0);
						SpeedMotorGpio_Dir_Brake(0);
						SpeedMotorGpio_Power_Disable(1);
						SpeedMotorGpio_PWM_Set(1,0);
						SpeedMotorGpio_Dir_Brake(1);
						
						BasicGateMotorManage[i].step.runtime = 0;
						BasicGateMotorManage[i].step.step = 0;
						BasicGateMotorManage[i].state.state = 0x02;
						BasicGateMotorManage[i].drive.enable = 0x00;
					}
				}
				break;
			}	
		}
	}
}

void BasicGateMotor_Task(void)
{
	BasicGateMotor_RunTest();
	BasicGateMotor_RunTask();
	BasicGateMotor_Collect();
}

