#ifndef __SYS_MALLOC_H
#define __SYS_MALLOC_H

#ifndef NULL
#define NULL 0
#endif

#define SYS_MEM_BLOCK_SIZE			 32 
#define SYS_MEM_MAX_SIZE         10*1024

#define SYS_MEM_ALLOC_TABLE_SIZE  (SYS_MEM_MAX_SIZE/SYS_MEM_BLOCK_SIZE)

//#define MEM_COPY_FOURBYTE(x,y) *((uint32_t*)(x))=*((uint32_t*)(y))

//内存管理控制器
typedef struct 
{
	void (*init)(void);					        //初始化
	unsigned char (*perused)(void);		 //内存使用率
	unsigned char 	*membase;					//内存池 管理2个区域的内存
	unsigned char *memmap; 					//内存管理状态表
	unsigned char  memrdy; 						//内存管理是否就绪
}Sys_mallco_dev;

//extern _mallco_dev mallco_dev;

void SysMem_init(void);
unsigned char SysMem_perused(void);
void SysMem_copy(void *des,void *src, unsigned int size);
void *SysMem_malloc(unsigned int size);
void SysMem_free(void *ptr);
#endif

