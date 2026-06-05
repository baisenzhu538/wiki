# 嵌入式自检模式（BIST）设计与实现

> 路径：`90_control/electronics-practice/bist-self-test-playbook.md`
>
> 在不使用示波器、万用表的情况下，让板子自己报告内部状态。

## 核心理念

```
普通固件：只管干活，坏了就说"坏了"
自检固件：能回答"哪个环节坏了？信号走到哪一步了？"
```

**BIST 不是测试阶段的一个技巧，是每个固件都应该内置的能力。**

## 一、最简单的自检：上电握手

每个固件上电后做的第一件事（甚至在 main() 之前）——用唯一的亮灯模式告诉观察者"我活着，且我是这个版本"。

```c
void PowerOnSelfTest(void)
{
    // 版本闪码：长闪=版本号
    for (int i = 0; i < FIRMWARE_VERSION; i++) {
        LED_ON;  Delay(200);  LED_OFF;  Delay(200);
    }
    Delay(1000);
    // 快速闪烁 3 次 = 自检通过
    for (int i = 0; i < 3; i++) {
        LED_ON;  Delay(100);  LED_OFF;  Delay(100);
    }
}
```

作用：不用任何工具，上电看灯闪几次就知道固件版本和自检结果。

## 二、两种自检模式

### 模式 1：按键触发式

上电时检测某个引脚电平（如按住按钮）→ 进入自检模式。

```c
void main(void)
{
    SystemInit();
    if (GPIO_ReadInputPin(BOOT_BUTTON_PIN) == 0) {
        EnterSelfTestMode();  // 按住按钮上电 → 自检模式
    }
    // 正常主循环
}
```

### 模式 2：串口命令式

运行时通过串口接收命令进入自检。

```
> selftest
CH0: TX ON ✓  | RX 145mV | MUX CH0 ✓ | OPAMP OK
CH1: TX ON ✓  | RX 132mV | MUX CH1 ✓ | OPAMP OK
...
> set rclk_delay 200
OK
> get rclk_delay
200
```

不需要示波器，不需要万用表——板子自己量自己，通过串口告诉你是哪一级出了问题。

## 三、固件参数配置化

这是"智进化"的核心支撑——**改参数不需要重新编译烧录。**

### 当前做法（不推荐）

```c
#define RCLK_DELAY 200      // 改参数 → 改源码 → 重新编译 → 重新烧录
```

### 推荐做法

```c
// 参数结构体，可从串口运行时修改
typedef struct {
    uint16_t rclk_delay;     // RCLK 后延时 (μs)
    uint16_t srclk_delay;    // SRCLK 后延时 (μs)
    uint16_t scan_interval;  // 通道扫描间隔 (μs)
    uint8_t  channels;       // 启用通道数 (bitmask)
} SystemConfig;

SystemConfig g_config = {
    .rclk_delay    = 200,
    .srclk_delay   = 50,
    .scan_interval = 1000,
    .channels      = 0xFFFF,  // 全部启用
};

// 串口命令处理
void ProcessUartCommand(char *cmd)
{
    if (strncmp(cmd, "set ", 4) == 0) {
        char *param = cmd + 4;
        char *eq = strchr(param, '=');
        if (eq) {
            *eq++ = '\0';
            int val = atoi(eq);
            if (strcmp(param, "rclk_delay") == 0)    g_config.rclk_delay = val;
            if (strcmp(param, "srclk_delay") == 0)   g_config.srclk_delay = val;
            if (strcmp(param, "scan_interval") == 0) g_config.scan_interval = val;
            printf("OK: %s = %d\n", param, val);
            SaveConfig(&g_config);  // 保存到 EEPROM/Flash
        }
    }
    if (strcmp(cmd, "selftest") == 0) { RunSelfTest(); }
    if (strcmp(cmd, "status") == 0)   { PrintStatus(); }
}
```

**效果**：调试新功能时不需要反复编译——直接在串口改参数，看效果，合适了就写进配置。每次调试都是系统自己学习参数的过程。

## 四、故障树驱动的自检报告

BIST 的最高级形态：不只是一级级报状态，而是直接输出故障树分析结果。

```c
void RunSelfTest(void)
{
    printf("=== 自检开始 ===\n");
    
    // 1. 电源检测
    printf("[PWR] VDD_5V=%d mV ", ReadVoltage(VDD_5V_PIN));
    printf(ReadVoltage(VDD_5V_PIN) > 4500 ? "✓\n" : "✗\n");
    
    // 2. 发射链路检测
    printf("[TX] ");
    ForceTxOn();
    if (DetectTxCurrent() > EXPECTED_TX_MA) {
        printf("发射管电流正常 ✓\n");
    } else {
        printf("发射管电流异常 ✗\n");
    }
    ForceTxOff();
    
    // 3. 接收链路检测
    printf("[RX] ");
    for (int ch = 0; ch < 16; ch++) {
        uint16_t val = ReadReceiverChannel(ch);
        printf("CH%d=%d ", ch, val);
    }
    printf("\n");
    
    // 4. 通信检测
    printf("[CAN] %s\n", CanBusTest() ? "✓" : "✗");
    
    printf("=== 自检结束 ===\n");
}
```

## 五、项目落地规范

每个固件项目必须包含：

| 组件 | 必须？ | 说明 |
|:----|:----:|:------|
| 上电闪码 | ✅ | 版本号 + 自检结果 |
| 自检模式入口 | ✅ | 按键或串口触发 |
| 参数运行时修改 | ✅ | 至少支持关键时序参数 |
| 参数持久化 | ⚠️ | 有 EEPROM/Flash 则做 |
| 故障树自检 | 🔲 | 复杂系统推荐 |

## 六、关联

- `diagnostic-firmware-skills.md` — 诊断版固件套路（BIST 的调试阶段前身）
- `project-standards.md` — 项目基线规则（BIST 作为基线的一部分）
