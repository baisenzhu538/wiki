#ifndef __SYSTEM_H
#define __SYSTEM_H
#include "task_manage.h"

#include "signal_scan.h"

#include "led.h"

#include "watchdog.h"
#include "ir.h"

void System_Init(void);
void System_TaskRun(void);

#endif
