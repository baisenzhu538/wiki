#ifndef __MOTOR_DRIVE_H
#define __MOTOR_DRIVE_H

#include "motor_gpio.h"
#include "digital_signal.h"

#define  MOTOR_MANAGE_MAXNUN 3

#define MOTOR_Y_MAX 8
#define MOTOR_X_MAX 16

#define MOTOR_BLOCKTIME   150  //1.5s堵转超时
#define D_MOTOR_OUTTIME   600  //电机在初始位置8s运行超时
#define E_MOTOR_OUTTIME   600  //电机不在初始位置，超时为6s  

#define MOTOR_COILMODE     0x00
#define MOTOR_CONVEYERMODE 0x01

#define MOTOR_SIGNAL_COLLECTTIME 5     //空闲信号采集周期50ms
#define MOTOR_STAR_DELAY         5     //启动延时50ms
#define MOTOR_STOP_DELAY         40     //电机停止延时


#define MOTOR_CHECKMODE_TIME     100   //检测货道模式延时

#define MOTOR_SIGLIFTER_TIME      100    //设置有效电平周期数，周期依采样时间而定
#define COIL_SIGLIFTER_TIME       600
#define CONVEYER_SIGLIFTER_TIME   100

#define MOTOR_MOTORCURRENT_MAX    (float)0.8
typedef struct
{
	uint32_t linkstate;                    //由低到高分别对应0-31号电机连接状态,1为连接，0为未连接
}MotorDrive_LinkStateTypedef;

typedef struct
{
	uint32_t positionstate;                //由低到高分别对应0-31号电机位置状态
	uint32_t risingstate;                  //由低到高分别对应0-31号电机位置弹起状态
	uint32_t fallingstate;                 //由低到高分别对应0-31号电机位置下压状态
	uint16_t hightleveltime[MOTOR_X_MAX];               //高电平采样时间
	uint16_t lowleveltime[MOTOR_X_MAX];                 //低电平采样时间
}MotorDrive_PositionStateTypedef;

typedef struct
{
	uint32_t blockstate;              //电机堵转状态位
	uint32_t outtimestate;            //电机超时状态位
}MotorDrive_ErrStateTypedef;

typedef struct
{
	uint8_t  motormod;                //电机运行模式，0为弹簧，1为履带
	uint8_t  errsta;                  //运行异常状态位，1为异常，0为正常
	uint8_t  runstate;                //电机运行状态位
	uint8_t  positerr;                //位置异常状态位，0正常，1异常
}MotorDrive_RunStateTypedef;

typedef struct
{
 uint8_t  runeneable;              //电机使能位，自动清0              
 uint8_t  motor_y;
 uint8_t  motor_x;
 uint8_t  outtime;
}MotorDrive_MotorSetTypeDef;

typedef struct
{
	uint8_t  motormaxnum;
	uint16_t triggertime;             //货道信号触发时间
	uint16_t maxtime;                 //最大运行时间
	uint16_t runtime;                 //电机运行时间
	uint16_t filtertime;              //出货信号滤波时间
	uint16_t blocktime;               //堵转计时
	float    motorcurrent;
	
	MotorDrive_RunStateTypedef         state;
	MotorDrive_MotorSetTypeDef         motorset;
	MotorDrive_LinkStateTypedef        link[MOTOR_Y_MAX];
  MotorDrive_ErrStateTypedef         err[MOTOR_Y_MAX];
	
	MotorDrive_PositionStateTypedef    position[MOTOR_Y_MAX];
}MotorDriveTypedef;


typedef struct
{
	MotorDrive_RunStateTypedef         state;
	MotorDrive_MotorSetTypeDef         motorset;
	MotorDrive_LinkStateTypedef        link[MOTOR_Y_MAX];
	MotorDrive_ErrStateTypedef         err[MOTOR_Y_MAX];
}MotorDrive_RegisterMapTypedef;

void MotorDrive_Init(void);
void MotorDrive_SignalCollect(void);
void MotorDrive_Task(void);
void MotorDrive_TimeTask(void);


uint8_t MotorDrive_SetBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
void MotorDrive_ResetBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint32_t MotorDrive_GetLinkState(uint8_t motor_y_ch);
uint8_t MotorDrive_GetLinkStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint32_t MotorDrive_GeOTState(uint8_t motor_y_ch);
uint8_t MotorDrive_GeOTStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t MotorDrive_GetBlockStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t MotorDrive_GetErrStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t MotorDrive_GetPositionStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t MotorDrive_GetErrStateBit(uint8_t motor_x_ch,uint8_t motor_y_ch);

uint8_t MotorDrive_GetRunState(void);
uint8_t MotorDrive_GetEnState(void);
void MotorDrive_RestPosit(void);
uint8_t MotorDrive_ReadMotorMode(void);
uint8_t MotorDrive_ReadPositErr(void);
uint8_t MotorDrive_GetRunErrState(void);
#endif
