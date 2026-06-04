#include "string.h"
#include "stdio.h"
#include "stdint.h"
#include "ota.h"
#include "sys_malloc.h"
#include "err_code.h"
#include "mqtt_ota_if.h"


Ota_UpFirmWareInfoTypeDef Ota_UpFirmWareInfo={NULL,NULL,NULL,NULL,{0}};
Ota_UpTaskTypeDef Ota_UpTask={NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL};

typedef struct
{
	char sta;
	int size;
	char *pData;
}Ota_ReceiveBuffTypeDef;

Ota_ReceiveBuffTypeDef Ota_ReceiveBuff;

char Ota_Receive(char *data,int size)
{
	if(Ota_ReceiveBuff.sta)
		return -1;
	Ota_ReceiveBuff.pData=SysMem_malloc(size);
	if(Ota_ReceiveBuff.pData==NULL)
	  return -1;
	SysMem_copy(Ota_ReceiveBuff.pData,data,size);
	Ota_ReceiveBuff.sta=1;
	return 1;
	
}

void* Ota_GetReceiveData(void)
{
	if(Ota_ReceiveBuff.sta==0)
	  return NULL;
	Ota_ReceiveBuff.sta=0;
	return Ota_ReceiveBuff.pData;
}

void ota_FreeData(void)
{
	SysMem_free(Ota_UpFirmWareInfo.host);
	SysMem_free(Ota_UpFirmWareInfo.url);
	SysMem_free(Ota_UpFirmWareInfo.ver);
	SysMem_free(Ota_UpTask.pFirmwareBuff);
}

char ota_CreateUpFirwareTask(Ota_UpFirmWareInfoTypeDef *p_UpFirmWareInfo
	                           ,char (*up_sta_callback)(void *)
														 ,char (*up_request_callback)(char *,int))
{
	if(Ota_UpTask.en||Ota_UpTask.sta)
		return 0;//升级中
	if(p_UpFirmWareInfo->host==NULL||p_UpFirmWareInfo->url==NULL||p_UpFirmWareInfo->ver==NULL||up_request_callback==NULL)
		return -1;//输入参数异常
	Ota_UpFirmWareInfo.host=SysMem_malloc(strlen(p_UpFirmWareInfo->host));
	Ota_UpFirmWareInfo.url=SysMem_malloc(strlen(p_UpFirmWareInfo->url));
	Ota_UpFirmWareInfo.ver=SysMem_malloc(strlen(p_UpFirmWareInfo->ver));
	
	Ota_UpTask.pFirmwareBuff=SysMem_malloc(sizeof(FirmwareBuffTypeDef));
	
  if(Ota_UpFirmWareInfo.ver==NULL||Ota_UpFirmWareInfo.url==NULL||Ota_UpFirmWareInfo.host==NULL||Ota_UpTask.pFirmwareBuff==NULL)
	{
		ota_FreeData();
		return -2;//未申请到足够内存空间
	}
	SysMem_copy(Ota_UpFirmWareInfo.host,p_UpFirmWareInfo->host,strlen(p_UpFirmWareInfo->host));
	SysMem_copy(Ota_UpFirmWareInfo.url,p_UpFirmWareInfo->url,strlen(p_UpFirmWareInfo->url));
	SysMem_copy(Ota_UpFirmWareInfo.ver,p_UpFirmWareInfo->ver,strlen(p_UpFirmWareInfo->ver));
	SysMem_copy(&Ota_UpFirmWareInfo.FirmwareInfo,&p_UpFirmWareInfo->FirmwareInfo,sizeof(FirmwareInfoTypeDef));
	
	Ota_UpTask.up_request_callback=up_request_callback;
	Ota_UpTask.up_sta_callback    =up_sta_callback;
	Ota_UpTask.en=0x01;
	return 1;
}



//1s运行一次
void otaTask(void)
{
	if(MQTT_Get_Start_Status() == 0)
		return ;
	if(Ota_UpTask.en==0&&Ota_UpTask.sta==0)
	 return;
	if(Ota_UpTask.en==0)
	{
		Ota_UpTask.sta=0;
	}
	else
	{
		switch(Ota_UpTask.sta)
		{
			case 0x00:
				if(strstr(Ota_UpFirmWareInfo.url,FILE_TYPE))//文件合法
				{
					if(strcmp(OTA_VER,Ota_UpFirmWareInfo.ver)!=0)//版本号不同
					{
						Ota_UpTask.sta=0x01;
						Ota_UpTask.up_sta.err = OTA_NORMAL;			//正常
						Ota_UpTask.up_sta.sta = OTA_UPDATA_START;	//升级开始
						if(Ota_UpTask.up_sta_callback)
							Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
					}
					else//相同版本号固件
					{
						ota_FreeData();
						Ota_UpTask.up_sta.err = OTA_VER_IDENTIACAL;	//固件版本相同
						Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;	//升级结束
						if(Ota_UpTask.up_sta_callback)
							Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
						Ota_UpTask.en=0;
						Ota_UpTask.sta = 0x05;	//重启机器
					}
				}
				else//文件不合法
				{
					ota_FreeData();
					Ota_UpTask.up_sta.err = OTA_DOC_ILLEGAL;	//文件不合法
					Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;	//升级结束
					if(Ota_UpTask.up_sta_callback)
						Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
					Ota_UpTask.en=0;
					Ota_UpTask.sta = 0x05;	//重启机器
				}
				break;
			case 0x01://初始化请求响应记录
				Iap_Rest_UpData();//复位固件升级模块
				Ota_UpTask.Http_GetRespon.Content_Length=0;
			  Ota_UpTask.Http_GetRespon.end_len=0;
			  Ota_UpTask.Http_GetRespon.max_len=0;
			  Ota_UpTask.Http_GetRespon.star_len=0;
			  Ota_UpTask.Http_GetRespon.sta_code=0;
		    Ota_UpTask.Http_GetRespon.data=(char*)Ota_UpTask.pFirmwareBuff->buf;
        Ota_UpTask.pFirmwareBuff->packet_num=0;
				Ota_UpTask.pFirmwareBuff->packet_size=0;
				Ota_UpTask.sta=0x02;
				break;
			case 0x02://清除响应数据
				Ota_UpTask.Http_GetRespon.Content_Length=0;
			  Ota_UpTask.Http_GetRespon.end_len=0;
			  Ota_UpTask.Http_GetRespon.max_len=0;
			  Ota_UpTask.Http_GetRespon.star_len=0;
			  Ota_UpTask.Http_GetRespon.sta_code=0;
			  Ota_UpTask.sta=0x03;
			  Ota_UpTask.request_num=0;
			  Ota_UpTask.respones_outtime=0;
			case 0x03://开始请求数据
				if(Ota_UpTask.request_num<OTA_MAX_REQUEST_NUM)
				{
					Ota_UpTask.request_num++;
				
						if(Ota_UpFirmWareInfo.FirmwareInfo.FW_Size-Ota_UpTask.up_sta.fw_pack_size<PACK_SIZE)
							Ota_UpTask.request_endlen=Ota_UpTask.up_sta.fw_pack_size
						                           +(Ota_UpFirmWareInfo.FirmwareInfo.FW_Size-Ota_UpTask.up_sta.fw_pack_size);
						else
							Ota_UpTask.request_endlen=Ota_UpTask.up_sta.fw_pack_size+PACK_SIZE;
							
						
						if(HTTP_Get_Request(Ota_UpFirmWareInfo.url,
														 Ota_UpFirmWareInfo.host,
														 Ota_UpTask.up_sta.fw_pack_size,
														 Ota_UpTask.request_endlen-1,
														 Ota_UpTask.up_request_callback)==-1)//内存不足
						{
							ota_FreeData();
							Ota_UpTask.up_sta.err = OTA_MEM_OVERFLOW;	//内存不足
							Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;		//升级结束
							if(Ota_UpTask.up_sta_callback)
								Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
							Ota_UpTask.en=0;
//							Ota_UpTask.sta=0x00;
							Ota_UpTask.sta = 0x05;	//重启机器
						}
						else
						{
							Ota_UpTask.sta=0x04;
							Ota_UpTask.respones_outtime=0;
						}
			  }
				else//请求失败，发送升级失败反馈
				{
					ota_FreeData();
					Ota_UpTask.up_sta.err = OTA_REQUEST_OUTTIME;	//请求失败
					Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;		//升级结束
					if(Ota_UpTask.up_sta_callback)
						Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
					Ota_UpTask.en=0;
//					Ota_UpTask.sta=0x00;
					Ota_UpTask.sta = 0x05;	//重启机器
				}
				break;
			case 0x04://等待数据响应
				if(Ota_UpTask.respones_outtime<OTA_MAX_RESPONES_OUTTIME)
				{
					char *pData,sta;
					Ota_UpTask.respones_outtime++;
					pData=Ota_GetReceiveData();
					if(pData)
					{
					  sta=HTTP_GET_ResponstParser(pData,&Ota_UpTask.Http_GetRespon);
						SysMem_free(pData);
						switch(sta)
						{
							case 1://获取数据成功
								if((Ota_UpTask.Http_GetRespon.max_len==Ota_UpFirmWareInfo.FirmwareInfo.FW_Size)
									&&Ota_UpTask.Http_GetRespon.end_len==Ota_UpTask.request_endlen
									&&Ota_UpTask.Http_GetRespon.star_len==Ota_UpTask.up_sta.fw_pack_size
									&&Ota_UpFirmWareInfo.FirmwareInfo.FW_Size>=(Ota_UpTask.up_sta.fw_pack_size+Ota_UpTask.Http_GetRespon.Content_Length))
								{
									Ota_UpTask.up_sta.fw_pack_size+=Ota_UpTask.Http_GetRespon.Content_Length;
									Ota_UpTask.pFirmwareBuff->packet_size=Ota_UpTask.Http_GetRespon.Content_Length;
									if(Iap_UpDataApp(Ota_UpTask.pFirmwareBuff)==0)//数据保存失败
									{
										ota_FreeData();
										Ota_UpTask.up_sta.err = OTA_SAVE_FAILURE;	//数据保存失败
										Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;	//升级结束
										if(Ota_UpTask.up_sta_callback)
											Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
										Ota_UpTask.en =0x00;
//										Ota_UpTask.sta=0x00;
										Ota_UpTask.sta = 0x05;	//重启机器
										return;
									}
									Ota_UpTask.pFirmwareBuff->packet_num++;
									if(Ota_UpTask.up_sta.fw_pack_size<Ota_UpFirmWareInfo.FirmwareInfo.FW_Size)//数据未请求完，继续请求
									{
										if(((Ota_UpTask.up_sta.fw_pack_size*100)/Ota_UpFirmWareInfo.FirmwareInfo.FW_Size)!=Ota_UpTask.up_sta.ratio)
										{
											Ota_UpTask.up_sta.ratio=(Ota_UpTask.up_sta.fw_pack_size*100)/Ota_UpFirmWareInfo.FirmwareInfo.FW_Size;
											Ota_UpTask.up_sta.err = OTA_NORMAL;		//正常
											Ota_UpTask.up_sta.sta = OTA_UPDATA_RUN;	//升级中
											if(Ota_UpTask.up_sta_callback)
												Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
										}
										Ota_UpTask.sta=0x02;
									}
									else if(Ota_UpTask.up_sta.fw_pack_size==Ota_UpFirmWareInfo.FirmwareInfo.FW_Size)//数据请求结束
									{
										if(Iap_UpData_Check(&Ota_UpFirmWareInfo.FirmwareInfo))//数据校验成功
										{
											Ota_UpTask.sta=0x05;//等待设备重启
											Ota_UpTask.rest_time=0;
										}
										else
										{
											
										}
										ota_FreeData();
										Ota_UpTask.up_sta.err = OTA_NORMAL;			//正常
										Ota_UpTask.up_sta.sta = OTA_UPDATA_FINSH;	//升级结束
										Ota_UpTask.up_sta.ratio=100;
										if(Ota_UpTask.up_sta_callback)
											Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
										
									}
								}
								else//数据异常,重新请求
								{
									Ota_UpTask.sta=0x04;
									Ota_UpTask.up_sta.err = OTA_DATA_UNUSUAL;	//数据异常，重新请求
									Ota_UpTask.up_sta.sta = OTA_UPDATA_RUN;		//升级中				
									if(Ota_UpTask.up_sta_callback)
											Ota_UpTask.up_sta_callback(&Ota_UpTask.up_sta);
								}
								break;
							case -1://传入数据地址为空
								Ota_UpTask.sta=0x04;
								break;
							case -2://异常响应
								Ota_UpTask.sta=0x04;
								break;
							case -3://数据丢失
								Ota_UpTask.sta=0x04;
								break;
							case -4://数据未分配到空间
								Ota_UpTask.sta=0x04;
								break;
						}
				 }
					
			  }
				else//响应超时，重新请求
				{
					Ota_UpTask.sta=0x03;
				}
				break;
			case 0x05://准备升级
				if(Ota_UpTask.rest_time<OTA_REST_TIME)
					Ota_UpTask.rest_time++;
				else
				{
					Iap_SysReset();//复位系统
					Ota_UpTask.en =0x00;
				  Ota_UpTask.sta=0x00;
				}
				break;
			default:
				Ota_UpTask.en =0x00;
				Ota_UpTask.sta=0x00;
				break;
		}
	}
}


