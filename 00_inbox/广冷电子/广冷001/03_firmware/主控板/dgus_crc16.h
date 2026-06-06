#ifndef	_DGUS_CRC16_H_
#define	_DGUS_CRC16_H_

#include "sys.h"

uint16_t CRC16(uint8_t * puchMsg, uint16_t usDataLen);
uint16_t CRC16_Toggle(uint8_t * puchMsg, uint16_t usDataLen);


#endif	/*_DGUS_CRC16_H_*/

