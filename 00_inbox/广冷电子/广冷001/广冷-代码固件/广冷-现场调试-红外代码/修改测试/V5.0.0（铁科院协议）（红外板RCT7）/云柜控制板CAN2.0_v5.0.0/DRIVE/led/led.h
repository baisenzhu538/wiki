#ifndef __LED_H
#define __LED_H	 
#include "sys.h"

#define PUSH_LED_ENABLE  GPIO_SetBits(GPIOC,GPIO_Pin_3);
#define PUSH_LED_DISABLE GPIO_ResetBits(GPIOC,GPIO_Pin_3);
                    

#define BEEP_OP     GPIO_ResetBits(GPIOB,GPIO_Pin_9);
#define BEEP_CL     GPIO_SetBits(GPIOB,GPIO_Pin_9);

#define POWER_12V_OPEN    GPIO_ResetBits(GPIOC,GPIO_Pin_11)
#define POWER_12V_CLOSE   GPIO_SetBits(GPIOC,GPIO_Pin_11)
#define BEEPOPEN_TIME   2
#define BEEPCLOSE_TIME  2

#define GLINT_TIME  5
#define GLINT_NUM   9
typedef struct
{
	uint8_t en;//使能位
	uint8_t state;
	uint8_t glint_num;//闪烁次数
	uint8_t glint_cycle;//闪烁周期
}LED_ControlTypeDef;

typedef struct
{
	uint8_t en;//使能位
	uint8_t state;
	uint8_t glint_num;//闪烁次数
	uint8_t beep_cycle;//闪烁周期
}Beep_ControlTypeDef;

extern LED_ControlTypeDef LED_Control;
extern LED_ControlTypeDef LED[3];

void LED_Init(void);//初始化
void LED_Set(u8 dri_no);
void LED_Drive(void);

void Beep_Enable(void);
void Beep_Disable(void);
#endif
