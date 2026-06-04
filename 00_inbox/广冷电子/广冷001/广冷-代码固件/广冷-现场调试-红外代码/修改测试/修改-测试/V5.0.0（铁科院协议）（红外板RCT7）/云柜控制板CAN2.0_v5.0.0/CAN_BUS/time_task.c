/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN总线定时器任务
*	文件名称 : time_task.c
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
#include "time_task.h"

TimeTask_LinkesListTypeDef TimeTask_LinkedList; //创建链表



void TimeTask_Init(void)
{
	TimeTask_LinkedList.head=0;
	TimeTask_LinkedList.tail=0;
	TimeTask_LinkedList.linkdelist_len=0;
}

void TimeTask_TaskInit(TimeTaskTypeDef *pTimeTask)
{
	pTimeTask->count_vaule=0;
	pTimeTask->overflow=0;
}
/*************************************************************
函数：TimeTask_TraverseBlockNum
功能：查找链表中的任务块
参数：blocknum 任务块编号
返回：NULL                          链表中无相应任务块
      TimeTask_TaskBlockTypeDef     对应任务块地址
*************************************************************/
TimeTask_TaskBlockTypeDef *TimeTask_TraverseBlockNum(uint8_t blocknum) //获取对应任务块的地址
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	if(TimeTask_LinkedList.head==NULL)             //链表中无数据
		return NULL;
	pTimeTask_TaskBlock=TimeTask_LinkedList.head;
	while((pTimeTask_TaskBlock->blocknum!=blocknum)&&(pTimeTask_TaskBlock!=NULL))
	{
		pTimeTask_TaskBlock=pTimeTask_TaskBlock->next;
	}
	if(pTimeTask_TaskBlock==NULL)                                         //无对应任务块
		pTimeTask_TaskBlock=NULL;
	else if(pTimeTask_TaskBlock->blocknum==blocknum)
    return pTimeTask_TaskBlock;
	return pTimeTask_TaskBlock;
}

/*************************************************************
函数：TimeTask_AddLinkedList
功能：向链表中增加定时器任务块
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表空间满
      0x01     队列中存在相同任务号
      0x02     内存分配失败
      0xFF     增加成功
*************************************************************/
uint8_t TimeTask_AddLinkedList(uint8_t blocknum,TimeTaskTypeDef *pTimeTask)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	if(TimeTask_LinkedList.linkdelist_len==TIMETASK_TASKMAXSIZE)
		return 0x00;                                                        //空间满
	if(TimeTask_TraverseBlockNum(blocknum)!=NULL)
		return 0x01;                                                        //队列中已有相同任务号
  pTimeTask_TaskBlock=Mem_malloc(sizeof(TimeTask_TaskBlockTypeDef));
	if(pTimeTask_TaskBlock==NULL)
		return 0x02;                              //创建失败
	
	Mem_copy(&pTimeTask_TaskBlock->TimeTask,pTimeTask,sizeof(TimeTaskTypeDef));
	TimeTask_TaskInit(&pTimeTask_TaskBlock->TimeTask);
	if(TimeTask_LinkedList.head==NULL)          //链表为空
	{
		pTimeTask_TaskBlock->next=0;
		pTimeTask_TaskBlock->prior=0;
		pTimeTask_TaskBlock->blocknum=blocknum;
		TimeTask_LinkedList.head=pTimeTask_TaskBlock;
		TimeTask_LinkedList.tail=pTimeTask_TaskBlock;
		TimeTask_LinkedList.linkdelist_len++;
	}
	else
	{
		pTimeTask_TaskBlock->blocknum=blocknum;
		pTimeTask_TaskBlock->next=NULL;
		TimeTask_LinkedList.tail->next=pTimeTask_TaskBlock;
		pTimeTask_TaskBlock->prior=TimeTask_LinkedList.tail;
		TimeTask_LinkedList.tail=pTimeTask_TaskBlock;
		TimeTask_LinkedList.linkdelist_len++;
	}
	return 0xFF;                                //创建成功
}

/*************************************************************
函数：TimeTask_RemoveLinkedList
功能：删除定时器任务块
参数：blocknum 任务块编号
      TimeTask 定时器任务参数
返回：0x00     链表中无相应任务块
      0xFF     删除成功
*************************************************************/
uint8_t TimeTask_RemoveLinkedList(uint8_t blocknum)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_TraverseBlockNum(blocknum);
	if(pTimeTask_TaskBlock==NULL)             //链表中无数据
		return 0x00;
	if((TimeTask_LinkedList.linkdelist_len==1)&&(TimeTask_LinkedList.head==TimeTask_LinkedList.tail))//链表中只存在一个节点，头尾相同
	{ 
		TimeTask_LinkedList.tail=0;
		TimeTask_LinkedList.head=0;
	}
	else if(pTimeTask_TaskBlock->next==NULL)
	{
		TimeTask_LinkedList.tail=pTimeTask_TaskBlock->prior;
		TimeTask_LinkedList.tail->next=0;
	}
	else if(pTimeTask_TaskBlock->prior==NULL)
	{
		TimeTask_LinkedList.head=pTimeTask_TaskBlock->next;
		TimeTask_LinkedList.head->prior=0;
	}
	else 
	{
		pTimeTask_TaskBlock->prior->next=pTimeTask_TaskBlock->next;
		pTimeTask_TaskBlock->next->prior=pTimeTask_TaskBlock->prior;	
	}
	TimeTask_LinkedList.linkdelist_len--;
  Mem_free(pTimeTask_TaskBlock);
	return 0xFF;  //删除成功
}

/*************************************************************
函数：TimeTask_RevampLinkedList
功能：修改定时器任务块参数
参数：无
返回：无
*************************************************************/
uint8_t TimeTask_RevampLinkedList(uint8_t blocknum,TimeTaskTypeDef *pTimeTask)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_TraverseBlockNum(blocknum);
	if(pTimeTask_TaskBlock==NULL)             //链表中无数据
	  return 0x00;
	Mem_copy(&pTimeTask_TaskBlock->TimeTask,pTimeTask,sizeof(TimeTaskTypeDef));
	return 0xFF;
}
	
/*************************************************************
函数：TimeTask_TaskRun
功能：定时器运行函数，定时调用该函数驱动定时器运作
参数：无
返回：无
*************************************************************/
void TimeTask_TaskRun(void)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_LinkedList.head;
	if(pTimeTask_TaskBlock==NULL)
		return;
	while(pTimeTask_TaskBlock)
	{
		if((pTimeTask_TaskBlock->TimeTask.count_vaule<pTimeTask_TaskBlock->TimeTask.time_value)&&(pTimeTask_TaskBlock->TimeTask.enable==0x01))
		  pTimeTask_TaskBlock->TimeTask.count_vaule++;
		if(pTimeTask_TaskBlock->TimeTask.count_vaule==pTimeTask_TaskBlock->TimeTask.time_value)
		{
			switch(pTimeTask_TaskBlock->TimeTask.time_mode)
			{
				case 0x00:
					pTimeTask_TaskBlock->TimeTask.count_vaule=0;
					pTimeTask_TaskBlock->TimeTask.overflow=1;
					if((pTimeTask_TaskBlock->TimeTask.TimeTack_CallBack!=NULL)&&(pTimeTask_TaskBlock->TimeTask.callback==1))
						(*pTimeTask_TaskBlock->TimeTask.TimeTack_CallBack)(pTimeTask_TaskBlock->blocknum);                                                //调用回调函数
					break;
				case 0x01:
					pTimeTask_TaskBlock->TimeTask.overflow=1;
				  if((pTimeTask_TaskBlock->TimeTask.TimeTack_CallBack!=NULL)&&(pTimeTask_TaskBlock->TimeTask.callback==1))
						(*pTimeTask_TaskBlock->TimeTask.TimeTack_CallBack)(pTimeTask_TaskBlock->blocknum);
					break;
			}
		}
		pTimeTask_TaskBlock=pTimeTask_TaskBlock->next;
	}
}
/*以下为定时器外部控制接口*/

/*************************************************************
函数：TimeTask_ReadOverflowFlag
功能：获取指定定时器溢出标志位
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0x01        定时器未溢出
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_Add(uint8_t timetasknum,TimeTaskTypeDef *pTimeTask)
{
	uint8_t return_state;
  return_state=TimeTask_AddLinkedList(timetasknum,pTimeTask);
	return return_state;
}
/*************************************************************
函数：TimeTask_Remove
功能：删除指定定时器
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_Remove(uint8_t timetasknum)
{
	uint8_t return_state;
  return_state=TimeTask_RemoveLinkedList(timetasknum);
	return return_state;
}

/*************************************************************
函数：TimeTask_Revamp
功能：删除指定定时器
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_Revamp(uint8_t timetasknum,TimeTaskTypeDef *pTimeTask)
{
	uint8_t return_state;
	return_state=TimeTask_RevampLinkedList(timetasknum,pTimeTask);
	return return_state;
}

/*************************************************************
函数：TimeTask_Enable
功能：使能定时器
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_Cmd(uint8_t timetasknum,uint8_t enable)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_TraverseBlockNum(timetasknum);
	if(pTimeTask_TaskBlock==NULL)
		return 0x00;
	pTimeTask_TaskBlock->TimeTask.enable=enable;     //清楚定时器标志位
	return 0xFF;
}
/*************************************************************
函数：TimeTask_ReadOverflowFlag
功能：获取指定定时器溢出标志位
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0x01        定时器未溢出
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_ReadOverflowFlag(uint8_t timetasknum)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_TraverseBlockNum(timetasknum);
	if(pTimeTask_TaskBlock==NULL)
		return 0x00;
	if(pTimeTask_TaskBlock->TimeTask.overflow==0x01)
	{
		pTimeTask_TaskBlock->TimeTask.overflow=0;     //清楚定时器标志位
		return 0xFF;
	}
	return 0x01;
}


/*************************************************************
函数：TimeTask_ReadOverflowFlag
功能：获取指定定时器溢出标志位
参数：timetasknum 定时器号
返回：0x00        无对应定时器
      0x01        定时器未溢出
      0xFF        定时器溢出
*************************************************************/
uint8_t TimeTask_RestCount(uint8_t timetasknum)
{
	TimeTask_TaskBlockTypeDef *pTimeTask_TaskBlock;
	pTimeTask_TaskBlock=TimeTask_TraverseBlockNum(timetasknum);
	if(pTimeTask_TaskBlock==NULL)
		return 0x00;
  pTimeTask_TaskBlock->TimeTask.count_vaule=0;     //清楚定时器标志位
	return 0xFF;
}
