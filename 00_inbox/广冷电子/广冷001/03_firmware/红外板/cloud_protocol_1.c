#include "cloud_protocol.h"
#include "stdio.h"
#include "sell_app.h"
#include "cryogen_drive.h"
#include "sys_config.h"
//#include "lock.h"
#include "at_7s4.h"
#include "wireless_module_init.h"
#include "wireless_hardware_interface.h"
//#include "mqtt_manage.h"
#include "string.h"
#include "time_stamp.h"
#include "NetworkModule.h"
#include "at_ebyte.h"
//#include "relay.h"
//#include "battery.h"
#include "mqtt_recive.h"
#include "mqtt_connect.h"
#include "mqtt_ota_if.h"
//#include "power.h"

CloudProtol_ManageTypeDef CloudProtol_Manage;
CloudProtocol_SnManageTypeDef CloudProtocol_SnManage={0,0,0,{0}};

static uint16_t counttime=0;
static uint8_t  sendnum=0;
char *sMsg=NULL;

const char HexChar[16]={"0123456789ABCDEF"};
uint8_t DeviceId[]="13701201901000001300000000000000";		//机器 ID

//设备信息
//供应商代号
//设备型号
//设备ID
//货道总行数
//货道总列数
CloudProtocol_DeviceInfo_TypeDef	CloudProtocolDeviceInfo={8,16,{DEVICE_INFO_BRAND},{DEVICE_INFO_MODEL},{"GL2021398668183306870485"},{"00000000"}};

//设备状态
//门状态
//系统状态
//商店状态
CloudProtocol_DeviceState_TypeDef	CloudProtocolDeviceState={0,0,0};

//出货任务状态
//出货码
//订单ID
CloudProtocol_SellState_TypeDef		CloudProtocolSellState;

//货道检测
//检测状态
//货道连接状态
//操作行号
//操作列号
CargoCheckManage_TypeDef			CargoCheckManage;

CloudProtocol_SellStateTable_TypeDef	CloudProtocolSellStateTable={NULL,NULL,0};

u8 CloudProtocol_Get_DeviceState_StoreState(void)
{
	return CloudProtocolDeviceState.store_state;
}

u8 CloudProtocol_Get_DeviceState_DoorState(void)
{
	return CloudProtocolDeviceState.door_state;
}

int CloudProtocol_Get_DeviceState(void)
{
	return CloudProtocolDeviceState.system_state;
}
void CloudProtocol_Set_DeviceState(int state)
{
//	if(CloudProtocolDeviceState.system_state)
//	{		
//		if(CloudProtocolDeviceState.system_state != state)
//		{
//			CloudProtocolDeviceState.system_state = SYSTEM_STATE_SCREEN_OR_SENSOR_ERR;			
//		}		
//	}
//	else
//	{
		CloudProtocolDeviceState.system_state = state;
//	}
	DgusApp_Set_ShowSystemErrorInfo(CloudProtocolDeviceState.system_state);
}

u8 CloudProtocol_SellStateBlock_Remove(void)
{
	CloudProtocol_SellStateBlock_TypeDef * pBlock;
	
	if(CloudProtocolSellStateTable.head == NULL)
		return NULL;
	pBlock = CloudProtocolSellStateTable.head;
	if(CloudProtocolSellStateTable.head->next)
		CloudProtocolSellStateTable.head->next->proir = NULL;
	CloudProtocolSellStateTable.head = CloudProtocolSellStateTable.head->next;
	CloudProtocolSellStateTable.table_len--;
	SysMem_free(pBlock);
	return 0xFF;
}


u8 CloudProtocol_SellStateBlock_Add(int	code,char * orderId,int row,int list)
{	
	CloudProtocol_SellStateBlock_TypeDef * pBlock;
	if(CloudProtocolSellStateTable.table_len == CLOUD_PROTOCOL_SELL_STATE_TABLE_MAX_LEN)
	{
		CloudProtocol_SellStateBlock_Remove();
	}
	
	pBlock = (CloudProtocol_SellStateBlock_TypeDef*)SysMem_malloc(sizeof(CloudProtocol_SellStateBlock_TypeDef));
	if(pBlock == NULL)
		return 0x00;
	
	SysMem_copy((u8*)&pBlock->SellStateUint.orderId, orderId, strlen(orderId));
	pBlock->SellStateUint.code = code;
	pBlock->SellStateUint.row = row;
	pBlock->SellStateUint.list = list;
	pBlock->SellStateUint.state = 1;	//出货中
	
	if(CloudProtocolSellStateTable.head == NULL)
	{
		pBlock->next = NULL;
		pBlock->proir = NULL;
		CloudProtocolSellStateTable.head = pBlock;
		CloudProtocolSellStateTable.tail = pBlock;
		CloudProtocolSellStateTable.table_len++;
	}
	else
	{
		pBlock->next = NULL;				
		CloudProtocolSellStateTable.tail->next = pBlock;
		pBlock->proir = CloudProtocolSellStateTable.tail;
		CloudProtocolSellStateTable.tail = pBlock;
		CloudProtocolSellStateTable.table_len++;
	}
	return 0xFF;
}

int CloudProtocol_SellStateBlock_Get2(int code)
{
	CloudProtocol_SellStateBlock_TypeDef * pBlock;
	
	pBlock = CloudProtocolSellStateTable.head;
	
	while(pBlock)
	{
		if(pBlock->SellStateUint.code == code)
		{
			return pBlock->SellStateUint.state;
		}
		pBlock = pBlock->next;
	}
	
	return 303;		
}

CloudProtocol_SellStateBlock_TypeDef * CloudProtocol_SellStateBlock_Get(int code)
{
	CloudProtocol_SellStateBlock_TypeDef * pBlock;
	
	pBlock = CloudProtocolSellStateTable.head;
	
	while(pBlock)
	{
		if(pBlock->SellStateUint.code == code)
		{
			return pBlock;
		}
		pBlock = pBlock->next;
	}
	
	return NULL;	
}


void CloudProtocol_SellStateBlock_Fix(int code,int state)
{
	CloudProtocol_SellStateBlock_TypeDef * pBlock;
	
	pBlock = CloudProtocolSellStateTable.head;
	
	while(pBlock)
	{
		if(pBlock->SellStateUint.code == code)
		{
			pBlock->SellStateUint.state = state;
		}
		pBlock = pBlock->next;
	}
}


u8 * CloudProtocol_Read_DeviceId(void)
{
	return (u8*)CloudProtocolDeviceInfo.deviceId;
}

void CloudProtol_Enable(void)
{
	CloudProtol_Manage.enable = 0x01;
}
void CloudProtol_Disable(void)
{
	CloudProtol_Manage.enable = 0x00;
}

void CloudProtol_Manage_Struct_Clear(void)
{
	CloudProtol_Manage.HeartMsgSn = 0x00;
	CloudProtol_Manage.HeartTime = CLOUD_HEART_TIME;
	CloudProtol_Manage.HeartTimeOut = 0;
	CloudProtol_Manage.link = 0x00;
	CloudProtol_Manage.RegMsgSn = 0x00;
	CloudProtol_Manage.RegMsgTime = CLOUD_REGMSG_TIME;
	CloudProtol_Manage.RegOuttime = 0;
	CloudProtol_Manage.DeviceStatusTime = 59000;
	CloudProtol_Manage.DeviceStatusTimeOut = 0;
	CloudProtol_Manage.enable = 0x01;
}


/*************************************************************
函数：CloudProtocol_CompareRxSn
功能：查找是否存在相同Sn码
参数：msg 消息指针
返回：MSG_QUEUE_FULL 队列满
      MSG_QUEUE_ADD  队列加入成功
*************************************************************/
uint8_t CloudProtocol_CompareRxSn(uint64_t sn)
{
	uint8_t i;
	for(i=0;i<CLOUD_SN_TABLE_NUM;i++)
	{
		if(CloudProtocol_SnManage.rx_sn_table[i]==sn)
			return 0x00;//存在相同sn码
	}
	CloudProtocol_SnManage.rx_sn_table[CloudProtocol_SnManage.rx_sn_tabletail]=sn;
	CloudProtocol_SnManage.rx_sn_tabletail++;
	if(CloudProtocol_SnManage.rx_sn_tabletail==CLOUD_SN_TABLE_NUM)
		CloudProtocol_SnManage.rx_sn_tabletail=0;
	return 0xFF;
}

uint8_t CloudProtocol_ReadGoodsSta(void)
{
	return CloudProtol_Manage.GoodsSta;
}
uint8_t CloudProtocol_ReadLink(void)
{
	return CloudProtol_Manage.link;
}
void CloudProtocol_AddMsg(char *s)
{
	counttime=0;
	sendnum=0;
	if(sMsg)
		SysMem_free(sMsg);
	sMsg=s;
}

static u8 RebootMqttStatus = 0;
void CloudProtocol_SetRebootMqtt(void)
{
	RebootMqttStatus = 1;
}

void CloudProtocol_ClearRebootMqtt(void)
{
	RebootMqttStatus = 0;
}

u8 CloudProtocol_ReadRebootMqttFlag(void)
{
	return RebootMqttStatus;
}



void CloudProtocol_HexNumbleToString_LittleEnd(uint8_t *pString,uint8_t *pNumble,uint8_t ByteNum)
{
	uint8_t i;
	for(i=0;i<ByteNum;i++)
	{
		pString[i*2]    =HexChar[(pNumble[ByteNum-i-1]>>4)&0x0F];
		pString[(i*2)+1]=HexChar[pNumble[ByteNum-i-1]&0x0F];
	}
}

void CloudProtocol_HexNumbleToString_BigEnd(uint8_t *pString,uint8_t *pNumble,uint8_t ByteNum)
{
	uint8_t i;
	for(i=0;i<ByteNum;i++)
	{
		pString[i*2]    =HexChar[(pNumble[i]>>4)&0x0F];
		pString[(i*2)+1]=HexChar[pNumble[i]&0x0F];
	}
}

void CloudProtocol_HexNumbleToString(uint8_t *pString,uint8_t *pNumble,uint8_t ByteNum)
{
	uint8_t i;
	for(i=0;i<ByteNum;i++)
	{
		pString[i*2]    =HexChar[(pNumble[ByteNum-i-1]>>4)&0x0F];
		pString[(i*2)+1]=HexChar[pNumble[ByteNum-i-1]&0x0F];
	}
}

uint8_t CloudProtocol_CharToHexNumble(uint8_t string)
{
	uint8_t res;
	if(string>('0'-1)&&string<('9'+1))
	{
		res=string-0x30;
		return res;
	}
	if(string>('a'-1)&&string<('f'+1))
	{
		res=string-0x57;
		return res;
	}
	if(string>('A'-1)&&string<('F'+1))
	{
		res=string-0x37;
		return res;
	}
	return -1;
}

void CloudProtocol_StringToHexNumble(uint8_t* pString,uint8_t *pNumble,uint8_t ByteNum)
{
	uint8_t i,hex;
	for(i=0;i<ByteNum;i++)
	{
		hex=0x00;
		hex=CloudProtocol_CharToHexNumble(pString[(i*2)+1]);
		hex|=(CloudProtocol_CharToHexNumble(pString[i*2])<<4);
		pNumble[ByteNum-1-i]=hex;
	}
}

void CloudProtocol_StringToHexNumbleBig(uint8_t* pString,uint8_t *pNumble,uint8_t ByteNum)
{
	uint8_t i,hex;
	for(i=0;i<ByteNum;i++)
	{
		hex=0x00;
		hex=CloudProtocol_CharToHexNumble(pString[(i*2)+1]);
		hex|=(CloudProtocol_CharToHexNumble(pString[i*2])<<4);
		pNumble[i]=hex;
	}
}



/********************************************************************************************************************/




void CloudProtocol_SensorScan_TimeTask(void)
{
	if(!ElcLock_ReadLockState())
		CloudProtocolDeviceState.door_state = 1;
	else
		CloudProtocolDeviceState.door_state = 0;
}

void CloudProtocol_DeviceInfoInit(void)
{
	SysConfig_Get_DeviceId(CloudProtocolDeviceInfo.deviceId);
	SysConfig_Get_QrCode(CloudProtocolDeviceInfo.QrCodeUrl);
	if(SysConfig_Get_QrCodeSize())
		DgusApp_Set_QRCode((u8*)CloudProtocolDeviceInfo.QrCodeUrl,strlen(CloudProtocolDeviceInfo.QrCodeUrl));
//	DgusApp_Set_StoreSta(CloudProtocolDeviceState.store_state);	
	DgusApp_Set_DeviceId((u8*)CloudProtocolDeviceInfo.deviceId);
	CloudProtocolDeviceState.store_state = SysConfig_Get_StoreState();
	
}

void CloudProtocol_Init(void)
{
	cJSON_Hooks  hooks; 
	WirelessModule_Init();//模块初始化
	hooks.malloc_fn=SysMem_malloc;		//将系统内存管理函数稼接到cJSON
	hooks.free_fn  =SysMem_free;
	cJSON_InitHooks(&hooks);			//cJSON内存管理相关初始化

	CloudProtocol_DeviceInfoInit();

}

//1000
//上报心跳信息
void CloudProtocol_Up_HeartInfo(void)
{
	cJSON *root;
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;		//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();		//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1000);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//货道总行数
	cJSON_AddNumberToObject(root,"row",CloudProtocolDeviceInfo.row_num);
	
	//货道总列数
	cJSON_AddNumberToObject(root,"column",CloudProtocolDeviceInfo.list_num);
	
	//心跳
	cJSON_AddNumberToObject(root,"macno",1);
	
	s= cJSON_PrintUnformatted(root);
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	
	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}


	pMsg->qos = 0;
	pMsg->dup = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	SysMem_free(pMsg_Data);
	SysMem_free(pMsg);
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象
}

//1001
//上报系统信息
void CloudProtocol_Up_SystemInfo(void)
{	
	cJSON *root;
	cJSON *data;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	data =  cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1001);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//货道总行数
	cJSON_AddNumberToObject(root,"row",CloudProtocolDeviceInfo.row_num);
	
	//货道总列数
	cJSON_AddNumberToObject(root,"column",CloudProtocolDeviceInfo.list_num);
	
	//系统数据，系统的工作状态
	cJSON_AddItemToObject(root,"data",data);	
	
	//门状态 1：门已打开，0：门关闭
	cJSON_AddNumberToObject(data,"door state",CloudProtocolDeviceState.door_state);
	//系统状态 0：系统正常，1XX:系统故障
	cJSON_AddNumberToObject(data,"system state",CloudProtocolDeviceState.system_state);
	//商店状态，1：开店，0：关店
	cJSON_AddNumberToObject(data,"store state",CloudProtocolDeviceState.store_state);
	
	s= cJSON_PrintUnformatted(root);
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	
	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}


	pMsg->qos = 0;
	pMsg->dup = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	SysMem_free(pMsg_Data);
	SysMem_free(pMsg);
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象
}

//待机模式下才进行
//定时20S，交替上报心跳数据或系统数据。
void CloudProtocol_UpHeartOrSystem_TimeTask(void)
{	
	static u16 time10ms_cnt = 18*100;
	static u8	UpSelect=0;
	
	if(time10ms_cnt < 2000)
	{
		time10ms_cnt++;
	}
	else	
	{
		time10ms_cnt = 0;
		
		if(!UpSelect)
		{
			CloudProtocol_Up_HeartInfo();
		}
		else
		{
			CloudProtocol_Up_SystemInfo();
		}
		UpSelect = !UpSelect;
	}
}

//1002
//读数据请求

//1003
//读数据请求响应
void CloudProtocol_ReadSystemRespont(char * ts)
{
	cJSON *root;
	cJSON *data;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	data =  cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1003);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//货道总行数
	cJSON_AddNumberToObject(root,"row",CloudProtocolDeviceInfo.row_num);
	
	//货道总列数
	cJSON_AddNumberToObject(root,"column",CloudProtocolDeviceInfo.list_num);
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	
	
	//系统数据，系统的工作状态
	cJSON_AddItemToObject(root,"data",data);	
	
	//门状态 1：门已打开，0：门关闭
	cJSON_AddNumberToObject(data,"door state",CloudProtocolDeviceState.door_state);
	//系统状态 0：系统正常，1XX:系统故障
	cJSON_AddNumberToObject(data,"system state",CloudProtocolDeviceState.system_state);
	//商店状态，1：开店，0：关店
	cJSON_AddNumberToObject(data,"store state",CloudProtocolDeviceState.store_state);
	
	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象
}

//读数据请求解析
void CloudProtocol_ReadSystemparsing(cJSON * root)
{
	cJSON * pPara = NULL;
	char * ts = NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
	
	CloudProtocol_ReadSystemRespont(ts);
}


//1004
//开关店请求
//1005
//开关店请求响应
void CloudProtocol_SwitchStoreRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1005);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//标志位，1 为接收成功，其他值为失败
	cJSON_AddNumberToObject(root,"flag",1);
	
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"msg",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象
}

//开关店请求解析
void CloudProtocol_SwitchStoreParsing(cJSON * root)
{
	cJSON * pPara = NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//解析开关店字段
	pPara=cJSON_GetObjectItem(root,"store state");
		
	if(pPara == NULL)
		return ;
	
	//执行开关店动作
	//得出开关店动作结果	
	CloudProtocolDeviceState.store_state = pPara->valueint;
	
	if(CloudProtocolDeviceState.store_state)
	{
		SysConfig_Up_StoreState(1);
		DgusApp_Set_GotoPage(3);
	}
	else
	{
		SysConfig_Up_StoreState(0);
		
		if(SysConfig_Get_QrCodeSize())
		{
			DgusApp_Set_GotoPage(5);
		}
		else
		{
			DgusApp_Set_GotoPage(4);
		}
	}
	
	//根据开关店状态更新显示文字信息
//	DgusApp_Set_StoreSta(CloudProtocolDeviceState.store_state);	
		
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;

	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
	
	CloudProtocol_SwitchStoreRespont(ts);
}

//1006
//出货请求
//1007
//出货请求响应
void CloudProtocol_SellRespont(char * ts,int code,char * orderId)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1007);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//出货码
	cJSON_AddNumberToObject(root,"code",code);
	
	//订单ID
	cJSON_AddStringToObject(root,"orderId",(char*)orderId);
		
	//标志位，1 为接收成功，其他值为失败
	cJSON_AddNumberToObject(root,"flag",1);
	
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"msg",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象	
}

void CloudProtocol_SellParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	static cJSON * pVar = NULL;
	SellIdTypeDef SellId;	
	int	code;
	char * orderId=NULL;
	char * ts=NULL;
	int row;
	int column;
	HistoryUintTypeDef	Uint;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//解析出货码
	pPara=cJSON_GetObjectItem(root,"code");
		
	if(pPara == NULL)
		return ;
	
	code = pPara->valueint;
	
	//去重
	if(SellHistory_CheckLogCodeForCode(code))
		return ;
	
	
	//解析订单ID
	pPara=cJSON_GetObjectItem(root,"orderId");
		
	if(pPara == NULL)
		return ;
		
	orderId = pPara->valuestring;
//	SysMem_copy(orderId,pPara->valuestring,strlen(pPara->valuestring));
	
	
	//提取参数
	pVar =cJSON_GetObjectItem(root,"var");
		
	if(pVar == NULL)
		return ;
	
	//解析货道行号
	pPara =cJSON_GetObjectItem(pVar,"row");
		
	if(pPara == NULL)
		return ;
	
	row = pPara->valueint;
	
	//解析货道列号
	pPara =cJSON_GetObjectItem(pVar,"column");
		
	if(pPara == NULL)
		return ;
	
	column = pPara->valueint;
	
	//执行出货动作
	//新增出货状态任务	
//	CloudProtocol_SellStateBlock_Add(code, orderId, row, column);
			
	SellApp_SetSellTask2(code,(row-1),(column-1),CloudProtocol_SellStateBlock_Fix);
	DgusApp_Set_ShowSellLog(orderId);
	DgusApp_Set_GotoPage(6);
	
	Uint.code = code;
	Uint.row = row;
	Uint.list = column;
	Uint.state = 1;
	TimeStamp_Get_TimeStamp(&Uint.time); 	
	SellHistory_AddLog(&Uint);	
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));		
		
	CloudProtocol_SellRespont(ts,code,orderId);
}

//1008
//开门请求
//1009
//开门请求响应
void CloudProtocol_OpenGateResponrt(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1009);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//标志位，1 为接收成功，其他值为失败
	cJSON_AddNumberToObject(root,"flag",1);
	
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"msg",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象		
}

//开门请求解析
void CloudProtocol_OpenGateParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	int	door_state;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;

	//解析开关门字段
	pPara=cJSON_GetObjectItem(root,"doorstate");
		
	if(pPara == NULL)
		return ;
	
	//执行开关门操作
	//得出开关门结果
	
	door_state = pPara->valueint;
	
	if(door_state)
	{
		ElcLock_SetEnable();
	}
	else
	{
		ElcLock_ResetEnable();
	}

	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));
	
	CloudProtocol_OpenGateResponrt(ts);
}

//1110
//出货状态请求
//1111
//出货状态请求响应
void CloudProtocol_SellStateRespont(char * ts, int code, char * orderId)
{
	cJSON *root;
	int	shipment_state;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1111);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//出货码
	cJSON_AddNumberToObject(root,"code",code);
	
	//订单ID
	cJSON_AddStringToObject(root,"orderId",(char*)orderId);
	
	//根据订单ID查出货任务出货状态
	shipment_state = SellHistory_GetLogStateForCode(code);
	
	//出货状态：1：出货中，2：出货成功，3XX：出货失败
	cJSON_AddNumberToObject(root,"shipment state",shipment_state);	
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象			
}

//出货状态查询解析
void CloudProtocol_SellStateParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	int	code;
	char * orderId=NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//解析出货码
	pPara=cJSON_GetObjectItem(root,"code");
		
	if(pPara == NULL)
		return ;
	
	code = pPara->valueint;
	
	//解析订单ID
	pPara=cJSON_GetObjectItem(root,"orderId");
		
	if(pPara == NULL)
		return ;
			
	orderId = pPara->valuestring;
//	SysMem_copy(orderId,pPara->valuestring,strlen(pPara->valuestring));
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
		
	CloudProtocol_SellStateRespont(ts,code,orderId);
}

//1114
//二维码更新请求
//1115
//二维码更新请求响应
void CloudProtocol_QRCodeUpdateRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1115);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//标志位
	cJSON_AddNumberToObject(root,"flag",1);
		
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"message",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象				
}

//二维码更新请求解析
void CloudProtocol_QRCodeUpdateParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	char * ts = NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//解析二维码 url
	pPara=cJSON_GetObjectItem(root,"url");
		
	if(pPara == NULL)
		return ;
	
	//保存url至FLASH
	//显示最新url
	//得出操作结果
	memset(CloudProtocolDeviceInfo.QrCodeUrl,0,sizeof(CloudProtocolDeviceInfo.QrCodeUrl));
	SysMem_copy(CloudProtocolDeviceInfo.QrCodeUrl,pPara->valuestring,strlen(pPara->valuestring));
	SysConfig_Up_QrCode(CloudProtocolDeviceInfo.QrCodeUrl,strlen(pPara->valuestring));
	
	if(CloudProtocolDeviceState.store_state)
	{
		DgusApp_Set_GotoPage(3);
		DgusApp_Set_QRCode((u8*)CloudProtocolDeviceInfo.QrCodeUrl,strlen(pPara->valuestring));		
	}
	else
	{
		DgusApp_Set_GotoPage(5);
		DgusApp_Set_QRCode((u8*)CloudProtocolDeviceInfo.QrCodeUrl,strlen(pPara->valuestring));
	}
	
	
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
		
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));
		
	CloudProtocol_QRCodeUpdateRespont(ts);
}





void CloudProtocol_UpDate_CargoAllCheckResult(void)
{
	u8 i;
	
	for(i=0;i<8;i++)
	{		
		CargoCheckManage.cargo_state[i] = SellMotor_GetLinkState(0,i);
	}
	CargoCheckManage.check_state = 2;
}

//1116
//货道检测请求
//1117
//货道检测请求响应
void CloudProtocol_CargoCheckRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1117);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//标志位
	cJSON_AddNumberToObject(root,"flag",1);
		
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"message",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象			
}

void CloudProtocol_CargoCheckParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	static cJSON * pVar = NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//提取VAR对象
	pVar=cJSON_GetObjectItem(root,"var");
		
	if(pVar == NULL)
		return ;
	
	//提取货道行号
	pPara=cJSON_GetObjectItem(pVar,"row");
		
	if(pPara == NULL)
		return ;
	
	CargoCheckManage.sigle_row = pPara->valueint;
	
	//提取货道列号
	pPara=cJSON_GetObjectItem(pVar,"column");
		
	if(pPara == NULL)
		return ;
	
	CargoCheckManage.sigle_list = pPara->valueint;
	
	//执行检测动作
	//得出检测结果
	CloudProtocol_UpDate_CargoAllCheckResult();
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));
	
	CloudProtocol_CargoCheckRespont(ts);
}

//1118
//货道检测结果查询
//1119
//货道检测结果查询响应
void CloudProtocol_CargoCheckResultRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。
	int	asile_state = 0;
	
	if(CargoCheckManage.cargo_state[(CargoCheckManage.sigle_row-1)] & (0x0001<<(CargoCheckManage.sigle_list-1)))
		asile_state = 2;
	else
		asile_state = 3;

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1119);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//标志位
	cJSON_AddNumberToObject(root,"asile state",asile_state);
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象	
}

void CloudProtocol_CargoCheckResultParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	static cJSON * pVar = NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
	
	CloudProtocol_CargoCheckResultRespont(ts);
}


//1120
//货道全检请求
//1121
//货道全检响应
void CloudProtocol_CargoAllCheckRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1121);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
		
	//标志位
	cJSON_AddNumberToObject(root,"flag",1);
	
	//错误信息，当下发失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"message",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;	
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象	
}

void CloudProtocol_CargoAllCheckParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	static cJSON * pVar = NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//更新货道全检结果
	CloudProtocol_UpDate_CargoAllCheckResult();
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));		
	
	CloudProtocol_CargoAllCheckRespont(ts);
}



//1122
//货道全检结果查询
//1123
//货道全检结果响应

void CloudProtocol_CargoAllCheckResultRespont(char * ts)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。	
	u8	cargo_state[7]={'0','x','0','0','0','0',0};

	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1123);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);	
	
	//检测状态，0空闲，1检测中，2检测完成。
	cJSON_AddNumberToObject(root,"check state", CargoCheckManage.check_state);

	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[0],2);

	//此处表示第1行，第1、3列电机故障
	cJSON_AddStringToObject(root,"row 1",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[1],2);	
	
	//此处表示第2行，第1、2列电机故障
	cJSON_AddStringToObject(root,"row 2",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[2],2);		
	
	//此处表示第3行，第1列电机故障
	cJSON_AddStringToObject(root,"row 3",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[3],2);			
	
	//此处表示第4行，第1、3、5、9、11列电机故障
	cJSON_AddStringToObject(root,"row 4",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[4],2);				
	
	//此处表示第5行，第1、2、3、5、9列电机故障
	cJSON_AddStringToObject(root,"row 5",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[5],2);			

	cJSON_AddStringToObject(root,"row 6",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[6],2);			
		
	cJSON_AddStringToObject(root,"row 7",(char*)cargo_state);	
	
	CloudProtocol_HexNumbleToString_BigEnd(&cargo_state[2],(u8*)&CargoCheckManage.cargo_state[7],2);				

	cJSON_AddStringToObject(root,"row 8",(char*)cargo_state);	

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象		
}

void CloudProtocol_CargoAllCheckResultParsing(cJSON * root)
{
	static cJSON * pPara = NULL;
	static cJSON * pVar = NULL;
	char * ts=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//执行货道全检动作
	//得出货道全检结果
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
		
	CloudProtocol_CargoAllCheckResultRespont(ts);
}

void CouldProtocol_GetHistoryRespont(char * ts,char * date)
{
	cJSON *root;
	
	char *s;
	static MQTT_Msg_TypeDef * pMsg = NULL;	//因为该地址需要传递给下级函数，不能定义在栈区。
	static u8 * pMsg_Data = NULL;			//因为该地址需要传递给下级函数，不能定义在栈区。
	char	* Buffer = NULL;
	Time_TypeDef	Time;
	int	logNum;
	
	root = cJSON_CreateObject();			//創建空的cJSON對象
	
	//指令号
	cJSON_AddNumberToObject(root,"cmdId", 1127);
	
	//供应商（？此处供应商代号需要与铁科院商议确定，是否为铁科院统一分配）
	cJSON_AddStringToObject(root,"brand",(char*)CloudProtocolDeviceInfo.brand);
	
	//设备型号（？此处设备型号需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"model",(char*)CloudProtocolDeviceInfo.model);
	
	//设备ID（？此处理设备ID需要与铁科院、广冷商议确定，是否已有相应规则）
	cJSON_AddStringToObject(root,"deviceId",(char*)CloudProtocolDeviceInfo.deviceId);
	
	//标志位，1 为接收成功，其他值为失败
	cJSON_AddNumberToObject(root,"flag",1);
	
	//错误信息，当写入失败时，会提供错误信息。
	cJSON_AddStringToObject(root,"msg",(char*)"success");
	
	//时间戳（？此处时间戳的生成规则是怎么样的）
	cJSON_AddStringToObject(root,"ts",(char*)ts);
	
	//从FLASH中提取日志
	
	Time.year = (date[0]-0x30)*1000
				+(date[1]-0x30)*100
				+(date[2]-0x30)*10
				+(date[3]-0x30);
	Time.month = (date[4]-0x30)*10
				+(date[5]-0x30);
	Time.day = (date[6]-0x30)*10
				+(date[7]-0x30);		
	Time.hour = 0;
	Time.min = 0;
	Time.sec = 0;
	
	logNum = SellHistory_CreatLogStringForTimeRange1(&Time,(u8*)Buffer);
		
	Buffer = (char*)SysMem_malloc(logNum*33);
	if(Buffer)
		logNum = SellHistory_CreatLogStringForTimeRange1(&Time,(u8*)Buffer);
	
	//日志字符串
	cJSON_AddStringToObject(root,"log",(char*)Buffer);
	
	//日志总数量
	cJSON_AddNumberToObject(root,"logNum",logNum);

	s= cJSON_PrintUnformatted(root);	//将root解释为字符串
		
	if(s == NULL)
	{
		cJSON_Delete(root);
		return ;
	}
	if(*s != '{')
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}

	pMsg_Data = (u8*)SysMem_malloc(strlen(s));
	if(pMsg_Data == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		return ;
	}
	pMsg = SysMem_malloc(sizeof(MQTT_Msg_TypeDef));
	if(pMsg == NULL)
	{
		cJSON_Delete(root);
		SysMem_free(s);
		SysMem_free(pMsg_Data);
		return ;
	}
	
	
	pMsg->qos = 1;
	pMsg->dup = 0;
	pMsg->SendSn = 0;
	pMsg->packid = MQTT_Get_PackId();
	pMsg->retain = 0;
	pMsg->TopicSize = strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC);
	SysMem_copy(pMsg->Topic, CLOUD_PROTOCOL_PUBLISH_TOPIC, strlen(CLOUD_PROTOCOL_PUBLISH_TOPIC));
	if(pMsg->Topic == NULL)
	{
		while(0);
	}
	pMsg->DataSize = strlen(s);
	pMsg->Data = pMsg_Data;
	SysMem_copy(pMsg->Data,s,strlen(s));
	
	MQTT_Send_Publish(pMsg);
	
	if(pMsg->qos != 1)
	{
		SysMem_free(pMsg_Data);
		SysMem_free(pMsg);
	}
	else
	{
		pMsg->dup = 1;
		if(MQTT_Msg_Add_Queue(pMsg) == 0xFF)
		{
			SysMem_free(pMsg_Data);
			SysMem_free(pMsg);
		}
	}
	SysMem_free(s);		//釋放s的內存
	cJSON_Delete(root);	//刪除cJSON對象
}

void CouldProtocol_GetHistoryParsing(cJSON * root)
{
	cJSON * pPara = NULL;
	char * ts=NULL;
	char * date=NULL;
	
	//比较供应商代号
	pPara=cJSON_GetObjectItem(root,"brand");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.brand))
		return ;
	
	//比较设备型号
	pPara=cJSON_GetObjectItem(root,"model");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.model))
		return ;
	
	//比较设备ID
	pPara=cJSON_GetObjectItem(root,"deviceId");
		
	if(pPara == NULL)
		return ;
	
	if(strcmp(pPara->valuestring,CloudProtocolDeviceInfo.deviceId))
		return ;
	
	//解析日志时间
	pPara=cJSON_GetObjectItem(root,"date");
		
	if(pPara == NULL)
		return ;
	
	date = pPara->valuestring;
//	SysMem_copy(date,pPara->valuestring,strlen(pPara->valuestring));		
	
	//截取时间戳
	pPara=cJSON_GetObjectItem(root,"ts");
		
	if(pPara == NULL)
		return ;
	
	ts = pPara->valuestring;
//	SysMem_copy(ts,pPara->valuestring,strlen(pPara->valuestring));	
	
	CouldProtocol_GetHistoryRespont(ts,date);	
}


/********************************************************************************************************************/




void Cloud_UartRx_Server(void)
{
	static uint16_t	size = 0;
	static u8 * js_string;	
	int res = 0;
	u8 mode = 0;
	
	if(WierlessHarware_GetDataLen())
	{
		size=WierlessHarware_GetDataLen();
		js_string=SysMem_malloc(WierlessHarware_GetDataLen());
		if(js_string==NULL)
			return;
		WierlessHarware_GetData((uint8_t *)js_string);
		
		if(WirelessModule_ReciveParsing(js_string,size)==NULL)
		{
			SysMem_free(js_string);
		}
		else//为AT指令，不进行后续解析
		{
		 SysMem_free(js_string);
		 return;
		}
	}	
}

void CloudProtocol_TimeTask(void)
{
	WirelessModule_RunTask();//无线模块定时调用
	if(WirelessModule_ReadInitSta() == NULL)	//检查初始化是否完成
		return;
	if(MQTT_Get_Start_Status() == 0x00)			//检查MQTT初始化是否完成
	{
		CloudProtol_Manage.link = 0x00;
		return;	
	}
	
	CloudProtocol_UpHeartOrSystem_TimeTask();
	CloudProtocol_SensorScan_TimeTask();
}

//任务
static uint16_t	size = 0;
void CloudProtocol_Task(void)
{
	static uint8_t TaskSta=0x00;
	static uint16_t cmdId;
	
	uint8_t laynum = 0;
	uint8_t motonum = 0;	
	uint8_t containnum = 0;
	uint64_t Sn = 0;
	static uint8_t * mqtt_js_string = NULL;
	u8 error = 0;			
	uint8_t contain_no;
	
	static cJSON *root = NULL;
	static cJSON *js_time = NULL;
	static cJSON *pCmd = NULL;
	static cJSON *js_data = NULL;
	static cJSON *pSn;
	
	if(WirelessModule_ReadRunStaus()==NULL)//检查初始化是否完成
		return;
	
	Cloud_UartRx_Server();	
	
	if(MQTT_Get_Start_Status() == NULL)
		return;
	
	switch(TaskSta)		//TaskSta 状态机
	{
		case 0x00:
				{
					mqtt_js_string = (u8 *)Mqtt_Get_Json();
					
					if(mqtt_js_string != NULL)
						TaskSta = 0x01;
				}	
				break;
		case 0x01:	//解释指令
				{	 
					root = cJSON_Parse((const char *)mqtt_js_string);	//字符串js_string中的数据解析为cJSON格式
					if(root!=NULL)	//解析成功
					{
						pCmd=cJSON_GetObjectItem(root,"cmdId");	//获取cJSON对象root中的"int_Cmd"项
						if(pCmd == NULL)
						{
							TaskSta=0x03;
							return;
						}
						cmdId = pCmd->valueint;
						TaskSta=0x02;	//下次跳转至状态0x02
					}
					else	//解析失败
						TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
		case 0x02:	//分配功能
		{
			switch(cmdId)
			{				
				case 1002://读数据请求
				{
					CloudProtocol_ReadSystemparsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1004://开关店请求
				{
					CloudProtocol_SwitchStoreParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1006://出货请求
				{
					CloudProtocol_SellParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;				
				case 1008://开门请求
				{
					CloudProtocol_OpenGateParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1110://出货状态查询请求
				{
					CloudProtocol_SellStateParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1114://二维码更新请求
				{
					CloudProtocol_QRCodeUpdateParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1116://货道检测请求
				{
					CloudProtocol_CargoCheckParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1118://货道检测结果查询
				{
					CloudProtocol_CargoCheckResultParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1120://货道全检请求
				{
					CloudProtocol_CargoAllCheckParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1122://货道全检结果查询
				{					
					CloudProtocol_CargoAllCheckResultParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				case 1126://获取日志
				{
					CouldProtocol_GetHistoryParsing(root);
					
					TaskSta=0x03;		//下次跳转至状态0x03
				}
				break;
				default://未知指令
				{										
					TaskSta=0x03;
				}
				break;
			}
		}
		break;
		
		case 0x03:	
		{
			if(root)	
				cJSON_Delete(root);	//释放root占用内存
			SysMem_free(mqtt_js_string);
			TaskSta=0x00;	//下次跳转到状态0
		}
		break;
	}
  
}


