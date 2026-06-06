#ifndef __CRYOGEN_DRIVE_H
#define __CRYOGEN_DRIVE_H
#include "stm32f10x.h"
#include "compressor_control.h"
#include "sensor.h"

#define CRYOGEN_LONGTIME   7200    //单位为s，最长工作时间2个小时
#define CRYOGEN_CYCLETIME  1200    //单位s，循环时间为20分钟
#define CRYOGEN_STARTTIME  180     //单位s，启动时间为3分钟
#define CRYOGEN_RECOVETIME 1800    //30分钟
#define FWV_AHEADTTIME     5       //四通阀提前启动时间，单位s
#define TEMP_DEVIATION     1       //温度偏差超过该值启动压缩机

#define CRYOGEN_COLDMODE       0
#define CRYOGEN_HOTMODE        1

typedef struct
{
	uint8_t  cryogen_state :1;    //0机组休眠中，1机组工作中
  uint8_t  comp_state    :1;    //工作状态       0压缩机停止工作，1压缩机工作
	uint8_t  fan_state     :1;    //风扇状态       0风扇停止工作，1风扇工作
	uint8_t  fwv_state     :1;    //四通阀状态  
	uint8_t  spare_state   :1;    //保留继电器状态
	uint8_t  temp_state    :1;    //温度状态，0为未达到设定温度，1为达到设定温度
	uint8_t  forst_staste  :1;    //化霜状态
	uint8_t  humid_state   :1;    //湿度控制状态，0为未达到设定湿度，1为达到设定湿度
}StateBitTypeDef;


typedef struct
{
 StateBitTypeDef state_bit;
 uint8_t  currrent_mode:4;
 uint8_t  err          :4;
 int8_t   current_temp;        //当前温度
 int8_t   current_humid;       //当前湿度 
}CryogenStateTypeDef;

typedef struct
{
 CryogenStateTypeDef runsta;
 uint16_t  cRecoveTime;         //恢复时间计数	
 uint16_t  cFanTime;            //风扇运行时间计数
 uint16_t  cRunTime;            //机组运行时间计数
 uint16_t  cStartTime;          //启动时间计数
}CryogenDriveStateTypeDef;


typedef struct
{
 uint8_t  cryogen_en:1;    //制冷工作使能位 0执行温度控制1停止机组工作
 uint8_t  comp_en   :1;
 uint8_t  fan_en    :1;
 uint8_t  fwv_en    :1;
 uint8_t  spare_en  :1;
 uint8_t  humid_en  :1;    //湿度控制使能位
 uint8_t  receve    :2;     //io控制使能位 bn 
}EnbaleBitTypeDef;

typedef struct
{
 EnbaleBitTypeDef enable_bit;
 uint8_t mode;          //温控模式
 int8_t  temp;          //设置温度+-125
 int8_t  humid;         //设置湿度
}CryogenSetTypeDef;

typedef	struct
{
	int8_t	T1;
	int8_t	T2;
	
}CryogenSet2TypeDef;

typedef struct
{
 CryogenSetTypeDef set;
 uint8_t  fwv_ahead;     //四通阀提前开启时间
 uint16_t longtime;      //最长运行时间
 uint16_t recovetime;    //压缩机恢复时间
 uint16_t starttime;     //压缩机上电、模式转换启动时间
 uint16_t cycletime;     //风扇循环时间
}CryogenDriveInfoTypeDef;

extern CryogenDriveStateTypeDef CryogenDriveState;
extern CryogenDriveInfoTypeDef  CryogenDriveInfo;

void CryogenDrive_Init(void);
void CryogenDrive_TaskRun(void);
int8_t CryogenDrive_GetDevTemp(void);
uint8_t CryogenDrive_GetDevHumid(void);
void CryogenDrive_SetDriveInfo(uint8_t ensta,uint8_t mode,uint8_t temp);
#endif
