
/*
*********************************************************************************************************
*
*	模块名称 : IAP在线升级模块
*	文件名称 : iap.c
*	版    本 : V1.2.1
*	说    明 : iap模块分为bootload模式和用户模式，bootload模式下主要进行固件更新操作，用户模式下主要实现固件
             的下载和保存，该模块需要将flash分成三个区，分别为bootload，user，backup，三个区，bootload存放
						 的是bootload程序，user存放的为用户程序，backup用于备份固件数据，三个区的大小可通过iap.h设置
*	修改记录 :
*		版本号  日期       作者     说明
*		V1.0    2017-12-01 Waves    发布初始版本
*   V1.01   2018-06-04 Waves    修改 Iap_UpDataApp 函数错误代码
*   V1.10   2018-08-23 Waves    增加MD5校验
*   V1.20   2018-10-13 Waves    修改bootload空间大小为6KB
*   V1.2.1  2018-12-28 Waves    修改iap_write_appbin 支持写入固件不超过64KB问题
*   V1.2.2  2019-04-09 Waves    增加数据存储空间宏定义IAP_DATABASE_FLASHADDR IAP_DATABASE_FLASHSIZE
                                增加数据校验接口 uint8_t Iap_UpData_Check(FirmwareInfoTypeDef *pFirmwareInfo)
																增加系统复位接口 void Iap_SysReset(void);
*********************************************************************************************************
*/

#include "iap.h"
#include "stmflash.h"

#ifdef IAP_USER_MODE
#include "md5.h"
#endif

#ifdef IAP_BOOTLOAD_MODE
const uint16_t App_UpDataFlag __attribute__( (at(IAP_UPFLAG_ADDR)))=0xFFFF;        //应用程序更新标志位,0xFFFF为无需更新直接进入应用程序，0x0000为进入更新状态
#endif

iapfun jump2app;
u16 iapbuf[1024];

//系统软件复位
void Iap_SysReset(void) 
{ 
 __set_FAULTMASK(1); 
 NVIC_SystemReset(); 
}
//appxaddr:应用程序的起始地址
//appbuf:应用程序CODE.
//appsize:应用程序大小(字节).
void iap_write_appbin(uint32_t appxaddr,uint8_t *appbuf,uint32_t appsize)
{
	u32 t;
	u32 i=0;
	u32 temp;
	u32 fwaddr=appxaddr;//当前写入的地址
	u8 *dfu=appbuf;
	for(t=0;t<appsize;t+=2)
	{						    
		temp=(u16)dfu[1]<<8;
		temp+=(u16)dfu[0];	  
		dfu+=2;//偏移2个字节
		iapbuf[i++]=temp;	    
		if(i==1024)
		{
			i=0;
			STMFLASH_Write(fwaddr,iapbuf,1024);	
			fwaddr+=2048;//偏移2048  16=2*8.所以要乘以2.
		}
	}
	if(i)
	 STMFLASH_Write(fwaddr,iapbuf,i);//将最后的一些内容字节写进去.  
}

//跳转到应用程序段
void iap_load_app(uint32_t appxaddr)
{
	if(((*(vu32*)appxaddr)&0x2FFE0000)==0x20000000)	//检查栈顶地址是否合法.
	{ 
		jump2app=(iapfun)*(vu32*)(appxaddr+4);		//用户代码区第二个字为程序开始地址(复位地址)		
		MSR_MSP(*(vu32*)appxaddr);					//初始化APP堆栈指针(用户代码区的第一个字用于存放栈顶地址)
		jump2app();									//跳转到APP.
	}
}	

void Iap_LoadApp(void)
{
	uint16_t UpdataFlag;
	UpdataFlag=0xFFFF;
	STMFLASH_Write(IAP_UPFLAG_ADDR,(uint16_t*)&UpdataFlag,sizeof(UpdataFlag));
	iap_load_app(IAP_USER_ADDR);
}

#ifdef IAP_USER_MODE
void Iap_SetBase(void)
{
	SCB->VTOR = FLASH_BASE | IAP_USER_ADDR;
}
#endif
#ifdef IAP_BOOTLOAD_MODE
void Iap_TaskRun(void)
{
	uint16_t UpdataFlag;
	STMFLASH_Read(IAP_UPFLAG_ADDR,&UpdataFlag,sizeof(UpdataFlag));
	if(UpdataFlag==0xFFFF)//检测是否更新，如果未更新则跳入用户应用
	 iap_load_app(IAP_USER_ADDR);//跳转到用户程序地址
  iap_write_appbin(IAP_USER_ADDR,(uint8_t*)IAP_BACKUPAREA_ADDR,IAP_USER_FLASHSIZE);
	Iap_LoadApp();//跳转进入应用程序
}
#endif

u16 app_bufnum=0;
u32 app_bufsize=0;

#ifdef IAP_USER_MODE

uint8_t Iap_FwCheck(uint8_t *pData,uint32_t size,uint8_t *pchecksum)
{
	uint8_t i;
	FirmwareInfoTypeDef FirmwareInfo;
	MD5_CTX MD5context;
	MD5Init(&MD5context);//MD5初始化
	MD5Update(&MD5context,(unsigned char *)pData,size);
	MD5Final(&MD5context,FirmwareInfo.FW_Check);
	for(i=0;i<IAP_FWCHECK_BYTENUM;i++)
	{
		if(pchecksum[i]!=FirmwareInfo.FW_Check[i])
			return 0x00;
	}
	return 0xFF;
}
//数据更新完成
uint8_t Iap_UpData_Finish(FirmwareInfoTypeDef *pFirmwareInfo)
{
	uint16_t UpdataFlag;
  
	if(Iap_FwCheck((uint8_t*)IAP_BACKUPAREA_ADDR,pFirmwareInfo->FW_Size,pFirmwareInfo->FW_Check))
	{
	 UpdataFlag=0x0000;
	 STMFLASH_Write(IAP_UPFLAG_ADDR,(uint16_t*)&UpdataFlag,sizeof(UpdataFlag));//置位标志位
//	 Iap_SysReset();
	OWN_RESET();
	 return 0xFF;
	}
	else
		return 0x00;
}

uint8_t Iap_UpData_Check(FirmwareInfoTypeDef *pFirmwareInfo)
{
	uint16_t UpdataFlag;
	if(Iap_FwCheck((uint8_t*)IAP_BACKUPAREA_ADDR,pFirmwareInfo->FW_Size,pFirmwareInfo->FW_Check))
	{
	 UpdataFlag=0x0000;
	 STMFLASH_Write(IAP_UPFLAG_ADDR,(uint16_t*)&UpdataFlag,sizeof(UpdataFlag));//置位标志位
	 return 0xFF;
	}
	else
		return 0x00;
}


void Iap_Rest_UpData(void)
{
	app_bufnum=0;
	app_bufsize=0;
}

uint8_t Iap_UpDataApp(FirmwareBuffTypeDef *pApp_Buf)
{
	if(pApp_Buf->packet_num==app_bufnum)
	{
		iap_write_appbin(IAP_BACKUPAREA_ADDR+app_bufsize,pApp_Buf->buf,pApp_Buf->packet_size);
		app_bufnum++;
		app_bufsize+=pApp_Buf->packet_size;
		return 0xFF;//写入完成
	}
  else
  return 0x00;//返回数据段出错		
}
#endif

