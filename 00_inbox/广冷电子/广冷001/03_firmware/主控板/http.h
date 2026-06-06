#ifndef __HTTP_H
#define __HTTP_H
#include "string.h"
#include "stdio.h"
#include "stdint.h"


typedef struct
{
	int  max_len;
	int  star_len;
	int  end_len;
	int  Content_Length;
	int  sta_code;
	char *data;
}Http_GetResponTypeDef;

int HTTP_Get_Request(const char *url, const char *host,int starlen,int endlen,char (*send)(char*,int));
int HTTP_GET_ResponstParser(const char *pkt,Http_GetResponTypeDef *pGetRespon);
#endif


