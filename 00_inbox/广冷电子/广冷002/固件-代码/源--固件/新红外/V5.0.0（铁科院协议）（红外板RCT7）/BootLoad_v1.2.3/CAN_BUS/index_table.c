/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN资源表映射
*	文件名称 : index_table.c
*	版    本 : V1.0
*	说    明 : 1.实现CAN总线模块的主从机的参数映射
*            2.实现CAN总线模块主从机参数映射表的管理以及读写
*            3.实现用户对参数映射表的操作接口函数
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "index_table.h"
IndexTableTypeDef sIndexTable;
IndexTableTypeDef mIndexTable;
IndexTableTaskTypeDef sIndexTableTask;
IndexTableTaskTypeDef mIndexTableTask;


/*****************************************
函数：IndexTable_SendMsg
功能：发送资源节点数据
参数：*pSource 资源节点信息
      funcid   发送该节点信息的类型
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
uint8_t IndexTable_SendMsg(SourceInfoTypeDef *pSource,uint8_t funcid)
{
	TransportCanMsgTypeDef MsgBuff;
	uint8_t state=0x00;
	MsgBuff.TransportMsgFilter.DestMacID=pSource->SourceData.nodeid;//从站节点ID
	
	MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo_GetNodeId();//本节点ID
	
	MsgBuff.TransportMsgFilter.SourceID =pSource->SourceData.sourceid;
	MsgBuff.TransportMsgFilter.FuncID   =funcid;
	
	if(funcid==FUNCID_CYCLETRIGGER)
	 MsgBuff.TransportMsgFilter.Ack      =0x01;//无需等待响应
	else
	 MsgBuff.TransportMsgFilter.Ack      =0x00;
	
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	

	MsgBuff.TransportMsgData.DataSize   =pSource->SourceData.datalen;
	

	MsgBuff.TransportMsgData.Data      =Mem_malloc(MsgBuff.TransportMsgData.DataSize);
	if(MsgBuff.TransportMsgData.Data==NULL)
		return 0x00;
	Mem_copy(MsgBuff.TransportMsgData.Data,
	         pSource->SourceData.data,
	         pSource->SourceData.datalen); 
		                               	                              
	if(TransportLayer_TxMsg(&MsgBuff)!=0xFF)
		Mem_free(MsgBuff.TransportMsgData.Data);
	else
		state=0xFF;

	return state;
}

/*****************************************
函数：IndexTable_SendAsk
功能：发送响应报文
参数：DestMacID  目标节点地址
      SrcMacID   本地节点地址
      SourceID   资源节点地址
      FuncID     功能码
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
void IndexTable_SendAsk(uint8_t DestMacID,uint8_t SrcMacID,uint8_t SourceID,uint8_t FuncID)
{
	TransportCanMsgTypeDef MsgBuff;
	MsgBuff.TransportMsgFilter.DestMacID=DestMacID;
	MsgBuff.TransportMsgFilter.SrcMacID =SrcMacID;
	MsgBuff.TransportMsgFilter.SourceID =SourceID;
	MsgBuff.TransportMsgFilter.FuncID   =FuncID;
	MsgBuff.TransportMsgFilter.Ack      =0x01;      //响应报文
	MsgBuff.TransportMsgManage.ErrID    =0x00;
	MsgBuff.TransportMsgData.DataSize   =0x00;
	TransportLayer_TxMsg(&MsgBuff);
}

/*****************************************
函数：IndexTable_TraverseUint
功能：查找资源表中的资源单元
参数：*pTable  资源表内存地址
      nodeid   节点地址
      sourceid 资源地址
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
IndexTableUintTypeDef *IndexTable_TraverseUint(IndexTableTypeDef *pTable,uint8_t nodeid,uint8_t sourceid) //获取对应任务块的地址
{
	IndexTableUintTypeDef *pTableUint;
	if(pTable->head==NULL)             //链表中无数据
		return NULL;
	pTableUint=pTable->head;
	while(pTableUint)
	{
		if(pTableUint->Source.SourceData.nodeid==nodeid&&pTableUint->Source.SourceData.sourceid==sourceid)
			return pTableUint;
		pTableUint=pTableUint->next;
	}
	return pTableUint;
}

/*****************************************
函数：IndexTable_AddSource
功能：向指定的资源表新增资源单元
参数：*pTable  资源表内存地址
      *pSource 新增资源信息内存地址
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/

uint8_t IndexTable_AddSource(IndexTableTypeDef *pTable,SourceInfoTypeDef *pSource)
{
	IndexTableUintTypeDef *pTableUint;
	
	if(pTable->tablesize==pTable->maxsize)
		return 0x00;                                                        //空间满
	if(IndexTable_TraverseUint(pTable,pSource->SourceData.nodeid,pSource->SourceData.sourceid)!=NULL)
		return 0x01;                                                        //队列中已有相同任务号
  pTableUint=Mem_malloc(sizeof(IndexTableUintTypeDef));
	if(pTableUint==NULL)
		return 0x02;                              //创建失败
	Mem_copy(&pTableUint->Source,pSource,sizeof(SourceInfoTypeDef));
	if(pTable->head==NULL)          //链表为空
	{
		pTableUint->next=0;
		pTableUint->prior=0;
		pTable->head=pTableUint;
		pTable->tail=pTableUint;
		pTable->tablesize++;
	}
	else
	{
		pTableUint->next=NULL;
		pTable->tail->next=pTableUint;
		pTableUint->prior=pTable->tail;
		pTable->tail=pTableUint;
		pTable->tablesize++;
	}
	return 0xFF;                                //创建成功
}

/*****************************************
函数：IndexTable_RemoveSource
功能：向指定的资源表删除资源单元
参数：*pTable  资源表内存地址
      *pSource 新增资源信息内存地址
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
uint8_t IndexTable_RemoveSource(IndexTableTypeDef *pTable,SourceInfoTypeDef *pSource)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(pTable,pSource->SourceData.nodeid,pSource->SourceData.sourceid);
	if(pTableUint==NULL)             //链表中无数据
		return 0x00;
	if((pTable->tablesize==1)&&(pTable->head==pTable->tail))//链表中只存在一个节点，头尾相同
	{ 
		pTable->tail=0;
		pTable->head=0;
	}
	else if(pTableUint->next==NULL)
	{
		pTable->tail=pTableUint->prior;
		pTable->tail->next=0;
	}
	else if(pTableUint->prior==NULL)
	{
		pTable->head=pTableUint->next;
		pTable->head->prior=0;
	}
	else 
	{
		pTableUint->prior->next=pTableUint->next;
		pTableUint->next->prior=pTableUint->prior;	
	}
	pTable->tablesize--;
  Mem_free(pTableUint);
	return 0xFF;  //删除成功
}

/*****************************************
函数：id_tb_writedata
功能：向指定的资源表指定节点地址指定索引号写入数据
      本函数只在内部调用
参数：*pTable   资源表内存地址
      node_id   节点地址
      index_num 资源索引号
      *pdata    写入数据地址
      datalen   写入数据长度
返回：0x00      数据不存在
      0xFF      写入成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
static uint8_t id_tb_writedata(IndexTableTypeDef *pTable,uint8_t node_id,uint8_t index_num,void *pdata,uint16_t datalen)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(pTable,node_id,index_num);
	if(pTableUint==NULL)
	{
		return 0x00;//节点不存在
	}
	else
	{
		if(pTableUint->Source.SourceData.datalen!=datalen)
			return 0x01;//数据不符合
		Mem_copy(pTableUint->Source.SourceData.data,pdata,datalen);
	}
	return 0xFF;//写入成功
}
/*****************************************
函数：id_tb_readdata
功能：向指定的资源表指定节点地址指定索引号读出数据
      本函数只在内部调用
参数：*pTable   资源表内存地址
      node_id   节点地址
      index_num 资源索引号
      *pdata    读出数据地址
      datalen   读出数据长度
返回：0x00      指定数据不存在
      0xFF      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
static uint8_t id_tb_readdata(IndexTableTypeDef *pTable,uint8_t node_id,uint8_t index_num,void *pdata)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(pTable,node_id,index_num);
	if(pTableUint==NULL)
	{
		return 0x00;//节点不存在
	}
	else
	{
		Mem_copy(pdata,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
	}
	return 0xFF;//读取
}
/*****************************************
函数：id_tb_getdatalen
功能：获取指定的资源表指定节点地址指定索引号指向数据长度
      本函数只在内部调用
参数：*pTable   资源表内存地址
      node_id   节点地址
      index_num 资源索引号
      *pdata    读出数据地址
      datalen   读出数据长度
返回：0x0000    节点不存在
      other     数据长度
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
******************************************/
static uint16_t id_tb_getdatalen(IndexTableTypeDef *pTable,uint8_t node_id,uint8_t index_num)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(pTable,node_id,index_num);
	if(pTableUint==NULL)
	{
		return 0x0000;//节点不存在
	}
	return pTableUint->Source.SourceData.datalen;//获取成功
}
/*************************************************************
函数：sIndexTable_GetDataLen
功能：获取指定节点数据长度
参数：node_id   写入站点地址
      index_num 资源索引号
返回：0x00      数据不存在
      Other      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint16_t sIndexTable_GetDataLen(uint8_t node_id,uint8_t index_num)
{
	uint16_t cb_state;
	cb_state=id_tb_getdatalen(&sIndexTable,node_id,index_num);
	return cb_state;
}
/*************************************************************
函数：mIndexTable_GetDataLen
功能：获取指定节点数据长度
参数：node_id   写入站点地址
      index_num 资源索引号
返回：0x00      数据不存在
      Other      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint16_t mIndexTable_GetDataLen(uint8_t node_id,uint8_t index_num)
{
	uint16_t cb_state;
	cb_state=id_tb_getdatalen(&mIndexTable,node_id,index_num);
	return cb_state;
}

/*************************************************************
函数：sIndexTable_WriteData
功能：往指定节点写数据
参数：node_id   写入站点地址
      index_num 资源索引号
      drdata    数据存放到该地址
返回：0x00      数据不存在
      0x01      数据长度不符合
      0xFF      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_WriteData(uint8_t node_id,uint8_t index_num,void *srdata,uint16_t datalen)
{
	uint8_t cb_state;
	cb_state=id_tb_writedata(&sIndexTable,node_id,index_num,srdata,datalen);
	return cb_state;
}

/*************************************************************
函数：mIndexTable_WriteData
功能：往指定节点写数据
参数：node_id   写入站点地址
      index_num 资源索引号
      drdata    数据存放到该地址
返回：0x00      数据不存在
      0x01      数据长度不符合
      0xFF      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_WriteData(uint8_t node_id,uint8_t index_num,void *srdata,uint16_t datalen)
{
	uint8_t cb_state;
	cb_state=id_tb_writedata(&mIndexTable,node_id,index_num,srdata,datalen);
	return cb_state;
}

/*************************************************************
函数：sIndexTable_ReadData
功能：读取指定节点数据
参数：node_id   读取站点地址
      index_num 资源索引号
      drdata    读取数据存放到该地址
返回：0x00      数据不存在
      0xFF      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_ReadData(uint8_t node_id,uint8_t index_num,void *drdata)
{
	uint8_t cb_state;
	cb_state=id_tb_readdata(&sIndexTable,node_id,index_num,drdata);
	return cb_state;
}

/*************************************************************
函数：mIndexTable_ReadData
功能：读取指定节点数据
参数：node_id   读取站点地址
      index_num 资源索引号
      drdata    读取数据存放到该地址
返回：0x00      数据不存在
      0xFF      读取成功
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_ReadData(uint8_t node_id,uint8_t index_num,void *drdata)
{
	uint8_t cb_state;
	cb_state=id_tb_readdata(&mIndexTable,node_id,index_num,drdata);
	return cb_state;
}
/*************************************************************
函数：sIndexTable_AddSource
功能：创建从站资源节点
参数：nodeid   节点地址
      sourceid 资源地址
      type     数据类型
      *srcdr   资源内存地址
      datalen  数据长度
      
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_AddSource(uint8_t nodeid,uint8_t sourceid,uint8_t type,void *srcdr,uint16_t datalen)
{
	SourceInfoTypeDef src;
	uint8_t cb_state;
	src.SourceManage.type=type;
	src.SourceData.sourceid=sourceid;
	src.SourceData.nodeid=nodeid;
	src.SourceData.datalen=datalen;
	src.SourceData.data=srcdr;
	src.SourceManage.cycle_enable=0;
	src.SourceManage.receive_enable=0;
	src.SourceManage.threshold_enable=0;
	cb_state=IndexTable_AddSource(&sIndexTable,&src);
	return cb_state;
}
/*************************************************************
函数：mIndexTable_AddSource
功能：创建主站资源节点
参数：nodeid   节点地址
      sourceid 资源地址
      type     数据类型
      *srcdr   资源内存地址
      datalen  数据长度
      
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_AddSource(uint8_t nodeid,uint8_t sourceid,uint8_t type,void *srcdr,uint16_t datalen)
{
	SourceInfoTypeDef src;
	uint8_t cb_state;
	src.SourceManage.type=type;
	src.SourceData.sourceid=sourceid;
	src.SourceData.nodeid=nodeid;
	src.SourceData.datalen=datalen;
	src.SourceData.data=srcdr;
	src.SourceManage.cycle_enable=0;
	src.SourceManage.receive_enable=0;
	src.SourceManage.threshold_enable=0;
	cb_state=IndexTable_AddSource(&mIndexTable,&src);
	return cb_state;
}
/*************************************************************
函数：mIndexTable_SetConnectFlag
功能：设置节点连接状态
参数：nodeid       节点地址
      connectflag  连接标志位
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
void mIndexTable_SetConnectFlag(uint8_t nodeid,uint8_t connectflag)
{
	IndexTableUintTypeDef *pTableUint;
	
	if(mIndexTable.head==NULL)             //链表中无数据
		return;
	pTableUint=mIndexTable.head;
	while(pTableUint)
	{
		if(pTableUint->Source.SourceData.nodeid==nodeid)
		{
			pTableUint->Source.SourceManage.connectflag=connectflag;
			if(pTableUint->Source.SourceManage.connectflag==1)
			{
				if(pTableUint->Source.SourceManage.type==RW)
				{
				 pTableUint->Source.SourceManage.cycleinit=0;
				 pTableUint->Source.SourceManage.stateinit=0;
				 pTableUint->Source.SourceManage.thresholdinit=0;
				}
				else
				{
				 pTableUint->Source.SourceManage.cycleinit=1;
				 pTableUint->Source.SourceManage.stateinit=1;
				 pTableUint->Source.SourceManage.thresholdinit=1;
				}
			}
		}
		pTableUint=pTableUint->next;
	}
}

/*************************************************************
函数：sIndexTable_SetConnectFlag
功能：设置节点连接状态
参数：nodeid       节点地址
      connectflag  连接标志位
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
void sIndexTable_SetConnectFlag(uint8_t nodeid,uint8_t connectflag)
{
	IndexTableUintTypeDef *pTableUint;
	
	if(sIndexTable.head==NULL)             //链表中无数据
		return;
	pTableUint=sIndexTable.head;
	while(pTableUint)
	{
		if(pTableUint->Source.SourceData.nodeid==nodeid)
		{
			pTableUint->Source.SourceManage.connectflag=connectflag;
			if(pTableUint->Source.SourceManage.connectflag==1)
			{
				if(pTableUint->Source.SourceManage.type==RO)
				{
				 pTableUint->Source.SourceManage.cycleinit=0;
				 pTableUint->Source.SourceManage.stateinit=0;
				 pTableUint->Source.SourceManage.thresholdinit=0;
				}
				else
				{
				 pTableUint->Source.SourceManage.cycleinit=1;
				 pTableUint->Source.SourceManage.stateinit=1;
				 pTableUint->Source.SourceManage.thresholdinit=1;
				}
			}
		}
		pTableUint=pTableUint->next;
	}
}

/*************************************************************
函数：sIndexTable_SetCycSync
功能：设置资源循环同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
      time      同步周期，单位为10ms
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_SetCycSync(uint8_t nodeid,uint8_t sourceid,uint16_t time)
{
	IndexTableUintTypeDef *pTableUint;
  pTableUint=IndexTable_TraverseUint(&sIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	pTableUint->Source.SourceManage.cycle_enable=1;
	pTableUint->Source.SourceManage.time        =time;
  return 0xFF;
}

/*************************************************************
函数：mIndexTable_SetCycSync
功能：设置资源循环同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
      time      同步周期，单位为10ms
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_SetCycSync(uint8_t nodeid,uint8_t sourceid,uint16_t time)
{
	IndexTableUintTypeDef *pTableUint;
  pTableUint=IndexTable_TraverseUint(&mIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	pTableUint->Source.SourceManage.cycle_enable=1;
	pTableUint->Source.SourceManage.time        =time;
  return 0xFF;
}
/*************************************************************
函数：sIndexTable_SetStateSync
功能：设置资源状态同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_SetStateSync(uint8_t nodeid,uint8_t sourceid)
{
	IndexTableUintTypeDef *pTableUint;
  pTableUint=IndexTable_TraverseUint(&sIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	if(pTableUint->Source.SourceManage.type==RO)     //只读变量需同步主机资源表
		pTableUint->Source.SourceManage.stateinit=0;
	else if(pTableUint->Source.SourceManage.type==RW) //读写变量不需同步主机资源表
		pTableUint->Source.SourceManage.stateinit=1;
	pTableUint->Source.SourceManage.state_enable=1;
	Mem_copy(&pTableUint->Source.SourceManage.last_state,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
  return 0xFF;
}

/*************************************************************
函数：mIndexTable_SetStateSync
功能：设置资源状态同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_SetStateSync(uint8_t nodeid,uint8_t sourceid)
{
	IndexTableUintTypeDef *pTableUint;
  pTableUint=IndexTable_TraverseUint(&mIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	if(pTableUint->Source.SourceManage.type==RO)       //只读变量不需同步资源表
		pTableUint->Source.SourceManage.stateinit=1;
	else if(pTableUint->Source.SourceManage.type==RW)  //读写变量需同步资源表
		pTableUint->Source.SourceManage.stateinit=0;
	
	pTableUint->Source.SourceManage.state_enable=1;
	Mem_copy(&pTableUint->Source.SourceManage.last_state,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
  return 0xFF;
}


/*************************************************************
函数：sIndexTable_SetThresoldSync
功能：设置资源阈值同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
      u_lim     阈值上限
      l_lim     阈值下限
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t sIndexTable_SetThresoldSync(uint8_t nodeid,uint8_t sourceid,uint32_t u_lim,uint32_t l_lim)
{
	IndexTableUintTypeDef *pTableUint;
	uint32_t DataBuf;
	uint32_t State;
  pTableUint=IndexTable_TraverseUint(&sIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	if(pTableUint->Source.SourceManage.type==RO)
		pTableUint->Source.SourceManage.stateinit=0;
	else if(pTableUint->Source.SourceManage.type==RW)
		pTableUint->Source.SourceManage.stateinit=1;
	
	pTableUint->Source.SourceManage.threshold_enable=1;
	Mem_copy(&DataBuf,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
	if(DataBuf>u_lim)
		State=THRESHOLD_UP_STATE;
	else if(DataBuf<l_lim)
		State=THRESHOLD_LOW_STATE;
	else
		State=THRESHOLD_RANGE_STATE;
	pTableUint->Source.SourceManage.last_threshold=State;
  return 0xFF;
}

void sIndexTable_SetStarTx(uint8_t nodeid,uint8_t sourceid)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(&sIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return;
	pTableUint->Source.SourceManage.star_tx=0x01;
}
void mIndexTable_SetStarTx(uint8_t nodeid,uint8_t sourceid)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=IndexTable_TraverseUint(&mIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return;
	pTableUint->Source.SourceManage.star_tx=0x01;
}
/*************************************************************
函数：sIndexTable_SetThresoldSync
功能：设置资源阈值同步模式
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
uint8_t sIndexTable_UpDataLate(uint8_t nodeid,uint8_t sourceid)
{
	IndexTableUintTypeDef *pTableUint;
	uint32_t DataBuf;
	uint32_t State;
	pTableUint=IndexTable_TraverseUint(&sIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	if(pTableUint->Source.SourceManage.state_enable)
		Mem_copy(&pTableUint->Source.SourceManage.last_state,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
	if(pTableUint->Source.SourceManage.threshold_enable)
	{
		Mem_copy(&DataBuf,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
		if(DataBuf>pTableUint->Source.SourceManage.upper_limit)
		 State=THRESHOLD_UP_STATE;
	 else if(DataBuf<pTableUint->Source.SourceManage.lower_limit)
		State=THRESHOLD_LOW_STATE;
	 else
		State=THRESHOLD_RANGE_STATE;
	pTableUint->Source.SourceManage.last_threshold=State;
	}
}
/*************************************************************
函数：mIndexTable_SetThresoldSync
功能：设置资源阈值同步模式
参数：nodeid    节点连接状态
      sourceid  资源地址
      u_lim     阈值上限
      l_lim     阈值下限
返回：
修改记录 :
		版本号  日期        作者     说明
		V1.0    2017-06-24  欧阳     新增
*************************************************************/
uint8_t mIndexTable_SetThresoldSync(uint8_t nodeid,uint8_t sourceid,uint32_t u_lim,uint32_t l_lim)
{
	IndexTableUintTypeDef *pTableUint;
	uint32_t DataBuf;
	uint32_t State;
  pTableUint=IndexTable_TraverseUint(&mIndexTable,nodeid,sourceid);
	if(pTableUint==NULL)
		return 0x00;
	if(pTableUint->Source.SourceManage.type==RO)
		pTableUint->Source.SourceManage.thresholdinit=1;
	else if(pTableUint->Source.SourceManage.type==RW)
		pTableUint->Source.SourceManage.thresholdinit=0;
	
	pTableUint->Source.SourceManage.threshold_enable=1;
	Mem_copy(&DataBuf,pTableUint->Source.SourceData.data,pTableUint->Source.SourceData.datalen);
	if(DataBuf>u_lim)
		State=THRESHOLD_UP_STATE;
	else if(DataBuf<l_lim)
		State=THRESHOLD_LOW_STATE;
	else
		State=THRESHOLD_RANGE_STATE;
	pTableUint->Source.SourceManage.last_threshold=State;
  return 0xFF;
}


void mIndexTable_ReceiveTask(TransportCanMsgTypeDef *pRxMsg)
{
	IndexTableUintTypeDef *pTableUint;
	
	if(pRxMsg->TransportMsgFilter.Ack==0x00)
	 IndexTable_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID,
											pRxMsg->TransportMsgFilter.DestMacID,
											pRxMsg->TransportMsgFilter.SourceID,
											pRxMsg->TransportMsgFilter.FuncID 
											);
	
	pTableUint=IndexTable_TraverseUint(&mIndexTable,
	                                   pRxMsg->TransportMsgFilter.SrcMacID,
	                                   pRxMsg->TransportMsgFilter.SourceID);
	if(pTableUint==NULL)
		return;
	if(pRxMsg->TransportMsgData.DataSize!=0)
	{
		 Mem_copy(pTableUint->Source.SourceData.data,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);
			
		 if(pTableUint->Source.SourceManage.state_enable==1)
		  Mem_copy(&pTableUint->Source.SourceManage.last_state,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);//更新last值
		 
		 if(pTableUint->Source.SourceManage.threshold_enable==1)
		 {
			 uint32_t last;
			 Mem_copy(&last,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);
			 if(last>pTableUint->Source.SourceManage.upper_limit)
				 last=THRESHOLD_UP_STATE;
			 else if(last<pTableUint->Source.SourceManage.lower_limit)
				 last=THRESHOLD_LOW_STATE;
			 else
				 last=THRESHOLD_RANGE_STATE;
			 pTableUint->Source.SourceManage.last_threshold=last;
		 } 
  }
  if(mIndexTableTask.Receive_CallBack!=NULL)
		(*mIndexTableTask.Receive_CallBack)(&pTableUint->Source.SourceData);
}

void sIndexTable_ReceiveTask(TransportCanMsgTypeDef *pRxMsg)
{
	IndexTableUintTypeDef *pTableUint;
	
	if(pRxMsg->TransportMsgFilter.Ack==0x00)
	 IndexTable_SendAsk(pRxMsg->TransportMsgFilter.SrcMacID,
											pRxMsg->TransportMsgFilter.DestMacID,
											pRxMsg->TransportMsgFilter.SourceID,
											pRxMsg->TransportMsgFilter.FuncID 
											);
	
	pTableUint=IndexTable_TraverseUint(&sIndexTable,
	                                   pRxMsg->TransportMsgFilter.SrcMacID,
	                                   pRxMsg->TransportMsgFilter.SourceID);
	if(pTableUint==NULL)
		return;
	if((pRxMsg->TransportMsgData.DataSize!=0)&&(pTableUint->Source.SourceManage.type==RW))//可读写数据才能更新
	{
		 Mem_copy(pTableUint->Source.SourceData.data,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);
			
		 if(pTableUint->Source.SourceManage.state_enable==1)
		  Mem_copy(&pTableUint->Source.SourceManage.last_state,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);//更新last值
		 
		 if(pTableUint->Source.SourceManage.threshold_enable==1)
		 {
			 uint32_t last;
			 Mem_copy(&last,pRxMsg->TransportMsgData.Data,pRxMsg->TransportMsgData.DataSize);
			 if(last>pTableUint->Source.SourceManage.upper_limit)
				 last=THRESHOLD_UP_STATE;
			 else if(last<pTableUint->Source.SourceManage.lower_limit)
				 last=THRESHOLD_LOW_STATE;
			 else
				 last=THRESHOLD_RANGE_STATE;
			 pTableUint->Source.SourceManage.last_threshold=last;
		 } 
  }
  if(sIndexTableTask.Receive_CallBack!=NULL)
		(*sIndexTableTask.Receive_CallBack)(&pTableUint->Source.SourceData);
}
/*************************************************************
函数：indextable_synctask
功能：资源表同步任务，内部调用
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void mIndexTable_SyncTaskRun(void)
{
	if(mIndexTable.head==NULL)
		return;
	if(mIndexTableTask.now==NULL)
	  mIndexTableTask.now=mIndexTable.head;
	
	if(mIndexTableTask.now->Source.SourceManage.connectflag==1)//判断连接状态
	{	
		if(mIndexTableTask.now->Source.SourceManage.type!=RO)
		{
			if(sIndexTableTask.now->Source.SourceManage.star_tx)//用于支持主动启动发送
			{
				if(IndexTable_SendMsg(&sIndexTableTask.now->Source,FUNCID_CYCLETRIGGER))
				{
					sIndexTableTask.now->Source.SourceManage.star_tx=0;
					if(sIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
					 (*sIndexTableTask.Trigger_CallBack)(&sIndexTableTask.now->Source.SourceData);
				}
			}
			if(mIndexTableTask.now->Source.SourceManage.cycle_enable)
			{
				if(mIndexTableTask.now->Source.SourceManage.timeoverflag==0x01)
				{
					if(IndexTable_SendMsg(&mIndexTableTask.now->Source,FUNCID_CYCLETRIGGER))
					{
					 mIndexTableTask.now->Source.SourceManage.timeoverflag=0;
					 mIndexTableTask.now->Source.SourceManage.cycleinit=1;
					 if(mIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
						 (*mIndexTableTask.Trigger_CallBack)(&mIndexTableTask.now->Source.SourceData);
					}
				}
			}
			
			if(mIndexTableTask.now->Source.SourceManage.state_enable)
			{
				uint32_t Data=0;
				Mem_copy(&Data,mIndexTableTask.now->Source.SourceData.data,mIndexTableTask.now->Source.SourceData.datalen);
				if((mIndexTableTask.now->Source.SourceManage.last_state!=Data)
					||(mIndexTableTask.now->Source.SourceManage.stateinit==0))//只读数据主动进行初始化
				{
					if(IndexTable_SendMsg(&mIndexTableTask.now->Source,FUNCID_STATETRIGGER))//发送成功
					{
					 mIndexTableTask.now->Source.SourceManage.stateinit=1;
					 mIndexTableTask.now->Source.SourceManage.last_state=Data;
					 if(mIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
						 (*mIndexTableTask.Trigger_CallBack)(&mIndexTableTask.now->Source.SourceData);
					}
				}
			}
			else if(mIndexTableTask.now->Source.SourceManage.threshold_enable)
			{
				uint8_t  state=0;
				uint32_t Data=0;
				Mem_copy(&Data,mIndexTableTask.now->Source.SourceData.data,mIndexTableTask.now->Source.SourceData.datalen);
				if(Data<mIndexTableTask.now->Source.SourceManage.lower_limit)
					state=THRESHOLD_LOW_STATE;
				else if(Data>mIndexTableTask.now->Source.SourceManage.upper_limit)
					state=THRESHOLD_UP_STATE;
				else
					state=THRESHOLD_RANGE_STATE;
				if((mIndexTableTask.now->Source.SourceManage.last_threshold!=state)
					||(mIndexTableTask.now->Source.SourceManage.thresholdinit==0))
				{
					if(IndexTable_SendMsg(&mIndexTableTask.now->Source,FUNCID_THRESTRIGGER))
					{
					 mIndexTableTask.now->Source.SourceManage.thresholdinit=1;
					 mIndexTableTask.now->Source.SourceManage.last_threshold=state;
					 if(mIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
						 (*mIndexTableTask.Trigger_CallBack)(&mIndexTableTask.now->Source.SourceData);
					}
				}
			}
    }
  }
	mIndexTableTask.now=mIndexTableTask.now->next;
}

/*************************************************************
函数：indextable_synctask
功能：资源表同步任务，内部调用
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void sIndexTable_SyncTaskRun(void)
{
	if(sIndexTable.head==NULL)
		return;
	if(sIndexTableTask.now==NULL)
	  sIndexTableTask.now=sIndexTable.head;
	
	if(sIndexTableTask.now->Source.SourceManage.connectflag==1)//判断连接状态
	{	
		if(sIndexTableTask.now->Source.SourceManage.star_tx)
		{
			if(IndexTable_SendMsg(&sIndexTableTask.now->Source,FUNCID_CYCLETRIGGER))
		  {
			  sIndexTableTask.now->Source.SourceManage.star_tx=0;
				if(sIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
				 (*sIndexTableTask.Trigger_CallBack)(&sIndexTableTask.now->Source.SourceData);
			}
		}
		if(sIndexTableTask.now->Source.SourceManage.cycle_enable)
		{
			if(sIndexTableTask.now->Source.SourceManage.timeoverflag==0x01)
			{
				if(IndexTable_SendMsg(&sIndexTableTask.now->Source,FUNCID_CYCLETRIGGER))
				{
				 sIndexTableTask.now->Source.SourceManage.timeoverflag=0;
				 sIndexTableTask.now->Source.SourceManage.cycleinit=1;
				 if(sIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
					 (*sIndexTableTask.Trigger_CallBack)(&sIndexTableTask.now->Source.SourceData);
				}
			}
		}
		//字节数长度大于4不能实现状态同步和阈值同步
		if(sIndexTableTask.now->Source.SourceData.datalen<5)
		{
			if(sIndexTableTask.now->Source.SourceManage.state_enable)
			{
				uint32_t Data=0;
				Mem_copy(&Data,sIndexTableTask.now->Source.SourceData.data,sIndexTableTask.now->Source.SourceData.datalen);
				if((sIndexTableTask.now->Source.SourceManage.last_state!=Data)
					||(sIndexTableTask.now->Source.SourceManage.stateinit==0))//只读数据主动进行初始化
				{
					if(IndexTable_SendMsg(&sIndexTableTask.now->Source,FUNCID_STATETRIGGER))//发送成功
					{
					 sIndexTableTask.now->Source.SourceManage.stateinit=1;
					 sIndexTableTask.now->Source.SourceManage.last_state=Data;
					 if(sIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
						 (*sIndexTableTask.Trigger_CallBack)(&sIndexTableTask.now->Source.SourceData);
					}
				}
			}
			if(sIndexTableTask.now->Source.SourceManage.threshold_enable)
			{
				uint8_t  state=0;
				uint32_t Data=0;
				Mem_copy(&Data,sIndexTableTask.now->Source.SourceData.data,sIndexTableTask.now->Source.SourceData.datalen);
				if(Data<sIndexTableTask.now->Source.SourceManage.lower_limit)
					state=THRESHOLD_LOW_STATE;
				else if(Data>sIndexTableTask.now->Source.SourceManage.upper_limit)
					state=THRESHOLD_UP_STATE;
				else
					state=THRESHOLD_RANGE_STATE;
				if((sIndexTableTask.now->Source.SourceManage.last_threshold!=state)
					||(sIndexTableTask.now->Source.SourceManage.thresholdinit==0))
				{
					if(IndexTable_SendMsg(&sIndexTableTask.now->Source,FUNCID_THRESTRIGGER))
					{
					 sIndexTableTask.now->Source.SourceManage.thresholdinit=1;
					 sIndexTableTask.now->Source.SourceManage.last_threshold=state;
					 if(sIndexTableTask.Trigger_CallBack!=NULL)//调用回调函数
						 (*sIndexTableTask.Trigger_CallBack)(&sIndexTableTask.now->Source.SourceData);
					}
				}
			}
	  }
  }
	sIndexTableTask.now=sIndexTableTask.now->next;
}

/*************************************************************
函数：sIndexTable_TimeTask
功能：主站资源表定时器任务，循环调用
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void sIndexTable_CycTimeTask(uint8_t timenum)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=sIndexTable.head;
	while(pTableUint)
	{
		if(pTableUint->Source.SourceManage.connectflag==1)
		{
			if(pTableUint->Source.SourceManage.timeoverflag==0x00&&pTableUint->Source.SourceManage.cycle_enable==1)
			{
				pTableUint->Source.SourceManage.timecount++;
				if(pTableUint->Source.SourceManage.timecount==pTableUint->Source.SourceManage.time)
				{
					pTableUint->Source.SourceManage.timecount=0;
					pTableUint->Source.SourceManage.timeoverflag=1;
				}
			}
		}
		pTableUint=pTableUint->next;
	}
}

/*************************************************************
函数：mIndexTable_CycTimeTask
功能：主站资源表定时器任务，循环调用
参数：pLinkManage 节点连接状态
返回：
*************************************************************/
void mIndexTable_CycTimeTask(uint8_t timenum)
{
	IndexTableUintTypeDef *pTableUint;
	pTableUint=mIndexTable.head;
	while(pTableUint)
	{
		if(pTableUint->Source.SourceManage.connectflag==1)
		{
			if(pTableUint->Source.SourceManage.timeoverflag==0x00&&pTableUint->Source.SourceManage.cycle_enable==1)
			{
				pTableUint->Source.SourceManage.timecount++;
				if(pTableUint->Source.SourceManage.timecount==pTableUint->Source.SourceManage.time)
				{
					pTableUint->Source.SourceManage.timecount=0;
					pTableUint->Source.SourceManage.timeoverflag=1;
				}
			}
		}
		pTableUint=pTableUint->next;
	}
}

void sIndexTable_Init(void)
{
	TimeTaskTypeDef TimeTask;
	sIndexTable.head=NULL;
	sIndexTable.tail=NULL;
	sIndexTable.tablesize=0;
	sIndexTable.maxsize=S_INDEXTABLE_MAX;
	sIndexTableTask.now=NULL;
	sIndexTableTask.Receive_CallBack=NULL;
	sIndexTableTask.Trigger_CallBack=NULL;
	
	TimeTask.callback=1;                                  //定时器设置
	TimeTask.enable=0x01;
	TimeTask.time_value=1;                 //10ms
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=sIndexTable_CycTimeTask;
	TimeTask_Add(S_INDEXTABLE_TIMENUM,&TimeTask);
}

void mIndexTable_Init(void)
{
	TimeTaskTypeDef TimeTask;
	mIndexTable.head=NULL;
	mIndexTable.tail=NULL;
	mIndexTable.tablesize=0;
	mIndexTable.maxsize=M_INDEXTABLE_MAX;
	mIndexTableTask.now=NULL;
	mIndexTableTask.Receive_CallBack=NULL;
	mIndexTableTask.Trigger_CallBack=NULL;
	
	TimeTask.callback=1;                                  //定时器设置
	TimeTask.enable=0x01;
	TimeTask.time_value=1;                 //10ms
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=mIndexTable_CycTimeTask;
	TimeTask_Add(M_INDEXTABLE_TIMENUM,&TimeTask);
}
