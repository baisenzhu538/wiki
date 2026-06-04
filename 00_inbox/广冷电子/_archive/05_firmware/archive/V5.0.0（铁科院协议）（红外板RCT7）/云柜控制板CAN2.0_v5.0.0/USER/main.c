#include "system.h"

 int main(void)
 {
//	Iap_SetBase();
  System_Init();

	while(1)
	{
		System_TaskRun();
	}
 }

