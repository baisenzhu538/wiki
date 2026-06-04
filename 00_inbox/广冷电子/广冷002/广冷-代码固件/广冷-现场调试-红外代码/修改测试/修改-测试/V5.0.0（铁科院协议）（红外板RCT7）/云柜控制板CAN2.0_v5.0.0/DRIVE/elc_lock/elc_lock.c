#include "elc_lock.h"
ElcLockDriveTypeDef ElcLockDrive={0,0,0,0};
ElcLockSignalTypeDef ElcLockSignal[2];

void ElcLock_GpioInit(void)
{
 GPIO_InitTypeDef  GPIO_InitStructure;
 	
  RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB|RCC_APB2Periph_GPIOC
	                      |RCC_APB2Periph_AFIO, 
							ENABLE);	 
	GPIO_PinRemapConfig(GPIO_Remap_SWJ_JTAGDisable, ENABLE);

	GPIO_InitStructure.GPIO_Mode  = GPIO_Mode_Out_PP; 		 //推挽输出
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;		 //IO口速度为50MHz
	GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_3;
	GPIO_Init(GPIOB, &GPIO_InitStructure); 	
	
	GPIO_ResetBits(GPIOB,GPIO_Pin_3);
	GPIO_SetBits(GPIOB,GPIO_Pin_3);
	
	GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_15;
	GPIO_Init(GPIOC, &GPIO_InitStructure); 
	
	ELCLOCK_CLOSE1;
		
}

void ElcLock_Open(void)
{
//	if(ElcLockDrive.sta==0x00)
//	{
	 ElcLockDrive.sta=0x01;
	 ELCLOCK_OPEN1;	
//   ELCLOCK_OPEN2;		
//	}
}

void ElcLock_Close(void)
{
//	if(ElcLockDrive.sta==0x01)
//	{
	 ElcLockDrive.sta=0x00;
   ELCLOCK_CLOSE1;
//   ELCLOCK_CLOSE2;		
//	}
}

uint8_t ElcLock_ReadLockState(void)
{
	if(ElcLockSignal[0].state==0)//完全打开
	 return 0x00;
	else if(ElcLockSignal[0].state==1)//完全关闭
	 return 0x01;
	else//未完全开关
	 return 0x02;
}

uint8_t ElcLock_ReadLockErr(void)
{
	return ElcLockDrive.err;
}

void ElcLock_SetEnable(void)
{
	ElcLockDrive.en=0x01;
}

void ElcLock_ResetEnable(void)
{
	ElcLockDrive.en=0x00;
}

uint8_t ElcLock_ReadEnableSta(void)
{
	return ElcLockDrive.en;
}



//10ms定时运行
void ElcLock_GetSignalSta(void)
{
	ElcLockSignal[0].state=DigitalSignal_GetSignalLevelBit(3,2);
	
	ElcLockSignal[0].ft|=DigitalSignal_GetSignalFallingBit(3,2);
	
	ElcLockSignal[0].rt|=DigitalSignal_GetSignalRisingBit(3,2);
}
void ElcLock_TaskRun(void)
{
	ElcLock_GetSignalSta();
	if(ElcLockDrive.en)
	{
		ElcLock_Open();
		if(ElcLockDrive.opentime<ELCLOCK_OPEN_OVERTIMR)
		 ElcLockDrive.opentime++;
//		if(ElcLock_ReadLockState()==0x00)//打开成功
//		{
//			ElcLock_Close();
//			ElcLockDrive.en=0x00;
//			ElcLockDrive.err=0x00;
//		}
		else if(ElcLockDrive.opentime==ELCLOCK_OPEN_OVERTIMR)//超时开启失败
		{
			ElcLock_Close();
			ElcLockDrive.opentime=0;
			ElcLockDrive.en=0x00;
			ElcLockDrive.err=0x01;
		}
	}
	else
	{
		ElcLock_Close();
		ElcLockDrive.opentime=0;
	}
}





