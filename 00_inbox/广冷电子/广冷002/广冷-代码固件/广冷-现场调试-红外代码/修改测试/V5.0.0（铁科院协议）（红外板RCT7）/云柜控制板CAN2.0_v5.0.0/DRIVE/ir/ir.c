#include "ir.h"

//8个灯珠一组，4ms内完成一轮扫描，
//4051选通接收灯珠，595依次开启发射灯珠，开启500us后？
//确认有无接收到。

Ir_TypeDef	IrTask;

/**
 * @brief 简单延时函数
 * @param cnt 延时计数（通过循环次数控制延时长度）
 * @note 实际延时时间与CPU主频相关，用于控制硬件操作的时序
 */
void Ir_Delay(u32 cnt)
{
	u32 i;
	
	for(i=0;i<cnt;i++)
	{
		while(0);
	}
}

/**
 * @brief 通过595移位寄存器控制发射灯珠的开启/关闭
 * @param no 发射灯珠编号（0-7，对应8个灯珠）
 * @param enable 使能标志（1：开启对应发射灯珠；0：关闭所有发射灯珠）
 * @note 595是串行输入并行输出的移位寄存器，通过SRCLK（移位时钟）、RCLK（锁存时钟）控制
 *       此处控制的是发射灯珠的驱动信号，QD1、QD3为595的输出引脚（可能对应不同组发射管）
 */
void Ir_Select_Send(u8 no,u8 enable)
{
	u8 i;
	u16 mask;// 用于生成串行输出的位掩码
	
	if(enable)
		mask=((u16)0x0001<<no);// 0101-->0001 // 使能时，仅对应编号的位为1（选通单个发射灯珠）
	else
		mask=0;// 不使能时，所有位为0（关闭所有发射灯珠）

	IR_595_RCLK=0;// 锁存时钟拉低（准备接收移位数据）
	Ir_Delay(15); // 短暂延时，确保电平稳定
	for(i=0;i<16;i++) // 循环16次（2组595，控制两组8位发射灯珠），串行输出数据
	{
		IR_595_SRCLK=0;// 移位时钟拉低（准备输入一位数据）
		Ir_Delay(15);
		
		 // 判断当前位是否需要输出高电平
		if(mask&((u16)0x8000>>i)) // 从高位到低位依次输出（0x8000是16位的最高位）
		{
			IR_595_QD1=1;// 输出高电平，开启对应发射灯珠（QD1通道）
//      IR_595_QD3=1;// 不屏蔽 QD3通道暂不使用
		}
		else
		{
			IR_595_QD1=0;// 输出低电平，关闭QD1通道
			IR_595_QD3=0;// 关闭QD3通道
		}
		Ir_Delay(15);// 确保数据稳定
		
		IR_595_SRCLK=1;// 移位时钟拉高（将当前位数据移入595）
		
		Ir_Delay(15);// 确保移位完成
		
	}
	IR_595_RCLK=1;// 锁存时钟拉高（将移位寄存器中的数据输出到并行端口）
	Ir_Delay(15); // 确保锁存完成
}

/**
 * @brief 通过4051多路选择器读取接收灯珠的状态
 * @param no 接收灯珠编号（0-7，对应8个灯珠，通过4051的A/B/C引脚选通）
 * @return 接收状态（1：检测到有效信号；0：未检测到）
 * @note 4051是8选1多路选择器，通过A/B/C三个控制引脚选择8个通道中的一个
 *       此处读取4个接收输入（IN1-IN4），最终根据IN3和IN4的状态判断是否有效
 */
u8 Ir_Read_Recive(u8 no)
{
	// 根据编号配置4051的A/B/C控制引脚（选通对应的接收通道）
	switch(no)
	{
		case 0:// 选通通道0
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
		case 1:
		{
			IR_4051_A=1;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
		case 2:
		{
			IR_4051_A=0;
			IR_4051_B=1;
			IR_4051_C=0;			
		}
		break;
		case 3:
		{
			IR_4051_A=1;
			IR_4051_B=1;
			IR_4051_C=0;			
		}
		break;
		case 4:
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=1;			
		}
		break;
		case 5:
		{
			IR_4051_A=1;
			IR_4051_B=0;
			IR_4051_C=1;			
		}
		break;
		case 6:
		{
			IR_4051_A=0;
			IR_4051_B=1;
			IR_4051_C=1;			
		}
		break;
		case 7:
		{
			IR_4051_A=1;
			IR_4051_B=1;
			IR_4051_C=1;			
		}
		break;
		default: // 默认选通通道0
		{
			IR_4051_A=0;
			IR_4051_B=0;
			IR_4051_C=0;			
		}
		break;
	}

	// 读取4个接收输入的状态，存储到IrTask中（供调试或扩展使用）
	if(IR_4051_IN1) // IN1状态（1：有信号，0：无信号）
		IrTask.x1=1;
	else
		IrTask.x1=0;
	
	if(IR_4051_IN2)
		IrTask.x2=1;
	else
		IrTask.x2=0;
	
	if(IR_4051_IN3)
		IrTask.x3=1;
	else
		IrTask.x3=0;
	
	if(IR_4051_IN4)
		IrTask.x4=1;
	else
		IrTask.x4=0;	

//	if((IR_4051_IN1&&IR_4051_IN2)||(IR_4051_IN3&&IR_4051_IN4))
//	if(IR_4051_IN1&&IR_4051_IN2&&IR_4051_IN3&&IR_4051_IN4)
	
	if(IR_4051_IN3&&IR_4051_IN4) // 核心判断：仅当IN3和IN4同时有信号时，认为接收到有效反射
//	if(IR_4051_IN1&&IR_4051_IN2)
		return 1;// 有效接收
	else
		return 0;// 无效接收
}


/**
 * @brief 红外扫描任务主函数（状态机实现）
 * @note 循环扫描8个灯珠，每个灯珠的扫描流程分为4个步骤，总周期控制在4ms内
 *       通过状态机（step）控制开启发射、检测接收、关闭发射、验证状态的流程
 */
void Ir_Scan_Task(void)
{

	// 控制总使能引脚
	if(IrTask.sta==0xFF) // 若所有灯珠都检测到信号（sta全1）
	{
		IR_LEVEL_OUT=1;// 开启电平输出
		IR_LED_OUT=1;  // 开启LED指示
	}
	else
	{
		IR_LEVEL_OUT=0;// 关闭电平输出
		IR_LED_OUT=0;  // 关闭LED指示
	}
	
	// 状态机：控制单个灯珠的扫描流程
	switch(IrTask.step)
	{
		case 0://选择发射管，接收管。(开) -- 步骤0：开启当前编号的发射灯珠和接收通道
		{		
			Ir_Read_Recive(IrTask.no);	// 预先选通接收通道（确保通道稳定）		
			Ir_Select_Send(IrTask.no,1);// 开启编号为no的发射灯珠
			
			IrTask.step=1;     // 进入下一步
			IrTask.scan_cnt=10;// 步骤1的延时计数（控制检测时长）
			IrTask.ok_cnt_on=0; // 重置发射开启时的有效计数
		}
		break;
		case 1:// 步骤1：发射开启时，持续检测接收信号
		{
			if(Ir_Read_Recive(IrTask.no))// 若接收有效，累加有效计数
			{
				IrTask.ok_cnt_on++;
			}
			
			if(IrTask.scan_cnt)// 延时计数递减，直到为0（确保信号稳定）
				IrTask.scan_cnt--;
			else
			{
				IrTask.step=2;// 进入下一步
			}
		}
		break;
		case 2://选择发射管，接收管。(关) -- 步骤2：关闭当前编号的发射灯珠
		{
			Ir_Select_Send(IrTask.no,0);// 关闭编号为no的发射灯珠	
			
			IrTask.step=3;// 进入下一步
			IrTask.scan_cnt=5;// 步骤3的延时计数（控制验证时长）
			IrTask.ok_cnt_off=0;// 重置发射关闭时的无效计数
		}
		break;
		case 3:// 步骤3：发射关闭时，验证接收信号是否消失（排除干扰）
		{	
			if(!Ir_Read_Recive(IrTask.no))// 若接收无效（信号消失），累加无效计数
			{
				IrTask.ok_cnt_off++;
			}
			
			// 延时计数递减，直到为0（完成验证）
			if(IrTask.scan_cnt)
				IrTask.scan_cnt--;
			else
			{
				if(IrTask.ok_cnt_off>2&&IrTask.ok_cnt_on>1)// 综合判断：关闭时无效计数>2 且 发射开启时有效计数>1，认为检测有效
				{
					IrTask.sta|=0x1<<IrTask.no;// 标记当前灯珠为"检测到"（对应bit置1）
				}
				else
				{
					IrTask.sta &=~(0x1<<IrTask.no);// 标记当前灯珠为"未检测到"（对应bit清0）
				}
				IrTask.step=4;// 进入下一步
				IrTask.no++;  // 切换到下一个灯珠
				IrTask.no%=8; // 循环扫描8个灯珠（0-7）
				IrTask.scan_cnt=10;// 步骤4的延时计数（间隔时间）				
			}
		}
		break;
		case 4:// 步骤4：扫描间隔（确保灯珠切换时信号稳定）
		{
			if(IrTask.scan_cnt)
				IrTask.scan_cnt--;
			else
			{
				IrTask.step=0;// 回到步骤0，开始下一个灯珠的扫描
			}
		}
		break;
	}
}

/**
 * @brief 红外模块初始化函数
 * @note 配置控制发射（595）和接收（4051）的GPIO引脚，设置输入/输出模式
 */
void Ir_Init(void)
{
	GPIO_InitTypeDef  GPIO_InitStructure;// GPIO初始化结构体
  
	// 使能GPIOA、GPIOB、GPIOC的时钟（根据实际硬件连接配置）
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA
							|RCC_APB2Periph_GPIOB
							|RCC_APB2Periph_GPIOC, ENABLE);	
  
	// 配置发射控制引脚（595的SRCLK、RCLK等）为推挽输出
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; // 推挽输出（强驱动能力）		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;// 50MHz高速
	
//	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2;	 
//	GPIO_Init(GPIOA, &GPIO_InitStructure);	
  
	// 配置GPIOB的Pin1、Pin2（可能是595的控制引脚）
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_1|GPIO_Pin_2;	 
	GPIO_Init(GPIOB, &GPIO_InitStructure);	

	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP; 		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_1|GPIO_Pin_2;// 配置GPIOA的Pin0、Pin1、Pin2（可能是4051的A/B/C控制引脚）	 
	GPIO_Init(GPIOA, &GPIO_InitStructure);		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_13|GPIO_Pin_14|GPIO_Pin_15|GPIO_Pin_6;  // 配置GPIOC的Pin13、Pin14、Pin15、Pin6（可能是595的数据线或其他控制引脚）	 
	GPIO_Init(GPIOC, &GPIO_InitStructure);	
	
	
	// 配置接收输入引脚（4051的IN1-IN4）为浮空输入
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_IN_FLOATING;// 浮空输入（不接上下拉，由外部信号决定） 		
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
		
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0|GPIO_Pin_14|GPIO_Pin_15;// 配置GPIOB的Pin0、Pin14、Pin15（可能是IN1-IN3接收引脚）	 
	GPIO_Init(GPIOB, &GPIO_InitStructure);	
	
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_5;// 配置GPIOC的Pin5（可能是IN4接收引脚）	 
	GPIO_Init(GPIOC, &GPIO_InitStructure);	
  
	// 初始化595的时钟引脚为低电平（初始状态）
	IR_595_RCLK=0; // 锁存时钟初始为低
	IR_595_SRCLK=0;// 移位时钟初始为低
}
