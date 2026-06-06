#ifndef __MOTOR_DRIVE_
#define __MOTOR_DRIVE_
#include "motor_gpio.h"
#include "digital_signal.h"

#define MOTOR_MAXNUM 13
#define MOTOR_SIGNCONNECT 10
#define MOTOR_BLOCKTIME   150 //2.5s堵转超时
#define D_MOTOR_OUTTIME   800 //电机在初始位置8s运行超时
#define E_MOTOR_OUTTIME   600 //电机不在初始位置，超时为6s  

#define MOTOR_COILMODE     0x00
#define MOTOR_CONVEYERMODE 0x01
typedef struct
{
	uint32_t linkstate;                    //由低到高分别对应0-31号电机连接状态,1为连接，0为未连接
}MotorDrive_LinkStateTypedef;

typedef struct
{
	uint32_t positionstate;                //由低到高分别对应0-31号电机位置状态
	uint32_t risingstate;                  //由低到高分别对应0-31号电机位置弹起状态
	uint32_t fallingstate;                 //由低到高分别对应0-31号电机位置下压状态
}MotorDrive_PositionStateTypedef;

typedef struct
{
	uint32_t runeneable;              //电机使能位，自动清0
	uint32_t runstate;                //由高到底分别对应电机运行状态
	uint32_t blockstate;              //电机堵转状态位
	uint32_t outtimestate;            //电机超时状态位
	uint32_t errstate;
  uint16_t runtime[MOTOR_MAXNUM];  //电机运行时间
	uint16_t maxtime[MOTOR_MAXNUM];
}MotorDrive_DriveTypedef;


typedef struct
{
	uint8_t  motormaxnum;
	uint8_t  motormod;
  MotorDrive_DriveTypedef            drive;
	MotorDrive_PositionStateTypedef    position;
	MotorDrive_LinkStateTypedef        link;
}MotorDrive_MotorManageTypedef;







void MotorDrive_Init(void);
void MotorDrive_SignalCollect(void);
void MotorDrive_Task(void);

uint8_t MotorDrive_GetLinkStateBit(uint8_t motor_ch);
uint8_t MotorDrive_SetBit(uint8_t motor_ch);
uint8_t MotorDrive_GetRunStateBit(uint8_t motor_ch);
uint8_t MotorDrive_GeOTStateBit(uint8_t motor_ch);
uint8_t MotorDrive_GetBlockStateBit(uint8_t motor_ch);
uint8_t MotorDrive_GetErrStateBit(uint8_t motor_ch);
uint8_t MotorDrive_GetPositionStateBit(uint8_t motor_ch);
uint8_t MotorDrive_GetEnStateBit(uint8_t motor_ch);
void MotorDrive_RestPosit(void);
uint8_t MotorDrive_ReadMotorMode(void);
void MotorDrive_ResetBit(uint8_t motor_ch);
uint32_t MotorDrive_GetErrState(void);
#endif
