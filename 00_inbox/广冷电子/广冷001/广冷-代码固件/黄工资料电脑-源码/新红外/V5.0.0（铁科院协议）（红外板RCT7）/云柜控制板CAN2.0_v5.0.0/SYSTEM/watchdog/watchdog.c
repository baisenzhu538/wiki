#include "watchdog.h"

//当前设置溢出时间为1S
//Tout=((4×2^prer) ×rlr) /40
void WatchDog_Init(u8 prer,u16 rlr)
{
	IWDG_WriteAccessCmd(IWDG_WriteAccess_Enable);
	//使能对寄存器 IWDG_PR 和 IWDG_RLR 的写操作
	IWDG_SetPrescaler(prer); 
	//设置 IWDG 预分频值:设置 IWDG 预分频值为 64
	IWDG_SetReload(rlr); 	//设置 IWDG 重装载值
	IWDG_ReloadCounter(); 	//按照 IWDG 重装载寄存器的值重装载 IWDG 计数器
	IWDG_Enable(); 			//使能 IWDG
}
	
	
//喂独立看门狗
void WatchDog_Feed(void)
{
	IWDG->KR=0XAAAA;//reload
}


void WatchDog_Drive(void)
{
	WatchDog_Feed();
}


