#ifndef __INDEX_TABLE_H
#define __INDEX_TABLE_H	
#include "data_struct.h"
#include "malloc.h"

#define INDEX_DATASIZE_MAX       64*7

#define INDEX_DATATYPE_NUM       4
#define INDEXADDR_MAXNUM         255  //最大索引地址


#define INDEX_SINGLE_STARTADDR  0x00  //单字节类型数据起始索引地址
#define INDEX_SINGLE_ENDADDR    0x3F  //单字节类型数据结束索引地址
 
#define INDEX_DOUBLE_STARTADDR  0x40
#define INDEX_DOUBLE_ENDADDR    0x7F

#define INDEX_FOUR_STARTADDR    0x80
#define INDEX_FOUR_ENDADDR      0xBF

#define INDEX_CUSTOM_STARTADDR  0xC0
#define INDEX_CUSTOM_ENDADDR    0xFF

#define INDEX_SINGLE_DATASIZE   INDEX_SINGLE_ENDADDR-INDEX_SINGLE_STARTADDR
#define INDEX_DOUBLE_DATASIZE   INDEX_DOUBLE_ENDADDR-INDEX_DOUBLE_STARTADDR
#define INDEX_FOUR_DATASIZE     INDEX_FOUR_ENDADDR-INDEX_FOUR_STARTADDR
#define INDEX_CUSTOM_DATASIZE   INDEX_CUSTOM_ENDADDR-INDEX_CUSTOM_STARTADDR
//can标准数据包结构体

void IndexTable_Init(void);

uint16_t IndexTable_GetDataLen(uint8_t index_num);
uint16_t IndexTable_WriteData(uint8_t index_Num,void *data,uint16_t datasize);
uint16_t IndexTable_ReadData(uint8_t index_Num,void *data);
uint8_t IndexTable_SetAddr(uint8_t index_num,uint16_t bytenum,void *index_address);
uint8_t IndexTable_RemoveAddr(uint8_t index_Num);
void *IndexTable_GetAddr(uint8_t index_Num);

#endif
