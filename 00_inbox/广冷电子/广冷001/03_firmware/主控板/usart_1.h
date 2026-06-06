#ifndef __USART_H
#define __USART_H
#include "stdio.h"	
#include "stm32f10x_dma.h"


#define	UART1_ENABLE	 0
#define	UART2_ENABLE	 1
#define	UART3_ENABLE	 1
#define	UART4_ENABLE	 1
#define	UART5_ENABLE	 1

/* 定义端口号 */
typedef enum
{
	COM1 = 0,	/* UART1  PA9, PA10 */
	COM2 = 1,	/* UART2, PA2, PA3 */
	COM3 = 2,	/* UART3, PB10, PB11 */
	COM4 = 3,	/* UART4, PC10, PC11 */
	COM5 = 4,	/* UART5, PC12, PD2 */
}COM_PORT;


/* 定义串口波特率和FIFO缓冲区大小，分为发送缓冲区和接收缓冲区, 支持全双工 */
#if UART1_ENABLE
#define UART1_INTERFACE1 /*PA9,PA10*/

	#define UART1_BAUD			  9600
	#define UART1_TX_BUF_SIZE	1*1024
	#define UART1_RX_BUF_SIZE	1*1024
  #define UART1_DMACHANNEL  DMA1_Channel4
  
  #define UART1_PACKAGED_TIME 50     //单位ms
//  #define UART1_PACKAGED_MOD         //打包模式
  #define UART1_DATAFRAME_MOD        //数据帧模式

	#define UART1_DMA_RX_MOD           //DMA模式
//	#define UART3_IT_RX_MOD            //中断接收
#endif

#if UART2_ENABLE

  #define UART2_INTERFACE1  /*PA2,PA3*/
//  #define UART2_INTERFACE2  /*PD5,PD6*/

	#define UART2_BAUD			  115200
	#define UART2_TX_BUF_SIZE	1*1024
	#define UART2_RX_BUF_SIZE	1*1024
  #define UART2_DMACHANNEL  DMA1_Channel7
	
	#define UART2_PACKAGED_TIME 50     //单位ms
//	#define UART2_PACKAGED_MOD         //打包模式
  #define UART2_DATAFRAME_MOD        //数据帧模式
	
//	#define UART2_DMA_RX_MOD           //DMA模式
	#define UART2_IT_RX_MOD            //中断接收
#endif

#if UART3_ENABLE
	#define UART3_BAUD			  115200
	#define UART3_TX_BUF_SIZE		6*1024
	#define UART3_RX_BUF_SIZE		1*1024
	
	#define UART3_PACKAGED_TIME 5     //单位ms
//	#define UART3_PACKAGED_MOD         //打包模式
  #define UART3_DATAFRAME_MOD        //数据帧模式
	
	#define UART3_DMA_RX_MOD           //DMA模式
//	#define UART3_IT_RX_MOD            //中断接收
#endif

#if UART4_ENABLE
	#define UART4_BAUD			    115200
	#define UART4_TX_BUF_SIZE	  1*1024
	#define UART4_RX_BUF_SIZE	  1*1024
	
	#define UART4_PACKAGED_TIME 5     //打包时间单位ms
//	#define UART4_PACKAGED_MOD         //打包模式
  #define UART4_DATAFRAME_MOD        //数据帧模式
	
	
	#define UART4_DMA_RX_MOD           //DMA模式
//	#define UART4_IT_RX_MOD            //中断接收
#endif

#if UART5_ENABLE
	#define UART5_BAUD			115200
	#define UART5_TX_BUF_SIZE	1*1024
	#define UART5_RX_BUF_SIZE	1*1024
	
	#define UART5_PACKAGED_TIME 50     //单位ms
//	#define UART5_PACKAGED_MOD         //打包模式
  #define UART5_DATAFRAME_MOD        //数据帧模式
#endif

typedef struct _UART_DEVICE_   //串口接收数据缓存格式
{
	u8  rxstate;                    //串口当前状态0为空闲,1为忙碌
	u8  txstate;
	u16 rx_datasize;                //数据包存放数据大小
	u16 tx_datasize;
	u16 rx_buf_tail;
	u16 rx_buf_head;
	u16 rx_packaged_time;
	u8  *rx_buf;
	u8  *tx_buf;
	void (*ReceiveBytes_CallBack)(u8);
	void (*ReceiveFrame_CallBack)(u8*,u16);
}UART_DEVICE;

extern u8 Uart3_TxBuf[UART3_TX_BUF_SIZE];
extern u8 Uart3_RxBuf[UART3_RX_BUF_SIZE];

void Usart_TimeTask(COM_PORT port_num);//1ms调用一次
void SerialDevice_Init(COM_PORT port_num);
uint8_t Uart_GetData(COM_PORT port_num,u8 *data);
u16 Uart_GetSate(COM_PORT port_num);
u16 Uart_GetTxSate(COM_PORT port_num);
uint8_t Uart_SendData(COM_PORT port_num,u8 *data,u16 datasize);
void Uart_Sendchar(COM_PORT port_num,u8 data);
void Usart_ClearDataPack(COM_PORT port_num);
uint16_t Usart_GetDataPackLen(COM_PORT port_num);
uint8_t Uart_SendPack(COM_PORT port_num,u8 *data,u16 datasize);
void SerialDevice_SetReceiveFrameCallBack(COM_PORT port_num,void(*p)(uint8_t*,uint16_t));
void SerialDevice_SetReceiveByteCallBack(COM_PORT port_num,void(*p)(u8));
#endif


