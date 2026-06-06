#ifndef __USART_H
#define __USART_H
#include "stdio.h"	
#include "sys.h" 
#include "stm32f10x_dma.h"

#define	UART1_ENABLE	 1
#define	UART2_ENABLE	 0
#define	UART3_ENABLE	 0
#define	UART4_ENABLE	 0
#define	UART5_ENABLE   0

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
	#define UART1_BAUD			  9600
	#define UART1_TX_BUF_SIZE	1*1024
	#define UART1_RX_BUF_SIZE	1*1024
  #define UART1_DMACHANNEL  DMA1_Channel4
#endif

#if UART2_ENABLE
	#define UART2_BAUD			  9600
	#define UART2_TX_BUF_SIZE	1*1024
	#define UART2_RX_BUF_SIZE	1*1024
  #define UART2_DMACHANNEL  DMA1_Channel7
#endif

#if UART3_ENABLE
	#define UART3_BAUD			  9600
	#define UART3_TX_BUF_SIZE	1*1024
	#define UART3_RX_BUF_SIZE	1*1024
#endif

#if UART4_ENABLE
	#define UART4_BAUD			115200
	#define UART4_TX_BUF_SIZE	1*1024
	#define UART4_RX_BUF_SIZE	1*1024
#endif

#if UART5_ENABLE
	#define UART5_BAUD			115200
	#define UART5_TX_BUF_SIZE	1*1024
	#define UART5_RX_BUF_SIZE	1*1024
#endif

typedef struct _UART_DEVICE_   //串口接收数据缓存格式
{
	u8  rxstate;                    //串口当前状态0为空闲,1为忙碌
	u8  txstate;
	u16 rx_datasize;                //数据包存放数据大小
	u16 tx_datasize;
	u8  *rx_buf;
	u8  *tx_buf;
}UART_DEVICE;


void SerialDevice_Init(void);
void Uart_GetData(COM_PORT port_num,u8 *data);
u16 Uart_GetSate(COM_PORT port_num);
uint8_t Uart_SendData(COM_PORT port_num,u8 *data,u16 datasize);
void Uart_Sendchar(COM_PORT port_num,u8 data);
void Usart_GetDataPack(COM_PORT port_num,uint16_t datalen,uint8_t *data);
uint16_t Usart_GetDataPackLen(COM_PORT port_num);
uint8_t Uart_SendPack(COM_PORT port_num,u8 *data,u16 datasize);
#endif


