/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : 动态内存管理
*	文件名称 : malloc.c
*	版    本 : V1.0
*	说    明 : 1.实现内存的动态管理
*            2.实现内存的分配释放
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "malloc.h"

__align(4) unsigned char mem_base[MEM_MAX_SIZE];  //创建内存池
unsigned char  mem_mapbase[MEM_ALLOC_TABLE_SIZE];	//内存表

unsigned int memtblsize=MEM_ALLOC_TABLE_SIZE;		//内存表大小
unsigned int memblksize=MEM_BLOCK_SIZE;					//内存分块大小
unsigned int memsize=MEM_MAX_SIZE;							//内存总大小

_mallco_dev mallco_dev={
	                      Mem_init,
	                      Mem_perused,
	                      mem_base,
	                      mem_mapbase,
	                      0
                       };
/********************************
函数功能：复制内存            
参数：*des:目的地址           
      *src:源地址            
      size数据字节数          
返回：无    
********************************/
void Mem_copy(void *des,void *src, unsigned int size)  
{  
    unsigned char *xdes=des;
	 unsigned char *xsrc=src; 
    while(size--)*xdes++=*xsrc++;  
} 


/********************************
函数功能：设置制定内存       
参数：*des:目的地址           
      *src:源地址            
      size数据字节数          
返回：无    
********************************/

void Mem_set(void *src,unsigned char data,unsigned int count)  
{  
    unsigned char *xs = src;  
    while(count--)*xs++=data;  
}	

/********************************
函数功能：内存管理器初始化    
参数：无        
返回：无    
********************************/
void Mem_init(void)  
{  
  Mem_set(mallco_dev.memmap, 0,MEM_ALLOC_TABLE_SIZE);//内存状态表数据清零  
	Mem_set(mallco_dev.membase, 0,MEM_MAX_SIZE);	//内存池所有数据清零  
	mallco_dev.memrdy=1;								//内存管理初始化OK  
} 

/********************************
函数功能：内存管理器初始化    
参数：无        
返回：无    
********************************/
unsigned char Mem_perused(void)  
{  
	unsigned int used=0; 	
	unsigned int i;  
	for(i=0;i<MEM_ALLOC_TABLE_SIZE;i++)  
	{  
			if(mallco_dev.memmap[i])
				used++; 
	} 
 return (used*100)/(MEM_ALLOC_TABLE_SIZE);  
}


unsigned int mem_malloc(unsigned int size)  
{  
    signed long offset=0;  
    unsigned short nmemb;	//需要的内存块数  
	  unsigned short cmemb=0;//连续空内存块数
    unsigned int i;  
    if(!mallco_dev.memrdy)
			mallco_dev.init();//未初始化,先执行初始化 
    if(size==0)return 0XFFFFFFFF;//不需要分配

    nmemb=size/memblksize;  	//获取需要分配的连续内存块数
    if(size%memblksize)
			nmemb++;  
    for(offset=memtblsize-1;offset>=0;offset--)//搜索整个内存控制区  
    {     
			if(!mallco_dev.memmap[offset])
				cmemb++;                       //连续空内存块数增加
			else 
				cmemb=0;								       //连续内存块清零
			if(cmemb==nmemb)							   //找到了连续nmemb个空内存块
			{
				for(i=0;i<nmemb;i++)  					//标注内存块非空 
				{  
						mallco_dev.memmap[offset+i]=nmemb;  
				}  
				return (offset*memblksize);//返回偏移地址  
			}
    }  
    return 0XFFFFFFFF;//未找到符合分配条件的内存块  
}

unsigned char mem_free(unsigned int offset)  
{  
    int i;  
    if(!mallco_dev.memrdy)//未初始化,先执行初始化
	{
		mallco_dev.init();    
        return 1;//未初始化  
    }  
    if(offset<memsize)//偏移在内存池内. 
    {  
        int index=offset/memblksize;			//偏移所在内存块号码  
        int nmemb=mallco_dev.memmap[index];	//内存块数量
        for(i=0;i<nmemb;i++)  						//内存块清零
        {  
            mallco_dev.memmap[index+i]=0;  
        }  
        return 0;  
    }else 
		return 2;//偏移超区了.  
} 

void Mem_free(void *ptr)  
{  
	unsigned int offset;  
   if(ptr==NULL)return;//地址为0.  
 	  offset=(unsigned int)ptr-(unsigned int)mallco_dev.membase;
   mem_free(offset);//释放内存     
}

void *Mem_malloc(unsigned int size)  
{  
  unsigned int offset;  									      
	offset=mem_malloc(size);  	   				   
    if(offset==0XFFFFFFFF)return NULL;  
    else return (void*)((unsigned int)mallco_dev.membase+offset);  
}

void *myrealloc(void *ptr,unsigned int size)  
{  
    unsigned int offset;  
    offset=mem_malloc(size);  
    if(offset==0XFFFFFFFF)return NULL;     
    else  
    {  									   
	    Mem_copy((void*)((unsigned int)mallco_dev.membase+offset),ptr,size);	//拷贝旧内存内容到新内存   
        Mem_free(ptr);  											  		//释放旧内存
        return (void*)((unsigned int)mallco_dev.membase+offset);  				//返回新内存首地址
    }  
} 

