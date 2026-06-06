#include "http.h"
#include "stdlib.h"
#include "sys_malloc.h"
#include "cloud_protocol.h"


int HTTP_Get_Request(const char *url, const char *host,int starlen,int endlen,char (*send)(char*,int))
{
  char*pkt;
	pkt=SysMem_malloc(1024);
	if(pkt==NULL)
		return -1;
	
	sprintf(pkt,"GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: GeneralDownloadApplication\r\nRange: bytes=%d-%d\r\nAccept: */*\r\nConnection: keep-alive\r\nDeviceId: %s\r\n\r\n", url,host,starlen,endlen,(char*)DeviceId);
//	sprintf(pkt, "Host: %s\r\n", host);
//	sprintf(pkt, "User-Agent: GeneralDownloadApplication\r\n");
//	sprintf(pkt, "Range: bytes=%d-%d\r\n", starlen,endlen);
//	sprintf(pkt, "Accept: */*\r\n");
//  sprintf(pkt, "Connection: close\r\n");
//  sprintf(pkt, "\r\n");
  if(send)
	{
	 send(pkt,strlen(pkt));
	 SysMem_free(pkt);
	}
	else
	{
		SysMem_free(pkt);
		return -2;
	}
	return 1;
}



//int HTTP_GET_ResponstParser(const char *pkt,char *databuf)
//{
//  char *data;
//	uint32_t len;
//	http_parser *parser;
//	size_t parsed;
//	http_parser_settings settings_null={
//		                                  NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL
//	                                   };
//	parser=SysMem_malloc(sizeof(http_parser));
//	if(parser==NULL)
//		return NULL;
//	http_parser_init(parser, HTTP_RESPONSE);
//	parsed = http_parser_execute(parser, &settings_null, pkt, strlen(pkt));
//  
//	if(parser->content_length>0&&parser->status_code==200)
//	{
//		len=parser->content_length;
//		data=strstr(pkt,"\r\n\r\n"); 
//		if(data==NULL)
//		{
//		 SysMem_free(parser);
//		 return NULL;
//		}
//		SysMem_copy(databuf,data+8,parser->content_length);
//		SysMem_free(parser);
//		return len;
//  }
//	SysMem_free(parser);
//  return 	NULL;
//}

int HTTP_GET_ResponstParser(const char *pkt,Http_GetResponTypeDef *pGetRespon)
{
	int temp1 = 0;
	
  char *data;
	uint32_t len;
	if(pkt==NULL||pGetRespon==NULL)
		return -1;
  data=strstr(pkt,"HTTP/1.1 ");
	if(data==NULL)
		return -1;//数据不符合
	pGetRespon->sta_code=atoi(data+strlen("HTTP/1.1 "));//获取状态
	
	data=strstr(data+strlen("HTTP/1.1 "),"206 Partial Content");
	if(data==NULL)
	{
		return -2;//响应异常
	}
	data=strstr(pkt,"Content-Length: ");
	if(data==NULL)
	{
		return -3;//数据丢失
	}
	pGetRespon->Content_Length=atoi(data+strlen("Content-Length: "));

	data=strstr(pkt,"Content-Range: bytes ");
	if(data==NULL)
		return -3;
	pGetRespon->star_len=atoi(data+strlen("Content-Range: bytes "));
	data=strstr(data+strlen("Content-Range: bytes "),"-");
	if(data==NULL)
		return -3;
	pGetRespon->end_len=atoi(data+strlen("-"))+1;
	data=strstr(data+strlen("-"),"/");
	if(data==NULL)
		return -3;
	pGetRespon->max_len=atoi(data+strlen("/"));
	data=strstr(pkt,"\r\n\r\n");  

	if(data==NULL)
		return -3;
	if(pGetRespon->data==NULL&&pGetRespon->Content_Length!=NULL)
		return -4;//数据段未分配空间
	
	temp1 = strlen(data+strlen("\r\n\r\n"));//test
	SysMem_copy(pGetRespon->data,data+strlen("\r\n\r\n"),pGetRespon->Content_Length);
  return 	1;
}














