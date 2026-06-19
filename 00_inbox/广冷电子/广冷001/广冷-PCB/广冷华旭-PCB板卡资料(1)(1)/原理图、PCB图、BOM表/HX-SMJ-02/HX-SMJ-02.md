# HX-SMJ-02

1                                       2                                                                3                            4                       5

A                                                                                                                                                                                                         A

                 DC-DC 3.3V@3A(max) output for 4G module

                                                                                                                                                    VDD_3V3

            VDD_24V                                                                    U41             C78     L2
                                                                                                               15uH/4.5A
                                                                                       TPS54302DDCR 100nF/50v

B                                                                             1   GND  BOOT    6                                                                                                          B
                                                                              2   SW       EN  5
                                                                              3   VIN      FB  4

                                                                                                                          C70   R55      C77
                                                                                                                          68pF  100K 1%  220uF/16v

                            C73                                                                                                                     C76     C75
                                                                                                                                                    100nF   1nF
                 C74        100nF/50v

                 220uF/50V

                                                                                                                                R54                              VDD_3V3_4G     VDD_3V3_WIFI
                                                                                                                                22K 1%

                                                                                                                                                                    VDD_3V3

                                                                                                                                                                    1               SW1
                                                                                                                                                                          2         SS-12D10L4
                                                                                                                                                                                 3
                                                                                                                                                                                                                                              C
                                                                        DGND

C

                            F1                                                                 D2
                            JK30-160
                                                                                               SS56BF VDD_24V

      1  1
      2  2
      3  3

      VH3.96-3A                        C3                                     R4            D1              C4
        JP1                            1nF/2kv                                390KD10       P6SMB24CA       100nF/50v

                                                                                                       DGND

D                PGND                  R5                                     1M                                                                                                                          D

                                       C9 1nF/2kv                                      PGND

                                                                                                                                          TITLE:                                              REV: 1.0

                                                                                                                                                       01-  Company: HX-SMJ-02                Sheet: 1/1

   1                                       2                                                                3                            4                  Date: 2021-10-19 Drawn By: smile-hkz

                                                                                                                                                                                         5
   1                             2                             3                               4                         5

A                                                                                                                                                           A

                                                                              RS232(reserved)

                                                                                          C23
                                                                                       100nF

B                                                                       DGND                           VDD_3V3                                              B

                                                                     C20           U4          VCC 16     C19
                                                                  100nF       15 GND                   100nF

                                                     DGND            C21      6 V-             V+ 2       C22   DGND
                                                                  100nF                                100nF
                                                                              5 C2-            C1- 3                              WIFI_3V3_RXD
                                                                                                                                  WIFI_3V3_TXD
         3       TX2                                                          4 C2+            C1+ 1                             4G_3V3_RXD
         2       RX2                                                                                                             4G_3V3_TXD
      3  1                          R2 33R                                    8                   9
      2                                                                       7                   10
      1                                                                           RIN2   ROUT2
                                                                                  DOUT2    DIN2

                                    R3 33R                                    13                  12
                                                                              14                  11
          RS2         C2  C1                                                      RIN1   ROUT1
      VH3.96-3A                                                                   DOUT1    DIN1
                      11pF 11pF

                                                                                  MAX3232EID

C                DGND                       3  TX1                                                                                                          C
                                            2  RX1
                                    3       1                  R13 33R
                                    2
                                    1

                                                               R14 33R

                                        RS1         C25 C24
                                    VH3.96-3A       11pF 11pF

                                               DGND

D                                                                                                                                                           D

                                                                                                 TITLE:                                         REV: 1.0

                                                                                                              02-TTL232

                                                                                                               Company: HX-SMJ-02               Sheet: 1/1

                                                                                                               Date: 2021-10-19 Drawn By: smile-hkz

   1                             2                             3                               4                         5
   1                2                                 3                                 4                     5

A                                                                                                                                                  A

      VDD_3V3_WIFI            VDD_3V3_WIFI DGND

      C5            C6               R7    1  GND 39GND   GND    38
      100nF         33pF             10K   2  3V3        IO23    37
                                    C31    3  EN         IO22    36
                                    1uF    4  SENSOR_VP  TXD0    35  VDD_3V3_WIFI
                                           5  SENSOR_VN  RXD0    34
      DGND                    DGND         6  IO34       IO21    33
                                           7  IO35               32
                                DGND       8  IO32           NC  31                R8   R9
                                           9  IO33       IO19    30                10K  10K
                                          10  IO25       IO18    29
B                                         11  IO26               28       R1                   WIFI_3V3_TXD                                        B
                                          12  IO27         IO5   27       499                  WIFI_3V3_RXD
                                          13  IO14       IO17    26
                                          14  IO12       IO16    25  R10       33
                                          15  GND                24
      VDD_3V3_WIFI                        16  IO13         IO4   23
                                          17  NC           IO0   22
                                          18  NC           IO2   21
                                          19  NC         IO15    20
                                                             NC
                                                             NC
                                                             NC

      R6                                      U3
      2K
                                          ESP32-WROOM-32UE(4MB)

            LED1
            BL-HUB36G-AV-TRB

C                                                                                                                                                  C

      DGND

D                                                                                                                                                  D

                                                                                        TITLE:                                   REV: 1.0

                                                                                                     03-WIFI

                                                                                                             Company: HX-SMJ-02  Sheet: 1/1

                                                                                                             Date: 2021-10-19 Drawn By: smile-hkz

   1                2                                 3                                 4                     5
   1                                                                       2                                            3                                       4                                   5

                                                             VDD_3V3_4G

                                                                                                                        EC20_VDD_EXT

                                                                                                                                                                                                                               7
                                                                                                                                                                                                                                  8

A                                                                                              R61 R60                                                USIM_DATA R67      22R                              DATA        C7  I/O  GND                  A
                                                                                               4.7K 10K                                                                                                   CLK         C3  CLK     GND
                                                             R63      R64                                                                             USIM_CLK     R68   22R                                          C6  VPP
                                                                                           Q7                                                                                                             RST         C2  RST
                                                             10K      10K                  SS8050

                                                                                           Q8                                                         USIM_RST     R69   22R                                                           CARD1
                                                                                           SS8050                                                                                                                                      SIM-1305-6P
                                      R65 33R                                                                           EC20_RXD_1V8                                                                                  C5  GND  GND
                                                                                                                        EC20_TXD_1V8                                                                                  C1  VCC     S/W
   4G_3V3_RXD                                                                                                                                         USIM_VDD

                                                                                                                                                                                  C69       C71           C72                  10
                                                                                                                                                                                                                                  9

                                                                                                                                                                               33pF/50V 33pF/50V 33pF/50V

                                      R66 33R

   4G_3V3_TXD

                                                                                                                                                                              DGND

                                                                                           4.7K  R70
                                                                                           R62     10K

                                                                                                                        EC20_VDD_EXT                                                                      D5

B                                                                                                                                                                                                         SRV05-4                                   B

                                                                                                                                                                                       DATA 1                      6 USIM_VDD

                                                                                                                                                                         DGND                    2                 5                   VDD_3V3_4G

                                                                                           U7                                                                                          CLK       3                 4      RST
                                                                                           EC20 R2.1 Mini PCIe-C

                                                                  1      MIC_P                   VBAT               2                     VDD_3V3_4G
                                                                  3      MIC_N                    GND               4
                                                                  5      SPK_P                                      6                  USIM_VDD
                                                                                                    NC                                 USIM_DATA
                                                                   7                                                8                  USIM_CLK
                                      EC20_VDD_EXT                 9     SPK_N                    USIM_VDD          10                 USIM_RST
                                                                  11     GND                     USIM_DATA          12
                                                                  13     VDD_EXT                                    14
                                                                         RESERVED                  USIM_CLK
                                                                                                   USIM_RST
                                                                  15 GND                         RESERVED 16

C                                                                 17     RESERVED                             GND   18                                                   VDD_3V3_4G
                                               EC20_RXD_1V8       19     WAKEUP_IN               W_DISABLE#         20
                                               EC20_TXD_1V8                                                                                                                                                                                                                                                C

         VDD_3V3_4G                                               21     GND                        PERST#          22                                                         C39       C40        C67        C68    C79      C7
                                                                  23     UART_RXD                        VBAT       24                                                         100nF                           100nF  100nF    100nF
                                                                  25     UART_RTS                         GND       26                                                                   100nF 100nF
                                                                  27     GND                                        28
                                                                                                 UART_CTS
                                                                  29                                                30
                                                                  31     GND                         UART_DCD       32                                                      DGND
                                                                  33     UART_TXD                WAKEUP_OUT         34
                                                                  35     PERST#                                     36                                R59
                                                                  37     GND                                   GND  38                                 2K
                                                                         GND                             USB_DM
                                                                  39                                      USB_DP    40                 LED2
                                                                  41                                                42
                                                                  43     VBAT                                 GND   44                                          VDD_3V3_4G
                                                                  45     VBAT                   LED_WWAN#           46
                                                                         GND               USIM_PRESENCE                                                                       USIM_VDD
                                                                  47     RESERVED                                   48                 BL-HUB36G-AV-TRB
                                                                  49                                UART_DTR        50
                                                                  51                                                52
                                                                         RESERVED                   NC                                                                         C84       C83        C82
                                                                         RESERVED                 GND                                                                                               33pF
                                                                         RESERVED                VBAT                                                                          100nF 1nF

D                                                                                                                                                                           DGND                                                                    D
                                   1
                                                             DGND                                                       DGND                                     TITLE:  04-4G-PCIE                                                    REV: 1.0

                                                                                        2                                           3                           4              Company: HX-SMJ-02                                      Sheet: 1/1

                                                                                                                                                                               Date: 2021-10-19 Drawn By: smile-hkz

                                                                                                                                                                                                            5
