#ifndef	_IR_H_
#define	_IR_H_

#include "sys.h"

#define	IR_4051_A	PAout(0)
#define	IR_4051_B	PAout(1)
#define	IR_4051_C	PAout(2)

#define	IR_4051_IN1	PBin(15)
#define	IR_4051_IN2 PBin(14)
#define	IR_4051_IN3 PCin(5)
#define	IR_4051_IN4 PBin(0)

#define	IR_595_RCLK		PCout(13)
#define	IR_595_SRCLK 	PCout(14)

//#define	IR_595_RCLK		PCout(14)
//#define	IR_595_SRCLK 	PCout(13)


#define	IR_595_QD1		PCout(6)
#define	IR_595_QD2		PCout(7)
#define	IR_595_QD3		PCout(15)
#define	IR_595_QD4		PCout(8)		/* TODO: verify QD4 GPIO on V2.2 PCB */

#define	IR_LEVEL_OUT	PBout(1)
#define	IR_LED_OUT		PBout(2)

typedef	struct
{
	u8	step;
	u8	no;
	u8	cnt;
	u16  sta;
	u16	scan_cnt;
	u8	ok_cnt_on;
	u8	ok_cnt_off;	
	u8	x1;
	u8	x2;
	u8	x3;
	u8	x4;
	u8	new_sta;
}Ir_TypeDef;



void Ir_Init(void);
void Ir_Scan_Task(void);


#endif	/*_IR_H_*/

