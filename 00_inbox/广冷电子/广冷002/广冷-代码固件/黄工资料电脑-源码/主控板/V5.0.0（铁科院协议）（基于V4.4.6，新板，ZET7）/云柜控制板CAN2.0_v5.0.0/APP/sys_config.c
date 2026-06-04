#include "sys_config.h"
__IO SysConfigParameterTypeDef *pSysConfigBuff;
SysConfigParameterTypeDef SysConfig={
	                                   /*出厂设备信息*/
	                                   {0,0,0,0,{0},{0}},
	                                   /*制冷默认出厂参数*/
	                                   {
																			{
																		   {{1,0,0,0,0,0},CRYOGEN_COLDMODE,4,0},//0号机柜制冷参数
																		   {{1,0,0,0,0,0},CRYOGEN_COLDMODE,4,0},//1号机柜制冷参数
																		   {{1,0,0,0,0,0},CRYOGEN_COLDMODE,4,0} //2号机柜制冷参数
																		  }
																		 },
																		 /*出货升降平台控制默认出厂参数*/
																		 {
																			 {
																				 {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},//0号机柜升降平台出货口位置
																				 {
																					 0x00000907,//0
																					 0x00002713,//1
																					 0x00004434,//2
																					 0x00006140,//3
																					 0x00008964,//4
																					 0x0000A809,//5
																					 0x0000C302,//6
																					 0x0000E32B,//7
																					 0x0001156E,//8
																					 0x00012C1A,//9
																					 0x000152E1,//A
																					 0x0000D2A9,//B
																					 0x0000D2A9,//C
																					 0x0000D2A9,//D
																					 0x0000D2A9,//E
																					 0x0000D2A9 //F
																				 },                                  //1号升降平台出货口位置
																				 {
																					 0x000152E1,//0
																					 0x00013D61,//1
																					 0x000114D1,//2
																					 0x0000779B,//3
																					 0x0000F32D,//4
																					 0x0000779B,//5
																					 0x0000D90A,//6
																					 0x0000779B,//7
																					 0x0000BDB3,//8
																					 0x0000779B,//9
																					 0x0000A087,//A
																					 0x0000779B,//B
																					 0x00006A86,//C
																					 0x0000779B,//D
																					 0x00003E3E,//E
																					 0x0000181E,//F
																				 }
																			 },                                     //2号升降平台出货口位置
																			 {0,0x0000D6F5,0x00007EB3}//机柜出货口升降平台位置
																		 },
																		 //货架标准样式
																		 {
																			 0x00010,
																			 0x00008,
																			 {
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF,
																			 0xFFFF
																			 }
																		 },
																		 {
																			{"0000000000000000000000000000000"},
																			{"0000000000000000000000000000000"}
																		},
																		 0,
																		 24,
																		 0,
																		 {"GL2022000000000000000003"},//GL2021398668183306870485
																		 {"00000000"},																		 
																		/*校验和*/	
																		 0x00231291
                                    };//系统配置参数

__IO AuxConfigParameterTypeDef * pAuxConfigBuff;
AuxConfigParameterTypeDef	AuxConfig = {0xA0A0,0x00,
											{"39.96.10.250","11883","TCP"},
											{"crgtVending","123456789"},
											{"123456",6,"123456",6},
											{"00000000000000000000000000000000"},
											0xB087D979};
									
//AuxConfigParameterTypeDef	AuxConfig = {0xA0A0,0x00,
//											{"39.96.10.250","11883","TCP"},
//											{"crgtVending","123456789"},
//											{"123456",6,"123456",6},
//											{"00000000000000000000000000000000"},
//											0xB087D979};
															
	
											
//获取货道样式																		
uint32_t SysConfig_GetShelfType(uint8_t shel_num)
{
	return SysConfig.cargo_type.cargo_sta[shel_num];
}
//获取货道行数
uint8_t SysConfig_GetHeightNum(void)
{
	return SysConfig.cargo_type.cargo_y;
}
//获取货道列数
uint8_t SysConfig_GetWidthNum(void)
{
	return SysConfig.cargo_type.cargo_x;
}


uint32_t SysConfig_CheckSum(uint8_t *data,uint32_t size)
{
	uint32_t i=0,check=0;
	uint32_t *buf;
	buf=(uint32_t*)data;
	for(i=0;i<(size/4);i++)
	{
		check+=(*buf);
		buf++;
	}
	if(size%4)
	{
		check+=(*buf)&(0xFFFFFFFF>>((4-(size%4))*8));
	}
	return check;
}

uint8_t SysConfig_CheckZero(uint8_t *data,uint32_t size)//校验数据段是否都为0
{
	uint32_t i;
	for(i=0;i<size;i++)
	{
		if((__IO uint8_t)data[i])
			return 0x00;
	}
	return 0xFF;
}
void SysConfig_Init(void)
{
	uint32_t checksum;
	pSysConfigBuff=(SysConfigParameterTypeDef*)DATABASE_FLASHADDR;
	checksum=SysConfig_CheckSum((uint8_t*)pSysConfigBuff,sizeof(SysConfigParameterTypeDef)-4);
	if(pSysConfigBuff->checksum==checksum)
	{
		if(checksum==0)//检验是否内存未存数据
		{
			if(SysConfig_CheckZero((uint8_t*)pSysConfigBuff,sizeof(SysConfigParameterTypeDef)-4)==0xFF)//无有效数据
			{
				checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
				SysConfig.checksum=checksum;
				STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
			}
			else//数据合法
			{
				STMFLASH_Read(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
			}
		}
		else//合法数据
		{
			STMFLASH_Read(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
		}
	}
	else//不存在合法数据
	{
		checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
		SysConfig.checksum=checksum;
		STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
	}
}
																		
void SysConfig_UpTempControl(CryogenConfigTypeDef *pCryogenConfig)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.tempcontrol,pCryogenConfig,sizeof(CryogenConfigTypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
}

void SysConfig_GetTempControlConfig(CryogenConfigTypeDef *pCryogenConfig)
{
	SysMem_copy(pCryogenConfig,&SysConfig.tempcontrol,sizeof(CryogenConfigTypeDef));
}

void SysConfig_UpSellConfig(Sell_ConfigTypeDef *pSellConfig)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.Sell_Config,pSellConfig,sizeof(Sell_ConfigTypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
}
																		
void SysConfig_GetSellConfig(Sell_ConfigTypeDef *pSellConfig)
{
	SysMem_copy(pSellConfig,&SysConfig.Sell_Config,sizeof(Sell_ConfigTypeDef));
}																		
																		
void SysConfig_UpDevInfoConfig(DeviceInfoTypeDef *pDevInfoConfig)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.dev_info,pDevInfoConfig,sizeof(DeviceInfoTypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
}
																		
void SysConfig_GetDevInfoConfig(DeviceInfoTypeDef *pDevInfoConfig)
{
	SysMem_copy(pDevInfoConfig,&SysConfig.dev_info,sizeof(DeviceInfoTypeDef));
}	

void SysConfig_UpPublishTopicConfig(Mqtt_PublishTopic * pPublishTopic)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.publish_topic,pPublishTopic,sizeof(Mqtt_PublishTopic));
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
}

void SysConfig_GetPublishTopicConfig(Mqtt_PublishTopic * pPublishTopic)		
{
	SysMem_copy(pPublishTopic,&SysConfig.publish_topic,sizeof(Mqtt_PublishTopic));	//将设备信息从FLASH中拷贝并传出
}

void SysConfig_UP_DeviceId(char * deviceId,u8 size)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.deviceId,deviceId,size);
	SysConfig.deviceIdSize = size;
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));	
}

void SysConfig_Up_QrCode(char * url,u8 size)
{
	uint32_t checksum;
	SysMem_copy(&SysConfig.qrCodeUrl,url,size);
	SysConfig.qrCodeUrlSize = size;
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));
}

void SysConfig_Get_DeviceId(char * deviceId)
{	
	SysMem_copy(deviceId,&SysConfig.deviceId,SysConfig.deviceIdSize);
}

void SysConfig_Get_QrCode(char * url)
{
	SysMem_copy(url,&SysConfig.qrCodeUrl,SysConfig.qrCodeUrlSize);	
}

u8 SysConfig_Get_QrCodeSize(void)
{
	return SysConfig.qrCodeUrlSize;
}

void SysConfig_Up_StoreState(u8 store_state)
{
	uint32_t checksum;
	SysConfig.store_state = store_state;
	checksum=SysConfig_CheckSum((uint8_t*)&SysConfig,sizeof(SysConfigParameterTypeDef)-4);
	SysConfig.checksum=checksum;
	STMFLASH_Write(DATABASE_FLASHADDR,(uint16_t*)&SysConfig,(sizeof(SysConfigParameterTypeDef)/2)+(sizeof(SysConfigParameterTypeDef)%2));	
}

u8 SysConfig_Get_StoreState(void)
{
	return SysConfig.store_state;
}

void AuxConfig_Init(void)
{
	uint32_t checksum = 0;//0xB087D979
	pAuxConfigBuff=(AuxConfigParameterTypeDef*)AUX_DATABASE_FLASHADDR;
	checksum=SysConfig_CheckSum((uint8_t*)pAuxConfigBuff,sizeof(AuxConfigParameterTypeDef)-4);
	if(checksum == pAuxConfigBuff->checksum)
	{
		if(checksum==0)//检验是否内存未存数据
		{
			if(pAuxConfigBuff->protecf != 0xA0A0)
			{
				checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
				AuxConfig.checksum=checksum;
				STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));
			}
			else//数据合法
			{
				STMFLASH_Read(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));
			}
		}
		else
		{
			STMFLASH_Read(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));
		}
	}
	else
	{
		checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
		AuxConfig.checksum=checksum;
		STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));
	}
}

//获取网络参数
void AuxConfig_GetNetWorkPara(NetworkPara_TypeDef * pNetworkPara)
{
	SysMem_copy(pNetworkPara, &AuxConfig.NetworkPara, sizeof(NetworkPara_TypeDef));
}

//修改网络参数
void AuxConfig_UpNetWorkPara(NetworkPara_TypeDef * pNetworkPara)
{
	uint32_t checksum;
	SysMem_copy(&AuxConfig.NetworkPara,pNetworkPara,sizeof(NetworkPara_TypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
	AuxConfig.checksum=checksum;
	STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));
}

//获取WIFI热点信息
void AuxConfig_Get_WifiApPara(WifiApPara_TypeDef * pWifiApPara)
{
	SysMem_copy(pWifiApPara, &AuxConfig.WifiApPara, sizeof(WifiApPara_TypeDef));
}

//更新WIFI热点信息
void AuxConfig_Up_WifiApPara(WifiApPara_TypeDef * pWifiApPara)
{
	uint32_t checksum;
	SysMem_copy(&AuxConfig.WifiApPara,pWifiApPara,sizeof(WifiApPara_TypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
	AuxConfig.checksum=checksum;
	STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));		
}

//获取串口屏登录参数
void AuxConfig_Get_DgusLoginPara(DgusLoginPara_TypeDef * pDgusLoginPara)
{
	SysMem_copy(pDgusLoginPara, &AuxConfig.DgusLoginPara, sizeof(DgusLoginPara_TypeDef));
}

//更新串口屏登录参数
void AuxConfig_Up_DgusLoginPara(DgusLoginPara_TypeDef * pDgusLoginPara)
{
	uint32_t checksum;
	SysMem_copy(&AuxConfig.DgusLoginPara,pDgusLoginPara,sizeof(DgusLoginPara_TypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
	AuxConfig.checksum=checksum;
	STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));		
}

//获取设备ID
void AuxConfig_Get_DgusDeviceId(DgusAppDeviceId_TypeDef * pDgusAppDeviceId)
{
	SysMem_copy(pDgusAppDeviceId, &AuxConfig.DgusDeviceId, sizeof(DgusAppDeviceId_TypeDef));
}

//更新设备ID
void AuxConfig_Up_DgusDeviceId(DgusAppDeviceId_TypeDef * pDgusAppDeviceId)
{
	uint32_t checksum;
	SysMem_copy(&AuxConfig.DgusDeviceId,pDgusAppDeviceId,sizeof(DgusAppDeviceId_TypeDef));
	checksum=SysConfig_CheckSum((uint8_t*)&AuxConfig,sizeof(AuxConfigParameterTypeDef)-4);
	AuxConfig.checksum=checksum;
	STMFLASH_Write(AUX_DATABASE_FLASHADDR,(uint16_t*)&AuxConfig,(sizeof(AuxConfigParameterTypeDef)/2)+(sizeof(AuxConfigParameterTypeDef)%2));		
}

u16	History_Get_TableInit(void)
{
	u16 init=0;
	
	STMFLASH_Read(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*0,(uint16_t*)&init,1);
	
	return init;
}

u16	History_Get_TableLenth(void)
{
	u16 lenth=0;
	
	STMFLASH_Read(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*1,(uint16_t*)&lenth,1);
	
	return lenth;
}

u16	History_Get_TableHead(void)
{
	u16 head=0;
	
	STMFLASH_Read(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*2,(uint16_t*)&head,1);
	
	return head;
}

u16	History_Get_TableTail(void)
{
	u16 tail=0;
	
	STMFLASH_Read(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*3,(uint16_t*)&tail,1);
	
	return tail;
}

//根据出货码来检索
//根据出货时间来检索
//

//根据索引获取出货日志单元
void History_Get_TableUint(u16 index,HistoryUintTypeDef * pUint)
{			
	if(index<HISTORY_UINT_MAX_NUM)
		STMFLASH_Read(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*4+index*sizeof(HistoryUintTypeDef),(uint16_t*)pUint,(sizeof(HistoryUintTypeDef)/2+sizeof(HistoryUintTypeDef)%2));
}

//根据索引加入出货日志
void History_Add_TableUint(u16 index,HistoryUintTypeDef * pUint)
{
	if(index<HISTORY_UINT_MAX_NUM)	
		STMFLASH_Write(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*4+index*sizeof(HistoryUintTypeDef),(uint16_t*)pUint,(sizeof(HistoryUintTypeDef)/2+sizeof(HistoryUintTypeDef)%2));		
}

//置位日志初始化标示
void History_Set_TableInit(u16 init)
{
	STMFLASH_Write(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*0,(uint16_t*)&init,1);		
}

//设置日志表长度
void History_Set_TableLenth(u16 lenth)
{
	STMFLASH_Write(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*1,(uint16_t*)&lenth,1);		
	
}

//设置日志表头
void History_Set_TableHead(u16 head)
{
	STMFLASH_Write(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*2,(uint16_t*)&head,1);		
}

//设置日志表尾
void History_Set_TableTail(u16 tail)
{
	STMFLASH_Write(HISTORY_DATABASE_FLASHADDR+sizeof(u16)*3,(uint16_t*)&tail,1);		
}









