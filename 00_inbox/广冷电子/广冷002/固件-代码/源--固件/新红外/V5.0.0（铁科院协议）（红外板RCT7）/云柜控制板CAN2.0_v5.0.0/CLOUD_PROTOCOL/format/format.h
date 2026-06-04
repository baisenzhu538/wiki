#ifndef	_FORMAT_H_
#define	_FORMAT_H_

#include "sys.h"

void Format_Init(void);

int wifiSsid_GB2312_TO_UTF8(u8 * utf8_buf,u8 * gbk_buf,u8 gbk_len);


#endif	/*_FORMAT_H_*/