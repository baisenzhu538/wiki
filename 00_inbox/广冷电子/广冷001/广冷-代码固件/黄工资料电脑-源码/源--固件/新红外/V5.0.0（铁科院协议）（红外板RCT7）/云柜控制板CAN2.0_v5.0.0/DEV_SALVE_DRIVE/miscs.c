#include "miscs.h"

void Miscs_Init(void)
{
	MiscControl_Init();
}



AndroidApp_SetMiscs_RespontData_TypeDef	SetMiscsRespontData[4];

void AndroidApp_Set_Miscs(uint8_t cmd,void* pData,uint16_t size,uint64_t sn,void (*pFun)(uint8_t,void*,uint16_t,uint64_t))
{
	u8 	i;
	u8	num=0;
	
	AndroidApp_SetMiscs_ReciveData_TypeDef	* pSetMiscsReciveData;
	
	for(i=0;i<size/2;i++)
	{
		pSetMiscsReciveData=(AndroidApp_SetMiscs_ReciveData_TypeDef*)(((uint8_t*)pData)+(2*i));	
		
		if(pSetMiscsReciveData == NULL)
			return ;
				
		MiscControl_Set(pSetMiscsReciveData->device_no,pSetMiscsReciveData->set);
		
		SetMiscsRespontData[num].device_no = pSetMiscsReciveData->device_no;
		SetMiscsRespontData[num].state = 1;
		if(num<4)
			num++;
	}
		
	if(pFun)
		(*pFun)(cmd,
				SetMiscsRespontData,
				num*sizeof(AndroidApp_SetMiscs_RespontData_TypeDef),
				NULL);	
}

