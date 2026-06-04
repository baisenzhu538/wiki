#ifndef __OTA_H
#define __OTA_H
#include "http.h"
#include "iap.h"


#define FILE_TYPE "XYJ_V"			//YXG_V
#define OTA_VER   "V2.3.0"			//V3.6.1
#define PACK_SIZE 512     //请求数据包大小
#define OTA_MAX_REQUEST_NUM      128 //最大尝试请求次数
#define OTA_MAX_RESPONES_OUTTIME 10   //响应超时时间
#define OTA_REST_TIME            5


#define	OTA_UPDATA_START		0x0000
#define	OTA_UPDATA_RUN			0x0001
#define	OTA_UPDATA_FINSH		0x0002
#define	OTA_UPDATA_REBOOT		0x0003


typedef struct 
{
	char *host;
	char *url;
	char *ver;
  FirmwareInfoTypeDef FirmwareInfo;
}Ota_UpFirmWareInfoTypeDef;//固件信息

typedef struct
{
	int  fw_pack_size;    //请求固件包大小
	int ratio;
	int sta; 	 
	int err;
}Ota_UpFirmware_StaTypeDef;

typedef struct 
{
	char en;   //使能位
	char sta;  //状态位
	
	int  rest_time;
	int  request_endlen;	
	int  respones_outtime;//响应超时     
	int  runtime;         //运行时间
	int  request_num;   //响应时间
	char (*up_sta_callback)(void *);
	char (*up_request_callback)(char *,int);
	Http_GetResponTypeDef Http_GetRespon;
	Ota_UpFirmware_StaTypeDef up_sta;
	FirmwareBuffTypeDef  *pFirmwareBuff;
}Ota_UpTaskTypeDef;//升级运行任务

void otaTask(void);
char ota_CreateUpFirwareTask(Ota_UpFirmWareInfoTypeDef *p_UpFirmWareInfo
	                           ,char (*up_sta_callback)(void *)
								,char (*up_request_callback)(char *,int));
char Ota_Receive(char *data,int size);
#endif
