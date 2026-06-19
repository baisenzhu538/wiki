# HX-SMJ01

1                                                 2                                       3                                    4                                         5

         VCC        F1                                 D1 SS56BF                                                              VDD_24V
                    JK30-400_C369107
                                                                                            1         4
                                                                                                                                                                                                      Q1
                                                            D2 SS56BF                       2         3                                                                                      IRFR5410TRPBF           MOTOR_VDD_24V_Z

   1  1                         C1       R1            D3                       C2                   MORNSUN               C3       C4                       R2          C7
   2  2                         1nF/2kv  390KD10       P6SMB24CA                100nF       1 L1 4                         220uF    100nF
   3  3
                                                                                                                                                              2K         R4                  D4               C5     C6
                                                                                                                                                             2K          5110nF                               220uF  100nF
                 PGND
A                                                                                           2         3                     C8                         R3                                                                                       A

   VH3.96-3A                                                                                   MORNSUN                    220uF DGND                                                         1SMA4744A
                                                                                               L2                   MOTOR_24V_PWM_EN_PB7
   JP1                                          R5        1M                                                                                           Q2                                                            DGND
                                                   C9  1nF/2kv                                                                                         MMUN2233LT1G
        VCC JP2

              5557S-2*2P                                                 PGND

              2  2  1  1   24V IN
              4  4  3  3

                                                       VDD_24V                                                                                         L3                                                   VDD_12V
                                                                                                                                                       15uH

B                                                                                                        2 VIN      U1              C10                              Q3                                                                         B
                                                                                                                    TPS54331DDAR    100nF

                                                                                                                              PH 8

                                                                                                         3 EN       BOOT 1                         D5        R6

                                                                                                                                                   SS34_C115205 14K                                                      2  2
                                                                                                                                                                                                                         1  1
                                                                         C11                             4 SS       VSENSE 5                                                 12V_PWM_EN_PB6
                                                        C15              100nF                                                                                                               C12         C13  C14    D6
                                                        220uF
                                                                                                         6 COMP     GND 7                                    MMUN2233LT1G                    220uF/16v 100nF 1nF            A3963WV-2P
                                                                                                                                                                                                                            J11
   12V_PWM_EN_PB6
                                         Q16
                                                                                               C16                      EP 9
                                                                                C17    C18     1.5nF

                                                                                8.2nF 27pF                                                                   R7

                           MMUN2233LT1G                                                                                                                      1K                                                                     R140

                                                                                               R8                                                                                                                                   10K
                                                                                               44.2K

                                                                DGND                                                                                                                                                           LED9
                                                                                                                                                                                                                                                                 C
C

                                DC-DC 5V@3A(max) output                                                                                                LDO 3.3V@1000mA(max) output

   VDD_24V                                                                                                    L4                           VDD_5V
                                                                                                              15uH

                                                        U3                                                                                                   VDD_5V                                                      VDD_3V3
                                                        TPS54331DDAR
                                                2 VIN                                C19                                                                                    U2
                                                                  PH 8               100nF
                                                                                                                                                                            VIN
                                                3 EN                  BOOT 1                   D7                   R9                                                   3  VOUT(TAB)
                                                                                                                                                                         2  ADJ(GND)
                                                                                               SS34_C115205 10.2K                                                        1                        TAB 4                                  R10
                                                                                                                                                                                                                                         2K
                    C20                         4 SS    VSENSE 5                                                                                                                                              C21              C22
                    100nF
   C26                                                                                                                     C23      C24 C25                                                                   100uF/16V 100nF
   220uF
                                                6 COMP                GND 7                                                220uF/16v 100nF 1nF                              AMS1117-3.3_C347222

D                                                                                                                   R11                                                                                                                         D

                           C27  C28      C29                             EP 9                                       1.96K                                                                                                DGND LED1
                                         820pF
                           8.2nF 18pF

                                         R12                                                                                                       TITLE:                                                                           REV: 1.0
                                         56.2K 1%
                                                                                                                                                                01-

                                                                                                                                                                         Company: HX-SMJ01                                          Sheet: 1/1

   DGND                                                                                                                                                                  Date: 2021-10-19 Drawn By: 423857A

                    1                                                 2                                       3                                    4                                         5
   1             2                            3                                 4                       5

A                                                                                                                                                 A

                                                                 C30
                                                                 100nF

                                              DGND                                 VDD_3V3

      3  3                                       C31         U4         VCC 16     C32
      2  2                                       100nF  15 GND           V+ 2      100nF
      1  1                                                               C1- 3
                                                 C33     6 V-                      C34
B                                       DGND     100nF   5 C2-          C1+ 1      100nF          DGND                                            B
                                                         4 C2+
          RS2          C60 C59
      VH3.96-3A         11pF11pF

                                  R138  33              8   RIN2   ROUT2   9                            USART2_RX_PA3
                                                        7   DOUT2    DIN2  10                           USART2_TX_PA2
                 DGND             R139  33
                                                                                                        USART3_RX_PB11
      3  3                        R13   33              13  RIN1   ROUT1   12                           USART3_TX_PB10
      2  2                                              14  DOUT1    DIN1  11
      1  1                        R14   33

          RS1       C35 C36                                 MAX3232EID
      VH3.96-3A      11pF11pF

         DGND

C                                                           RS232                                                                                 C

D                                                                                                                                                 D

                                                                                TITLE:                                                REV: 1.0

                                                                                             02-

                                                                                                  Company: HX-SMJ01                   Sheet: 1/1

                                                                                                  Date: 2021-10-19 Drawn By: 423857A

   1             2                            3                                 4                       5
   1                                                         2                               3                                                              4                                                     5

                                                                U6                                                                                                                                                   VDD_3V3
                                                                STM32F103VET6

A       MOTOR2_IN1_PE2                                    1  PE2              VDD_3     100  VDD_3V3    MOTOR1_IN2_PE1                                                                              R15     R16 R17  C37          XH-5A                   A
B       MOTOR2_IN2_PE3                                    2  PE3              VSS_3     99    DGND      MOTOR1_IN1_PE0                                                                              10K     10K 10K  100nF                                B
C  MOTOR2_STATUS_PE4                                      3  PE4                        98     BOOT0    MOTOR2_PWM_PB9                                                                                                            5                       C
   MOTOR1_STATUS_PE5                                      4  PE5                  PE1   97     j_nTRST  MOTOR1_PWM_PB8                                         SWDIO_PA13                                                         4
                                                          5  PE6                  PE0   96                                                                                                                                        3
   REALY_R1_PC13                                VDD_3V3   6  VBAT                 PB9   95              MOTOR_24V_PWM_EN_PB7                                   SWCLK_PA14                                                         2  5
   REALY_R2_PC14                                   DGND   7  PC13-TAMPER-RTC      PB8   94              12V_PWM_EN_PB6                                                j_nTRST                                                     1  4
   REALY_R3_PC15                                          8  PC14-OSC32_IN    BOOT0     93              MOTOR_CTL_X_E_PB5                                                                                                            3
                                                VDD_3V3   9  PC15-OSC32_OUT       PB7   92                                                                                                                                           2
        FCLK_8MHZ                                        10  VSS_5                PB6   91                                                                                                                                           1
                                                         11  VDD_5                PB5   90
                                                         12  OSC_IN               PB4   89                                                                                                                                        CN1
                                                         13  OSC_OUT              PB3   88
                                                         14  NRST                 PD7   87                   MOTOR_CTL_X_EN_PD7                                                                                   DGND
                                                         15  PC0                  PD6   86                   MOTOR_CTL_X_LE_PD6
                    NRST                                 16  PC1                  PD5   85                   MOTOR_CTL_X_A2_PD5                                                                                                   VDD_3V3
      REALY_R4_PC0                                       17  PC2                  PD4   84                    MOTOR_CTL_X_A1_PD4
      REALY_R5_PC1                                       18  PC3                  PD3   83                   MOTOR_CTL_X_A0_PD3                                        DGND
      REALY_R6_PC2                                       19  VSSA                 PD2   82                   MOTOR_CTL_Y_A0_PD2
      REALY_R7_PC3                                       20  VREF-                PD1   81                    MOTOR_CTL_Y_A1_PD1                                       R19                                       U5                 C38 R18
                                                         21  VREF+                PD0   80                   MOTOR_CTL_Y_A2_PD0                                        10K                                       CAT811STBI-GT3   100nF 10K
                                 AGND                    22  VDDA               PC12    79                   MOTOR_CTL_Y_LE_PC12
                                 AGND                    23  PA0-WKUP           PC11    78                   MOTOR_CTL_Y_EN_PC11                                                                         1  GND      VCC 4
                            VDDA_3V3                     24  PA1                PC10    77                    FLASH_LED_PC10
                            VDDA_3V3                     25  PA2                PA15    76
                                                         26  PA3                PA14    75     SWCLK_PA14
                                                         27  VSS_4            VDD_2     74   VDD_3V3                                           NRST                                                      2  RESET# MR# 3
                                                         28  VDD_4            VSS_2     73
                    USART2_TX_PA2                  DGND  29  PA4                    NC  72    DGND                                                                                 R20
                    USART2_RX_PA3               VDD_3V3  30  PA5                PA13    71                                                                                         10K
                                                         31  PA6                PA12    70
                                SW_PA4                   32  PA7                PA11    69   SWDIO_PA13                                                                      DGND
                                SW_PA5                   33  PC4                PA10    68                MOTOR_SW1_PA12
                                SW_PA6                   34  PC5                  PA9   67                MOTOR_SW2_PA11                                                                                                                      VDD_3V3
                                SW_PA7                   35  PB0                  PA8   66                MOTOR_SW3_PA10
                             ADC2_PC4                    36  PB1                  PC9   65                MOTOR_SW4_PA9
                             ADC1_PC5                    37  PB2                  PC8   64                MOTOR_SW5_PA8
   MOTOR_CURRENT_ADC_PB0                                 38  PE7                  PC7   63                MOTOR_SW6_PC9
           INFRARED_PW_EN_PB1                            39  PE8                  PC6   62                MOTOR_SW7_PC8
                                                         40  PE9                PD15    61                MOTOR_SW8_PC7
                          PNP2_PE8                       41  PE10               PD14    60                MOTOR_DETECT_Y8_PC6                                                                                            X1       C39    C40  C41
                          PNP1_PE9                       42  PE11               PD13    59                MOTOR_DETECT_Y7_PD15                                                                              4 VCC ST# 1
                                                         43  PE12               PD12    58                MOTOR_DETECT_Y6_PD14                                                                              3 OUT GND 2           1nF    100nF 100nF
   SIG2_INFRA_DETECT_PE10                                44  PE13               PD11    57                MOTOR_DETECT_Y5_PD13
   SIG1_INFRA_DETECT_PE11                                45  PE14               PD10    56                MOTOR_DETECT_Y4_PD12                              FCLK_8MHZ  R21         33                                  8MHz
                                                         46  PE15                 PD9   55                MOTOR_DETECT_Y3_PD11
                        NPN2_PE12                        47  PB10                 PD8   54                MOTOR_DETECT_Y2_PD10                                                                                                   DGND
                        NPN1_PE13                        48  PB11               PB15    53                MOTOR_DETECT_Y1_PD9
             SW1_DETECT_PE14                       DGND  49  VSS_1              PB14    52
                                                VDD_3V3  50  VDD_1              PB13    51                SW6_DETECT_PD8
             SW2_DETECT_PE15                                                    PB12                      SW5_DETECT_PB15
                                                                                                          SW4_DETECT_PB14
              USART3_TX_PB10                                                                              SW3_DETECT_PB13
              USART3_RX_PB11

                                                                                                                                                                                                            LED2             R22
                                                                                                                                                                                                                             2K

                                                                                                                                                               FLASH_LED_PC10                                                            VDD_3V3

      VDD_3V3

                                       RN1      SW1             VDD_3V3                                                                           VDDA_3V3                  BOOT0                                            R23
                                        10K     DSWB04LHGET                                                                                                                                                                  10K
                                                                                                                                    R24  C49 C50            TITLE:
D                                            4  8                                                                                   0    100nF 100nF                                                                                           DGND
                                                                                                                                                                         03-
               SW_PA4                        3  7                  C42 C43 C44 C45 C46 C47 C48                                                                                                                                                                                                D
               SW_PA5                                                                                                               R25
               SW_PA6                        2  6                                                                                                                                                                                                         REV: 1.0
               SW_PA7                                              1uF 100nF 100nF 100nF 100nF 100nF100n0F
                                             1  5

                                                                                                                                                                                   Company: HX-SMJ01                                          Sheet: 1/1

                                                DGND            DGND                                                                     AGND                                      Date: 2021-10-19 Drawn By: 423857A

   1                                                         2                               3                                                              4                                                   5
                    1                                        2                                          3                          4                               5

                       MOTOR_VDD_24V                                               MOTOR_VDD_24V

                       R26 R27                                                        R28 R29                                      MOTOR_VDD_24V                                  MOTOR_VDD_24V

A                                           Q4                                                             Q8                                                                                                          A
      MOTOR_X1 R30                          NCE4953                                                        NCE4953
      MOTOR_X2 R36
                             10K 10K  1  S1     D1  8   X1      MOTOR_X9 R31         10K 10K         1  S1  D1  8   X9             R32 R33         Q12                                 R34 R35         Q14
                       10K            2  G1     D1  7   X2      MOTOR_X10 R37  10K                   2  G1  D1  7   X10                            NCE6005AS                                           NCE6005AS
                                      3  S2     D2  6                                                3  S2  D2  6
                       10K            4  G2     D2  5           MOTOR_X11 R47  10K                   4  G2  D2  5                  10K 10K  1               8                          10K 10K  1          8
                                                                MOTOR_X12 R49                                                               2               7                                   2          7
                       MOTOR_VDD_24V                                               MOTOR_VDD_24V                         MOTOR_Y1           3  S2       D2  6  Y1  MOTOR_Y5                     3  S2  D2  6      Y5
                                                                MOTOR_X13 R57                                            MOTOR_Y2           4  G2       D2  5  Y2  MOTOR_Y6                     4  G2  D2  5      Y6
                                                                MOTOR_X14 R61                                                                  S1       D1                                         S1  D1
                                                                                                                                               G1       D1                                         G1  D1
                                                                MOTOR_X15 R71
                                                                MOTOR_X16 R73                                                      R38 R39                                             R40 R41

                       R42 R43                                                        R44 R45

                                            Q5                                                             Q9                      10K 10K                                             10K 10K
                                            NCE4953                                                        NCE4953

      MOTOR_X3 R46           10K 10K  1  S1     D1  8   X3                           10K 10K         1  S1  D1  8   X11            MOTOR_DGND                                MOTOR_DGND
      MOTOR_X4 R48     10K            2  G1     D1  7   X4                     10K                   2  G1  D1  7   X12
                                      3  S2     D2  6                                                3  S2  D2  6                                                                                                                                  B
B                      10K            4  G2     D2  5                          10K                   4  G2  D2  5
                                                                                                                                                                             MOTOR_VDD_24V
                       MOTOR_VDD_24V                                               MOTOR_VDD_24V

                       R50 R51                                                        R52 R53                                      MOTOR_VDD_24V

                                            Q6                                                             Q10                                                                         R54 R55
                                            NCE4953                                                        NCE4953

                             10K 10K  1  S1     D1  8                                10K 10K         1  S1  D1  8                  R58 R59         Q13                                                 Q15
                       10K            2  G1     D1  7                          10K                   2  G1  D1  7                                                                                      NCE6005AS
   MOTOR_X5 R56                       3  S2     D2  6   X5                                           3  S2  D2  6   X13                            NCE6005AS
   MOTOR_X6 R60        10K            4  G2     D2  5   X6                     10K                   4  G2  D2  5
                                                                                                                    X14            10K 10K  1               8                          10K 10K  1  S2  D2  8
                                                                                                                                            2               7                                   2  G2  D2  7
                                                                                                                         MOTOR_Y3           3  S2       D2  6  Y3  MOTOR_Y7                     3  S1  D1  6      Y7
                                                                                                                         MOTOR_Y4           4  G2       D2  5  Y4  MOTOR_Y8                     4  G1  D1  5      Y8
                                                                                                                                               S1       D1
                       MOTOR_VDD_24V                                               MOTOR_VDD_24V                                               G1       D1

                                                                                                                                   R64 R65                                             R62 R63

                       R66 R67                                                        R68 R69

                                            Q7                                                             Q11                         10K 10K                                   10K 10K
                                            NCE4953                                                        NCE4953
                                                                                                                                   MOTOR_DGND                                                                                                      C
C MOTOR_X7 R70               10K 10K  1  S1     D1  8   X7                           10K 10K         1  S1  D1  8   X15
      MOTOR_X8 R72     10K            2  G1     D1  7   X8                     10K                   2  G1  D1  7   X16                                                      MOTOR_DGND
                                      3  S2     D2  6                                                3  S2  D2  6                                                              VDD_3V3
                       10K            4  G2     D2  5                          10K                   4  G2  D2  5                                                                 DGND

                          F2
                          A30-050

   VDD_24V             1                 2      MOTOR_VDD_24V                                                                                                                      D8
                                                                                                                                                                        BAT54S,215
                                                                                                                                   MOTOR_CURRENT_ADC_PB0                                                   MOTOR_DGND
                                                                                                                                                                   R74 1K
                                                                                                                                                                                                R75 R76
                                            J6                                                                                                                                                  11
                                            5557S-2*8P

D                         X1 1              1    2  2   X2                               J7                                                                                                                                                   D
                          X3 3              3    4  4   X4                               5557S-2*4P
                          X5 5              5    6  6   X6                                                                                                                                      DGND
                          X7 7              7    8  8   X8                     Y1  1  1  2  2  Y2                                  TITLE:                                                                      REV: 1.0
                          X9 9              9   10  10  X10                    Y3  3  3  4  4  Y4
                          X1111             11  12  12  X12                    Y5  5  5  6  6  Y6                                               04-
                          X1313             13  14  14  X14                    Y7  7  7  8  8  Y8
                          X1515             15  16  16  X16

                                                                                                                                                               Company: HX-SMJ01                           Sheet: 1/1

                                                                                                                                                               Date: 2021-10-19 Drawn By: 423857A

                    1                                        2                                          3                          4                               5
   1                                                  2                                    3                           4                    5

                                                                                                     U7

                                                                                                     ULN2003AIDR

                                                           U8                                 1  1B        1C  16      MOTOR_X1
                                                                                              2  2B        2C  15      MOTOR_X2
A                                                     74HC237D,653                            3  3B        3C  14      MOTOR_X3                                                             A
                                                                                              4  4B        4C  13      MOTOR_X4
                  MOTOR_CTL_X_A0_PD3               1  A0        Y0  15                        5  5B        5C  12      MOTOR_X5
                  MOTOR_CTL_X_A1_PD4               2  A1        Y1  14                        6  6B        6C  11      MOTOR_X6
                  MOTOR_CTL_X_A2_PD5               3  A2        Y2  13                        7  7B        7C  10      MOTOR_X7
                                                                Y3  12                        8  E      COM    9
                  MOTOR_CTL_X_LE_PD6                            Y4  11                                                       MOTOR_VDD_24V
                    MOTOR_CTL_X_E_PB5
                                                   4 LE#            10                           C51 100nF
                  MOTOR_CTL_X_EN_PD7               5                9
                                                   6  E1#       Y5  7
                                                      E2        Y6
                                                                Y7
                                                                                              DGND

                                       VDD_5V 16 VCC GND 8

                                                      C52 100nF                                         U9

                                                                                                        ULN2003AIDR

                                                                      DGND                    1  1B         1C  16     MOTOR_X8
                                                                                              2  2B         2C  15     MOTOR_X9
                                                           U10                                3  3B         3C  14     MOTOR_X10
                                                                                              4  4B         4C  13     MOTOR_X11
B                                                          74HC237D,653                       5  5B         5C  12     MOTOR_X12                                                            B
                                                                                              6  6B         6C  11     MOTOR_X13
   MOTOR_CTL_X_A0_PD3                              1  A0        Y0  15                        7  7B         7C  10     MOTOR_X14
   MOTOR_CTL_X_A1_PD4                              2  A1        Y1  14                        8  E       COM    9
   MOTOR_CTL_X_A2_PD5                              3  A2        Y2  13                                                    MOTOR_VDD_24V

   MOTOR_CTL_X_LE_PD6                              4            Y3  12                              C53 100nF
                                                   5            Y4  11
   MOTOR_CTL_X_EN_PD7                  MOTOR_X_E1  6  LE#       Y5  10
                                                      E1#       Y6  9
                                                      E2                                      DGND
                                                                Y7 7

                                       VDD_5V 16 VCC GND 8                                              U11

                                                                                                        ULN2003AIDR

                                                      C54 100nF                               1  1B         1C  16     MOTOR_X15
                                                                                              2  2B         2C  15     MOTOR_X16
                                                                      DGND                    3  3B         3C  14
                                                                                              4  4B         4C  13     MOTOR_Y1
                                                                VDD_5V                        5  5B         5C  12
                                                                                              6  6B         6C  11       MOTOR_VDD_24V
                                                                                              7  7B         7C  10
                                                                                              8  E       COM    9

C                                                         U12            C55                                                                                                                C

                 MOTOR_CTL_Y_LE_PC12                  74HC137D,653       100nF

                 MOTOR_CTL_Y_A0_PD2                4 LE# VCC 16                      DGND           C56 100nF
                 MOTOR_CTL_Y_A1_PD1
                 MOTOR_CTL_Y_A2_PD0                1  A0       Y0#  15                        DGND
                                                   2  A1       Y1#  14
                 MOTOR_CTL_Y_EN_PC11               3  A2       Y2#  13                                  U13
                                                                                                        ULN2003AIDR
                                                   6           Y3#  12
                                                   5  E1#      Y4#  11                           1  1B         1C  16  MOTOR_Y2
                                                      E2       Y5#  10                           2  2B         2C  15  MOTOR_Y3
                                                               Y6#  9                            3  3B         3C  14  MOTOR_Y4
                                                                                                 4  4B         4C  13  MOTOR_Y5
                                                   8 GND       Y7# 7                             5  5B         5C  12  MOTOR_Y6
                                                                                                 6  6B         6C  11  MOTOR_Y7
                                             DGND                                                7  7B         7C  10  MOTOR_Y8
                                                                                                 8  E       COM    9
                                                                                                                         MOTOR_VDD_24V
                                                U14
                                                74HC1G04GV,125          VDD_5V

D  MOTOR_CTL_X_E_PB5                         1  N.C                                                    C57 100nF                                                                            D
                            DGND MOTOR_X_E1  2  A
                                             3  GND                           C58             DGND
                           VDD_5V            4  Y                             100nF
                                             5  VCC
                                                                                                                       TITLE:
                                                                                                                                                                                REV: 1.0
                                                                                                                                    05-

                                                                        DGND

                                                                                                                                            Company: HX-SMJ01                   Sheet: 1/1

   1                                                  2                                    3                           4                    Date: 2021-10-19 Drawn By: 423857A

                                                                                                                                                                         5
                  1                                                           2                                      3                                          4                              5

                           J5                                                                                                                        U15                                  RN2
                           5557S-2*4P                                                                                                                ULN2003AIDR                          1K

                                                                                 PNP2_24V R77   10K                                        1     1B     1C  16                                 PNP2_PE8
                                                                                                                                           2     2B     2C  15                                 PNP1_PE9
   SW1               1              2  SW2                                       PNP1_24V R78   10K                                        3     3B     3C  14                                 SIG2_INFRA_DETECT_PE10
   SW3               3              4  SW4                                                                                                 4     4B     4C  13                                 SIG1_INFRA_DETECT_PE11
   SW5               5  1        2  6  SW6                                       PNP_IR R79     10K                                        5     5B     5C  12
   SW7               7  3        4  8  SW8                                                                                                 6     6B     6C  11                                                                                                                      A
                        5        6                                                                                                         7     7B     7C  10
A                       7        8                                                                                                         8     E   COM    9

                                                                                                                                                                   VDD_3V3

                                                                                                                                                 C62 100nF

                                                                                                                                                                                          RN3

                                            VDD_5V                                                                                         DGND                                           1K

                                                               R80       10K     NPN_IR                                                                                                           NPN2_PE12
                                                                                                                                                                                                  NPN1_PE13

                                                                    RN4
                                                                    10K

                                                                                 NPN2_24V

                                                                                 NPN1_24V                                                            U16

                                                                    RN5          SW1_DETECT_IN                                                       ULN2003AIDR                          RN6     SW1_DETECT_PE14
                                                                                                                                                                                                  SW2_DETECT_PE15
                                                                    10K          SW2_DETECT_IN                                             1     1B     1C  16                            1K      SW3_DETECT_PB13
                                                                                                                                           2     2B     2C  15                                    SW4_DETECT_PB14
                                                                                 SW3_DETECT_IN                                             3     3B     3C  14                                    SW5_DETECT_PB15
                                                                                                                                           4     4B     4C  13                                    SW6_DETECT_PD8
                                                                                 SW4_DETECT_IN                                             5     5B     5C  12
                                                                                                                                           6     6B     6C  11
                                                                                 SW5_DETECT_IN                                             7     7B     7C  10
                                                                                                                                           8     E   COM    9
   J2                                                                            SW6_DETECT_IN
   A3963WV-7P
B                                                                                                                                                                                                                                   B

   7           7     SW6_DETECT_IN                                                                         C66 C67 C68 C69 C70 C71
               6     SW5_DETECT_IN
   6           5     SW4_DETECT_IN                                                                                                                                VDD_3V3
   5           4     SW3_DETECT_IN
   4           3     SW2_DETECT_IN                                                                         100n1F00n1F00n1F00n1F00n1F00nF
   3           2     SW1_DETECT_IN
   2           1                                                                                                                                 C72 100nF
   1                  DGND
                                                                                                      DGND                                 DGND

                                                                                                      C73               RN7                                                         RN8

                                                                                                      1C0704nF          10K                                                         1K

                                                                                                      1C0705nF Y1                                    U17                                       MOTOR_DETECT_Y1_PD9
                                                                                                      1C0706nF Y2                                    ULN2003AIDR                               MOTOR_DETECT_Y2_PD10
                                                                                                      1C0707nF Y3                                                                              MOTOR_DETECT_Y3_PD11
                                                                                                      1C0708nF Y4       R1N0K9             1  1B        1C  16                      RN10       MOTOR_DETECT_Y4_PD12
                                                                                                      1C0709nF Y5                          2  2B        2C  15                      1K         MOTOR_DETECT_Y5_PD13
                                                                                                      1C0800nF Y6                          3  3B        3C  14                                 MOTOR_DETECT_Y6_PD14
                                                                                                      100nF Y7                             4  4B        4C  13                                 MOTOR_DETECT_Y7_PD15
                                                                                                                                           5  5B        5C  12                                 MOTOR_DETECT_Y8_PC6
                                                                                                                 Y8                        6  6B        6C  11
                                                                                                                                           7  7B        7C  10
C                                                                                                                                          8  E      COM    9   VDD_3V3                                                             C

                                                                                                DGND                                             C81 100nF

                                                                                                                        RN11               DGND      U18                            RN12
                                                                                                                        10K                          ULN2003AIDR                    1K

   VDD_24V                                                                                      C82 100nF SW8                                                                       RN14       MOTOR_SW8_PC7
                                                                                                                                                                                    1K
                                                                                                C83 100nF SW7                              1  1B        1C  16                                 MOTOR_SW7_PC8
                                                                                                                                           2  2B        2C  15                                 MOTOR_SW6_PC9
   PNP2_24V                1  1                                                                 C84   100nF SW6         R1N0K13            3  3B        3C  14                                 MOTOR_SW5_PA8
   PNP1_24V                2  2                                                                 C85   100nF SW5                            4  4B        4C  13                                 MOTOR_SW4_PA9
   PNP_IR                  3  3                                                                                                            5  5B        5C  12                                 MOTOR_SW3_PA10
   NPN_IR                  4  4                                                                 C86 100nF SW4                              6  6B        6C  11                                 MOTOR_SW2_PA11
   NPN2_24V                5  5                                                                                                            7  7B        7C  10                                 MOTOR_SW1_PA12
   NPN1_24V                6  6                                                                 C87 100nF SW3                              8  E      COM    9
                           7  7
                           8  8                                                                 C88 100nF SW2

                                                                                                C89 100nF SW1

                                                                                                                                                                VDD_3V3

                                                                                                DGND                                             C90 100nF

                                             VH3.96-8A_C75270                                                                              DGND                                                                                     D
                                             J1
D

          Q17              R81         2K                      INFRARED_PW_EN_PB1
   NCE3400
                                                                                                                                                                  TITLE:
                                 R82                                                                                                                                                                                    REV: 1.0
                                 10K                                                                                                                                           06-

                                                                                                                                                                                    Company: HX-SMJ01                   Sheet: 1/1

            DGND                                                                                                                                                                    Date: 2021-10-19 Drawn By: 423857A

                  1                                                           2                                      3                                          4                              5
   1                                                               2                                3                                       4                             5

                                                            U19                                                                       VDD_24V                             VDD_24V_LED

                                                            ULN2003AIDR

A                                     REALY_R7_PC3   1  1B     1C  16  REALY_R7                                                                             Q18                                                     A
                                      REALY_R6_PC2   2  2B     2C  15  REALY_R6                                                                             NCE3007S
                                      REALY_R5_PC1   3  3B     3C  14  REALY_R5
                                      REALY_R4_PC0   4  4B     4C  13  REALY_R4                                                  R84   R83  R85  C91  1  S    D  8                      2  2
                                                     5  5B     5C  12  REALY_R3                              REALY_R7 10K              10K  51R  1nF  2  S    D  7                      1  1
                                      REALY_R3_PC15  6  6B     6C  11  REALY_R2                                                                       3  S    D  6
                                      REALY_R2_PC14  7  7B     7C  10  REALY_R1                                                                       4  G    D  5        C92 D9           A3963WV-2P
                                      REALY_R1_PC13  8  E   COM    9                                                                                                      100nF            J10
                                                                         VDD_24V

                                                        C93 100nF

                                                                                                                                                                          DGND

                                                     DGND

B                                                                                                                                                                                                                   B

                                      VDD_24V        10K LED3          VDD_24V     10K LED4      VDD_24V     10K LED5      VDD_24V     10K LED6             VDD_24V       10K LED7      VDD_24V       10K LED8
                                                     D10 REALY_R1                  D11 REALY_R2              D12 REALY_R3              D13 REALY_R4                       D14 REALY_R5                D15 REALY_R6
                                             R86                              R87                       R88                       R89                                R90                         R91

C                                                                                                                                                                                                                   C

                                                                                                 1  1        REALY_R1  VDD_24V
                                                                                                 2  2        REALY_R2
                                                                                                 3  3        REALY_R3
                                                                                                 4  4        REALY_R4
                                                                                                 5  5        REALY_R5
                                                                                                 6  6        REALY_R6
                                                                                                 7  7

                                                                                                 A3963WV-7P
                                                                                                 J12

D                                                                                                                                                                                                                   D
                                   1
                                                                                                                                            TITLE:                                                     REV: 1.0

                                                                                                                                                         07-

                                                                                                                                                                 Company: HX-SMJ01                     Sheet: 1/1

                                                                                                                                                                 Date: 2021-10-19 Drawn By: 423857A

                                                                   2                                3                                       4                             5
                   1                                      2                                        3                                       4                                            5

                                          VDD_5V                                                                   VDD_5V                                                          VDD_5V

                                            R95           R92                                                        R96      R93                                                   R97                     R94
                                             510          10K                                                         510     10K                                                    510                    10K

                                                               M1_IN1                                                              M1_IN2                                                                        M1_PWM

A                                           R98 1K                                                                   R99 1K                                                         R100 1K                                              A

                         MMBT5551LT1G                     Q19                                      MMBT5551LT1G               Q20                                     MMBT5551LT1G                          Q21

                                                          MMBT5551LT1G                                                        MMBT5551LT1G                                                                  MMBT5551LT1G

   MOTOR1_IN1_PE0        R101        1K     Q22                        MOTOR1_IN2_PE1             R102       1K      Q23                   MOTOR1_PWM_PB8             R103     1K   Q24

                                  R104                                                                    R105                                                              R106

                                     10K                                                                     10K                                                            10K

                                           DGND                                                                     DGND                                                            DGND
                                          VDD_5V                                                                   VDD_5V                                                          VDD_5V

                                            R110          R107                                                       R111     R108                                                  R112                    R109
                                             510          10K                                                         510     10K                                                    510                    10K

                                                               M2_IN1                                                              M2_IN2                                                                        M2_PWM

B                                                                                                                                                                                                                                        B

                                            R113 1K                                                                  R114 1K                                                        R115 1K

                         MMBT5551LT1G                     Q25                                      MMBT5551LT1G               Q26                                     MMBT5551LT1G                          Q27

                                                          MMBT5551LT1G                                                        MMBT5551LT1G                                                                  MMBT5551LT1G

   MOTOR2_IN1_PE2        R116        1K     Q28                        MOTOR2_IN2_PE3             R117       1K      Q29                   MOTOR2_PWM_PB9             R118     1K   Q30

                                  R119                                                                    R120                                                              R121

                                     10K                                                                     10K                                                            10K

                                          DGND                                                                       DGND                                                          DGND

                      VDD_3V3                                                                                                       VDD_3V3

MOTOR1_STATUS_PE5                           U20                                                           MOTOR2_STATUS_PE4                             U21
                                            TB6642FG                                                                                                    TB6642FG
                         R122                                                                  MOTOR_VDD_24V_Z                      R123                                                                         MOTOR_VDD_24V_Z
                         20K      1                   16                                                                            20K       1                   16
                                  2                   15                                                                                      2                   15
C            R124     0           3  ALERT  VREF      14  M1_PWM                            2             1                   R125  0         3  ALERT  VREF      14  M2_PWM                                2            1               C
                      M1_IN1      4  OSC     PWM      13  M1_OUT2                                                                   M2_IN1    4  OSC     PWM      13  M2_OUT2
                                  0  IN1    TISD      0                                        F3 A30-050                                     0  IN1    TISD      0                                              F4 A30-050
                      M1_IN2      5  SGND   VISD      12                                                                            M2_IN2    5  SGND   VISD      12
                      M1_OUT1     6  FIN              11                               C94  C95                                     M2_OUT1   6  FIN              11                                 C96    C97
                                  7  IN2       FIN    10                                    220uF                                             7  IN2       FIN    10                                        220uF
                                  8  NC        VM     9                R126 R127100nF                                                         8  NC        VM     9                                  100nF
                                     OUT1       NC                     10K 10K                                                                   OUT1       NC                     R128 R129
                                     RSGND  OUT2                                                                                                 RSGND  OUT2                       10K 10K
                                                NC                                                                                                          NC

                                                                              DGND                                                                                                           DGND

                                          M1_OUT2                                                                    M2_OUT2
                                                                                                                     M2_OUT1
   J9                                                                    J8
                                                                        VH3.96-3A
   VH3.96-3A                   R130                                                                          R131
                                                                                                             51
D      3  3                    51                                       3  3                                                                                                                                                             D
       2  2                                                             2  2
       1  1        PGND                                                 1  1                PGND

                                  C98                                                                         C99                           TITLE:
                                                                                                              100nF
          C100                    100nF M1_OUT1                               C102                                                                       08-                                                                 REV: 1.0
                                                                        1nF/2kv                    C103
                         C101                                                                      1nF/2kv                                 4

   1nF/2kv               1nF/2kv

                                                                                                                                                                  Company: HX-SMJ01                                          Sheet: 1/1

                   PGND                                                             PGND                                                                          Date: 2021-10-19 Drawn By: 423857A

                   1                                      2                                            3                                                                                       5
                                   1  2           3                                       4                           5
A
B                                                                                                                                                           A
C
D                                                               VDD_3V3

                                   1     J3                        R132
                                            1                      10K
                                            2
                                               1                   R133     1K               ADC1_PC5
                                               2

                                                       D16         R134         C104
                                                       BAT54S,215  300K              1nF

                                                                                                                                                            B

                                                  DGND VDD_3V3  DGND            DGND

                                                  NTC

                                                                VDD_3V3

                                         J4                        R135
                                            1                      10K
                                            2
                                               1                      R136  1K                              ADC2_PC4
                                               2

                                                       D17         R137         C105                                                                        C
                                                       BAT54S,215  300K            1nF

                                                  DGND VDD_3V3  DGND            DGND

                                                  NTC

                                                                                                                                                            D

                                                                                          TITLE:                                                REV: 1.0

                                                                                                       09-

                                                                                                            Company: HX-SMJ01                   Sheet: 1/1

                                                                                                            Date: 2021-10-19 Drawn By: 423857A

                                      2           3                                       4                           5
