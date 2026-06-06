#ifndef	_NET_WORK_MODULE_H_
#define	_NET_WORK_MODULE_H_

#include "sys.h"

typedef	struct
{
	u8 IPaddress[64];
	u8 port[10];
	u8 mode[10];
}NetworkPara_TypeDef;

typedef	struct
{
	u8	ssid[16];
	u8	pwd[16];
}WifiApPara_TypeDef;

typedef	struct
{	
	NetworkPara_TypeDef	NetworkPara;
	u8 en;
}NetworkModulePara_TypeDef;

void NetworkModule_Set(NetworkModulePara_TypeDef * pNetworkModulePara);
void NetworkModule_Init(void);
void NetworkModule_InitTask(void);


#endif	/*_NET_WORK_MODULE_H_*/

