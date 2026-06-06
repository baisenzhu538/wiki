#include "debug.h"

#pragma import(__use_no_semihosting)                             
struct __FILE { 
    int handle; 
}; 

FILE __stdout;          
_sys_exit(int x) 
{ 
    x = x; 
}

void _ttywrch(int ch) 
{
	ch=ch;
}
int fputc(int ch, FILE *f)
{      
  Uart_Sendchar(COM2,(uint8_t)ch);		
	return ch;
}

void Debug_Init(void)
{
	SerialDevice_Init(COM2);
	SerialDevice_Init(COM3);
	SerialDevice_Init(COM4);
//	SerialDevice_Init(COM5);
}

void Debug_Test(void)
{
	Uart_SendData(COM2,"I have a dream!\r\n",strlen("I have a dream!\r\n"));
	Uart_SendData(COM3,"I have a dream!\r\n",strlen("I have a dream!\r\n"));
	Uart_SendData(COM4,"I have a dream!\r\n",strlen("I have a dream!\r\n"));
//	Uart_SendData(COM5,"I have a dream!\r\n",strlen("I have a dream!\r\n"));
	
}