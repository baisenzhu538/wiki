#include "NetworkModule.h"
#include "at_ebyte.h"
#include "cloud_protocol.h"
#include "at_7s4.h"
#include "at_air720.h"
#include "at_ec20.h"
#include "mqtt_connect.h"


NetworkModulePara_TypeDef	NetworkModulePara = {{"zd.jumiai.cn","1883","TCP"},0x00};


void NetworkModule_InitTask(void)
{
//	static u8 mode = 0;
//	static u8 ModuleTypeNum = 0;
//	static u16 wait_time = 0;
//	u8 ret = 0;
//	
//	
//	if(NetworkModulePara.en == 0x01)
//	{
//		switch(mode)
//		{
//			case 0://延迟10秒
//			{
//				wait_time++;
//				if(wait_time > 1000)
//				{
//					wait_time = 0;
//					mode = 1;
//				}
//			}
//			break;
//			case 1://关闭其他应用，独占UART4
//			{
//				ModuleTypeNum = WirelessModule_ReadTypeNum();
//				CloudProtol_Disable();
//				MQTT_Start_Disable();
//				At7S4_Task_Disable();
//				AtEbyte_Task_Disable();
//				mode = 2;
//			}
//			break;
//			case 2://配置
//			{
//				switch(ModuleTypeNum)
//				{
//					case 0://合宙
//					{
//						ret = AtAir720_ModuleConfig(&NetworkModulePara.NetworkPara);
//						if(ret == 0xFF)
//						{
//							mode = 3;							
//						}
//						if(ret == 0xEE)
//						{
//							mode = 3;
//						}
//					}
//					break;
//					case 2://有人
//					{
//						ret = At7S4_ModuleConfig(&NetworkModulePara.NetworkPara);
//						if(ret == 0xFF)
//						{
//							mode = 3;							
//						}
//						if(ret == 0xEE)
//						{
//							mode = 3;
//						}
//					}
//					break;
//					case 1://亿佰特
//					{
//						ret = AtEbyte_ModuleConfig(&NetworkModulePara.NetworkPara);
//						if(ret == 0xFF)
//						{
//							mode = 3;							
//						}
//						if(ret == 0xEE)
//						{
//							mode = 3;
//						}
//					}
//					break;
//					case 3://移远
//					{
//						ret = EC20_ModuleConfig(&NetworkModulePara.NetworkPara);
//						if(ret == 0xFF)
//						{
//							mode = 3;
//						}
//						if(ret == 0xEE)
//						{
//							mode = 3;
//						}
//					
//					}
//					default:break;
//				}
//			}
//			break;
//			case 3://重启
//			{
//				mode = 0;
//				NetworkModulePara.en = 0x00;
//				At7S4_Task_Enable();
//				AtEbyte_Task_Enable();
//				MQTT_Start_Enable();
//				CloudProtol_Enable();
//				Iap_SysReset();//系统复位
//			}
//			break;
//			default:break;
//		}
//	
//	
//	}
}
void NetworkModule_Set(NetworkModulePara_TypeDef * pNetworkModulePara)
{
//	pNetworkModulePara->en = 0x01;
//	SysMem_copy(&NetworkModulePara, pNetworkModulePara, sizeof(NetworkModulePara_TypeDef));
}

