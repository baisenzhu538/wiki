/*
*********************************************************************************************************
* 开发平台 ：STM32F103
*	模块名称 : CAN驱动与传输层接口对接
*	文件名称 : drive_api.c
*	版    本 : V1.0
*	说    明 : CAN驱动与数据传输层的对接接口
* 
*           将数据传输层下发的数据转换为标准的CAN数据格式，下发到CAN驱动发送           
*           将CAN驱动上传的总线数据转换为数据传输层能够识别的数据格式并上传            
*
*	修改记录 :
*		版本号  日期        作者     说明
*		V1.0    2017-06-24  欧阳     
*
*********************************************************************************************************
*/	
#include "drive_api.h"

/*************************************************************
函数：Can_ReceiveMsg
功能：将接收的标准CAN报文转换为协议CAN报文，并传入接收队列中
参数：pRxMessage 标准格式报文
返回：无
*************************************************************/
void Can_ReceiveMsg(CanRxMsg *pRxMessage)
{
	CanMsgTypeDef Msg;
	uint8_t i;
	(*((uint32_t*)&Msg.MsgFilter))=pRxMessage->ExtId;
	if(pRxMessage->DLC>0)
	 Msg.MsgData.DataSize     =pRxMessage->DLC-1;
	else
	 Msg.MsgData.DataSize=0;
	if(Msg.MsgFilter.FuncID==0x00)
	{
		Msg.MsgManage.SegPolo=0;
		Msg.MsgManage.SegNum=0;
	  Msg.MsgManage.ErrID=pRxMessage->Data[0]&0xF0;
		Msg.MsgManage.ErrFunc=pRxMessage->Data[0]&0x0F;
	}
	else
	{
	 Msg.MsgManage.SegPolo   =(pRxMessage->Data[0]>>6)&0x03;  //
	 Msg.MsgManage.SegNum    =pRxMessage->Data[0]&(~(0x03<<6));
	 Msg.MsgManage.ErrID     =0x00;
	 Msg.MsgManage.ErrFunc    =0x00;
	}
	for(i=0;i<Msg.MsgData.DataSize;i++)
	 Msg.MsgData.Data[i]=pRxMessage->Data[i+1];
	TransportLayer_ReceiveQueue(&Msg); 	//数据包加入队列
}
/*************************************************************
函数：Can_SendMsag
功能：将协议CAN报文转换为标准CAN报文并发送
参数：pMessage 协议规定格式报文
返回：0x00     发送不成功
      0xFF     发送成功
*************************************************************/
uint8_t Can_SendMsag(CanMsgTypeDef *pMessage)
{
	CanTxMsg TxMessage;
	uint8_t i,mailbox;
	mailbox=Can_GetMailBox(CAN1);
	if(mailbox==CAN_TxStatus_NoMailBox)
		return 0x00;
	TxMessage.ExtId=0x00000000;
	TxMessage.ExtId=*((u32*)&pMessage->MsgFilter);
  TxMessage.IDE=CAN_ID_EXT;			 // 使用扩展标识符
  TxMessage.RTR=0;		 // 消息类型为数据帧，一帧8位
  TxMessage.DLC=pMessage->MsgData.DataSize+1;							 // 发送两帧信息
	if(pMessage->MsgManage.ErrID!=0x00)
	{
		TxMessage.Data[0]=0;
		TxMessage.Data[0]|=pMessage->MsgManage.ErrID<<4;
		TxMessage.Data[0]|=pMessage->MsgManage.ErrFunc;
	}
	else
	  TxMessage.Data[0]=pMessage->MsgManage.SegNum|(pMessage->MsgManage.SegPolo<<6);
  for(i=0;i<pMessage->MsgData.DataSize;i++)
  TxMessage.Data[i+1]=pMessage->MsgData.Data[i];		
  mailbox=CAN_Transmit(CAN1, &TxMessage);	      //发送消息
	if(mailbox==CAN_TxStatus_NoMailBox)
		return 0x00;
	return 0xFF;
}

void Can_Receive(void)
{
	uint8_t msgnum,i;
	CanRxMsg RxMessage;
	msgnum=CAN_MessagePending(CAN1,CAN_FIFO0);
	if(msgnum==0)
		return;
	for(i=0;i<msgnum;i++)
	{
		if(CAN_MessagePending(CAN1,CAN_FIFO0))//接收到报文
		{
			CAN_Receive(CAN1, 0, &RxMessage);
			Can_ReceiveMsg(&RxMessage);
		}
	}
}