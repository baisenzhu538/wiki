#include "tempcontrol.h"
#include "sys_config.h"
CryogenControlTypeDef CryogenControl[3];
CryogenConfigTypeDef  CryogenConfig;


uint8_t TempControl_GetHumid(uint8_t contain)
{
	if(contain==0)
		return CryogenDrive_GetDevHumid();
	else
	 return CryogenControl[contain].CryogenState.current_humid;
}

uint8_t TempControl_GetTemp(uint8_t contain)
{
	if(contain==0)
		return CryogenDrive_GetDevTemp();
	else
		return CryogenControl[contain].CryogenState.current_temp;
}

//温度控制初始化
void TempControl_Init(void)
{
	SysConfig_GetTempControlConfig(&CryogenConfig);//获取配置信息
	
	CryogenDrive_SetDriveInfo(CryogenConfig.CryogenSet[0].enable_bit.cryogen_en,
	                          CryogenConfig.CryogenSet[0].mode,
	                          CryogenConfig.CryogenSet[0].temp);
	
	SysMem_copy((u8*)&CryogenControl[0].CryogenSet, (u8*)&CryogenConfig.CryogenSet[0], sizeof(CryogenSetTypeDef));
	SysMem_copy((u8*)&CryogenControl[1].CryogenSet, (u8*)&CryogenConfig.CryogenSet[1], sizeof(CryogenSetTypeDef));
	SysMem_copy((u8*)&CryogenControl[2].CryogenSet, (u8*)&CryogenConfig.CryogenSet[2], sizeof(CryogenSetTypeDef));

}

void TempControl_CmdSet(uint8_t cmd,CryogenCmdTypeDef *pCmd)
{
	CryogenCmdResportTypeDef CryogenCmdResport;
	if(pCmd->contain==0x00)
	 CryogenDrive_SetDriveInfo(pCmd->en,
	                           pCmd->mod,
	                           pCmd->temp);
	
	CryogenConfig.CryogenSet[pCmd->contain].enable_bit.cryogen_en=pCmd->en;
	CryogenConfig.CryogenSet[pCmd->contain].mode                 =pCmd->mod;
	CryogenConfig.CryogenSet[pCmd->contain].temp                 =pCmd->temp;
	SysConfig_UpTempControl(&CryogenConfig);
	
	CryogenControl[pCmd->contain].CryogenSet.enable_bit.cryogen_en=pCmd->en;
	CryogenControl[pCmd->contain].CryogenSet.mode                 =pCmd->mod;
	CryogenControl[pCmd->contain].CryogenSet.temp                 =pCmd->temp;
	
	CryogenCmdResport.contain=pCmd->contain;
	CryogenCmdResport.err    =0x00;
	CryogenCmdResport.sta    =0x01;
	CryogenCmdResport.receve =0x00;
//	DeviceProtocol_TxResportMsg(cmd,(uint8_t*)&CryogenCmdResport,sizeof(CryogenCmdResportTypeDef));
}



