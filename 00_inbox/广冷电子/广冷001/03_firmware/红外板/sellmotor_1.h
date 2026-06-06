#ifndef __SELLMOTOR_H
#define __SELLMOTOR_H

#include "motor_drive.h"

#define  MOTOR_MANAGE_MAXNUN 3


uint8_t SellMotor_SetStar(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch);
void SellMotor_SetStop(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t SellMotor_GetLinkStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t SellMotor_GetBlockStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch);
uint8_t SellMotor_GeOTStateBit(uint8_t dri_no,uint8_t motor_x_ch,uint8_t motor_y_ch);
uint32_t SellMotor_GetLinkState(uint8_t dri_no,uint8_t motor_y_ch);

uint8_t SellMotor_GetRunErrState(uint8_t dri_no);
uint8_t SellMotor_ReadMotorMode(uint8_t dri_no);
uint8_t SellMotor_ReadPositErr(uint8_t dri_no);
uint8_t SellMotor_GetRunState(uint8_t dri_no);

#endif

