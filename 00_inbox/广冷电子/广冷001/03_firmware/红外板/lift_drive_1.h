#ifndef __LIFT_DRIVE_H
#define __LIFT_DRIVE_H
#include "stm32f10x.h"
#include "stm32f10x_tim.h"
#include "encoder.h"


#define LIFTMOTOR_HIGHESTSPEED_FRE        16000 //最高速运行频率
#define LIFTMOTOR_LOWESTSPEED_FRE         2560  //最低速运行频率
#define LIFTMOTER_UPSTEP_FRC              10                //加速步进频率

#define LIFTMOTOR_TIMER_FRE               (uint32_t)72000000//定时器时钟频率

#define LIFTMOTOR_HIGHESTSPEED_LEVEL      1344              //最高速级
#define LIFTMOTOR_LOWESTSPEED_LEVEL       0                 //最低速级

#define LIFTMOTOR_UPSEPEED1_HIGHEST       300
#define LIFTMOTOR_UPSEPEED2_HIGHEST       1000
#define LIFTMOTOR_UPSEPEED3_HIGHEST       1344

#define LIFTMOTOR_UPSEPEED1_STEP          4
#define LIFTMOTOR_UPSEPEED2_STEP          6
#define LIFTMOTOR_UPSEPEED3_STEP          8

#define LIFTMOTER_STAR_UP                  0x01 //电机上升
#define LIFTMOTER_STAR_DOWN                0x00 //电机下降

#define LIFTMOTOR_LIFTMOTOR_ENABLE        GPIO_SetBits(GPIOB,GPIO_Pin_11)     //驱动电机
#define LIFTMOTOR_LIFTMOTOR_DISABLE       GPIO_ResetBits(GPIOB,GPIO_Pin_11)   //停止电机

#define LIFTMOTOR_LIFTDIR_UP              GPIO_SetBits(GPIOA,GPIO_Pin_8)     //顺时针
#define LIFTMOTOR_LIFTDIR_DOWN            GPIO_ResetBits(GPIOA,GPIO_Pin_8)   //逆时针

#define LIFTMOTOR_MOTORDRIVE_ENABLE       GPIO_SetBits(GPIOC,GPIO_Pin_6)
#define LIFTMOTOR_MOTORDRIVE_DISABLE      GPIO_ResetBits(GPIOC,GPIO_Pin_6)


typedef struct
{
	uint8_t  sta;             //运行状态，0停止状态，1加速状态，2匀速状态，3减速状态	
	uint8_t  err;             //错误状态
	uint16_t highspeed;       //设置最高运行速度
	uint16_t starspeed0;       //设置起始速度
	
	uint16_t runspeed;        //运行速度
	uint16_t starspeed1;       //设置起始速度
	uint16_t starspeed2;       //设置起始速度
	uint16_t starspeed3;       //设置起始速度
	
	uint32_t uplaststep1;     
	uint32_t uplaststep2;
	uint32_t uplaststep3;
	
	uint32_t stepnum;         //电机运行步数
	uint32_t set_stepnum;     //设置步数
	
	int32_t  encoder_posit;   //编码器位置
	int32_t  star_posit;
}LiftDrive_MotorControlTypeDef;

void LiftDrive_Init(void);
void LifeDrive_StarMotor(uint16_t starspeed,uint16_t highspeed,uint32_t set_stepnum,uint8_t dir);
void LifeDrive_StopMotor(void);
void LifeDrive_StarMotorPositMod(uint32_t set_stepnum,uint8_t dir);
uint8_t LiftDrive_GetMotorSta(void);
uint8_t LiftDrive_GetMotorErr(void);
void LifeDrive_Enable(void);
void LifeDrive_Disable(void);
#endif
