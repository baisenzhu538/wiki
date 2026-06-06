#ifndef	_AT_AIR720_H_
#define	_AT_AIR720_H_


#include "NetworkModule.h"
#include "sys_malloc.h"
#include "stdio.h"
#include "string.h"
#include "sys.h"

#define	AT_MODE					0x00	//AT握手
#define	CPIN_MODE				0x01	//查询SIM卡
#define	CSQ_MODE				0x02	//查询CSQ
#define	CGATT_MODE				0x03
#define	CIPSHUT_MODE			0x04	//关闭移动场景
#define	CSTT_MODE				0x05	//配置APN
#define	CIICR_MODE				0x06	//激活移动场景
#define	CIFSR_MODE				0x07	//查询本地IP地址
#define	CIPSTART_MODE			0x08	//建立TCP连接
#define	CFUN_MODE				0x09	//飞行模式
#define	FREE_MODE				0x0A	//空闲模式
#define	ATE0_MODE				0x0B	//关闭回显
#define	CIPMODE_MODE			0x0C	//透传模式
#define	START_WAIT_MODE			0x0D	//等待模块启动
#define	MODE_RESET_MODE			0x0E	//复位
#define	AT_CMD_MODE				0x0F	//AT命令模式
#define	CIPMODE_WAIT_MODE		0x10	//
#define	CGATT_WAIT_MODE			0x11
#define	ATE0_WAIT_MODE			0x12
#define	CPIN_WAIT_MODE			0x13
#define	ICCID_MODE				0x14
#define	ICCID_WAIT_MODE			0x15

#define	CIPSTATUS1_MODE			0x14
#define	CIPSTATUS2_MODE			0x15
#define	CIPSTATUS3_MODE			0x16
#define	CIPSTATUS4_MODE			0x17
#define	CIPSTATUS5_MODE			0x18

#define	SHUTWAIT_MODE			0x19

#define EN_CFUN_MODE			0x1A
#define	EX_CFUN_MODE			0x1B
#define	CFUN_WAIT_MODE			0x1C
#define CIPSHUT_WAIT_MODE		0x1D
#define	AT_WAIT_MODE			0x1E
#define	CSQ_WAIT_MODE			0x1F
#define CIFSR_WAIT_MODE			0x20
#define	CHECK_CIPMODE_MODE		0x21
#define	WAIT_CHECK_CIPMODE_MODE	0x22
#define	WAIT_CIPSTART_MODE		0x23
#define	WAIT_CIICR_MODE			0x24
#define	WAIT_CSTT_MODE			0x25
#define	WAIT_CONNECT_MODE		0x26

#define	AIR720_RST_CTL	PCout(12)		//复位引脚
#define	AIR720_PWR_CTL	PCout(2)		//电源引脚

typedef	struct
{
	u16 EnterAtTime;
	u16 EnterAtOuttime;
	u16 EnterAtReNum;
	u16 GetAtTime;
	u16 GetAtOuttime;
	u16 GetAtReNum;
	u16 OutAtTime;
	u16 OutAtOuttime;
	u16 OutAtReNum;
	u8 EnterAtSta;
	u8 GetAtSta;
	u8 OutAtSta;
	u8 mode;
}AtCheckSta_TypeDef;


u8 AtAir720_Init(void);
char *AtAir720_ReadRssiStr(void);
char *AtAir720_ReadNetStr(void);
char *AtAir720_ReadModeStr(void);
void AtAir720_TaskRun(void);
char AtAir720_ReciveParsing(u8 * data, u16 size);
char AtAir720_SendData(u8* data,u16 size);
u8 AtAir720_CheckModule(void);
char AtAir720_ReadAtSta(void);
char *AtAir720_ReadIccidStr(void);

u8 AtAirHarware_PowerReset(void);
u8 AtAirHarware_ResetModule(void);
void AtAirHarware_ModuleInit(void);
u8 AtAir_CloseTcpConnect(void);	//关闭网络连接
int AtAir720_DeadLine_Check_Task(void);
void AtAit720_CheckRunState_Task(void);
void AtAir720_SetMode(u8 mode);
u8 AtAir720_ConfigModule(void);
int AtAir720_ModuleConfig(NetworkPara_TypeDef * pNetworkPara);
void AtAir720NetworkParaCopy(NetworkPara_TypeDef * NetworkPara);
char * AIR720GpsDrive_GetLatitude(void);
char * AIR720GpsDrive_GetLongitude(void);


#endif	/*_AT_AIR720_H_*/

