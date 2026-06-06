#ifndef __CLOUD_PROTOCOL_H
#define __CLOUD_PROTOCOL_H

#include "cloud_protocol.h"
#include "sys_malloc.h"
#include "usart.h"
#include "cJSON.h"
//#include "lock.h"
#include "ota.h"
#include "elc_lock.h"
#include "dgus_app.h"

#define CLOUD_REGMSG_TIME 		20*100		//10秒发送1个注册包
#define	CLOUD_REGMSG_OUTTIME	100*100		//90秒注册超时
#define CLOUD_HEART_TIME  		2000		//10分钟发送1个心跳包
#define CLOUD_HEART_OUTTIME  	6000		//90秒心跳超时

#define CLOUD_VER  "V4.0.4"

#define CLOUD_SN_TABLE_NUM  	32			//

#define	CLOUD_GET_PUBLISH_TOPIC_TIME	1000

#define	CLOUD_DEVICE_STATUS_TIME	10*60*100	//10分钟上传1次设备状态

#define	CLOUD_PROTOCOL_SELL_STATE_TABLE_MAX_LEN		32

//发布主题
#define	CLOUD_PROTOCOL_PUBLISH_TOPIC	"terminal_msg"

//供应商代号
#define	DEVICE_INFO_BRAND		"GLHX"
//设备类型
#define	DEVICE_INFO_MODEL		"GLHX-0511-0"
//设备ID
#define	DEVICE_INFO_ID			"123456789"
//货道总行数
#define	DEVICE_INFO_ROW_NUM		8
//货道总列数
#define	DEVICE_INFO_LIST_NUM	16

//系统故障代码
//正常
#define	SYSTEM_STATE_NORMAL						0
//驱动板通讯故障
#define	SYSTEM_STATE_DRIVE_ERR					101
//掉货检测故障
#define	SYSTEM_STATE_SENSOR_ERR					102
//驱动板通讯故障/掉货检测故障
#define	SYSTEM_STATE_DRIVE_OR_SENSOR_ERR		103
//显示屏通讯故障
#define	SYSTEM_STATE_SCREEN_ERR					104
//显示屏通讯故障/驱动板通讯故障
#define	SYSTEM_STATE_SCREEN_OR_DRIVE_ERR		105
//显示屏通讯故障/掉货检测故障
#define	SYSTEM_STATE_SCREEN_OR_SENSOR_ERR		106
//显示屏通讯故障/掉货检测故障/驱动板通讯故障
#define	SYSTEM_STATE_SCREEN_OR_SENSOR_DRIVE_ERR	107

//出货故障代码
//出货中
#define	SELL_STATE_START		1
//出货成功
#define	SELL_STATE_FINSH		2
//卡货故障
#define	SELL_STATE_BLOCK_ERR	301
//电机故障
#define	SELL_STATE_MOTOR_ERR	302
//其他
#define	SELL_STATE_OTHER		303

extern char Connect_Topic[30];

typedef	struct
{
	char	orderId[12];
	int		code;
	int		row;
	int		list;
	int		state;
}CloudProtocol_SellStateUint_TypeDef;

typedef struct _CloudProtocol_SellStateBlock_TypeDef
{
	struct _CloudProtocol_SellStateBlock_TypeDef *proir;
	struct _CloudProtocol_SellStateBlock_TypeDef *next;
	CloudProtocol_SellStateUint_TypeDef SellStateUint;
}CloudProtocol_SellStateBlock_TypeDef;


typedef struct 
{
	CloudProtocol_SellStateBlock_TypeDef *head;
	CloudProtocol_SellStateBlock_TypeDef *tail;
	uint32_t table_len;                         //任务表长度
}CloudProtocol_SellStateTable_TypeDef;


typedef struct
{
	uint16_t tx_sn;          //发送报文sn滚码
	uint8_t  rx_sn_tablehead;//接收sn码记录表表头
	uint8_t  rx_sn_tabletail;//接收sn码记录表表尾
	uint64_t rx_sn_table[CLOUD_SN_TABLE_NUM];
}CloudProtocol_SnManageTypeDef;

typedef struct
{
	uint64_t devid;
	uint64_t Sn;
	uint32_t  checksum;
	uint32_t  MotorLink[16];
	uint8_t  cmd;
	uint8_t  devtype;
	uint8_t  laynum;
	uint8_t  motornum;
	uint8_t  devsta;
	
}CloudProtol_RegisMsgTypeDef;


typedef struct
{
	uint64_t Sn;         //流水码记录
	uint64_t RegMsgSn;   //注册流水码记录
	uint64_t HeartMsgSn;
	uint64_t GoodsMsgSn;
	uint64_t UpHeartSn;
	uint64_t DownHeartSn;
	uint64_t GetPublicTopicSn;
	uint64_t ConfigNetworkModuleSn;
	uint64_t DeviceRebootSn;
	uint64_t OtaUpFirmWareSn;
	uint64_t OpenLockSn;
	uint64_t UpDeviceStatusSn;
	uint64_t GetDeviceStatusSn;
	uint64_t GetGPSLocationSn;
	uint64_t GetPowerStatusSn;
	uint64_t GetBatteryInfoSn;
	
	uint8_t  link;
	uint8_t  GoodsSta;
	uint16_t RegMsgTime;   //注册报文发送时间
	uint16_t HeartTime;    //心跳发送时间
	uint16_t HeartTimeOut; //心跳超时
	uint16_t ReqTopicTime;
	uint16_t ReqTopicOuttime;
	uint8_t	 ReqTopicSta;	
	uint16_t DeviceStatusTime;
	uint16_t DeviceStatusTimeOut;
	
	uint16_t HeartReq;
	uint16_t HeartResp;
	uint16_t RegOuttime;
	uint8_t enable;

}CloudProtol_ManageTypeDef;


typedef	struct
{
	u32 Error1;
}
SellAckError_TypeDef;


typedef	struct
{
	int		row_num;		//货道总行数
	int		list_num;		//货道总列数	
	char	brand[16];		//供应商代号
	char	model[16];		//设备型号
	char	deviceId[32];	//设备ID
	char 	QrCodeUrl[256];	//二维码URL	
}CloudProtocol_DeviceInfo_TypeDef;

typedef	struct
{
	int	door_state;		//门状态：		1 门已打开，0 门关闭
	int	system_state;	//系统状态：	0 系统正常，1XX 系统故障
	int	store_state;	//商店状态：	1 开店，0 关店
}CloudProtocol_DeviceState_TypeDef;

typedef	struct
{
	int	code;
	u8	orderId[16];
}CloudProtocol_SellState_TypeDef;

typedef	struct
{
	u8	check_state;		//检测状态：0 空闲，1 检测中，2 检测完成。
	u16	cargo_state[8];		//货道连接状态
	u8	sigle_row;
	u8	sigle_list;
}CargoCheckManage_TypeDef;	//货道全检管理

extern uint8_t DeviceId[];
extern CloudProtol_ManageTypeDef CloudProtol_Manage;
extern CloudProtocol_DeviceInfo_TypeDef	CloudProtocolDeviceInfo;

char Mqtt_Will_Message_Pack_Creat(char * message);
uint8_t CloudProtocol_ReadGoodsSta(void);
//void CloudProtocol_ResponseLockStaMessage(LockTaskStaTypeDef *pLockTaskSta, u8 ContainNum);
uint8_t CloudProtocol_ReadLink(void);
void CloudProtocol_Init(void);
void CloudProtocol_TimeTask(void);
void CloudProtocol_Task(void);
void CloudProtocol_ResetMod(void);
void CloudProtol_Manage_Struct_Clear(void);

void CloudProtol_Disable(void);
void CloudProtol_Enable(void);
u8 CloudProtocol_ReadRebootMqttFlag(void);
void CloudProtocol_ClearRebootMqtt(void);
u8 * CloudProtocol_Read_DeviceId(void);

int CloudProtocol_Get_DeviceState(void);
extern void CloudProtocol_Set_DeviceState(int state);

u8 CloudProtocol_Get_DeviceState_StoreState(void);
u8 CloudProtocol_Get_DeviceState_DoorState(void);

#endif
