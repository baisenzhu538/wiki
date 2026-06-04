#ifndef __MALLOC_H
#define __MALLOC_H

#include "canbus_config.h"

#ifndef NULL
#define NULL 0
#endif

#define MEM_BLOCK_SIZE			CAN_MEM_BLOCKSIZE 
#define MEM_MAX_SIZE        CAN_MEM_MAXSIZE

#define MEM_ALLOC_TABLE_SIZE MEM_MAX_SIZE/MEM_BLOCK_SIZE

#define MEM_COPY_FOURBYTE(x,y) *((uint32_t*)(x))=*((uint32_t*)(y))

//内存管理控制器
typedef struct _m_mallco_dev
{
	void (*init)(void);					        //初始化
	unsigned char (*perused)(void);		 //内存使用率
	unsigned char 	*membase;					//内存池 管理2个区域的内存
	unsigned char *memmap; 					//内存管理状态表
	unsigned char  memrdy; 						//内存管理是否就绪
}_mallco_dev;

//extern _mallco_dev mallco_dev;

void Mem_init(void);
unsigned char Mem_perused(void);
void Mem_copy(void *des,void *src, unsigned int size);
void *Mem_malloc(unsigned int size);
void Mem_free(void *ptr);
#endif
