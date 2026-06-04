/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN从机设备操作参数索引表
*	文件名称 : index_table.c
*	版    本 : V1.0
*	说    明 : 1.实现对用户索引数据的索引地址设置
*            2.实现对用户索引数据的读写
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2016-06-26  欧阳     
*
*********************************************************************************************************
*/	

#include "index_table.h" 

/******************添加对象字典参数信息*************************/

void *IndexTable[INDEXADDR_MAXNUM+1];                                                                                                               //创建索引地址表
uint16_t Index_CustomSize[INDEX_CUSTOM_DATASIZE];                                                                                                   //创建自定义数据字节数索引表，需在索引表初始化函数中对其进行初始化
const uint8_t  Index_DataAddr_Start[INDEX_DATATYPE_NUM]={INDEX_SINGLE_STARTADDR,INDEX_DOUBLE_STARTADDR,INDEX_FOUR_STARTADDR,INDEX_CUSTOM_STARTADDR};//创建各数据类型索引表起始索引地址表
const uint8_t  Index_DataAddr_End  [INDEX_DATATYPE_NUM]={INDEX_SINGLE_ENDADDR,INDEX_DOUBLE_ENDADDR,INDEX_FOUR_ENDADDR,INDEX_CUSTOM_ENDADDR};        //创建个数据类型索引表结束索引地址表

void IndexTable_Init(void)
{
	int32_t i;
	for(i=0;i<256;i++)
	 IndexTable[i]=0;
}
/*****************************************
函数：IndexTable_WriteData
功能：写入指定索引地址数据
参数：index_Num 索引号
      data      写入数据首地址
      datasize  写入数据字节数
返回：0xFFFF    索引号超出范围
      0xFFFE    资源节点不存在
      0xFFFD    数据与资源节点不匹配
      0x00FF    写入成功
******************************************/
uint16_t IndexTable_WriteData(uint8_t index_num,void *pdata,uint16_t datasize)
{
	uint8_t i_datatype;
	uint16_t err;
	if(index_num>INDEXADDR_MAXNUM)
		return 0xFFFF;                     //地址超出范围
	if(IndexTable[index_num]==NULL)
		return 0xFFFE;                     //资源节点不存在
	for(i_datatype=0;i_datatype<INDEX_DATATYPE_NUM;i_datatype++)
	{
	if(((index_num>Index_DataAddr_Start[i_datatype])||(index_num==Index_DataAddr_Start[i_datatype]))
		  &&((index_num<Index_DataAddr_End[i_datatype])||(index_num==Index_DataAddr_End[i_datatype])))
		{
			switch(i_datatype)
			{
				case 0x00:
				case 0x01:
				case 0x02:
					if(datasize!=(0x01<<i_datatype))
						err=0xFFFD;
					else
					{
					 Mem_copy(IndexTable[index_num],pdata,datasize);
					 err=0x00FF;
					}
				break;
				case 0x03:
					if(datasize!=Index_CustomSize[index_num-INDEX_CUSTOM_STARTADDR])
						err=0xFFFD;
					else
					{
					 Mem_copy(IndexTable[index_num],pdata,datasize);
					 err=0x00FF;
					}
			  break;
				default:break;
			}
			              //写入完成
		}
	}
 return err;	
}
/*****************************************
函数：IndexTable_ReadData
功能：写入指定索引地址数据
参数：index_Num 索引号
      data      读出数据首地址
      datasize  读出数据字节数
返回：0xFFFF    索引号超出范围
      0xFFFE    资源节点不存在
      其他      返回读取节点字节数
******************************************/
uint16_t IndexTable_ReadData(uint8_t index_num,void *pdata)
{
	uint8_t i_datatype;
	uint16_t datasize;
	if(index_num>INDEXADDR_MAXNUM)
		return 0xFFFF;                     //地址超出范围
	if(IndexTable[index_num]==NULL)
		return 0xFFFE;                     //资源节点不存在
	for(i_datatype=0;i_datatype<INDEX_DATATYPE_NUM;i_datatype++)
	{
	if(((index_num>Index_DataAddr_Start[i_datatype])||(index_num==Index_DataAddr_Start[i_datatype]))
		  &&((index_num<Index_DataAddr_End[i_datatype])||(index_num==Index_DataAddr_End[i_datatype])))
		{
			switch(i_datatype)
			{
				case 0x00:
				case 0x01:
				case 0x02:
					datasize=0x01<<i_datatype;
					Mem_copy(pdata,IndexTable[index_num],datasize);
				break;
				case 0x03:
					datasize=Index_CustomSize[index_num-INDEX_CUSTOM_STARTADDR];
					Mem_copy(pdata,IndexTable[index_num],datasize);
			  break;
				default:break;
			}
			              //写入完成
		}
	}
  return datasize;
}
/*****************************************
函数：IndexTable_SetAddr
功能：设置指定索引号指向地址
参数：index_Num     索引号
      index_address 指向地址
返回：0x00    索引号超出范围
      0x01    资源节点已存在
      0x02    资源节点数据大小不符
      0xFF    设置成功
******************************************/
uint8_t IndexTable_SetAddr(uint8_t index_num,uint16_t bytenum,void *index_address)
{
	uint8_t err=0x00;
	uint8_t i_datatype;
	if(index_num>INDEXADDR_MAXNUM)
	 return 0x00;
	if(IndexTable[index_num]!=NULL)
	 err=0x01;                                   //该索引号已设置
	else
	{
	 for(i_datatype=0;i_datatype<INDEX_DATATYPE_NUM;i_datatype++)
		{
		  if(((index_num>Index_DataAddr_Start[i_datatype])||(index_num==Index_DataAddr_Start[i_datatype]))
				&&((index_num<Index_DataAddr_End[i_datatype])||(index_num==Index_DataAddr_End[i_datatype])))
			{
				switch(i_datatype)
				{
					case 0x00:
					case 0x01:
					case 0x02:
						if(bytenum!=(0x01<<i_datatype))
							err=0x02;
						else
							err=0xFF;
					  break;
					case 0x03:
						if(bytenum>INDEX_DATASIZE_MAX)
							err=0x02;
						else
						{
							Index_CustomSize[index_num-INDEX_FOUR_ENDADDR-1]=bytenum;
							err=0xFF;
						}
					break;
					default:break;
				}
			}
		}
	 if(err==0xFF)
	  IndexTable[index_num]=index_address; 
	}
	return err;
}
/*****************************************
函数：IndexTable_RemoveAddr
功能：删除指定索引号指向地址
参数：index_Num     索引号
返回：0x00    索引号超出范围
      0xFF    设置成功
******************************************/
uint8_t IndexTable_RemoveAddr(uint8_t index_num)
{
	if(index_num>INDEXADDR_MAXNUM)
		return 0x00;
  IndexTable[index_num]=NULL;
	return 0xFF;
}
/*****************************************
函数：IndexTable_GetAddr
功能：获取指定索引号指向地址
参数：index_Num     索引号
返回：返回索引号指向地址
******************************************/
void *IndexTable_GetAddr(uint8_t index_num)
{
	return IndexTable[index_num];
}

/*****************************************
函数：IndexTable_GetDataLen
功能：获取指定索引号指向地址
参数：index_Num     索引号
返回：返回索引号指向地址
******************************************/
uint16_t IndexTable_GetDataLen(uint8_t index_num)
{
	uint8_t i_datatype;
	uint16_t datasize;
	if(index_num>INDEXADDR_MAXNUM)
		return 0xFFFF;                     //地址超出范围
	if(IndexTable[index_num]==NULL)
		return 0xFFFE;                     //资源节点不存在
	for(i_datatype=0;i_datatype<INDEX_DATATYPE_NUM;i_datatype++)
	{
	if(((index_num>Index_DataAddr_Start[i_datatype])||(index_num==Index_DataAddr_Start[i_datatype]))
		  &&((index_num<Index_DataAddr_End[i_datatype])||(index_num==Index_DataAddr_End[i_datatype])))
		{
			switch(i_datatype)
			{
				case 0x00:
				case 0x01:
				case 0x02:
					datasize=0x01<<i_datatype;
				break;
				case 0x03:
					datasize=Index_CustomSize[index_num-INDEX_CUSTOM_STARTADDR];
			  break;
				default:break;
			}
			              //写入完成
		}
	}
  return datasize;
}
