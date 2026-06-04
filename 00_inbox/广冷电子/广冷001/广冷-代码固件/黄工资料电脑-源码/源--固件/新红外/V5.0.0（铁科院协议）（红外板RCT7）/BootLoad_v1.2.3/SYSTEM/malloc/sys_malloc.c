#include "sys_malloc.h"

__align(4) unsigned char sysmem_base[SYS_MEM_MAX_SIZE];  //创建内存池
unsigned char  sysmem_mapbase[SYS_MEM_ALLOC_TABLE_SIZE];	//内存表

unsigned int sysmemtblsize=SYS_MEM_ALLOC_TABLE_SIZE;		//内存表大小
unsigned int sysmemblksize=SYS_MEM_BLOCK_SIZE;					//内存分块大小
unsigned int sysmemsize=SYS_MEM_MAX_SIZE;							//内存总大小

Sys_mallco_dev sys_mallco_dev={
	                      SysMem_init,
	                      SysMem_perused,
	                      sysmem_base,
	                      sysmem_mapbase,
	                      0
                       };
/********************************
函数功能：复制内存            
参数：*des:目的地址           
      *src:源地址            
      size数据字节数          
返回：无    
********************************/
void SysMem_copy(void *des,void *src, unsigned int size)  
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

void SysMem_set(void *src,unsigned char data,unsigned int count)  
{  
    unsigned char *xs = src;  
    while(count--)*xs++=data;  
}	

/********************************
函数功能：内存管理器初始化    
参数：无        
返回：无    
********************************/
void SysMem_init(void)  
{  
  SysMem_set(sys_mallco_dev.memmap, 0,SYS_MEM_ALLOC_TABLE_SIZE);//内存状态表数据清零  
	SysMem_set(sys_mallco_dev.membase, 0,SYS_MEM_MAX_SIZE);	//内存池所有数据清零  
	sys_mallco_dev.memrdy=1;								//内存管理初始化OK  
} 

/********************************
函数功能：内存管理器初始化    
参数：无        
返回：无    
********************************/
unsigned char SysMem_perused(void)  
{  
	unsigned int used=0; 	
	unsigned int i;  
	for(i=0;i<SYS_MEM_ALLOC_TABLE_SIZE;i++)  
	{  
			if(sys_mallco_dev.memmap[i])
				used++; 
	} 
 return (used*100)/(SYS_MEM_ALLOC_TABLE_SIZE);  
}


unsigned int sys_mem_malloc(unsigned int size)  
{  
    signed long offset=0;  
    unsigned short nmemb;	//需要的内存块数  
	  unsigned short cmemb=0;//连续空内存块数
    unsigned int i;  
    if(!sys_mallco_dev.memrdy)
			sys_mallco_dev.init();//未初始化,先执行初始化 
    if(size==0)return 0XFFFFFFFF;//不需要分配

    nmemb=size/sysmemblksize;  	//获取需要分配的连续内存块数
    if(size%sysmemblksize)
			nmemb++;  
    for(offset=sysmemtblsize-1;offset>=0;offset--)//搜索整个内存控制区  
    {     
			if(!sys_mallco_dev.memmap[offset])
				cmemb++;                       //连续空内存块数增加
			else 
				cmemb=0;								       //连续内存块清零
			if(cmemb==nmemb)							   //找到了连续nmemb个空内存块
			{
				for(i=0;i<nmemb;i++)  					//标注内存块非空 
				{  
						sys_mallco_dev.memmap[offset+i]=nmemb;  
				}  
				return (offset*sysmemblksize);//返回偏移地址  
			}
    }  
    return 0XFFFFFFFF;//未找到符合分配条件的内存块  
}

unsigned char sys_mem_free(unsigned int offset)  
{  
    int i;  
    if(!sys_mallco_dev.memrdy)//未初始化,先执行初始化
	{
		sys_mallco_dev.init();    
        return 1;//未初始化  
    }  
    if(offset<sysmemsize)//偏移在内存池内. 
    {  
        int index=offset/sysmemblksize;			//偏移所在内存块号码  
        int nmemb=sys_mallco_dev.memmap[index];	//内存块数量
        for(i=0;i<nmemb;i++)  						//内存块清零
        {  
            sys_mallco_dev.memmap[index+i]=0;  
        }  
        return 0;  
    }else 
		return 2;//偏移超区了.  
} 

void SysMem_free(void *ptr)  
{  
	unsigned int offset;  
   if(ptr==NULL)return;//地址为0.  
 	  offset=(unsigned int)ptr-(unsigned int)sys_mallco_dev.membase;
   sys_mem_free(offset);//释放内存     
}

void *SysMem_malloc(unsigned int size)  
{  
  unsigned int offset;  									      
	offset=sys_mem_malloc(size);  	   				   
    if(offset==0XFFFFFFFF)return NULL;  
    else return (void*)((unsigned int)sys_mallco_dev.membase+offset);  
}

void *sys_myrealloc(void *ptr,unsigned int size)  
{  
    unsigned int offset;  
    offset=sys_mem_malloc(size);  
    if(offset==0XFFFFFFFF)return NULL;     
    else  
    {  									   
	    SysMem_copy((void*)((unsigned int)sys_mallco_dev.membase+offset),ptr,size);	//拷贝旧内存内容到新内存   
        SysMem_free(ptr);  											  		//释放旧内存
        return (void*)((unsigned int)sys_mallco_dev.membase+offset);  				//返回新内存首地址
    }  
} 

