#include "misc_control.h"

void MiscControl_Init(void)
{
	MiscGpio_Init();
}

void MiscControl_Set(u8 device_no,u8 set)
{
	switch(device_no)
	{
		case 4:
		{
			if(set)
			{
				MiscGpio_MainLight_Enable();
			}
			else
			{
				MiscGpio_MainLight_Disable();
			}
		}
		break;
		default:break;
	}
}