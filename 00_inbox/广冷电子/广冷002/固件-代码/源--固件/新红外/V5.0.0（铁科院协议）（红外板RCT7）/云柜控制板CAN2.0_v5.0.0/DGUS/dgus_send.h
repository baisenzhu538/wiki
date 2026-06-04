#ifndef	_DGUS_SEND_H_
#define	_DGUS_SEND_H_

#include "dgus_crc16.h"
#include "usart.h"
#include "dgus_struct.h"
#include "dgus_recive.h"





void Dgus_83ReadCmd_Send(u8 * data,u16 datasize);
void Dgus_82WriteCmd_Send(u8 * data,u16 datasize);


#endif	/*_DGUS_SEND_H_*/

