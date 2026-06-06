/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN底层驱动
*	文件名称 : can_drive.c
*	版    本 : V1.0
*	说    明 : 1.实现CAN硬件驱动的参数设置
*            2.实现CAN驱动的数据收发接口
*            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	

#include "can_drive.h"
#include "drive_api.h"

u8 CAN_Mode_Init(u8 tsjw,u8 tbs2,u8 tbs1,u16 brp,u8 mode)
{
	CAN_InitTypeDef CAN_InitStructure;
	
	Can_GPIO_Init();
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_CAN1, ENABLE);//使能CAN1时钟

	CAN_DeInit(CAN1);
  //CAN单元设置
	CAN_InitStructure.CAN_TTCM=DISABLE;						 //非时间触发通信模式  //
	CAN_InitStructure.CAN_ABOM=ENABLE;						 //软件自动离线恢复管理	//
	CAN_InitStructure.CAN_AWUM=DISABLE;						 //睡眠模式通过软件唤醒(清除CAN->MCR的SLEEP位)//
	CAN_InitStructure.CAN_NART=DISABLE;						 //禁止报文自动传送 //
	CAN_InitStructure.CAN_RFLM=DISABLE;						 //报文不锁定,新的覆盖旧的 // 
	CAN_InitStructure.CAN_TXFP=ENABLE;						 //优先级由请求顺序决定 ,中文固件库手册描述错误//
	
	CAN_InitStructure.CAN_Mode= mode;	             //模式设置： mode:0,普通模式;1,回环模式; //
	//设置波特率
	CAN_InitStructure.CAN_SJW=tsjw;				//重新同步跳跃宽度(Tsjw)为tsjw+1个时间单位  CAN_SJW_1tq	 CAN_SJW_2tq CAN_SJW_3tq CAN_SJW_4tq
	CAN_InitStructure.CAN_BS1=tbs1;       //Tbs1=tbs1+1个时间单位CAN_BS1_1tq ~CAN_BS1_16tq
	CAN_InitStructure.CAN_BS2=tbs2;       //Tbs2=tbs2+1个时间单位CAN_BS2_1tq ~	CAN_BS2_8tq
	CAN_InitStructure.CAN_Prescaler=brp;            //分频系数(Fdiv)为brp+1	//
	CAN_Init(CAN1, &CAN_InitStructure);            // 初始化CAN1 

  //Can_FilterSet(Node_Info.MasterMACID,Node_Info.SlaveMACID,0,0);
	
#if CAN_RX0_INT_ENABLE
//	Can_NVIC_Init();//can中断初始化		
#endif
	return 0;
}

/*********************************/
/*函数功能：can相关中断初始化函数*/
/*********************************/
void Can_NVIC_Init()
{
	NVIC_InitTypeDef  NVIC_InitStructure;
	 //FIFO0消息挂号中断//FIFO0满中断//FIFO0溢出中断
	CAN_ITConfig(CAN1,CAN_IT_FMP0|CAN_IT_FF0|CAN_IT_FOV0,ENABLE);//FIFO0消息挂号中断允许.		    
	
	NVIC_InitStructure.NVIC_IRQChannel = USB_LP_CAN1_RX0_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;     // 主优先级为1
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;            // 次优先级为0
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
	//错误中断开启//主动错误中断//被动错误中断//离线中断//
	CAN_ITConfig(CAN1,CAN_IT_ERR|CAN_IT_EWG|CAN_IT_EPV|CAN_IT_BOF,ENABLE);//FIFO0消息挂号中断允许.		    
	
	NVIC_InitStructure.NVIC_IRQChannel = CAN1_SCE_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;     // 主优先级为1
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;            // 次优先级为0
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
	
}

/*********************************/
/*函数功能：canGPIO初始化函数    */
/*********************************/
void Can_GPIO_Init()
{
	GPIO_InitTypeDef GPIO_InitStructure; 
#ifdef CAN_INTERFACE1
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO|RCC_APB2Periph_GPIOA, ENABLE);//使能PORTA时钟	 

	GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_12;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode  = GPIO_Mode_AF_PP;	//复用推挽
	GPIO_Init(GPIOA, &GPIO_InitStructure);		//初始化IO
 
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;//上拉输入
	GPIO_Init(GPIOA, &GPIO_InitStructure);//初始化IO
#endif
#ifdef CAN_INTERFACE2
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_AFIO|RCC_APB2Periph_GPIOB, ENABLE);
	GPIO_PinRemapConfig(GPIO_Remap1_CAN1, ENABLE);
	GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Mode  = GPIO_Mode_AF_PP;	//复用推挽
	GPIO_Init(GPIOB, &GPIO_InitStructure);		//初始化IO
 
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8;
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;//上拉输入
	GPIO_Init(GPIOB, &GPIO_InitStructure);//初始化IO
#endif
}

/***************************/
/*函数功能： 滤波器初值设置*/
/***************************/
void Can_FilterSet(u8 MasteMacID,u8 SlaveMacID,u8 num)
{
	u32 ID;
	CAN_FilterInitTypeDef  CAN_FilterInitStructure;
	
  /*滤波器0初始化，用于过滤接收点对点的普通报文 Star */
	CAN_FilterInitStructure.CAN_FilterNumber=num;	  //过滤器0
	CAN_FilterInitStructure.CAN_FilterMode=CAN_FilterMode_IdMask; 	//掩码模式
	CAN_FilterInitStructure.CAN_FilterScale=CAN_FilterScale_32bit; //32位 
	
	/*修改滤波器初值*/
	ID=0x00000000;
	ID|=MasteMacID<<16;
	ID|=SlaveMacID<<8;
	CAN_FilterInitStructure.CAN_FilterIdHigh=(((u32)ID<<3)&0xffff0000)>>16;////32位ID
	CAN_FilterInitStructure.CAN_FilterIdLow =(((u32)ID<<3)|CAN_ID_EXT|CAN_RTR_DATA)&0xffff;//CAN_RTR_DATA CAN_RTR_REMOTE
	ID=0x00000000;
//	ID|=0xff<<16;
	ID|=0xff<<8;
	CAN_FilterInitStructure.CAN_FilterMaskIdHigh=(((u32)ID<<3)&0xffff0000)>>16;//32位MASK
	CAN_FilterInitStructure.CAN_FilterMaskIdLow =(((u32)ID<<3)|CAN_ID_STD|CAN_RTR_REMOTE)&0xffff;

	CAN_FilterInitStructure.CAN_FilterFIFOAssignment=CAN_Filter_FIFO0;//过滤器0关联到FIFO0
	CAN_FilterInitStructure.CAN_FilterActivation=ENABLE; //激活过滤器0

	CAN_FilterInit(&CAN_FilterInitStructure);//滤波器初始化
	/*滤波器0初始化，用于过滤接收点对点的普通报文 End */

}


//void Can_DriveInit(u8 LocalMacID)
//{
//	CAN_Mode_Init(CAN_SJW_1tq,CAN_BS2_2tq,CAN_BS1_5tq,9,0);//500Kbps
//	Can_FilterSet(0x00,LocalMacID,0x00);       //设置主从机过滤器
//	Can_FilterSet(0x00,0xFF,0x01);             //设置广播报文过滤器
//}

/***************************/
/*函数功能： 错误中断函数***/
/***************************/
void CAN1_SCE_IRQHandler(void)
{
  if(CAN_GetITStatus(CAN1,CAN_IT_EWG)==SET)//错误次数大于96错误中断
	{
   CAN_ClearITPendingBit(CAN1,CAN_IT_EWG);     //清除中断标志
  }
	if(CAN_GetITStatus(CAN1,CAN_IT_EPV)==SET)//错误次数大于128中断，被动错误状态将进入离线状态
	{
	 CAN_ClearITPendingBit(CAN1,CAN_IT_EPV);     //清除中断标志
	}
	if(CAN_GetITStatus(CAN1,CAN_IT_BOF)==SET)//进入离线状态中断
	{
		CAN_ClearITPendingBit(CAN1,CAN_IT_BOF);
	}

}
#if CAN_RX0_INT_ENABLE	//使能RX0中断

/***************************/
/*函数功能： FIFO0中断函数 */
/***************************/			    
void USB_LP_CAN1_RX0_IRQHandler(void)
{
	CanRxMsg RxMessage;
	if(CAN_GetITStatus(CAN1,CAN_IT_FF0)==SET) //FIFO0消息满中断
		{
			CAN_ClearITPendingBit(CAN1,CAN_IT_FF0);
		}
	if(CAN_GetITStatus(CAN1,CAN_IT_FOV0)==SET) //FIFO0消息溢出中断
		{
			CAN_ClearITPendingBit(CAN1,CAN_IT_FOV0);
		}
		
//	if(CAN_GetITStatus(CAN1,CAN_IT_FMP0)==SET) //FIFO0消息挂号中断
//		{
//			CAN_Receive(CAN1, 0, &RxMessage);
//			Can_ReceiveMsg(&RxMessage);
//			CAN_ClearITPendingBit(CAN1,CAN_IT_FMP0);	
//		}
}

#endif

/*************************************************************
函数：Can_GetMailBox
功能：获取CAN邮箱空邮箱号
参数：无
返回：无
*************************************************************/
u8 Can_GetMailBox(CAN_TypeDef* CANx)
{
	uint8_t transmit_mailbox = 0;
  if ((CANx->TSR&CAN_TSR_TME0) == CAN_TSR_TME0)
  {
    transmit_mailbox = 0;
  }
  else if ((CANx->TSR&CAN_TSR_TME1) == CAN_TSR_TME1)
  {
    transmit_mailbox = 1;
  }
  else if ((CANx->TSR&CAN_TSR_TME2) == CAN_TSR_TME2)
  {
    transmit_mailbox = 2;
  }
  else
  {
    transmit_mailbox = CAN_TxStatus_NoMailBox;
  }
	return transmit_mailbox;
}
