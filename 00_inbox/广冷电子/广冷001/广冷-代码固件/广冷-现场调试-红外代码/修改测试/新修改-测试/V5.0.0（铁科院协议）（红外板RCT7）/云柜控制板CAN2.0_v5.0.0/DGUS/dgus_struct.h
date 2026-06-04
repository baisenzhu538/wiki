#ifndef	_DGUS_STRUCT_H_
#define	_DGUS_STRUCT_H_

#include "sys.h"


#define	DGUS_WRITE_CMD	0x82
#define	DGUS_READ_CMD	0x83
#define	DGUS_FIX_HEAD	0x5AA5

#define	DGUS_DATA_BUFFER_MAX_SIZE	256
#define	DGUS_DATA_MAX_SIZE	250

typedef	struct
{
	u16	FixHead;					//固定为0x5AA5
	u8	DataLenth;					//指令+数据+校验的字节数目
	u8	Cmd;						//0x82写 0x83读
	u8	Data[DGUS_DATA_MAX_SIZE];	//最大249 字节	
	u16	Crc16;						//CRC-16(x16+x15+x2+1),校验段为Cmd、Data
}DgusDataPack_TypeDef;


#endif	/*_DGUS_STRUCT_H_*/

