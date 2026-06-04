#ifndef	_MISCS_H_
#define	_MISCS_H_

#include "misc_control.h"

typedef	struct
{
	u8	device_no;
	u8	set;
}AndroidApp_SetMiscs_ReciveData_TypeDef;

typedef	struct
{
	u8	device_no;
	u8	state;
}AndroidApp_SetMiscs_RespontData_TypeDef;

void Miscs_Init(void);
void AndroidApp_Set_Miscs(uint8_t cmd,void* pData,uint16_t size,uint64_t sn,void (*pFun)(uint8_t,void*,uint16_t,uint64_t));


#endif	/*_MISCS_H_*/

