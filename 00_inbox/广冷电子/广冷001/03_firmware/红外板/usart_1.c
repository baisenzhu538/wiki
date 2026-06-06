/*
*********************************************************************************************************
*
*	模块名称 : 串口驱动程序
*	文件名称 : usart.c
*	版    本 : V1.2
*	说    明 : 实现串口硬件接口的初始化与软件接口的初始化,并提供操作接口
*	修改记录 :
*		版本号  日期       作者    说明
*		V1.0    2016-12-01 OUSI    
*   V1.1    2016-12-03 OUSI    增加void Usart_Sendchar(COM_PORT port_num,u8 data)
*           2016_12_05 OUSI    增加UART3的配置
*   V1.2    2018_07_13 OUSI    增加字节接收和帧接收事件回调函数
    V1.3.0  2019-01-18 OUSI    增加定时打包功能,增加硬件异常诊断与相关处理
		V1.4.0  2019-02-22 Waves   uart4增加DMA接收模式
		V1.5.0  2019-07-02 Waves   uart1,uart2,uart3增加DMA接收模式
*********************************************************************************************************
*/
#include "usart.h"


static UART_DEVICE *pUartDevice[5];

#if UART1_ENABLE
UART_DEVICE UartDevice1={0,0,0,0,0,0,0,0,0,NULL,NULL};
u8 Uart1_TxBuf[UART1_TX_BUF_SIZE];
u8 Uart1_RxBuf[UART1_TX_BUF_SIZE];
#endif
#if UART2_ENABLE
UART_DEVICE UartDevice2={0,0,0,0,0,0,0,0,0,NULL,NULL};
u8 Uart2_TxBuf[UART2_TX_BUF_SIZE];
u8 Uart2_RxBuf[UART2_RX_BUF_SIZE];
#endif
#if UART3_ENABLE
UART_DEVICE UartDevice3={0,0,0,0,0,0,0,0,0,NULL,NULL};
u8 Uart3_TxBuf[UART3_TX_BUF_SIZE];
u8 Uart3_RxBuf[UART3_RX_BUF_SIZE];
#endif
#if UART4_ENABLE
UART_DEVICE UartDevice4={0,0,0,0,0,0,0,0,0,NULL,NULL};
u8 Uart4_TxBuf[UART4_TX_BUF_SIZE];
u8 Uart4_RxBuf[UART4_RX_BUF_SIZE];
#endif


void Usart_TimeTask(COM_PORT port_num)
{
	if(pUartDevice[port_num]->rx_packaged_time)
		pUartDevice[port_num]->rx_packaged_time--;
	else
	{
		if(pUartDevice[port_num]->rxstate)
		{
			pUartDevice[port_num]->rxstate=0;
			if(pUartDevice[port_num]->ReceiveFrame_CallBack)
			 {
				 pUartDevice[port_num]->ReceiveFrame_CallBack(pUartDevice[port_num]->rx_buf,pUartDevice[port_num]->rx_datasize);
				 pUartDevice[port_num]->rx_datasize=0;
			 }
	   }
	}
}
/*
*********************************************************************************************************
*	函 数 名: UartVarInit
*	功能说明: 初始化设备参数和缓存
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
static void UartVarInit(COM_PORT port_num)
{
	#if UART1_ENABLE
	if(port_num==COM1)
	{
	 pUartDevice[COM1]=&UartDevice1;      //初始化数据结构
	 pUartDevice[COM1]->rx_buf=Uart1_RxBuf;
	 pUartDevice[COM1]->tx_buf=Uart1_TxBuf;
	}
	#endif
	#if UART2_ENABLE
	if(port_num==COM2)
	{
	 pUartDevice[COM2]=&UartDevice2;
	 pUartDevice[COM2]->rx_buf=Uart2_RxBuf;
	 pUartDevice[COM2]->tx_buf=Uart2_TxBuf;
	}
	#endif
	
	#if UART3_ENABLE
	if(port_num==COM3)
	{
	 pUartDevice[COM3]=&UartDevice3;
	 pUartDevice[COM3]->rx_buf=Uart3_RxBuf;
	 pUartDevice[COM3]->tx_buf=Uart3_TxBuf;
	}
	#endif
	#if UART4_ENABLE
	if(port_num==COM4)
	{
	 pUartDevice[COM4]=&UartDevice4;
	 pUartDevice[COM4]->rx_buf=Uart4_RxBuf;
	 pUartDevice[COM4]->tx_buf=Uart4_TxBuf;
	}
	#endif
}
/*
*********************************************************************************************************
*	函 数 名: Uartx_Init
*	功能说明: 初始化UART1硬件接口
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/

#if UART1_ENABLE
void Uart1_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	USART_InitTypeDef USART_InitStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1|RCC_APB2Periph_GPIOA, ENABLE); 
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOA, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IPU;       //浮空输入
  GPIO_Init(GPIOA, &GPIO_InitStructure);                      //初始化GPIOA.10  

  NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=0;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel4_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure); 
  
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART1->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice1.tx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralDST;  
	DMA_InitStructure.DMA_BufferSize = UART1_TX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel4,&DMA_InitStructure);  
	DMA_ITConfig(DMA1_Channel4,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA1_Channel4,DISABLE);
	USART_DMACmd(USART1,USART_DMAReq_Tx,ENABLE);
	
	#ifdef UART1_DMA_RX_MOD
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART1->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice1.rx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;  
	DMA_InitStructure.DMA_BufferSize = UART1_RX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel5,&DMA_InitStructure);  

	DMA_Cmd(DMA1_Channel5,ENABLE);
	USART_DMACmd(USART1,USART_DMAReq_Rx,ENABLE);
	#endif
	
	USART_InitStructure.USART_BaudRate = UART1_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART1, &USART_InitStructure);
  #ifdef UART1_IT_RX_MOD	
  USART_ITConfig(USART1, USART_IT_RXNE, ENABLE);
	#endif
	USART_ITConfig(USART1, USART_IT_IDLE, ENABLE);
	USART_ITConfig(USART1, USART_IT_PE, ENABLE);
  USART_ITConfig(USART1, USART_IT_ERR, ENABLE);
	USART_ClearFlag(USART1, USART_FLAG_TC);
  USART_Cmd(USART1, ENABLE);
}
#endif


/*
*********************************************************************************************************
*	函 数 名: Uartx_Init
*	功能说明: 初始化UART2硬件接口
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
#if UART2_ENABLE
void Uart2_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	USART_InitTypeDef USART_InitStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART2,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
#ifdef UART2_INTERFACE1
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE); 
	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOA, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOA, &GPIO_InitStructure);                      //初始化GPIOA.10  
#endif
#ifdef UART2_INTERFACE2
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOD|RCC_APB2Periph_AFIO, ENABLE); 
	GPIO_PinRemapConfig(GPIO_Remap_USART2, ENABLE); 
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOD, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_6;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOD, &GPIO_InitStructure);                      //初始化GPIOA.10  
#endif
	
  NVIC_InitStructure.NVIC_IRQChannel = USART2_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=0 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel7_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure); 
  
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART2->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice2.tx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralDST;  
	DMA_InitStructure.DMA_BufferSize = UART2_TX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel7,&DMA_InitStructure);  
	DMA_ITConfig(DMA1_Channel7,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA1_Channel7,DISABLE);
	USART_DMACmd(USART2,USART_DMAReq_Tx,ENABLE);
	
	#ifdef UART2_DMA_RX_MOD
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART2->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice2.rx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;  
	DMA_InitStructure.DMA_BufferSize = UART2_RX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel6,&DMA_InitStructure);  
//	DMA_ITConfig(DMA2_Channel3,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA1_Channel6,ENABLE);
	USART_DMACmd(USART2,USART_DMAReq_Rx,ENABLE);
	#endif
	
	USART_InitStructure.USART_BaudRate = UART2_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART2, &USART_InitStructure);
  #ifdef UART2_IT_RX_MOD		
  USART_ITConfig(USART2, USART_IT_RXNE, ENABLE);
	#endif
	USART_ITConfig(USART2, USART_IT_IDLE, ENABLE);
	USART_ITConfig(USART2, USART_IT_PE, ENABLE);
  USART_ITConfig(USART2, USART_IT_ERR, ENABLE);
	USART_ClearFlag(USART2, USART_FLAG_TC);
  USART_Cmd(USART2, ENABLE);
  
	
}
#endif

/*
*********************************************************************************************************
*	函 数 名: Uartx_Init
*	功能说明: 初始化UART3硬件接口
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
#if UART3_ENABLE
void Uart3_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	USART_InitTypeDef USART_InitStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOB, ENABLE); 
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART3,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOB, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOB, &GPIO_InitStructure);                      //初始化GPIOA.10  

  NVIC_InitStructure.NVIC_IRQChannel = USART3_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=0 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel2_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure); 
  
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART3->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice3.tx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralDST;  
	DMA_InitStructure.DMA_BufferSize = UART3_TX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel2,&DMA_InitStructure);  
	DMA_ITConfig(DMA1_Channel2,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA1_Channel2,DISABLE);
	USART_DMACmd(USART3,USART_DMAReq_Tx,ENABLE);
	
	#ifdef UART3_DMA_RX_MOD
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&USART3->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice3.rx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;  
	DMA_InitStructure.DMA_BufferSize = UART3_RX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA1_Channel3,&DMA_InitStructure);  
//	DMA_ITConfig(DMA2_Channel3,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA1_Channel3,ENABLE);
	USART_DMACmd(USART3,USART_DMAReq_Rx,ENABLE);
	#endif
	
	USART_InitStructure.USART_BaudRate = UART3_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART3, &USART_InitStructure);
  #ifdef UART3_IT_RX_MOD	
  USART_ITConfig(USART3, USART_IT_RXNE, ENABLE);
	#endif
	USART_ClearFlag(USART3, USART_FLAG_TC);
	USART_ITConfig(USART3, USART_IT_PE, ENABLE);
  USART_ITConfig(USART3, USART_IT_ERR, ENABLE);
	USART_ITConfig(USART3, USART_IT_IDLE, ENABLE);

  USART_Cmd(USART3, ENABLE); 
}
#endif

/*
*********************************************************************************************************
*	函 数 名: Uartx_Init
*	功能说明: 初始化UART3硬件接口
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
#if UART4_ENABLE
void Uart4_Init(void)
{
	GPIO_InitTypeDef GPIO_InitStructure;
	USART_InitTypeDef USART_InitStructure;
	NVIC_InitTypeDef NVIC_InitStructure;
	DMA_InitTypeDef   DMA_InitStructure;
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOC, ENABLE); 
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_UART4,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA2, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_10;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOC, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOC, &GPIO_InitStructure);                      //初始化GPIOA.10  

  NVIC_InitStructure.NVIC_IRQChannel = UART4_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=0 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 1;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA2_Channel4_5_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;  
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 2;  
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;  
	NVIC_Init(&NVIC_InitStructure); 
  
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&UART4->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice4.tx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralDST;  
	DMA_InitStructure.DMA_BufferSize = UART4_TX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA2_Channel5,&DMA_InitStructure);  
	DMA_ITConfig(DMA2_Channel5,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA2_Channel5,DISABLE);
	USART_DMACmd(UART4,USART_DMAReq_Tx,ENABLE);
	
	#ifdef UART4_DMA_RX_MOD
	DMA_InitStructure.DMA_PeripheralBaseAddr = (u32)(&UART4->DR);  //DMA发送设置
	DMA_InitStructure.DMA_MemoryBaseAddr = (uint32_t)UartDevice4.rx_buf; 
	DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralSRC;  
	DMA_InitStructure.DMA_BufferSize = UART4_RX_BUF_SIZE;  
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;  
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;   
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_MemoryDataSize = DMA_PeripheralDataSize_Byte; 
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;   
	DMA_InitStructure.DMA_Priority = DMA_Priority_VeryHigh;  
	DMA_InitStructure.DMA_M2M = DMA_M2M_Disable;  
	DMA_Init(DMA2_Channel3,&DMA_InitStructure);  
//	DMA_ITConfig(DMA2_Channel3,DMA_IT_TC,ENABLE);
	DMA_Cmd(DMA2_Channel3,ENABLE);
	USART_DMACmd(UART4,USART_DMAReq_Rx,ENABLE);
	#endif
	
	USART_InitStructure.USART_BaudRate = UART4_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(UART4, &USART_InitStructure);
  #ifdef UART4_IT_RX_MOD	
  USART_ITConfig(UART4, USART_IT_RXNE, ENABLE);
	#endif
	USART_ClearFlag(UART4, USART_FLAG_TC);
	USART_ITConfig(UART4, USART_IT_PE, ENABLE);
  USART_ITConfig(UART4, USART_IT_ERR, ENABLE);	
	USART_ITConfig(UART4, USART_IT_IDLE, ENABLE);

  USART_Cmd(UART4, ENABLE); 
}
#endif
/*
*********************************************************************************************************
*	函 数 名: SerialDevice_Init
*	功能说明: 初始化串口设备
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
void SerialDevice_Init(COM_PORT port_num)
{
	UartVarInit(port_num);
	#if UART1_ENABLE
	if(port_num==COM1)
	 Uart1_Init();
	#endif
	#if UART2_ENABLE
	if(port_num==COM2)
	 Uart2_Init();
	#endif
	#if UART3_ENABLE
	if(port_num==COM3)
	 Uart3_Init();
	#endif
	#if UART4_ENABLE
	if(port_num==COM4)
	 Uart4_Init();
	#endif
}

/*
*********************************************************************************************************
*	函 数 名: SerialDevice_SetReceiveByteCallBack
*	功能说明: 设置字节接收回调函数
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
void SerialDevice_SetReceiveByteCallBack(COM_PORT port_num,void(*p)(u8))
{
	#if UART1_ENABLE
	if(port_num==COM1)
	 UartDevice1.ReceiveBytes_CallBack=p;
	#endif
	#if UART2_ENABLE
	if(port_num==COM2)
	 UartDevice2.ReceiveBytes_CallBack=p;
	#endif
	#if UART3_ENABLE
	if(port_num==COM3)
	 UartDevice3.ReceiveBytes_CallBack=p;
	#endif
	#if UART4_ENABLE
	if(port_num==COM4)
	 UartDevice4.ReceiveBytes_CallBack=p;
	#endif
}

/*
*********************************************************************************************************
*	函 数 名: SerialDevice_SetReceiveFrameCallBack
*	功能说明: 设置帧接收回调函数
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
void SerialDevice_SetReceiveFrameCallBack(COM_PORT port_num,void(*p)(uint8_t*,uint16_t))
{
	#if UART1_ENABLE
	if(port_num==COM1)
	 UartDevice1.ReceiveFrame_CallBack=p;
	#endif
	#if UART2_ENABLE
	if(port_num==COM2)
	 UartDevice2.ReceiveFrame_CallBack=p;
	#endif
	#if UART3_ENABLE
	if(port_num==COM3)
	 UartDevice3.ReceiveFrame_CallBack=p;
	#endif
	#if UART4_ENABLE
	if(port_num==COM4)
	 UartDevice4.ReceiveFrame_CallBack=p;
	#endif
}


/*
*********************************************************************************************************
*	函 数 名: Usart_GetSate
*	功能说明: 获取指定端口号状态
*	形    参:  char uart_num          :USART_0/USART_1/USART_2/USART_3/USART_4
*            unsigned int baud_rate :9600/115200/
*	返 回 值:  0x00                   :串口创建失败
*            0x01                   :串口创建成功
*********************************************************************************************************
*/

u16 Uart_GetSate(COM_PORT port_num)
{
 if(pUartDevice[port_num]->rxstate==1)
  return 0x00;                                 //数据还没接收完成
 if(pUartDevice[port_num]->rx_datasize)
	return pUartDevice[port_num]->rx_datasize;  //返回接收到的数据字节数
 return 0x00;
}

u16 Uart_GetTxSate(COM_PORT port_num)
{
 if(pUartDevice[port_num]->txstate==1)
	 return pUartDevice[port_num]->tx_datasize;  //返回待发送的数据字节数
 else
	 return 0x00;                                 //数据发送完成
 return 0x00;	
}

/*
*********************************************************************************************************
*	函 数 名: Usart_GetData
*	功能说明: 从指定端口获取数据
*	形    参:  char uart_num          :USART_0/USART_1/USART_2/USART_3/USART_4
*            unsigned int baud_rate :9600/115200/
*	返 回 值:  0x00                   :串口创建失败
*            0x01                   :串口创建成功
*********************************************************************************************************
*/
uint8_t Uart_GetData(COM_PORT port_num,u8 *data)
{
 uint16_t i;	
	if(pUartDevice[port_num]->rxstate==1)
   return 0x00;   
	for(i=0;i<pUartDevice[port_num]->rx_datasize;i++)
	 {
		data[i]=pUartDevice[port_num]->rx_buf[i];
	 }
	 pUartDevice[port_num]->rx_datasize=0;
	 return 0xFF;
}

void Usart_ClearDataPack(COM_PORT port_num)
{
 pUartDevice[port_num]->rx_datasize=0x0000;
}


/*
*********************************************************************************************************
*	函 数 名: Usart_SendData
*	功能说明: 数据发送函数
*	形    参:  char uart_num          :USART_0/USART_1/USART_2/USART_3/USART_4
*            unsigned int baud_rate :9600/115200/
*	返 回 值:  0x00                   :串口创建失败
*            0x01                   :串口创建成功
*********************************************************************************************************
*/

uint8_t Uart_SendData(COM_PORT port_num,u8 *data,u16 datasize)
{
 u16 i;
 if(pUartDevice[port_num]->txstate!=1)
 {
 pUartDevice[port_num]->tx_datasize=datasize;
 for(i=0;i<datasize;i++)
 {
	 pUartDevice[port_num]->tx_buf[i]=data[i];
 }
	pUartDevice[port_num]->txstate=1;
	
  if(port_num==COM1)
	{
	 DMA1_Channel4->CNDTR=pUartDevice[port_num]->tx_datasize;
	 DMA1_Channel4->CMAR =(uint32_t)pUartDevice[port_num]->tx_buf;
	 DMA_Cmd(DMA1_Channel4,ENABLE);
	}
	if(port_num==COM2)
	{
	 DMA1_Channel7->CNDTR=pUartDevice[port_num]->tx_datasize;
	 DMA1_Channel7->CMAR =(uint32_t)pUartDevice[port_num]->tx_buf;
	 DMA_Cmd(DMA1_Channel7,ENABLE);
	}
	if(port_num==COM3)
	{
	 DMA1_Channel2->CNDTR=pUartDevice[port_num]->tx_datasize;
	 DMA1_Channel2->CMAR =(uint32_t)pUartDevice[port_num]->tx_buf;
	 DMA_Cmd(DMA1_Channel2,ENABLE);
	}
	if(port_num==COM4)
	{
	 DMA2_Channel5->CNDTR=pUartDevice[port_num]->tx_datasize;
	 DMA2_Channel5->CMAR =(uint32_t)pUartDevice[port_num]->tx_buf;
	 DMA_Cmd(DMA2_Channel5,ENABLE);
	}
	return 0x01;
  }
 return 0x00;
}

void Uart_Sendchar(COM_PORT port_num,u8 data)
{
	u8 databuf;
	databuf=data;
	if(port_num==COM1)
	{
	USART_SendData(USART1, data);        
  while( USART_GetFlagStatus(USART1,USART_FLAG_TC)!= SET);
	}
  if(port_num==COM2)
	{
	USART_SendData(USART2, data);        
  while( USART_GetFlagStatus(USART2,USART_FLAG_TC)!= SET);
	}	
  if(port_num==COM3)
	{
	USART_SendData(USART3, data);        
  while( USART_GetFlagStatus(USART3,USART_FLAG_TC)!= SET);
	}	
  if(port_num==COM4)
	{
	USART_SendData(UART4, data);        
  while( USART_GetFlagStatus(UART4,USART_FLAG_TC)!= SET);
	}		
}
/*
*********************************************************************************************************
*	函 数 名: USART1_IRQHandler
*	功能说明: 初始化串口硬件
*	形    参:  char uart_num          :USART_0/USART_1/USART_2/USART_3/USART_4
*            unsigned int baud_rate :9600/115200/
*	返 回 值:  0x00                   :串口创建失败
*            0x01                   :串口创建成功
*********************************************************************************************************
*/
#if UART1_ENABLE
void USART1_IRQHandler(void)                	//串口1中断服务程序
{
	u8 Res;
	if(USART_GetITStatus(USART1, USART_IT_RXNE) != RESET)  //接收中断(接收到的数据必须是0x0d 0x0a结尾)
	{
		if(UartDevice1.ReceiveBytes_CallBack)
		{
			UartDevice1.ReceiveBytes_CallBack(USART_ReceiveData(USART1));
		}
		else
		{
			UartDevice1.rxstate=1;
			UartDevice1.rx_packaged_time=UART1_PACKAGED_TIME;
			if(UartDevice1.rx_datasize<UART1_RX_BUF_SIZE)
				UartDevice1.rx_buf[UartDevice1.rx_datasize++]=USART_ReceiveData(USART1); 
		}
	}
	if(USART_GetFlagStatus(USART1, USART_FLAG_ORE) != RESET)
	{
		Res=USART1->SR;
		Res=USART1->DR;
		USART_ClearFlag(USART1, USART_FLAG_ORE);
	}
	if(USART_GetFlagStatus(USART1, USART_FLAG_NE) != RESET)
	{
		Res=USART1->SR;
		Res=USART1->DR;
		USART_ClearFlag(USART1, USART_FLAG_NE);
	}
	if(USART_GetFlagStatus(USART1, USART_FLAG_FE) != RESET)
	{
		Res=USART1->SR;
		Res=USART1->DR;
		USART_ClearFlag(USART1, USART_FLAG_FE);
	}
	if(USART_GetFlagStatus(USART1, USART_FLAG_PE) != RESET)
	{
		Res=USART1->SR;
		Res=USART1->DR;
		USART_ClearFlag(USART1, USART_FLAG_PE);
	}
		
	if(USART_GetITStatus(USART1, USART_IT_IDLE) != RESET)
	{
		Res=USART1->SR;
		Res=USART1->DR;
		
#ifdef UART1_DMA_RX_MOD
		DMA_Cmd(DMA1_Channel5,DISABLE); 
		UartDevice1.rx_datasize=UART1_RX_BUF_SIZE - DMA_GetCurrDataCounter(DMA1_Channel5);
		DMA_SetCurrDataCounter(DMA1_Channel5,UART1_RX_BUF_SIZE);
		DMA_Cmd(DMA1_Channel5,ENABLE); 
#endif

#ifdef UART1_DATAFRAME_MOD
		if(UartDevice1.ReceiveFrame_CallBack)
		{
			UartDevice1.ReceiveFrame_CallBack(UartDevice1.rx_buf,UartDevice1.rx_datasize);
			UartDevice1.rx_datasize=0;
		}
		UartDevice1.rxstate=0;
#endif	
	}
  
} 



void DMA1_Channel4_IRQHandler(void)
{
	if(DMA_GetITStatus(DMA1_IT_TC4)!=RESET)
	{
		DMA_ClearITPendingBit(DMA1_IT_TC4);
		UartDevice1.txstate=0;
		UartDevice1.tx_datasize=0;
		DMA_Cmd(DMA1_Channel4,DISABLE);
	}
}
#endif

#if UART2_ENABLE
void USART2_IRQHandler(void)                	//串口2中断服务程序
{
	u8 Res;
	if(USART_GetITStatus(USART2, USART_IT_RXNE) != RESET)  //接收中断(接收到的数据必须是0x0d 0x0a结尾)
    {
		 if(UartDevice2.ReceiveBytes_CallBack)
		 {
			 UartDevice2.ReceiveBytes_CallBack(USART_ReceiveData(USART2));
		 }
		 else
		 {
		  UartDevice2.rxstate=1;
			UartDevice2.rx_packaged_time=UART2_PACKAGED_TIME;
			if(UartDevice2.rx_datasize<UART2_RX_BUF_SIZE)
		   UartDevice2.rx_buf[UartDevice2.rx_datasize++]=USART_ReceiveData(USART2); 
		 }
    }
	  if(USART_GetFlagStatus(USART2, USART_FLAG_ORE) != RESET)
		{
		 Res=USART2->SR;
		 Res=USART2->DR;
		 USART_ClearFlag(USART2, USART_FLAG_ORE);
		}
		if(USART_GetFlagStatus(USART2, USART_FLAG_NE) != RESET)
		{
		 Res=USART2->SR;
		 Res=USART2->DR;
		 USART_ClearFlag(USART2, USART_FLAG_NE);
		}
		if(USART_GetFlagStatus(USART2, USART_FLAG_FE) != RESET)
		{
		 Res=USART2->SR;
		 Res=USART2->DR;
		 USART_ClearFlag(USART2, USART_FLAG_FE);
		}
		if(USART_GetFlagStatus(USART2, USART_FLAG_PE) != RESET)
		{
		 Res=USART2->SR;
		 Res=USART2->DR;
		 USART_ClearFlag(USART2, USART_FLAG_PE);
		}
	if(USART_GetITStatus(USART2, USART_IT_IDLE) != RESET)
	 {
		 Res=USART2->SR;
		 Res=USART2->DR;
		 #ifdef UART2_DMA_RX_MOD
		 DMA_Cmd(DMA1_Channel6,DISABLE); 
		 UartDevice2.rx_datasize=UART2_RX_BUF_SIZE - DMA_GetCurrDataCounter(DMA1_Channel6);
		 DMA_SetCurrDataCounter(DMA1_Channel6,UART2_RX_BUF_SIZE);
		 DMA_Cmd(DMA1_Channel6,ENABLE); 
		 #endif
		 
		 #ifdef UART2_DATAFRAME_MOD
		 if(UartDevice2.ReceiveFrame_CallBack)
		 {
			 UartDevice2.ReceiveFrame_CallBack(UartDevice2.rx_buf,UartDevice2.rx_datasize);
			 UartDevice2.rx_datasize=0;
		 }
		 UartDevice2.rxstate=0;
		 #endif	 
	 }
   
}

void DMA1_Channel7_IRQHandler(void)
{
	if(DMA_GetITStatus(DMA1_IT_TC7)!=RESET)
	{
		DMA_ClearITPendingBit(DMA1_IT_TC7);
		UartDevice2.txstate=0;
		UartDevice2.tx_datasize=0;
		DMA_Cmd(DMA1_Channel7,DISABLE);
	}
} 
#endif

#if UART3_ENABLE
void USART3_IRQHandler(void)                	//串口2中断服务程序
{
	u8 Res;
	if(USART_GetITStatus(USART3, USART_IT_RXNE) != RESET)  //接收中断(接收到的数据必须是0x0d 0x0a结尾)
    {
		 if(UartDevice3.ReceiveBytes_CallBack)
		 {
			 UartDevice3.ReceiveBytes_CallBack(USART_ReceiveData(USART3));
		 }
		 else
		 {
		  UartDevice3.rxstate=1;
			UartDevice3.rx_packaged_time=UART3_PACKAGED_TIME;
			if(UartDevice3.rx_datasize<UART3_RX_BUF_SIZE)
		   UartDevice3.rx_buf[UartDevice3.rx_datasize++]=USART_ReceiveData(USART3); 
		 }
    }
	  if(USART_GetFlagStatus(USART3, USART_FLAG_ORE) != RESET)
		{
		 Res=USART3->SR;
		 Res=USART3->DR;
		 USART_ClearFlag(USART3, USART_FLAG_ORE);
		}
		if(USART_GetFlagStatus(USART3, USART_FLAG_NE) != RESET)
		{
		 Res=USART3->SR;
		 Res=USART3->DR;
		 USART_ClearFlag(USART3, USART_FLAG_NE);
		}
		if(USART_GetFlagStatus(USART3, USART_FLAG_FE) != RESET)
		{
		 Res=USART3->SR;
		 Res=USART3->DR;
		 USART_ClearFlag(USART3, USART_FLAG_FE);
		}
		if(USART_GetFlagStatus(USART3, USART_FLAG_PE) != RESET)
		{
		 Res=USART3->SR;
		 Res=USART3->DR;
		 USART_ClearFlag(USART3, USART_FLAG_PE);
		}
	if(USART_GetITStatus(USART3, USART_IT_IDLE) != RESET)
	 {
		 Res=USART3->SR;
		 Res=USART3->DR;
		 #ifdef UART3_DMA_RX_MOD
		 DMA_Cmd(DMA1_Channel3,DISABLE); 
		 UartDevice3.rx_datasize=UART3_RX_BUF_SIZE - DMA_GetCurrDataCounter(DMA1_Channel3);
		 DMA_SetCurrDataCounter(DMA1_Channel3,UART3_RX_BUF_SIZE);
		 DMA_Cmd(DMA1_Channel3,ENABLE); 
		 #endif
		 #ifdef UART3_DATAFRAME_MOD
		 if(UartDevice3.ReceiveFrame_CallBack)
		 {
			 UartDevice3.ReceiveFrame_CallBack(UartDevice3.rx_buf,UartDevice3.rx_datasize);
			 UartDevice3.rx_datasize=0;
		 }
		 UartDevice3.rxstate=0;
		 #endif	
	 }
    
}

void DMA1_Channel2_IRQHandler(void)
{
	if(DMA_GetITStatus(DMA1_IT_TC2)!=RESET)
	{
		DMA_ClearITPendingBit(DMA1_IT_TC2);
		UartDevice3.txstate=0;
		UartDevice3.tx_datasize=0;
		DMA_Cmd(DMA1_Channel2,DISABLE);
	}
} 
#endif

#if UART4_ENABLE
void UART4_IRQHandler(void)                	//串口2中断服务程序
{
	u8 Res;
	
	#ifdef UART4_IT_RX_MOD
	if(USART_GetITStatus(UART4, USART_IT_RXNE) != RESET)  //接收中断(接收到的数据必须是0x0d 0x0a结尾)
    {
		 if(UartDevice4.ReceiveBytes_CallBack)
		 {
			 UartDevice4.ReceiveBytes_CallBack(USART_ReceiveData(UART4));
		 }
		 else
		 {
		  UartDevice4.rxstate=1;
			UartDevice4.rx_packaged_time=UART4_PACKAGED_TIME;
			if(UartDevice4.rx_datasize<UART4_RX_BUF_SIZE)
		   UartDevice4.rx_buf[UartDevice4.rx_datasize++]=USART_ReceiveData(UART4); 
		 }
    }
	#endif
		if(USART_GetFlagStatus(UART4, USART_FLAG_ORE) != RESET)
		{
		 Res=UART4->SR;
		 Res=UART4->DR;
		 USART_ClearFlag(UART4, USART_FLAG_ORE);
		}
		if(USART_GetFlagStatus(UART4, USART_FLAG_NE) != RESET)
		{
		 Res=UART4->SR;
		 Res=UART4->DR;
		 USART_ClearFlag(UART4, USART_FLAG_NE);
		}
		if(USART_GetFlagStatus(UART4, USART_FLAG_FE) != RESET)
		{
		 Res=UART4->SR;
		 Res=UART4->DR;
		 USART_ClearFlag(UART4, USART_FLAG_FE);
		}
		if(USART_GetFlagStatus(UART4, USART_FLAG_PE) != RESET)
		{
		 Res=UART4->SR;
		 Res=UART4->DR;
		 USART_ClearFlag(UART4, USART_FLAG_PE);
		}
	
	if(USART_GetITStatus(UART4, USART_IT_IDLE) != RESET)
	 {
		 Res=UART4->SR;
		 Res=UART4->DR;
		 #ifdef UART4_DMA_RX_MOD
		 DMA_Cmd(DMA2_Channel3,DISABLE); 
		 UartDevice4.rx_datasize=UART4_RX_BUF_SIZE - DMA_GetCurrDataCounter(DMA2_Channel3);
		 DMA_SetCurrDataCounter(DMA2_Channel3,UART4_RX_BUF_SIZE);
		 DMA_Cmd(DMA2_Channel3,ENABLE); 
		 #endif
		 
		 #ifdef UART4_DATAFRAME_MOD
		 if(UartDevice4.ReceiveFrame_CallBack)
		 {
			 UartDevice4.ReceiveFrame_CallBack(UartDevice4.rx_buf,UartDevice4.rx_datasize);
			 UartDevice4.rx_datasize=0;
		 }
		 UartDevice4.rxstate=0;
		 #endif	
	 }   
}

void DMA2_Channel4_5_IRQHandler(void)
{
	if(DMA_GetITStatus(DMA2_IT_TC5)!=RESET)
	{
		DMA_ClearITPendingBit(DMA2_IT_TC5);
		UartDevice4.txstate=0;
		UartDevice4.tx_datasize=0;
		DMA_Cmd(DMA2_Channel5,DISABLE);
	}
} 

//void DMA2_Channel3_IRQHandler(void)
//{
//	if(DMA_GetITStatus(DMA2_IT_TC3)!=RESET)
//	{
//		DMA_ClearITPendingBit(DMA2_IT_TC5);
//		UartDevice4.txstate=0;
//		UartDevice4.tx_datasize=0;
//		DMA_Cmd(DMA2_Channel5,DISABLE);
//	}
//} 

#endif









