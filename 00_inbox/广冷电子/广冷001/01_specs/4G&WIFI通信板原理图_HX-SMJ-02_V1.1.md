# 4G&WIFI通信板原理图_HX-SMJ-02_V1.1

1                                                                  2                                 3                                          4                                             5

                                                   VDD_3V3_4G

                                                                                                         EC20_VDD_EXT                                                                                                      7
                                                                                                  R60                                                                                                                         8
                                                                                                  10K
A                                                      R63       R64               R61                                                   USIM_DATA R67 33R                                            DATA        C7  I/O  GND                  A
                                                                                   4.7K                  EC20_RXD_1V8                                                                                 CLK         C3  CLK     GND
                                                       10K       10K                                                                     USIM_CLK     R68 33R                                                     C6  VPP
                                                                               Q7                        EC20_TXD_1V8                                                                                 RST         C2  RST
                                                                               SS8050                                                    USIM_RST     R69 33R                                                                      CARD1
                                                                                                  R70                                                                                                                              SIM-1305-6P
                                          R65 33R                              Q8                 10K                                                                                                             C5  GND  GND
                                                                               SS8050                                                                                                                             C1  VCC     S/W
   4G_3V3_RXD                                                                                            EC20_VDD_EXT                    USIM_VDD
                                                                         4.7K
                                                                         R62                                                                                                 C69         C71          C72                  10
                                                                                                                                                                                                                              9

                                                                                                                                                                             33pF/50V 33pF/50V 33pF/50V

                                          R66 33R

   4G_3V3_TXD

                                                                                                                                                               DGND

              3.3V1.3V                                                                                                                                                                                D5

B                                                                                                                                                                                                     SRV05-4                                   B

                                                                                                                                                                                    DATA 1                     6 USIM_VDD

                                                                                                                                                                       DGND                   2                5                   VDD_3V3_4G

                                                                                                                                         4G_SIM                                     CLK       3                4      RST

                                                                      U7
                                                                      EC20 R2.1 Mini PCIe-C

                                                   1   MIC_P             VBAT                 2            VDD_3V3_4G
                                                   3   MIC_N              GND                 4
                                                                                                        USIM_VDD
   EC20_VDD_EXT                                     5  SPK_P                          NC      6         USIM_DATA
                                                    7  SPK_N              USIM_VDD            8         USIM_CLK
                                                    9  GND               USIM_DATA            10        USIM_RST
                                                   11  VDD_EXT             USIM_CLK           12

                                                   13  RESERVED          USIM_RST             14
                                                   15  GND               RESERVED             16

C                                                  17 RESERVED           GND 18                         VDD_3V3_4G                                          VDD_3V3_4G
                            EC20_RXD_1V8
                            EC20_TXD_1V8                                                                              R59                                                                                                                                                                     C
                                                                                                                      2K
              VDD_3V3_4G                           19  WAKEUP_IN         W_DISABLE#           20                                                                             C39       C40       C67       C68    C79      C7
                                                   21  GND                       PERST#       22                           LED2                                              100nF                         100nF  100nF    100nF
                                                   23  UART_RXD                      VBAT     24                       BL-HUB36G-AV-TRB                                                100nF 100nF
                                                   25  UART_RTS                       GND     26

                                                   27  GND                    UART_CTS        28                                                            DGND
                                                   29  GND                   UART_DCD         30
                                                   31  UART_TXD          WAKEUP_OUT           32
                                                   33  PERST#                                 34
                                                   35  GND                             GND    36
                                                                                 USB_DM
                                                   37                                         38
                                                   39  GND                         USB_DP     40                                                                             USIM_VDD
                                                   41  VBAT                              GND  42
                                                   43  VBAT                                   44
                                                       GND                 LED_WWAN#
                                                   45                 USIM_PRESENCE           46
                                                   47                                         48
                                                   49  RESERVED          UART_DTR             50                                                                             C84       C83       C82/50V
                                                   51  RESERVED                      NC       52                                                                                                 33pF
                                                       RESERVED                                                                                                              100nF 1nF
                                                       RESERVED                   GND
                                                                                 VBAT

D                                                                                                                                                           DGND                                                                                D

                                          DGND                                                    DGND

                                                  4G_PCIE                                                                                           TITLE:  04-4G-PCIE                                                             REV: 1.0

                                                                                                                                                   4                         Company: HX-SMJ-02                                    Sheet: 1/1

   1                                                                  2                                 3                                                                    Date: 2021-10-19 Drawn By: smile-hkz

                                                                                                                                                                                                          5
   1                              2                          3                                                                                    4                     5

A                                                                                                                                                                                                            A

                                     VDD_3V3_WIFI DGND

      VDD_3V3_WIFI

      C5                C6                  R7    1  GNDGND 39                                                     GND    38  VDD_3V3_WIFI
      100nF             33pF/50V            10K   2  3V3                                                          IO23    37
                                           C31    3  EN                                                           IO22    36
      DGND                                 1uF    4  SENSOR_VP                                                    TXD0    35
                                                  5  SENSOR_VN                                                    RXD0    34
                                     DGND         6  IO34                                                         IO21    33                 R8   R9
                                                  7  IO35                                                                 32                 10K  10K
                                       DGND       8  IO32                                                             NC  31
B                                                 9  IO33                                                         IO19    30       R1                    WIFI_3V3_TXD                                        B
                                                 10  IO25                                                         IO18    29       499                   WIFI_3V3_RXD
                                                 11  IO26                                                                 28
                                                 12  IO27                                                           IO5   27  R10       33R
                                                 13  IO14                                                         IO17    26
      VDD_3V3_WIFI                               14  IO12                                                         IO16    25
                                                 15  GND                                                                  24
                    R6                           16  IO13                                                           IO4   23
                                                 17  NC                                                             IO0   22
                                                 18  NC                                                             IO2   21
                                                 19  NC                                                           IO15    20
                                                                                                                      NC
      2K                                                                                                              NC
                                                                                                              U3      NC

                                                 ESP32-WROOM-32UE(4MB)

            LED1
            BL-HUB36G-AV-TRB

C     DGND                                           WIFI                                                                                                                                                    C

D                                                                                                                                                                                                            D

                                                                                                                                                  TITLE:                                   REV: 1.0

                                                                                                                                                               03-WIFI

                                                                                                                                                                       Company: HX-SMJ-02  Sheet: 1/1

                                                                                                                                                                       Date: 2021-10-19 Drawn By: smile-hkz

   1                              2                          3                                                                                    4                     5
   1                                                          2                                3                                       4                                                                                                                          5

A                                                   IN:24V                                                                 D2                                                                                                                                                    A
                                                                                                                           SS56BF
                                                                     F1                               L1                               VDD_24V
                                                                                                 47uH/6.4A
                                                         1           JK30-160
                                                         2                               R4
                                                    1    3                                                                         C3
                                                    2
                                                    3                                                                 D1                  C4

                                                    VH3.96-3A                            390KD10                      P6SMB33CA    100uF 100nF/50v

                                                    JP1

                                                                     R5        1M                                                      DGND

                                                                         CY1 1nF/440V

                                                               PGND

B                                                                                                                                                                                                                                                                                B

                                        DC-DC 3.3V@3.5A(max) output for 4G module

                                                                                                                 VDD_3V3

      VCC_24V                                                               L2
                                                                         5.6uH/6A
                                                    C13 100nF/50v

                                                                                                                                                    VDD_3V3_4G  VDD_3V3_WIFI

C                                                   U2                 D4                       C9                                                                                                                                                             C
                                   C12                               B560C                      100uF
                                                    TPS54360                                                R17       R15                                 VDD_3V3
                                                                     FB                         FB
                                              1     BOOT SW      8                       DGND               31.6K/1% 10K                                                    SW1
                                              2     VIN GND      7                                                                                                          SS-12D10L4
                                              3     EN COMP      6
                                                    9 EP
                                                                                                                                                                                                                                                  1
                                                                                                                                                                                                                                                        2
                                                                                                                                                                                                                                                               3
                                              4 RT/CLK FB 5                                                               LED3

   100uF/50V                                                                                                R16

                                        R12                                    R18                          10.2K/1%
                                        365K                                   11.5K/1%
                                                    DGND                                                                                                  4G&WIFI

                                                                                         C16

                                                                                         47pF          DGND

                                        R11   R19                              C11
                                                                               5.6nF
                                        86.6K 162K

                              DGND                                                    DGND                                                                                                                                                                                       D

D                                                                                                                                       TITLE:                                                                                                                       REV: 1.0
                                   1
                                                                                                                                                     01-  Company: HX-SMJ-02                                                                                         Sheet: 1/1

                                                              2                                3                                       4                  Date: 2021-10-19 Drawn By: smile-hkz

                                                                                                                                                                                       5
   1                            2                     3                                          4                       5

A                                                                                                                                                      A

                                                                                            C23
                                                                                         100nF

B     WIFI  3  3       TX2                               DGND                                            VDD_3V3                                       B
            2  2       RX2
            1  1                       R2  33R                                       U4

                                       R3  33R

                RS2         C2     C1                       C20  15 GND                          VCC 16     C19
            VH3.96-3A                                    100nF    6 V-                            V+ 2   100nF

                            11pF 11pF           DGND                                                              DGND

                       DGND                                 C21  5 C2-                            C1- 3     C22
                                                         100nF   4 C2+                           C1+ 1   100nF

                                                                 8   RIN2                ROUT2      9                    WIFI_3V3_RXD
                                                                 7   DOUT2                 DIN2     10                   WIFI_3V3_TXD

      4G    3  3       TX1             R13 33R                   13  RIN1                ROUT1      12                   4G_3V3_RXD
            2  2       RX1             R14 33R                   14  DOUT1                 DIN1     11                   4G_3V3_TXD
            1  1

                RS1                                                  MAX3232EID
            VH3.96-3A
                            C25 C24                                  RS232
C                           11pF 11pF                                                                                                                  C

                       DGND

D                                                                                                                                                      D

                                                                                                 TITLE:                                REV: 1.0

                                                                                                              02-TTL232

                                                                                                                 Company: HX-SMJ-02    Sheet: 1/1

                                                                                                                 Date: 2021-10-19 Drawn By: smile-hkz

   1                            2                     3                                          4                       5
