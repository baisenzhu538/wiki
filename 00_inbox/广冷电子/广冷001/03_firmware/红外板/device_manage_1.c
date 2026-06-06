/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN主节点设备管理模块
*	文件名称 : device_manage.c
*	版    本 : V1.0
*	说    明 : 1.实现CAN驱动的参数设置
*            2.实现CAN总线网络节点的管理
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "device_manage.h"

DeviceMarkTypeDef DeviceMarkTable[DEVICE_MAXNUM];
DeviceMarkTypeDef ControllerMarkTable[CONTROLLER_MAXNUM];

DeviceManageTableTypeDef DeviceManageTable;
void (*pDeviceManage_ConnectCallBack)(NodeDiscernTypeDef*,DeviceLinkManageTypeDef*)=NULL;


uint8_t DeviceManage_AssignDeviceId(DeviceMarkTypeDef *pDeviceMark)
{
	uint16_t i;
	
		if(pDeviceMark->can_nodeid<NODE_DEVICEADDR_END)
		{
			for(i=0;i<DEVICE_MAXNUM;i++)
			{
				if((DeviceMarkTable[i].devicenum==pDeviceMark->devicenum)
					&&(DeviceMarkTable[i].devicetype==pDeviceMark->devicetype))//检测是否有过地址分配记录
				{
					return (i+NODE_DEVICEADDR_STAR);
				}
			}
		}
	
	if(pDeviceMark->can_nodeid>(NODE_DEVICEADDR_STAR-1)&&pDeviceMark->can_nodeid!=0xFF)
	{
		if((*((uint32_t*)&(DeviceMarkTable[pDeviceMark->can_nodeid-NODE_DEVICEADDR_STAR])))==0x00000000) //检测地址是否被占用                                      //设备未在主站注册过，检测设备ID是否已经被占用
		{
			Mem_copy(&DeviceMarkTable[pDeviceMark->can_nodeid-NODE_DEVICEADDR_STAR],pDeviceMark,sizeof(DeviceMarkTypeDef));//占用该地址
			return pDeviceMark->can_nodeid;
		}
	}
	for(i=0;i<DEVICE_MAXNUM;i++)//重新分配
	{
		if(*((uint32_t*)&(DeviceMarkTable[i]))==0x00000000)
		{
			Mem_copy(&DeviceMarkTable[i],pDeviceMark,sizeof(DeviceMarkTypeDef));//占用该地址
			DeviceMarkTable[i].can_nodeid=i+NODE_DEVICEADDR_STAR;
			return DeviceMarkTable[i].can_nodeid;
		}
	}
	return 0x00;//分配失败
}

//获取控制器ID
uint8_t DeviceManage_AssignControllerId(DeviceMarkTypeDef *pDeviceMark)
{
	uint16_t i;
	
		if(pDeviceMark->can_nodeid<NODE_DEVICEADDR_STAR)
		{
			for(i=1;i<DEVICE_MAXNUM;i++)
			{
				if((ControllerMarkTable[i].devicenum==pDeviceMark->devicenum)
					&&(ControllerMarkTable[i].devicetype==pDeviceMark->devicetype))//检测是否有过地址分配记录
				{
					return (i);
				}
			}
		}
	
	if(pDeviceMark->can_nodeid<NODE_DEVICEADDR_STAR&&pDeviceMark->can_nodeid!=0x00)
	{
		if((*((uint32_t*)&(ControllerMarkTable[pDeviceMark->can_nodeid])))==0x00000000) //检测地址是否被占用                                      //设备未在主站注册过，检测设备ID是否已经被占用
		{
			Mem_copy(&ControllerMarkTable[pDeviceMark->can_nodeid],pDeviceMark,sizeof(DeviceMarkTypeDef));//占用该地址
			return pDeviceMark->can_nodeid;
		}
	}
	for(i=1;i<CONTROLLER_MAXNUM;i++)//重新分配
	{
		if(*((uint32_t*)&(ControllerMarkTable[i]))==0x00000000)
		{
			Mem_copy(&ControllerMarkTable[i],pDeviceMark,sizeof(DeviceMarkTypeDef));//占用该地址
			ControllerMarkTable[i].can_nodeid=i;
			return DeviceMarkTable[i].can_nodeid;
		}
	}
	return 0x00;//分配失败
}

void DeviceManage_SetConnectCallBack(void(*p)(NodeDiscernTypeDef*,DeviceLinkManageTypeDef*))
{
	pDeviceManage_ConnectCallBack=p;
}
uint8_t DeviceManage_ReadPort(uint8_t nodeid,uint8_t sounrcid,void *data)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAckTask;
	TransportCanMsgTypeDef MsgBuff;
	AskTaskTypeDef        AckTask;
	uint8_t               state=0;
	pDeviceManage=DeviceManage_GetDeviceManage(nodeid);
	if(pDeviceManage==NULL)
		return 0x00;         //节点不存在
	if(pDeviceManage->LinkManage.connectflag==0x00)
		return 0x01;         //节点未连接
	pAckTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,sounrcid,FUNCID_READPORT);
	if(pAckTask==NULL)
	{
		MsgBuff.TransportMsgFilter.DestMacID=nodeid;
		MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo_GetNodeId();//MasterManage.LinkManage.LocalMACID;
		MsgBuff.TransportMsgFilter.SourceID =sounrcid;
		MsgBuff.TransportMsgFilter.FuncID   =FUNCID_READPORT;
		MsgBuff.TransportMsgFilter.Ack      =0x00;//报文需响应
		MsgBuff.TransportMsgManage.ErrID    =0x00;
		MsgBuff.TransportMsgData.DataSize   =0x00;
		MsgBuff.TransportMsgData.Data       =NULL;
		if(TransportLayer_TxMsg(&MsgBuff)==0xFF)
    {
			AckTask.sourceid=sounrcid;
			AckTask.funcid=FUNCID_READPORT;
			AckTask.askfuncid=FUNCID_NONASK;
			AckTask.lifeover=0;
			AckTask.lifeover=0; 
			DeviceManage_AddAskTask(&pDeviceManage->AskTaskTable,&AckTask);
			return 0x03;
		}
		return 0x04;
	}
	else
	{
		switch(pAckTask->askfuncid)
		{
			case FUNCID_NONASK:
				state=0x05;
				break;
			case FUNCID_READPORT:
				Mem_copy(data,pAckTask->devicedata.Data,pAckTask->devicedata.DataSize);
				Mem_free(pAckTask->devicedata.Data);//释放内存
			  DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
			  state=0xFF;
				break;//数据读取成功
			case FUNCID_EXCEPTIONS:
				DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
			  state=0xEE;
				break;//读取失败
		}
	}
	return state;
}

uint8_t DeviceManage_WritePort(uint8_t nodeid,uint8_t sounrcid,void *data,uint8_t datasize)
{
	DeviceManageTypeDef *pDeviceManage;
	AskTaskTypeDef      *pAckTask;
	TransportCanMsgTypeDef MsgBuff;
	AskTaskTypeDef        AckTask;
	uint8_t               state=0x00;
	pDeviceManage=DeviceManage_GetDeviceManage(nodeid);
	if(pDeviceManage==NULL)
		return 0x00;         //节点不存在
	if(pDeviceManage->LinkManage.connectflag==0x00)
		return 0x01;         //节点未连接
	pAckTask=DeviceManage_GetAskTask(&pDeviceManage->AskTaskTable,sounrcid,FUNCID_WRITEPORT);
	if(pAckTask==NULL)
	{
		MsgBuff.TransportMsgFilter.DestMacID=nodeid;
		MsgBuff.TransportMsgFilter.SrcMacID =NodeInfo_GetNodeId();//MasterManage.LinkManage.LocalMACID;
		MsgBuff.TransportMsgFilter.SourceID =sounrcid;
		MsgBuff.TransportMsgFilter.FuncID   =FUNCID_WRITEPORT;
		MsgBuff.TransportMsgFilter.Ack      =0x00;//报文需响应
		MsgBuff.TransportMsgManage.ErrID    =0x00;
		MsgBuff.TransportMsgData.DataSize   =datasize;
		MsgBuff.TransportMsgData.Data       =Mem_malloc(datasize);
		if(MsgBuff.TransportMsgData.Data==NULL)
			return 0x02;                          //内存空间不足
		Mem_copy(MsgBuff.TransportMsgData.Data,data,datasize);
		if(TransportLayer_TxMsg(&MsgBuff)==0xFF)
    {
			AckTask.sourceid=sounrcid;
			AckTask.funcid=FUNCID_WRITEPORT;
			AckTask.askfuncid=FUNCID_NONASK;
			AckTask.lifeover=0;
			AckTask.lifeover=0; 
			DeviceManage_AddAskTask(&pDeviceManage->AskTaskTable,&AckTask);
			return 0x03;//发送数据成功
		}
		else
		{
			if(MsgBuff.TransportMsgData.DataSize!=0)
				Mem_free(MsgBuff.TransportMsgData.Data);
			return 0x04;//发送不成功
		}
		
	}
	else
	{
		switch(pAckTask->askfuncid)
		{
			case FUNCID_NONASK:
				state=0x05;
				break;
			case FUNCID_WRITEPORT:
			  DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
			  state=0xFF;
				break;//数据写完成
			case FUNCID_EXCEPTIONS:
				DeviceManage_RemoveAskTask(&pDeviceManage->AskTaskTable,pAckTask);
			  state=0xEE;
				break;//读取失败
		}
	}
	return state;
}

void DeviceManage_AskTableInit(AskTaskTableTypeDef *pAskTable)
{
  pAskTable->head=NULL;
	pAskTable->tail=NULL;
	pAskTable->tablelen=0;
}
void DeviceManage_LinkManageInit(DeviceLinkManageTypeDef *pLinkManage)
{
  pLinkManage->connectflag=0x00;
	pLinkManage->heartflag  =0x01;
	pLinkManage->heartover    =0x00;
	pLinkManage->hearttime    =0x00;
}

AskTaskTableTypeDef *DeviceManage_GetAskTable(uint8_t nodeid)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.can_nodeid==nodeid)
			return (&pManageBlock->DeviceManage.AskTaskTable);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}

AskTaskTypeDef *DeviceManage_GetAskTask(AskTaskTableTypeDef *pAskTable,uint8_t sourceid,uint8_t Funcid)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	if(pAskTable->head==NULL)
		return NULL;
	pAskTaskBlock=pAskTable->head;
	while(pAskTaskBlock)
	{
		if(pAskTaskBlock->DeviceAskTask.sourceid==sourceid&&pAskTaskBlock->DeviceAskTask.funcid==Funcid)
			return &pAskTaskBlock->DeviceAskTask;
		pAskTaskBlock=pAskTaskBlock->next;
	}
	return NULL;
}

/*************************************************************
函数：DeviceManage_GetAskTaskBlock
功能：获取设备响应任务
参数：pAskTable 设备响应任务表
      sourceid  资源节点地址
      Funcid    操作功能码
返回：NULL      任务不存在
      其他      任务块地址
*************************************************************/
AskTaskBlockTypeDef *DeviceManage_GetAskTaskBlock(AskTaskTableTypeDef *pAskTable,uint8_t sourceid,uint8_t Funcid)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	if(pAskTable->head==NULL)
		return NULL;
	pAskTaskBlock=pAskTable->head;
	while(pAskTaskBlock)
	{
		if(pAskTaskBlock->DeviceAskTask.sourceid==sourceid&&pAskTaskBlock->DeviceAskTask.funcid==Funcid)
			return pAskTaskBlock;
		pAskTaskBlock=pAskTaskBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_AddAskTask
功能：添加设备响应任务
参数：pAskTable 设备响应任务表
      pAskTask  设备响应任务
返回：0x00      任务不存在
      0xFF      删除成功
*************************************************************/
uint8_t DeviceManage_AddAskTask(AskTaskTableTypeDef *pAskTable,AskTaskTypeDef *pAskTask)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	if(pAskTable->tablelen==ASKTASK_MAXNUM)//链表中无空间
		return 0x00;
	if(DeviceManage_GetAskTask(pAskTable,pAskTask->sourceid,pAskTask->funcid)!=NULL)
		return 0x01;
	pAskTaskBlock=Mem_malloc(sizeof(AskTaskBlockTypeDef));
	if(pAskTaskBlock==NULL) //分配空间不足
		return 0x02;
	Mem_copy(&pAskTaskBlock->DeviceAskTask,pAskTask,sizeof(AskTaskTypeDef));
	if(pAskTable->head==NULL)//链表中无响应任务
	{
		pAskTaskBlock->next=NULL;
		pAskTaskBlock->prior =NULL;
		pAskTable->head=pAskTaskBlock;
		pAskTable->tail=pAskTaskBlock;	
	}
	else
	{
		pAskTaskBlock->next=NULL;
		pAskTable->tail->next=pAskTaskBlock;
		pAskTaskBlock->prior=pAskTable->tail;
		pAskTable->tail=pAskTaskBlock;
	}
	pAskTable->tablelen++;
	return 0xFF;
}
/*************************************************************
函数：DeviceManage_RemoveAskTask
功能：删除设备响应任务
参数：pAskTable 设备响应任务表
      pAskTask  设备响应任务
返回：0x00      任务不存在
      0xFF      删除成功
*************************************************************/
uint8_t DeviceManage_RemoveAskTask(AskTaskTableTypeDef *pAskTable,AskTaskTypeDef *pAskTask)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	pAskTaskBlock=DeviceManage_GetAskTaskBlock(pAskTable,pAskTask->sourceid,pAskTask->funcid);
	if(pAskTaskBlock==NULL)
		return 0x00;
	if((pAskTable->tablelen==0x01)&&(pAskTable->head==pAskTable->tail))//只有一个节点
	{
		pAskTable->head=NULL;
		pAskTable->tail=NULL;
	}
	else if(pAskTaskBlock->next==NULL)//链表最后一个节点
	{
		pAskTable->tail=pAskTaskBlock->prior;
		pAskTable->tail->next=NULL;
	}
	else if(pAskTaskBlock->prior==NULL)//链表第一个节点
	{
		pAskTable->head=pAskTaskBlock->next;
		pAskTable->head->prior=NULL;
	}
	else
	{
		pAskTaskBlock->next->prior=pAskTaskBlock->prior;
		pAskTaskBlock->prior->next=pAskTaskBlock->next;
	}
  pAskTable->tablelen--;
	Mem_free(pAskTaskBlock);
	return 0xFF;
}
/*************************************************************
函数：DeviceManage_GetLinkManage
功能：获取设备连接管理信息
参数：nodeid   设备mac 地址
返回：设备连接管理信息地址
*************************************************************/
DeviceLinkManageTypeDef *DeviceManage_GetLinkManage(uint8_t nodeid)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==0)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.can_nodeid==nodeid)
			return (&pManageBlock->DeviceManage.LinkManage);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetLinkManage2
功能：获取设备连接管理信息
参数：devicenum   设备编号
      devicetype  设备类型
返回：设备连接管理信息地址
*************************************************************/
DeviceLinkManageTypeDef *DeviceManage_GetLinkManage2(uint8_t devicenum,uint16_t devicetype)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==0)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.devicenum ==devicenum&&pManageBlock->DeviceManage.nodefilter.devicetype==devicetype)
			return (&pManageBlock->DeviceManage.LinkManage);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetDeviceBlock
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
DeviceManageBlockTypeDef *DeviceManage_GetDeviceBlock(uint8_t nodeid)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.can_nodeid==nodeid)
			return pManageBlock;
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetDeviceBlock2
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
DeviceManageBlockTypeDef *DeviceManage_GetDeviceBlock2(uint8_t devicenum,uint16_t devicetype)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.devicenum ==devicenum&&pManageBlock->DeviceManage.nodefilter.devicetype==devicetype)
			return pManageBlock;
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetDeviceManage
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
DeviceManageTypeDef *DeviceManage_GetDeviceManage(uint8_t nodeid)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.can_nodeid==nodeid)
			return (&pManageBlock->DeviceManage);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetDeviceManage2
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
DeviceManageTypeDef *DeviceManage_GetDeviceManage2(uint8_t devicenum,uint16_t devicetype)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.devicenum ==devicenum&&pManageBlock->DeviceManage.nodefilter.devicetype==devicetype)
			return (&pManageBlock->DeviceManage);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetDeviceID
功能：获取指定设备ID
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
uint8_t DeviceManage_GetDeviceID(uint8_t devicenum,uint16_t devicetype)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.devicenum ==devicenum&&pManageBlock->DeviceManage.nodefilter.devicetype==devicetype)
			return (pManageBlock->DeviceManage.nodefilter.can_nodeid);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}

/*************************************************************
函数：DeviceManage_GetLinkFlag
功能：获取指定设备连接状态
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
uint8_t DeviceManage_GetLinkFlag(uint8_t devicenum,uint16_t devicetype)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.devicenum ==devicenum&&pManageBlock->DeviceManage.nodefilter.devicetype==devicetype)
			return (pManageBlock->DeviceManage.LinkManage.connectflag);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_GetLinkFlag
功能：获取指定设备连接状态
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
uint8_t DeviceManage_GetLinkFlag2(uint8_t nodeid)
{
	DeviceManageBlockTypeDef *pManageBlock;
	if(DeviceManageTable.head==NULL)
		return NULL;
	pManageBlock=DeviceManageTable.head;
	while(pManageBlock)
	{
		if(pManageBlock->DeviceManage.nodefilter.can_nodeid==nodeid)
			return (pManageBlock->DeviceManage.LinkManage.connectflag);
		pManageBlock=pManageBlock->next;
	}
	return NULL;
}
/*************************************************************
函数：DeviceManage_AddDevice
功能：设置阀值触发任务
参数：SourceID 触发索引地址
      low      阀值下限
      up       阀值上限
返回：
*************************************************************/
uint8_t DeviceManage_AddDevice(NodeDiscernTypeDef *pFilter)
{
	DeviceManageTypeDef *pDeviceManage;
	DeviceManageBlockTypeDef *pDeviceBlock;
	if(DeviceManageTable.tablelen==DEVICEBLOCK_MAXNUM)
		return 0x00;
	pDeviceManage=DeviceManage_GetDeviceManage(pFilter->can_nodeid);
	if(pDeviceManage!=NULL) //已经有相同ID号节点接入
		return 0x01;
	pDeviceBlock=Mem_malloc(sizeof(DeviceManageBlockTypeDef));
	if(pDeviceBlock==NULL)  //创建失败
		return 0x02;
	DeviceManage_AskTableInit(&pDeviceBlock->DeviceManage.AskTaskTable);//初始化节点响应表
	DeviceManage_LinkManageInit(&pDeviceBlock->DeviceManage.LinkManage);//初始化节点连接管理
	Mem_copy(&pDeviceBlock->DeviceManage.nodefilter,pFilter,sizeof(NodeDiscernTypeDef));
	if(DeviceManageTable.head==NULL)
	{
		pDeviceBlock->next=NULL;
		pDeviceBlock->prior=NULL;
		DeviceManageTable.head=pDeviceBlock;
		DeviceManageTable.tail=pDeviceBlock;
		DeviceManageTable.tablelen++;
	}
	else
	{
		pDeviceBlock->next=NULL;
		DeviceManageTable.tail->next=pDeviceBlock;
		pDeviceBlock->prior=DeviceManageTable.tail;
		DeviceManageTable.tail=pDeviceBlock;
		DeviceManageTable.tablelen++;
	}
	return 0xFF;//添加成功
}

uint8_t DeviceManage_RemoveDevice(NodeDiscernTypeDef *pFilter)
{
	DeviceManageBlockTypeDef *pDeviceBlock;
	pDeviceBlock=DeviceManage_GetDeviceBlock(pFilter->can_nodeid);
	if(pDeviceBlock==NULL)           //设备表中无该节点
		return 0x00;
	if((DeviceManageTable.head==DeviceManageTable.tail)&&(DeviceManageTable.tablelen==1))
	{
		DeviceManageTable.head=NULL;
		DeviceManageTable.tail=NULL;	
	}
	else if(pDeviceBlock->next==NULL) //链表中最后一个节点
	{
		DeviceManageTable.tail=pDeviceBlock->prior;
		DeviceManageTable.tail->next=NULL;
	}
	else if(pDeviceBlock->prior==NULL) //链表中第一个节点
	{
		DeviceManageTable.head=pDeviceBlock->next;
		DeviceManageTable.head->prior=NULL;
	}
	else                                //中间节点
	{
		pDeviceBlock->prior->next=pDeviceBlock->next;
		pDeviceBlock->next->prior=pDeviceBlock->prior;
	}
	DeviceManageTable.tablelen--;
	Mem_free(pDeviceBlock);
	return 0xFF;
}

//删除设备节点中所有待响应任务
void DeviceManage_RemoveAllAskTask(AskTaskTableTypeDef *pAskTaskTable)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	AskTaskBlockTypeDef *pAskTaskBlockBuff;
	pAskTaskBlock=pAskTaskTable->head;
	while(pAskTaskBlock)
	{
		pAskTaskBlockBuff=pAskTaskBlock->next;
		if(pAskTaskBlock->DeviceAskTask.devicedata.DataSize!=0)
			Mem_free(pAskTaskBlock->DeviceAskTask.devicedata.Data);
		Mem_free(pAskTaskBlock);
		pAskTaskBlock=pAskTaskBlockBuff;
	}
	pAskTaskTable->head=NULL;
	pAskTaskTable->tail=NULL;
	pAskTaskTable->tablelen=0;
}

//节点响应任务处理
void DeviceManage_AskTimeTask(AskTaskTableTypeDef *pAskTaskTable)
{
	AskTaskBlockTypeDef *pAskTaskBlock;
	AskTaskBlockTypeDef *pAskTaskBlockBuff;
	pAskTaskBlock=pAskTaskTable->head;
	if(pAskTaskBlock==NULL)
		return;
	while(pAskTaskBlock)
	{
		pAskTaskBlockBuff=pAskTaskBlock->next;
		if(pAskTaskBlock->DeviceAskTask.askfuncid!=FUNCID_NONASK)//任务已经响应未取出
		{
			if(pAskTaskBlock->DeviceAskTask.lifetime<ASK_LIFETIME)
			 pAskTaskBlock->DeviceAskTask.lifetime++;
			else                                           //任务响应超时未取出，删除该任务
			{
				if(pAskTaskBlock->DeviceAskTask.devicedata.DataSize!=0)
				 Mem_free(pAskTaskBlock->DeviceAskTask.devicedata.Data);
				DeviceManage_RemoveAskTask(pAskTaskTable,&pAskTaskBlock->DeviceAskTask);//删除该节点
        pAskTaskBlock->DeviceAskTask.lifeover=0x01;
			}
		}
		 pAskTaskBlock=pAskTaskBlockBuff;
	}
}

void DeviceManage_CallBack(NodeDiscernTypeDef *pNodeDiscern,DeviceLinkManageTypeDef* pLinkManage)
{
	if(pDeviceManage_ConnectCallBack!=NULL)
		(*pDeviceManage_ConnectCallBack)(pNodeDiscern,pLinkManage);//断开连接回调函数
	                                                             //删除触发任务连接标志
	mIndexTable_SetConnectFlag(pNodeDiscern->devicetype,pNodeDiscern->devicenum,pNodeDiscern->can_nodeid,pLinkManage->connectflag);
}
//设备管理任务执行函数
void DeviceManage_TimeTaskRun(uint8_t timenum)
{
	DeviceManageBlockTypeDef *pManageBlock;
	DeviceManageBlockTypeDef *pManageBlockBuff;
	pManageBlock=DeviceManageTable.head;
	if(pManageBlock==NULL)
		return;
	while(pManageBlock)
	{
		pManageBlockBuff=pManageBlock->next;
		if(pManageBlock->DeviceManage.LinkManage.heartflag==0x01)
		{
			if(pManageBlock->DeviceManage.LinkManage.hearttime<SLAVEHEART_OVERTIME)
			{
			  pManageBlock->DeviceManage.LinkManage.hearttime++;
				DeviceManage_AskTimeTask(&pManageBlock->DeviceManage.AskTaskTable);//处理节点响应任务
			}
			else                                                                 //心跳超时删除节点设备
			{
				pManageBlock->DeviceManage.LinkManage.heartover =0x01;//超时
				pManageBlock->DeviceManage.LinkManage.connectflag=0x00;
				DeviceManage_CallBack(&pManageBlock->DeviceManage.nodefilter,&pManageBlock->DeviceManage.LinkManage);//回调函数
				DeviceManage_RemoveAllAskTask(&pManageBlock->DeviceManage.AskTaskTable);
				DeviceManage_RemoveDevice(&pManageBlock->DeviceManage.nodefilter); //删除设备节点	
			}
		}	
		pManageBlock=pManageBlockBuff;
	}
}


void DeviceManage_TaskInit(void)
{
	TimeTaskTypeDef TimeTask;
	
	DeviceManageTable.head=NULL;
	DeviceManageTable.tail=NULL;
	DeviceManageTable.tablelen=0;
	
	TimeTask.callback=1;
	TimeTask.enable=0x01;
	TimeTask.time_value=1;                 //10ms
	TimeTask.time_mode=0x00;               //自动复位定时值
	TimeTask.TimeTack_CallBack=DeviceManage_TimeTaskRun;
	TimeTask_Add(DEVICEMANAGE_TASK_TIMENUM,&TimeTask);	
}

