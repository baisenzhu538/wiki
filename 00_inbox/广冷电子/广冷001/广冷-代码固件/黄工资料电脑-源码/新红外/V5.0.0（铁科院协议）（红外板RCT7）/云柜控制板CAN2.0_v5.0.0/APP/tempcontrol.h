#ifndef __TEMPCONTROL_H
#define __TEMPCONTROL_H
#include "stm32f10x.h"
#include "cryogen_drive.h"

#define CRYOGEN_COLDMODE       0
#define CRYOGEN_HOTMODE        1

typedef struct
{
 CryogenSetTypeDef CryogenSet[3];
}CryogenConfigTypeDef;


typedef struct
{
	CryogenSetTypeDef CryogenSet;
	CryogenStateTypeDef CryogenState;
}CryogenControlTypeDef;

typedef struct
{
 uint8_t contain;
 uint8_t en;
 uint8_t mod;
 uint8_t temp;
}CryogenCmdTypeDef;

typedef	struct
{
	uint8_t	contain_no;
	int8_t	T1;
	int8_t	T2;
	int8_t	forst_temp;
	uint8_t	forst_time_1minPer;
	uint8_t	corygen_max_time_1minPer;
	uint8_t	reciver[2];
}CryogenCmd2TypeDef;

typedef struct
{
 uint8_t contain;
 uint8_t sta;
 uint8_t err;
 uint8_t receve;
}CryogenCmdResportTypeDef;

void TempControl_CmdSet(uint8_t cmd,CryogenCmdTypeDef *pCmd);
uint8_t TempControl_GetTemp(uint8_t contain);
uint8_t TempControl_GetHumid(uint8_t contain);
void TempControl_Init(void);
#endif
