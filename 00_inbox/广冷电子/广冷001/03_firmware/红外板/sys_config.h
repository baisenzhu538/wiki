#ifndef __SYS_CONFIG_H
#define __SYS_CONFIG_H
#include "stm32f10x.h"
#include "tempcontrol.h"
#include "sell_app.h"
#include "stmflash.h"
#include "sys_malloc.h"
#include "NetworkModule.h"
#include "time_stamp.h"

#define  DATABASE_FLASHADDR 0x803D800
#define  DATABASE_FLASSIZE  5*1024

#define  AUX_DATABASE_FLASHADDR (0x803D800 + 5*1024)
#define  AUX_DATABASE_FLASSIZE  5*1024

#define		HISTORY_DATABASE_FLASHADDR	(0x8024800)
#define		HISTORY_DATABASE_FLASHSIZE	100*1024

#define		HISTORY_UINT_MAX_NUM	3600		//4000

//需要保存的信息
/*
1、设备ID
2、二维码url
*/

typedef	struct
{
	Time_TypeDef		time;
	int	code;
	int	row;
	int	list;
	int	state;
	u32	index;
}HistoryUintTypeDef;

typedef	struct
{
	u16	init;
	u16	lenth;
	u16	head;
	u16	tail;
	HistoryUintTypeDef	HistoryUint[HISTORY_UINT_MAX_NUM];	
}HistoryTypeDef;




typedef struct
{
	uint16_t cargo_x;
	uint16_t cargo_y;
	uint16_t cargo_sta[16];
}SysConfig_CargoType;


typedef struct
{
	char Device_Topic[64];
	char Server_Topic[64];
}Mqtt_PublishTopic;


typedef struct
{
	DeviceInfoTypeDef     	dev_info;
	CryogenConfigTypeDef  	tempcontrol;//温度控制参数
	Sell_ConfigTypeDef    	Sell_Config;//出货参数
	SysConfig_CargoType   	cargo_type; //貨道样式
	Mqtt_PublishTopic		publish_topic;	
	uint8_t	store_state;
	uint8_t	deviceIdSize;
	uint8_t	qrCodeUrlSize;
	char	deviceId[32];	
	char	qrCodeUrl[256];
	uint32_t checksum;                //校验和
}SysConfigParameterTypeDef;        //系统配置参数


typedef	struct
{
	u8	id[20];
	u8	id_size;
	u8	pwd[20];
	u8	pwd_size;
}DgusLoginPara_TypeDef;

typedef	struct
{
	u8 id[32];
}DgusAppDeviceId_TypeDef;	

typedef struct
{
	uint16_t protecf;
	uint16_t rtc_disable_write;
	NetworkPara_TypeDef	NetworkPara;
	WifiApPara_TypeDef	WifiApPara;
	DgusLoginPara_TypeDef	DgusLoginPara;
	DgusAppDeviceId_TypeDef	DgusDeviceId;
	uint32_t checksum;
}AuxConfigParameterTypeDef;

typedef struct
{
	uint8_t contain_no;
	uint8_t shelf_no;
	uint8_t sta;
	uint8_t err;
}SysConfigLiftStaTypeDef;

void SysConfig_UpDevInfoConfig(DeviceInfoTypeDef *pDevInfoConfig);
void SysConfig_GetDevInfoConfig(DeviceInfoTypeDef *pDevInfoConfig);
void SysConfig_UpSellConfig(Sell_ConfigTypeDef *pSellConfig);
void SysConfig_GetSellConfig(Sell_ConfigTypeDef *pSellConfig);
void SysConfig_GetTempControlConfig(CryogenConfigTypeDef *pCryogenConfig);
void SysConfig_UpTempControl(CryogenConfigTypeDef *pCryogenConfig);
void SysConfig_Init(void);
uint32_t SysConfig_GetShelfType(uint8_t shel_num);
uint8_t SysConfig_GetHeightNum(void);
uint8_t SysConfig_GetWidthNum(void);

void SysConfig_UpPublishTopicConfig(Mqtt_PublishTopic * pPublishTopic);
void SysConfig_GetPublishTopicConfig(Mqtt_PublishTopic * pPublishTopic);

void AuxConfig_UpRtcDisableWriteFlag(uint16_t flag);
uint16_t AuxConfig_GetRtcDisableWriteFlag(void);

void AuxConfig_Init(void);
void AuxConfig_GetNetWorkPara(NetworkPara_TypeDef * pNetworkPara);
void AuxConfig_UpNetWorkPara(NetworkPara_TypeDef * pNetworkPara);
void AuxConfig_Get_WifiApPara(WifiApPara_TypeDef * pWifiApPara);
void AuxConfig_Up_WifiApPara(WifiApPara_TypeDef * pWifiApPara);
void AuxConfig_Get_DgusLoginPara(DgusLoginPara_TypeDef * pDgusLoginPara);
void AuxConfig_Up_DgusLoginPara(DgusLoginPara_TypeDef * pDgusLoginPara);
void AuxConfig_Get_DgusDeviceId(DgusAppDeviceId_TypeDef * pDgusAppDeviceId);
void AuxConfig_Up_DgusDeviceId(DgusAppDeviceId_TypeDef * pDgusAppDeviceId);







void History_Set_TableTail(u16 tail);
void History_Set_TableHead(u16 head);
void History_Set_TableLenth(u16 lenth);
void History_Add_TableUint(u16 index,HistoryUintTypeDef * pUint);
void History_Get_TableUint(u16 index,HistoryUintTypeDef * pUint);
u16	History_Get_TableTail(void);
u16	History_Get_TableHead(void);
u16	History_Get_TableLenth(void);

void History_Init(void);

void SysConfig_UP_DeviceId(char * deviceId,u8 size);
void SysConfig_Up_QrCode(char * url,u8 size);
void SysConfig_Get_DeviceId(char * deviceId);
void SysConfig_Get_QrCode(char * url);
u16	History_Get_TableInit(void);
void History_Set_TableInit(u16 init);
u8 SysConfig_Get_QrCodeSize(void);



u8 SysConfig_Get_StoreState(void);
void SysConfig_Up_StoreState(u8 store_state);



#endif
