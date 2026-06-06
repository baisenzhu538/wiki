/*
*********************************************************************************************************
*
*	模块名称 : 串口驱动程序
*	文件名称 : usart.c
*	版    本 : V1.0
*	说    明 : 实现串口硬件接口的初始化与软件接口的初始化,并提供操作接口
*	修改记录 :
*		版本号  日期       作者    说明
*		V1.0    2016-12-01 OUSI    
*   V1.01   2016-12-03 OUSI    增加void Usart_Sendchar(COM_PORT port_num,u8 data)
*           2016_12_05 OUSI    增加UART3的配置
*********************************************************************************************************
*/
#include "usart.h"	  
static UART_DEVICE *pUartDevice[5];

#if UART1_ENABLE
UART_DEVICE UartDevice1={0,0,0,0,0,0};
u8 Uart1_TxBuf[UART1_TX_BUF_SIZE];
u8 Uart1_RxBuf[UART1_TX_BUF_SIZE];
#endif
#if UART2_ENABLE
UART_DEVICE UartDevice2={0,0,0,0,0,0};
u8 Uart2_TxBuf[UART2_TX_BUF_SIZE];
u8 Uart2_RxBuf[UART2_RX_BUF_SIZE];
#endif
#if UART3_ENABLE
UART_DEVICE UartDevice3={0,0,0,0,0,0};
u8 Uart3_TxBuf[UART3_TX_BUF_SIZE];
u8 Uart3_RxBuf[UART3_RX_BUF_SIZE];
#endif



/*
*********************************************************************************************************
*	函 数 名: UartVarInit
*	功能说明: 初始化设备参数和缓存
*	形    参: 无
*	返 回 值: 无
*********************************************************************************************************
*/
static void UartVarInit(void)
{
	#if UART1_ENABLE
	pUartDevice[COM1]=&UartDevice1;      //初始化数据结构
	pUartDevice[COM1]->rx_buf=Uart1_RxBuf;
	pUartDevice[COM1]->tx_buf=Uart1_TxBuf;
	
	#endif
	#if UART2_ENABLE
	pUartDevice[COM2]=&UartDevice2;
	pUartDevice[COM2]->rx_buf=Uart2_RxBuf;
	pUartDevice[COM2]->tx_buf=Uart2_TxBuf;
	#endif
	
	#if UART3_ENABLE
	pUartDevice[COM3]=&UartDevice3;
	pUartDevice[COM3]->rx_buf=Uart3_RxBuf;
	pUartDevice[COM3]->tx_buf=Uart3_TxBuf;
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
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOA, &GPIO_InitStructure);                      //初始化GPIOA.10  

  NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=3 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 3;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel4_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 3;  
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
	
	USART_InitStructure.USART_BaudRate = UART1_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART1, &USART_InitStructure); 
  USART_ITConfig(USART1, USART_IT_RXNE, ENABLE);
	USART_ITConfig(USART1, USART_IT_IDLE, ENABLE);
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
	
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE); 
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART2,ENABLE);
	RCC_AHBPeriphClockCmd(RCC_AHBPeriph_DMA1, ENABLE);
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2;                  //PA.9
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;	           //复用推挽输出
  GPIO_Init(GPIOA, &GPIO_InitStructure);                     //初始化GPIOA.9
   
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;                  //PA10
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;       //浮空输入
  GPIO_Init(GPIOA, &GPIO_InitStructure);                      //初始化GPIOA.10  

  NVIC_InitStructure.NVIC_IRQChannel = USART2_IRQn;           //接收中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=3 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 3;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel7_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 3;  
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
	
	USART_InitStructure.USART_BaudRate = UART2_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART2, &USART_InitStructure); 
  USART_ITConfig(USART2, USART_IT_RXNE, ENABLE);
	USART_ITConfig(USART2, USART_IT_IDLE, ENABLE);
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
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority=3 ;    //抢占优先级3
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 3;		      //子优先级3
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;			        //IRQ通道使能
	NVIC_Init(&NVIC_InitStructure);	
	
	NVIC_InitStructure.NVIC_IRQChannel = DMA1_Channel2_IRQn;     //DMA中断设置
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 3;  
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
	
	USART_InitStructure.USART_BaudRate = UART3_BAUD;              //串口波特率
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;  //字长为8位数据格式
	USART_InitStructure.USART_StopBits = USART_StopBits_1;       //一个停止位
	USART_InitStructure.USART_Parity = USART_Parity_No;           //无奇偶校验位
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;//无硬件数据流控制
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;	//收发模式
	
  USART_Init(USART3, &USART_InitStructure); 
  USART_ITConfig(USART3, USART_IT_RXNE, ENABLE);
	USART_ClearFlag(USART3, USART_FLAG_TC);
	USART_ITConfig(USART3, USART_IT_IDLE, ENABLE);
  USART_Cmd(USART3, ENABLE); 
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
void SerialDevice_Init(void)
{
	UartVarInit();
	#if UART1_ENABLE
	Uart1_Init();
	#endif
	#if UART2_ENABLE
	Uart2_Init();
	#endif
	#if UART3_ENABLE
	Uart3_Init();
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

void Uart_GetData(COM_PORT port_num,u8 *data)
{
 u16 i;	
	for(i=0;i<pUartDevice[port_num]->rx_datasize;i++)
	 {
		data[i]=pUartDevice[port_num]->rx_buf[i];
	 }
	 pUartDevice[port_num]->rx_datasize=0;
}

/*
*********************************************************************************************************
*	函 数 名: Usart_GetDataPack
*	功能说明: 从指定端口获取数据
*	形    参:  char uart_num          :USART_0/USART_1/USART_2/USART_3/USART_4
*            unsigned int baud_rate :9600/115200/
*	返 回 值:  0x00                   :串口创建失败
*            0x01                   :串口创建成功
*********************************************************************************************************
*/
uint16_t Usart_GetDataPackLen(COM_PORT port_num)
{
 uint16_t i;
 uint16_t checksumbuf;
 uint16_t checksum;
 uint16_t datalen;
  if((pUartDevice[port_num]->rxstate==1)||(pUartDevice[port_num]->rx_datasize==0))
    return 0x00;
  if((pUartDevice[port_num]->rx_buf[0]==0xAA)
		&&(pUartDevice[port_num]->rx_buf[1]==0xBB)
	  &&(pUartDevice[port_num]->rx_buf[pUartDevice[port_num]->rx_datasize-2]==0xBB)
	  &&(pUartDevice[port_num]->rx_buf[pUartDevice[port_num]->rx_datasize-1]==0xAA))
	{
		datalen=pUartDevice[port_num]->rx_buf[2]+pUartDevice[port_num]->rx_buf[3]*256;
		checksumbuf=pUartDevice[port_num]->rx_buf[pUartDevice[port_num]->rx_datasize-4]+pUartDevice[port_num]->rx_buf[pUartDevice[port_num]->rx_datasize-3]*256;
		for(i=0;i<datalen+2;i++)
		 checksum=pUartDevice[port_num]->rx_buf[i+2];
		if(checksumbuf==checksum)
		{
			return datalen;//返回数据包长度
		}
	}
	pUartDevice[port_num]->rx_datasize=0;
  return 0xEEEE;//数据包错误	
}

void Usart_GetDataPack(COM_PORT port_num,uint16_t datalen,uint8_t *data)
{
 uint16_t i;
 for(i=0;i<datalen;i++)
 {
	data[i]=pUartDevice[port_num]->rx_buf[i+4];
 }
 pUartDevice[port_num]->rx_datasize=0;
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
	return 0x01;
  }
 return 0x00;
}

uint8_t Uart_SendPack(COM_PORT port_num,u8 *data,u16 datasize)
{
 u16 i;
 uint16_t checksum;
 if(pUartDevice[port_num]->txstate!=1)
 {
  pUartDevice[port_num]->tx_datasize=datasize+8;
 
	pUartDevice[port_num]->tx_buf[0]=0xAA;
	pUartDevice[port_num]->tx_buf[1]=0xBB;
	pUartDevice[port_num]->tx_buf[2]=datasize&0x00FF;
	pUartDevice[port_num]->tx_buf[3]=(datasize&0xFF00)>>8;
	checksum=pUartDevice[port_num]->tx_buf[2]+pUartDevice[port_num]->tx_buf[3];
  for(i=0;i<datasize;i++)
  {
	 pUartDevice[port_num]->tx_buf[i+4]=data[i];
	 checksum+=pUartDevice[port_num]->tx_buf[i+4];
  }
	pUartDevice[port_num]->tx_buf[datasize+4]=checksum&0x00FF;
	pUartDevice[port_num]->tx_buf[datasize+5]=(checksum&0xFF00)>>8;
	
	pUartDevice[port_num]->tx_buf[datasize+6]=0xBB;
	pUartDevice[port_num]->tx_buf[datasize+7]=0xAA;
	
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
	return 0x01;
  }
 return 0x00;
}

void Uart_Sendchar(COM_PORT port_num,u8 data)
{
	u8 databuf;
	databuf=data;
	Uart_SendData(port_num,(u8*)&databuf,1);
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
		 UartDevice1.rxstate=1;
		 UartDevice1.rx_buf[UartDevice1.rx_datasize++]=USART_ReceiveData(USART1);
    }
	if(USART_GetITStatus(USART1, USART_IT_IDLE) != RESET)
	 {
		 Res=USART1->SR;
		 Res=USART1->DR;
		 UartDevice1.rxstate=0;
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
		 UartDevice2.rxstate=1;
		 UartDevice2.rx_buf[UartDevice2.rx_datasize++]=USART_ReceiveData(USART2);;

    }
	if(USART_GetITStatus(USART2, USART_IT_IDLE) != RESET)
	 {
		 Res=USART2->SR;
		 Res=USART2->DR;
		 UartDevice2.rxstate=0;
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
		 UartDevice3.rxstate=1;
		 UartDevice3.rx_buf[UartDevice3.rx_datasize++]=USART_ReceiveData(USART3);;

    }
	if(USART_GetITStatus(USART3, USART_IT_IDLE) != RESET)
	 {
		 Res=USART3->SR;
		 Res=USART3->DR;
		 UartDevice3.rxstate=0;
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










