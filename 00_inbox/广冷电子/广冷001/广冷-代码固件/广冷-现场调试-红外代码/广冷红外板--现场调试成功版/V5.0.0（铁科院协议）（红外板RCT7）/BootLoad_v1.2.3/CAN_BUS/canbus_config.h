#ifndef __CANBUS_CONFIG_H
#define __CANBUS_CONFIG_H

#define CAN_MASTE_NODE  //设备为主节点
#define CAN_SLAVE_NODE   //设备为从节点

/*各个模块使用的定时器号，不可重复*/


#define CAN_TRANSPORT_TIMETASKNUM_0     0x00
#define CAN_TRANSPORT_TIMETASKNUM_1     0x01
#define CAN_TRANSPORT_LINKESTIMENUM     0x02
#define CAN_SLAVEHEART_OVER_TIMENUM     0x04//从站心跳超时定时器号
#define CAN_SLAVEHEART_TX_TIMENUM       0x05//从站心跳发送定时器号
#define CAN_TRIGGER_TIMENUM             0x03 //定时器触发定时器号
#define CAN_MASTERHEART_TIMENUM         0x08 //主站心跳定时器号
#define CAN_DEVICEMANAGE_TIMENUM        0x09 //设备管理定时器号
#define CAN_TRIGGERRECEIVE_TIMENUM      0x0A




/*malloc 设置*/
#define CAN_MEM_MAXSIZE              15*1024      //动态内存池大小
#define CAN_MEM_BLOCKSIZE            32          //内存块大小
/*transport_queue 设置*/
#define CAN_RX_QUEUELEN              20          //接收队列长度 

/*transport_linkeslist 设置*/
#define CAN_TX_LINKLEN               128         //传输任务链表长度
#define CAN_RESPONSE_OUTTIME         10          //报文响应超时单位时间10ms，总100ms


/*transport_layer 设置*/
#define CAN_RX_SECTIONMSG_NUM        2           //分段报文接收缓冲区数

/*time_task 设置*/
#define CAN_TIMETASK_MAXNUM         256          //允许创建定时器最大数量

/*initiative_task 设置*/
#define CAN_TRGGERTASK_MAXNUM       128         //触发任务最大数量 

/*resport_task 设置*/
#define CAN_RESPONSE_ERRNUM          2           //允许错误响应次数，超过将不在重发
#define CAN_RESPONSE_OVERTIMENUM     2           //允许错误响应次数，超过将不再重发


/*slave_protoco 部分宏定义*/
#define CAN_SLAVEHEART_OVERTIME       300         //心跳超时3s
#define CAN_SLAVEHEART_TXTIME         100         //心跳发送时间间隔


/*master_protoco 部分宏定义*/
#define CAN_MASTERHEART_TXTIME        100

/*device_manage 部分宏定义*/
#define CAN_MASTERHEART_OVERTIME      300      //心跳超时时间
#define CAN_DEVICEMANAGE_LIFETIME     10      //报文响应后，任务存活时间，超过则会删除该任务
#define CAN_ACKTASK_MAXNUM            20       //每个节点最大同时存在20个待响应任务
#define CAN_DEVICE_MAXNUM             64       //设备管理器最多能接入64个节点

/*initiative_receive 设置*/
#define CAN_TRGGERRECEVICE_MAXNUM     256      //最大可设置接收的触发报文数量


#define CAN_TRIGGER_TRANSPORT         //注释不加载触发发送功能，从站有效
#define CAN_TRIGGER_RECEIVE           //注释不加载触发接收功能，主站有效


#endif
