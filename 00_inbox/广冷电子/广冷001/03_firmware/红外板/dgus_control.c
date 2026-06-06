#include "dgus_control.h"



void DgusControl_Init(void)
{
	Dgus_Recive_Init();
}

u8 DgusControlBuffer[256];

void DgusControl_ShowSellErrorInfo(int state)
{
	DgusControlBuffer[0] = 0x71;
	DgusControlBuffer[1] = 0x60;
	DgusControlBuffer[2] = state/100+'0';
	DgusControlBuffer[3] = state%100/10+'0';
	DgusControlBuffer[4] = state%10+'0';
	Dgus_82WriteCmd_Send(DgusControlBuffer,5);		
}

void DgusControl_ShowSystemErrorInfo(int state)
{
	DgusControlBuffer[0] = 0x71;
	DgusControlBuffer[1] = 0x20;
	DgusControlBuffer[2] = state/100+'0';
	DgusControlBuffer[3] = state%100/10+'0';
	DgusControlBuffer[4] = state%10+'0';
	Dgus_82WriteCmd_Send(DgusControlBuffer,5);	
}

void DgusControl_ShowSellLogo(char * orderId)
{
	
	DgusControlBuffer[0] = 0x7F;
	DgusControlBuffer[1] = 0x20;
	

	DgusControlBuffer[2] = orderId[0];
	DgusControlBuffer[3] = orderId[1];
	DgusControlBuffer[4] = orderId[2];
	DgusControlBuffer[5] = orderId[3];
	DgusControlBuffer[6] = orderId[4];
	DgusControlBuffer[7] = orderId[5];
	DgusControlBuffer[8] = orderId[6];
	DgusControlBuffer[9] = orderId[7];
	DgusControlBuffer[10] = orderId[8];
	DgusControlBuffer[11] = orderId[9];
	DgusControlBuffer[12] = orderId[10];
	DgusControlBuffer[13] = orderId[11];


	Dgus_82WriteCmd_Send(DgusControlBuffer,14);		
}
void DgusControl_ClearSellLogo(void)
{
	DgusControlBuffer[0] = 0x71;
	DgusControlBuffer[1] = 0x80;	
	Dgus_82WriteCmd_Send(DgusControlBuffer,2);		
}

void DgusControl_ShowErrorInfo(u8 contain_no,u8 shelf_no,u8 motor_no,u32 err1,u32 err2)
{
	u8	str[]="故障信息";
	
	DgusControlBuffer[0] = 0x71;
	DgusControlBuffer[1] = 0x00;
	DgusControlBuffer[2] = str[0];
	DgusControlBuffer[3] = str[1];
	DgusControlBuffer[4] = str[2];
	DgusControlBuffer[5] = str[3];	
	DgusControlBuffer[6] = str[4];
	DgusControlBuffer[7] = str[5];	
	DgusControlBuffer[8] = str[6];
	DgusControlBuffer[9] = str[7];
	DgusControlBuffer[10] = ':';
	DgusControlBuffer[11] = contain_no/10+'0';
	DgusControlBuffer[12] = contain_no%10+'0';
	DgusControlBuffer[13] = '-';
	DgusControlBuffer[14] = shelf_no/10+'0';
	DgusControlBuffer[15] = shelf_no%10+'0';	
	DgusControlBuffer[16] = '-';
	DgusControlBuffer[17] = motor_no/10+'0';
	DgusControlBuffer[18] = motor_no%10+'0';
	DgusControlBuffer[19] = ',';
	DgusControlBuffer[20] = err1/100000+'0';
	DgusControlBuffer[21] = err1%100000/10000+'0';
	DgusControlBuffer[22] = err1%10000/1000+'0';
	DgusControlBuffer[23] = err1%1000/100+'0';
	DgusControlBuffer[24] = err1%100/10+'0';
	DgusControlBuffer[25] = err1%10+'0';
	DgusControlBuffer[26] = ',';
	DgusControlBuffer[27] = err2/100000+'0';
	DgusControlBuffer[28] = err2%100000/10000+'0';
	DgusControlBuffer[29] = err2%10000/1000+'0';
	DgusControlBuffer[30] = err2%1000/100+'0';
	DgusControlBuffer[31] = err2%100/10+'0';
	DgusControlBuffer[32] = err2%10+'0';
	DgusControlBuffer[33] = '.';
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,(34));		
}

void DgusControl_ShowGoodsHistory(u16 addr,u16 year,u8 month,u8 day,u8 hour,u8 min,u8 sec,u8 contain_no,u8 shelf_no,u8 cargo_no,u8 sta,u32 err1,u32 err2)
{
	u8	str1[]="货柜号:";
	u8	str2[]="层架号:";
	u8	str3[]="货道号:";
	u8	str4[]="出货成功";
	u8	str5[]="出货失败";
	u8	str6[]="红外检测成功";
	u8	str7[]="红外检测失败";
	u8	str8[]="红外模块故障";
	u8	str9[]="货道电机正常";
	u8	str10[]="货道电机超时";
	u8	str11[]="货道电机离线";
	
	DgusControlBuffer[0] = addr/256;
	DgusControlBuffer[1] = addr%256;
	DgusControlBuffer[2] = year/1000+'0';
	DgusControlBuffer[3] = year%1000/100+'0';
	DgusControlBuffer[4] = year%100/10+'0';
	DgusControlBuffer[5] = year%10+'0';
	DgusControlBuffer[6] = '-';
	DgusControlBuffer[7] = month/10+'0';
	DgusControlBuffer[8] = month%10+'0';
	DgusControlBuffer[9] = '-';
	DgusControlBuffer[10] = day/10+'0';
	DgusControlBuffer[11] = day%10+'0';
	DgusControlBuffer[12] = ' ';
	DgusControlBuffer[13] = hour/10+'0';
	DgusControlBuffer[14] = hour%10+'0';
	DgusControlBuffer[15] = ':';
	DgusControlBuffer[16] = min/10+'0';
	DgusControlBuffer[17] = min%10+'0';
	DgusControlBuffer[18] = ':';
	DgusControlBuffer[19] = sec/10+'0';
	DgusControlBuffer[20] = sec%10+'0';
	DgusControlBuffer[21] = ' ';
	DgusControlBuffer[22] = '[';
	DgusControlBuffer[23] = str1[0];
	DgusControlBuffer[24] = str1[1];
	DgusControlBuffer[25] = str1[2];
	DgusControlBuffer[26] = str1[3];
	DgusControlBuffer[27] = str1[4];
	DgusControlBuffer[28] = str1[5];
	DgusControlBuffer[29] = str1[6];
	DgusControlBuffer[30] = contain_no/10+'0';
	DgusControlBuffer[31] = contain_no%10+'0';
	DgusControlBuffer[32] = ',';
	DgusControlBuffer[33] = str2[0];
	DgusControlBuffer[34] = str2[1];
	DgusControlBuffer[35] = str2[2];
	DgusControlBuffer[36] = str2[3];
	DgusControlBuffer[37] = str2[4];
	DgusControlBuffer[38] = str2[5];
	DgusControlBuffer[39] = str2[6];
	DgusControlBuffer[40] = shelf_no/10+'0';
	DgusControlBuffer[41] = shelf_no%10+'0';
	DgusControlBuffer[42] = ',';	
	DgusControlBuffer[43] = str3[0];
	DgusControlBuffer[44] = str3[1];
	DgusControlBuffer[45] = str3[2];
	DgusControlBuffer[46] = str3[3];
	DgusControlBuffer[47] = str3[4];
	DgusControlBuffer[48] = str3[5];
	DgusControlBuffer[49] = str3[6];
	DgusControlBuffer[50] = cargo_no/10+'0';
	DgusControlBuffer[51] = cargo_no%10+'0';
	DgusControlBuffer[52] = ',';		
	
	if(sta)
	{
		//出货成功
		DgusControlBuffer[53] = str4[0];
		DgusControlBuffer[54] = str4[1];
		DgusControlBuffer[55] = str4[2];
		DgusControlBuffer[56] = str4[3];
		DgusControlBuffer[57] = str4[4];
		DgusControlBuffer[58] = str4[5];
		DgusControlBuffer[59] = str4[6];	
		DgusControlBuffer[60] = str4[7];
		DgusControlBuffer[61] = ',';				
	}
	else
	{
		//出货失败
		DgusControlBuffer[53] = str5[0];
		DgusControlBuffer[54] = str5[1];
		DgusControlBuffer[55] = str5[2];
		DgusControlBuffer[56] = str5[3];
		DgusControlBuffer[57] = str5[4];
		DgusControlBuffer[58] = str5[5];
		DgusControlBuffer[59] = str5[6];	
		DgusControlBuffer[60] = str5[7];
		DgusControlBuffer[61] = ',';			
	}
	
	if(err1 == 101000)
	{
		//电机正常
		DgusControlBuffer[62] = str9[0];
		DgusControlBuffer[63] = str9[1];
		DgusControlBuffer[64] = str9[2];
		DgusControlBuffer[65] = str9[3];
		DgusControlBuffer[66] = str9[4];
		DgusControlBuffer[67] = str9[5];
		DgusControlBuffer[68] = str9[6];	
		DgusControlBuffer[69] = str9[7];
		DgusControlBuffer[70] = str9[8];	
		DgusControlBuffer[71] = str9[9];
		DgusControlBuffer[72] = str9[10];	
		DgusControlBuffer[73] = str9[11];		
		DgusControlBuffer[74] = ',';	
	}
	else if(err1 == 101301)
	{
		//电机超时
		DgusControlBuffer[62] = str10[0];
		DgusControlBuffer[63] = str10[1];
		DgusControlBuffer[64] = str10[2];
		DgusControlBuffer[65] = str10[3];
		DgusControlBuffer[66] = str10[4];
		DgusControlBuffer[67] = str10[5];
		DgusControlBuffer[68] = str10[6];	
		DgusControlBuffer[69] = str10[7];
		DgusControlBuffer[70] = str10[8];	
		DgusControlBuffer[71] = str10[9];
		DgusControlBuffer[72] = str10[10];	
		DgusControlBuffer[73] = str10[11];		
		DgusControlBuffer[74] = ',';			
	}
	else
	{
		//电机离线
		DgusControlBuffer[62] = str11[0];
		DgusControlBuffer[63] = str11[1];
		DgusControlBuffer[64] = str11[2];
		DgusControlBuffer[65] = str11[3];
		DgusControlBuffer[66] = str11[4];
		DgusControlBuffer[67] = str11[5];
		DgusControlBuffer[68] = str11[6];	
		DgusControlBuffer[69] = str11[7];
		DgusControlBuffer[70] = str11[8];	
		DgusControlBuffer[71] = str11[9];
		DgusControlBuffer[72] = str11[10];	
		DgusControlBuffer[73] = str11[11];		
		DgusControlBuffer[74] = ',';				
	}
	
	if(err2 == 102000)
	{
		//红外正常
		DgusControlBuffer[75] = str6[0];
		DgusControlBuffer[76] = str6[1];
		DgusControlBuffer[77] = str6[2];
		DgusControlBuffer[78] = str6[3];
		DgusControlBuffer[79] = str6[4];
		DgusControlBuffer[80] = str6[5];
		DgusControlBuffer[81] = str6[6];	
		DgusControlBuffer[82] = str6[7];
		DgusControlBuffer[83] = str6[8];	
		DgusControlBuffer[84] = str6[9];
		DgusControlBuffer[85] = str6[10];	
		DgusControlBuffer[86] = str6[11];		
		DgusControlBuffer[87] = ']';
	}
	else if(err2 == 102401)
	{
		//红外检测失败
		DgusControlBuffer[75] = str7[0];
		DgusControlBuffer[76] = str7[1];
		DgusControlBuffer[77] = str7[2];
		DgusControlBuffer[78] = str7[3];
		DgusControlBuffer[79] = str7[4];
		DgusControlBuffer[80] = str7[5];
		DgusControlBuffer[81] = str7[6];	
		DgusControlBuffer[82] = str7[7];
		DgusControlBuffer[83] = str7[8];	
		DgusControlBuffer[84] = str7[9];
		DgusControlBuffer[85] = str7[10];	
		DgusControlBuffer[86] = str7[11];		
		DgusControlBuffer[87] = ']';		
	}
	else
	{
		//红外检测故障
		DgusControlBuffer[75] = str8[0];
		DgusControlBuffer[76] = str8[1];
		DgusControlBuffer[77] = str8[2];
		DgusControlBuffer[78] = str8[3];
		DgusControlBuffer[79] = str8[4];
		DgusControlBuffer[80] = str8[5];
		DgusControlBuffer[81] = str8[6];	
		DgusControlBuffer[82] = str8[7];
		DgusControlBuffer[83] = str8[8];	
		DgusControlBuffer[84] = str8[9];
		DgusControlBuffer[85] = str8[10];	
		DgusControlBuffer[86] = str8[11];		
		DgusControlBuffer[87] = ']';
	}
	Dgus_82WriteCmd_Send(DgusControlBuffer,(88));	
}

void DgusControl_ShowDeviceId(u8 * DeviceId)
{
	u8 i;
	
	DgusControlBuffer[0] = 0x50;
	DgusControlBuffer[1] = 0x00;
	
	for(i=0;i<32;i++)
	{
		DgusControlBuffer[2+i] = DeviceId[i];
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,(34));
}

//首页显示购买二维码
void DgusControl_ShowQRCode(u8 * qrcode,u8 size)
{
	u8 i;
	
	DgusControlBuffer[0] = 0x52;
	DgusControlBuffer[1] = 0x40;
	
	for(i=0;i<size;i++)
	{
		DgusControlBuffer[2+i] = *(qrcode+i);
	}
	DgusControlBuffer[2+size] = 0xFF;
	DgusControlBuffer[2+size+1] = 0xFF;
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,(size+4));
}

void DgusControl_UpTime(u8 year,u8 month,u8 day,u8 week,u8 hour,u8 min,u8 sec)
{
	DgusControlBuffer[0] = 0x00;
	DgusControlBuffer[1] = 0x9C;
	DgusControlBuffer[2] = 0x5A;
	DgusControlBuffer[3] = 0xA5;	
	DgusControlBuffer[4] = year%100;
	DgusControlBuffer[5] = month%13;
	DgusControlBuffer[6] = day%32;
	DgusControlBuffer[7] = hour%24;
	DgusControlBuffer[8] = min%60;
	DgusControlBuffer[9] = sec%60;
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,10);		
}

//首页显示温度
void DgusControl_ShowTemp(u8 temp)
{
	u8 dustr[]="度";
	u8	yichangstr[] ="异常";
	
	if(temp==0xFF)
	{
		DgusControlBuffer[0] = 0x50;
		DgusControlBuffer[1] = 0x80;		
		DgusControlBuffer[2] = yichangstr[0];	
		DgusControlBuffer[3] = yichangstr[1];		
		DgusControlBuffer[4] = yichangstr[2];
		DgusControlBuffer[5] = yichangstr[3];
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,6);		
	}
	else
	{
		if(temp>99)
			temp=99;
		
		DgusControlBuffer[0] = 0x50;
		DgusControlBuffer[1] = 0x80;		
		DgusControlBuffer[2] = ' ';
		DgusControlBuffer[3] = temp/10+0x30;	
		DgusControlBuffer[4] = temp%10+0x30;	
		DgusControlBuffer[5] = ' ';
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,6);		
	}
}

void DgusControl_ShowTemp2(u8 temp)
{
	u8 dustr[]="度";
	u8	yichangstr[] ="异常";
	
	if(temp==0xFF)
	{
		DgusControlBuffer[0] = 0x7F;
		DgusControlBuffer[1] = 0xF0;		
		DgusControlBuffer[2] = yichangstr[0];	
		DgusControlBuffer[3] = yichangstr[1];		
		DgusControlBuffer[4] = yichangstr[2];
		DgusControlBuffer[5] = yichangstr[3];
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,6);		
	}
	else
	{
		if(temp>99)
			temp=99;
		
		DgusControlBuffer[0] = 0x7F;
		DgusControlBuffer[1] = 0xF0;		
		DgusControlBuffer[2] = ' ';
		DgusControlBuffer[3] = temp/10+0x30;	
		DgusControlBuffer[4] = temp%10+0x30;		
		DgusControlBuffer[5] = ' ';
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,6);		
	}
}


//首页显示网络状态
void DgusControl_ShowNetSta(u8 sta)
{
	u8	onlinestr[]="在线";
	u8	unlinestr[]="离线";
	
	DgusControlBuffer[0] = 0x50;
	DgusControlBuffer[1] = 0x60;	

	if(sta)
	{		
		DgusControlBuffer[2] = onlinestr[0];
		DgusControlBuffer[3] = onlinestr[1];		
		DgusControlBuffer[4] = onlinestr[2];
		DgusControlBuffer[5] = onlinestr[3];			
	}
	else
	{
		DgusControlBuffer[2] = unlinestr[0];
		DgusControlBuffer[3] = unlinestr[1];		
		DgusControlBuffer[4] = unlinestr[2];
		DgusControlBuffer[5] = unlinestr[3];			
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,6);	
}


void DgusControl_ShowStoreSta(u8 sta)
{
	u8	str1[]="设备尚未启用";
	u8	str2[]=" 请扫码购物 ";
	
	DgusControlBuffer[0] = 0x51;
	DgusControlBuffer[1] = 0x00;
	
	if(sta)
	{
		DgusControlBuffer[2] = str2[0];
		DgusControlBuffer[3] = str2[1];
		DgusControlBuffer[4] = str2[2];
		DgusControlBuffer[5] = str2[3];
		DgusControlBuffer[6] = str2[4];
		DgusControlBuffer[7] = str2[5];
		DgusControlBuffer[8] = str2[6];
		DgusControlBuffer[9] = str2[7];
		DgusControlBuffer[10] = str2[8];
		DgusControlBuffer[11] = str2[9];
		DgusControlBuffer[12] = str2[10];
		DgusControlBuffer[13] = str2[11];
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,14);	
	}
	else
	{
		DgusControlBuffer[2] = str1[0];
		DgusControlBuffer[3] = str1[1];
		DgusControlBuffer[4] = str1[2];
		DgusControlBuffer[5] = str1[3];
		DgusControlBuffer[6] = str1[4];
		DgusControlBuffer[7] = str1[5];
		DgusControlBuffer[8] = str1[6];
		DgusControlBuffer[9] = str1[7];
		DgusControlBuffer[10] = str1[8];
		DgusControlBuffer[11] = str1[9];
		DgusControlBuffer[12] = str1[10];
		DgusControlBuffer[13] = str1[11];
		
		Dgus_82WriteCmd_Send(DgusControlBuffer,14);	
	}
}

//页切换
void DgusControl_GotoPage(u8 page_no)
{
	DgusControlBuffer[0] = 0x00;
	DgusControlBuffer[1] = 0x84;	
	DgusControlBuffer[2] = 0x5A;
	DgusControlBuffer[3] = 0x01;
	DgusControlBuffer[4] = 0x00;
	DgusControlBuffer[5] = page_no;

	Dgus_82WriteCmd_Send(DgusControlBuffer,6);		
}

//清空文本显示
void DgusControl_ClearText(u16 addr,u8 byte_num)
{
	u8 i;
	
	DgusControlBuffer[0] = addr/256;
	DgusControlBuffer[1] = addr%256;	
	
	for(i=0;i<byte_num;i++)
	{
		DgusControlBuffer[2+i] = 0x20;
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,2+byte_num);			
}


void DgusControl_ShowSellReset(u8 row,u8 list)
{
	switch(row)
	{
		case 0:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		

											
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
					
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
					
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
					
				}
				break;
				default:break;
			}
		}
		break;
		case 1:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xD0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xE0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xF0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x00;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				default:break;
			}
		}
		break;
		case 2:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x10;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
					
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				default:break;
			}
		}
		break;
		case 3:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xD0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xE0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xF0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x00;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x10;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);					
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		case 4:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = ' ';
					DgusControlBuffer[6] = ' ';
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = ' ';
					DgusControlBuffer[12] = ' ';
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					DgusControlBuffer[16] = ' ';
					DgusControlBuffer[17] = ' ';
					DgusControlBuffer[18] = ' ';
					DgusControlBuffer[19] = ' ';

					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		default:break;
	}		
}

void DgusControl_ShowSellColor(u8 row,u8 list,u8 motor_err)
{
	switch(row)
	{
		case 0:
		{
			switch(list)
			{
				case 0:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
					
							
				}
				break;
				case 1:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
					
				}
				break;
				case 2:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
					
				}
				break;
				case 3:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
					
				}
				break;
				default:break;
			}
		}
		break;
		case 1:
		{
			switch(list)
			{
				case 0:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 1:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 2:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 3:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 4:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 5:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 6:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 7:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xB3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xB3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 8:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xC3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xC3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 9:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xD3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xD3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 10:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xE3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xE3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				default:break;
			}
		}
		break;
		case 2:
		{
			switch(list)
			{
				case 0:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xF3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x80;
						DgusControlBuffer[1] = 0xF3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 1:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 2:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 3:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 4:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 5:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 6:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 7:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
				}
				break;
				case 8:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}
					
				}
				break;
				case 9:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 10:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				default:break;
			}
		}
		break;
		case 3:
		{
			switch(list)
			{
				case 0:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 1:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xB3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xB3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 2:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xC3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xC3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 3:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xD3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xD3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 4:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xE3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xE3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 5:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xF3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x81;
						DgusControlBuffer[1] = 0xF3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 6:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x03;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 7:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x13;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 8:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x23;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 9:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x33;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}			
				}
				break;
				case 10:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x43;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				default:break;
			}
		}
		break;
		case 4:
		{
			switch(list)
			{
				case 0:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x53;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 1:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x63;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 2:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x73;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				case 3:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x83;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 4:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0x93;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}	
				}
				break;
				case 5:
				{
					if(motor_err)
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0xF8;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
					}
					else
					{
						DgusControlBuffer[0] = 0x82;
						DgusControlBuffer[1] = 0xA3;
						DgusControlBuffer[2] = 0x00;
						DgusControlBuffer[3] = 0x00;
						Dgus_82WriteCmd_Send(DgusControlBuffer,4);	
					}		
				}
				break;
				default:break;
			}
		}
		break;
		default:break;
	}	
}

void DgusControl_ShowMotorCheckColor(u8 sta)
{
	DgusControlBuffer[0] = 0x83;
	DgusControlBuffer[1] = 0x03;	
	
	if(sta)
	{
		DgusControlBuffer[2] = 0x00;
		DgusControlBuffer[3] = 0x00;
	}
	else
	{
		DgusControlBuffer[2] = 0xF8;
		DgusControlBuffer[3] = 0x00;
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,4);			
}

void DgusControl_ShowIrCheckColor(u8 sta)
{
	DgusControlBuffer[0] = 0x83;
	DgusControlBuffer[1] = 0x13;	
	
	if(sta)
	{
		DgusControlBuffer[2] = 0x00;
		DgusControlBuffer[3] = 0x00;
	}
	else
	{
		DgusControlBuffer[2] = 0xF8;
		DgusControlBuffer[3] = 0x00;
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,4);		
}

void DgusControl_ShowMotorCheck(u8 sta)
{
	u8 str1[]="驱动板正常";
	u8 str2[]="驱动板故障";
	
	DgusControlBuffer[0] = 0x78;
	DgusControlBuffer[1] = 0x20;
	
	if(sta)
	{
		DgusControlBuffer[2] = str1[0];
		DgusControlBuffer[3] = str1[1];
		DgusControlBuffer[4] = str1[2];
		DgusControlBuffer[5] = str1[3];
		DgusControlBuffer[6] = str1[4];
		DgusControlBuffer[7] = str1[5];
		DgusControlBuffer[8] = str1[6];
		DgusControlBuffer[9] = str1[7];
		DgusControlBuffer[10] = str1[8];
		DgusControlBuffer[11] = str1[9];	
	}
	else
	{
		DgusControlBuffer[2] = str2[0];
		DgusControlBuffer[3] = str2[1];
		DgusControlBuffer[4] = str2[2];
		DgusControlBuffer[5] = str2[3];
		DgusControlBuffer[6] = str2[4];
		DgusControlBuffer[7] = str2[5];
		DgusControlBuffer[8] = str2[6];
		DgusControlBuffer[9] = str2[7];
		DgusControlBuffer[10] = str2[8];
		DgusControlBuffer[11] = str2[9];
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,12);	
}

void DgusControl_ShowIrCheck(u8 sta)
{
	u8 str1[]="掉货检测正常";
	u8 str2[]="掉货检测故障";
	
	DgusControlBuffer[0] = 0x78;
	DgusControlBuffer[1] = 0x30;
	
	if(sta)
	{
		DgusControlBuffer[2] = str1[0];
		DgusControlBuffer[3] = str1[1];
		DgusControlBuffer[4] = str1[2];
		DgusControlBuffer[5] = str1[3];
		DgusControlBuffer[6] = str1[4];
		DgusControlBuffer[7] = str1[5];
		DgusControlBuffer[8] = str1[6];
		DgusControlBuffer[9] = str1[7];
		DgusControlBuffer[10] = str1[8];
		DgusControlBuffer[11] = str1[9];
		DgusControlBuffer[12] = str1[10];
		DgusControlBuffer[13] = str1[11];		
	}
	else
	{
		DgusControlBuffer[2] = str2[0];
		DgusControlBuffer[3] = str2[1];
		DgusControlBuffer[4] = str2[2];
		DgusControlBuffer[5] = str2[3];
		DgusControlBuffer[6] = str2[4];
		DgusControlBuffer[7] = str2[5];
		DgusControlBuffer[8] = str2[6];
		DgusControlBuffer[9] = str2[7];
		DgusControlBuffer[10] = str2[8];
		DgusControlBuffer[11] = str2[9];
		DgusControlBuffer[12] = str2[10];
		DgusControlBuffer[13] = str2[11];	
	}
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,14);	
}

void DgusControl_ClearMotorCheck(void)
{
	DgusControlBuffer[0] = 0x78;
	DgusControlBuffer[1] = 0x20;

	DgusControlBuffer[2] = ' ';
	DgusControlBuffer[3] = ' ';
	DgusControlBuffer[4] = ' ';
	DgusControlBuffer[5] = ' ';
	DgusControlBuffer[6] = ' ';
	DgusControlBuffer[7] = ' ';
	DgusControlBuffer[8] = ' ';
	DgusControlBuffer[9] = ' ';
	DgusControlBuffer[10] = ' ';
	DgusControlBuffer[11] = ' ';
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,12);		
}

void DgusControl_ClearIrCheck(void)
{
	DgusControlBuffer[0] = 0x78;
	DgusControlBuffer[1] = 0x30;

	DgusControlBuffer[2] = ' ';
	DgusControlBuffer[3] = ' ';
	DgusControlBuffer[4] = ' ';
	DgusControlBuffer[5] = ' ';
	DgusControlBuffer[6] = ' ';
	DgusControlBuffer[7] = ' ';
	DgusControlBuffer[8] = ' ';
	DgusControlBuffer[9] = ' ';
	DgusControlBuffer[10] = ' ';
	DgusControlBuffer[11] = ' ';
	DgusControlBuffer[12] = ' ';
	DgusControlBuffer[13] = ' ';	
	
	Dgus_82WriteCmd_Send(DgusControlBuffer,14);		
}

//自检结果显示
u8	str1[] = "正常";
u8	str2[] = "故障";
void DgusControl_ShowSellTest(u8 row,u8 list,u8	motor_err)
{
	
	switch(row)
	{
		case 0:
		{
			switch(list)
			{
				case 0:
				{

					
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);	
					

					
							
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		case 1:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xD0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xE0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x75;
					DgusControlBuffer[1] = 0xF0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x00;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				default:break;
			}
		}
		break;
		case 2:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x10;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		case 3:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xD0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xE0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x76;
					DgusControlBuffer[1] = 0xF0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x00;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x10;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 6:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x20;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 7:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x30;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 8:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x40;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 9:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x50;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);				
				}
				break;
				case 10:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x60;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		case 4:
		{
			switch(list)
			{
				case 0:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x70;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 1:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x80;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 2:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0x90;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				case 3:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xA0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 4:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xB0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);		
				}
				break;
				case 5:
				{
					DgusControlBuffer[0] = 0x77;
					DgusControlBuffer[1] = 0xC0;
					DgusControlBuffer[2] = ' ';
					DgusControlBuffer[3] = ' ';
					DgusControlBuffer[4] = ' ';
					DgusControlBuffer[5] = (row+1)/10+0x30;
					DgusControlBuffer[6] = (row+1)%10+0x30;
					DgusControlBuffer[7] = ' ';
					DgusControlBuffer[8] = ' ';
					DgusControlBuffer[9] = ' ';
					DgusControlBuffer[10] = ' ';
					DgusControlBuffer[11] = (list+1)/10+0x30;
					DgusControlBuffer[12] = (list+1)%10+0x30;
					DgusControlBuffer[13] = ' ';
					DgusControlBuffer[14] = ' ';
					DgusControlBuffer[15] = ' ';
					if(!motor_err)
					{
						DgusControlBuffer[16] = str1[0];
						DgusControlBuffer[17] = str1[1];
						DgusControlBuffer[18] = str1[2];
						DgusControlBuffer[19] = str1[3];
					}
					else
					{
						DgusControlBuffer[16] = str2[0];
						DgusControlBuffer[17] = str2[1];
						DgusControlBuffer[18] = str2[2];
						DgusControlBuffer[19] = str2[3];
					}
					
					Dgus_82WriteCmd_Send(DgusControlBuffer,20);			
				}
				break;
				default:break;
			}
		}
		break;
		default:break;
	}
}