# 主板原理图_HX-SMJ01_V1.1

1                                    2                                          3                                     4                                                                                                                         5

                                                                                                                                               3.3V@1000mA(max) output

       IN:24V               F14A8A                                          VCC_24V

A                        F1                     L1           D2                                                                   VDD_5V                                                                                                                                           VDD_3V3                              A
                         JK30-400          47uH/6.4A         SS56BF
            JP1

            1    1                 R1                                       C9                                                                          3  U3                                                                                                 TAB 4                                 R17
            2    2                                                                    C12                                                               2                                                                                                                                           2K
            3    3                                                                                                                                      1  VIN
                                                                                                                                                           VOUT(TAB)
                                                      D1                                                                                                   ADJ(GND)                                                                                                     C19          C20
                                                                                                                                                                                                                                                                        10uF       100nF
   VH3.96-3A                       390KD10            P6SMB33CA 680uF/50V   100nF/50V                                                          C3
                                                                                                                                               10uF
                                                                                                                                                           AMS1117-3.3

                         R6            1M                                                                                                                                                                                                                                          DGND LED3

                            CY1 1nF/440V

                     PE

B                                                                                                                                                                                                                                                                                                                       B

                                                                                                                                                        5V@3A(max) output

                            12V@3A(max) output                                                                                    VCC_24V                  C8                                                                                                                                                 VDD_5V
                                                                                                                                                           100nF/50V
                                                                                                                                                                                                                                                                           L3
                                                                                                                                                                                                                                                                     15uH/6.25A

   VCC_24V                     C7                                                           VDD_12V
                            100nF/50V
                                                                 L2
                                                             22uH/5A                                                2  2                                     U2                                                                                                         D4                 C14
                                                          D3                                                        1  1                                                                                                                                              B560C              100uF/25V
                                                         B560C                                                                                          TPS54360                                                                                                                                         R13       R15
                                                                                                                                                                                                                                                                     13.3K/1% R10
                                                      21K/0.5% R9                                                                                    1  BOOT                                                                                           SW  8                                             53.6K/1% 10K
                                                                                                                                                     2  VIN                                                                                           GND  7              C11
                                   U1                                        C13                                       VH3.96-2P                                                                                                                                         8.2nF
                                                                           100uF/25V                                   J11
                            TPS54360                                                       R11       R16                          C2                 3  EN COMP                                                                                            6
                                                                      DGND                 143K/1%   10K                          100uF/50V          4  RT/CLK FB                                                                                          5
                         1  BOOT SW         8
                         2  VIN GND         7                                                                  D11                         R4
                         3  EN COMP         6                                                                                      523K/1%
                                   9 EP                                                                                                                                                                                                                                            DGND                            LED1
                                                                                                                                                                                                                                                9 EPR5                                                                       C
C  C1                    4 RT/CLK FB 5                                                                        M7                   37.4K/1%                                                                                                                                                              R14
                                                                                                     LED2                                                                                                                                                                                                10.2K/1%

   100uF/50V                                                                               R12                                                                 DGND                                                                                                                C16
                 R2                                                                        10.2K/1%                                                                                                                                                                                39pF
                                                                                                                                                     R8
         523K/1%                   DGND                                                                                                              162K/1%                                                                                                                                        DGND

               R3        R7                                  C10      C15             DGND
       37.4K/1%          162K/1%                             12nF     24pF

                                                                                                                                  DGND                                                                                                                                             DGND

   DGND                                                               DGND

D                                                                                                                                                                                                                                                                                                                       D

                                                                                                                                           TITLE:                                                                                                                                                        REV: 1.0

                                                                                                                                                        01-

                                                                                                                                                                                                                                                      Company: HX-SMJ01                                  Sheet: 1/1

                                                                                                                                                                                                                                                      Date: 2021-10-19 Drawn By: 423857A

                     1                                    2                                          3                                     4                                                                                                                         5
   1             2                           3                                 4                       5

A                                                                                                                                                A

                                                                C27
                                                                100nF

                                             DGND                                 VDD_3V3

      3  3                                      C25         U4         VCC 16     C28
      2  2                                      100nF  15 GND           V+ 2      100nF
      1  1                                                              C1- 3
                                                C26     6 V-                      C29
B                                      DGND     100nF   5 C2-          C1+ 1      100nF          DGND                                            B
                                                        4 C2+
          RS2          C22 C24
      VH3.96-3A        11pF 11pF

                                  R18  33              8   RIN2   ROUT2   9                            USART2_RX_PA3
                                                       7   DOUT2    DIN2  10                           USART2_TX_PA2
                 DGND             R19  33
                                                                                                       USART3_RX_PB11
      3  3                        R20  33              13  RIN1   ROUT1   12                           USART3_TX_PB10
      2  2                                             14  DOUT1    DIN1  11
      1  1                        R21  33

          RS1       C21 C23                                 MAX3232EID
      VH3.96-3A     11pF 11pF
                                                           RS232

         DGND

C                                                                                                                                                C

D                                                                                                                                                D

                                                                               TITLE:                                                REV: 1.0

                                                                                            02-

                                                                                                 Company: HX-SMJ01                   Sheet: 1/1

                                                                                                 Date: 2021-10-19 Drawn By: 423857A

   1             2                           3                                 4                       5
   1                                                         2                                     3                        4                              5

                                                                U5                                                                                                VDD_3V3
                                                                STM32F103VET7TR

                                                       1  PE2              VDD_3     100  VDD_3V3                                                    R27 R28 R29       C39                              XH-5A
                                                       2  PE3              VSS_3     99    DGND                                                      10K 10K 10K       100nF
                                                       3  PE4                        98   VDD_3V3                                                                                                       5
A  REALY_R1_PC13                             VDD_3V3   4  PE5                  PE1   97    DGND       BOOT0                    SWDIO_PA13                                                               4  5                     A
B  REALY_R2_PC14                                DGND   5  PE6                  PE0   96                                                                                                                 3  4
C  REALY_R3_PC15                                       6  VBAT                 PB9   95               12V_PWM_EN_PB6           SWCLK_PA14                                                               2  3
                                             VDD_3V3   7  PC13-TAMPER-RTC      PB8   94               MOTOR_CTL_X_E_PB5               j_nTRST                                                           1  2
        FCLK_8MHZ                                      8  PC14-OSC32_IN    BOOT0     93               j_nTRST                                                                                              1
                                                       9  PC15-OSC32_OUT       PB7   92
                                                      10  VSS_5                PB6   91               MOTOR_CTL_X_EN_PD7                                                                                CN1
                                                      11  VDD_5                PB5   90               MOTOR_CTL_X_LE_PD6
                                                      12  OSC_IN               PB4   89               MOTOR_CTL_X_A2_PD5                                      DGND
                                                      13  OSC_OUT              PB3   88               MOTOR_CTL_X_A1_PD4
                                    NRST              14  NRST                 PD7   87               MOTOR_CTL_X_A0_PD3                                   VDD_3V3
                      REALY_R4_PC0                    15  PC0                  PD6   86               MOTOR_CTL_Y_A0_PD2
                      REALY_R5_PC1                    16  PC1                  PD5   85               MOTOR_CTL_Y_A1_PD1                       NRST              R24
                      REALY_R6_PC2                    17  PC2                  PD4   84               MOTOR_CTL_Y_A2_PD0                                         10K
                                                      18  PC3                  PD3   83               MOTOR_CTL_Y_LE_PC12                                                                                                                    B
                               LED_PC3                19  VSSA                 PD2   82               MOTOR_CTL_Y_EN_PC11                                         C41
                                                AGND  20  VREF-                PD1   81                FLASH_LED_PC10                                          100nF                                                  VDD_3V3
                                                AGND  21  VREF+                PD0   80
                                                      22  VDDA               PC12    79               SWCLK_PA14                                           DGND
                                           VDDA_3V3   23  PA0-WKUP           PC11    78
                                           VDDA_3V3   24  PA1                PC10    77               SWDIO_PA13                                                        X1                                  C40  C42  C43
                               SW1_PA0                25  PA2                PA15    76               MOTOR_SW1_PA12                                       4 VCC ST# 1                                     1nF
                               SW2_PA1                26  PA3                PA14    75               MOTOR_SW2_PA11                                                                                             100nF 100nF
                                                      27  VSS_4            VDD_2     74               MOTOR_SW3_PA10
                    USART2_TX_PA2                     28  VDD_4            VSS_2     73               MOTOR_SW4_PA9
                    USART2_RX_PA3                     29  PA4                    NC  72               MOTOR_SW5_PA8
                                                      30  PA5                PA13    71               MOTOR_SW6_PC9
                                                DGND  31  PA6                PA12    70               MOTOR_SW7_PC8
                                             VDD_3V3  32  PA7                PA11    69               MOTOR_SW8_PC7
                                SW_PA4                33  PC4                PA10    68               MOTOR_DETECT_Y8_PC6
                                SW_PA5                34  PC5                  PA9   67               MOTOR_DETECT_Y7_PD15
                                SW_PA6                35  PB0                  PA8   66               MOTOR_DETECT_Y6_PD14
                                SW_PA7                36  PB1                  PC9   65               MOTOR_DETECT_Y5_PD13
                             ADC2_PC4                 37  PB2                  PC8   64               MOTOR_DETECT_Y4_PD12
                             ADC1_PC5                 38  PE7                  PC7   63               MOTOR_DETECT_Y3_PD11
   MOTOR_CURRENT_ADC_PB0                              39  PE8                  PC6   62               MOTOR_DETECT_Y2_PD10
                                                      40  PE9                PD15    61               MOTOR_DETECT_Y1_PD9
           INFRARED_PW_EN_PB1                         41  PE10               PD14    60               SW6_DETECT_PD8
                                                      42  PE11               PD13    59               SW5_DETECT_PB15
                                                      43  PE12               PD12    58               SW4_DETECT_PB14          FCLK_8MHZ       R25   33 3 OUT GND 2
                                                      44  PE13               PD11    57               SW3_DETECT_PB13
                          PNP2_PE8                    45  PE14               PD10    56                                                                           8MHz
                          PNP1_PE9                    46  PE15                 PD9   55
                                                      47  PB10                 PD8   54                                                                                                                 DGND
   SIG2_INFRA_DETECT_PE10                             48  PB11               PB15    53
   SIG1_INFRA_DETECT_PE11                             49  VSS_1              PB14    52                                                              LED4              R30                                                       C
                                                      50  VDD_1              PB13    51                                                                                2K
                        NPN2_PE12                                            PB12
                        NPN1_PE13                                                                                              FLASH_LED_PC10                                                              VDD_3V3
             SW1_DETECT_PE14
                                                DGND
             SW2_DETECT_PE15                 VDD_3V3

              USART3_TX_PB10
              USART3_RX_PB11

                                                                                                                                              BOOT0                    R31
                                                                                                                                                                       10K

                                                                                                                                                                                         DGND

      VDD_3V3                                                                                                                  VDD_3V3                                                                           VDDA_3V3

                                                                VDD_3V3                                                                                                                            R22  C37 C38
                                                                                                                                                                                                   0    100nF 100nF
                                                                                                  SW2
                                                                                                  K2-6639SP-C4SC-04               C30 C31 C32 C33 C34 C35 C36
                                                                                                                                                                                                   R23

                                                                                                                                  1uF 100nF 100nF 100nF 100nF 100nF100n0F

                                       RN1                                                R26 1       3
                                        10K
                                                SW1                                       10K  2      4
D                                               DSWB04LHGET
                                                                SW1_PA0                           SW3                          DGND                                                                                              D
               SW_PA4                                           SW2_PA1                           K2-6639SP-C4SC-04                                                                                            AGND
               SW_PA5                        4  8
               SW_PA6
               SW_PA7                        3  7                                         R32 1       3

                                             2  6                                         10K                               TITLE:

                                             1  5                                              2      4                                  03-                                                                         REV: 1.0

                                                                                                         DGND                                  Company: HX-SMJ01                                                     Sheet: 1/1

                                                DGND                                                                                           Date: 2021-10-19 Drawn By: 423857A

   1                                                         2                                     3                        4                              5
   1                                                        2                               3                                         4                                        5   6                                           7                        8

                                                            MOTOR_VDD_24V                                                                            MOTOR_VDD_24V

                                                                                                                                                                                                MOTOR_VDD_24V

                      R41 R45 D18                D19                                                                       R51 R52 D29        D28

                                                                     Q1                                                                                    Q5
                                                                                                                                                           NCE4953
A                              1SMA4744A                             NCE4953                                                          1SMA4744A                                                 R67 R71                                                                        A
                               1SMA4744A                                                                                              1SMA4744A
                      10K 10K                                  1  S1     D1  8                                             10K 10K                   1  S1  D1  8                                                                        Q9
                                                               2  G1     D1  7                                                                       2  G1  D1  7
   MOTOR_X1 R34  10K                                           3  S2     D2  6      X1         MOTOR_X9 R53           10K                            3  S2  D2  6      X9                                                                NCE6005AS
                                                               4  G2     D2  5      X2                                                               4  G2  D2  5      X10
   MOTOR_X2 R33  10K                                                                           MOTOR_X10 R54          10K                                                                                  10K 10K                1  S2      D2  8  Y1
                                                                                                                                                                                      MOTOR_Y1                                    2  G2      D2  7  Y2
                                                                                                                                                                                                                                  3  S1      D1  6
                                                                                                                                                                                      MOTOR_Y2                                    4  G1      D1  5

                                                                                                                                                                                                R68 R72             D20  D21

                                                            MOTOR_VDD_24V                                                                            MOTOR_VDD_24V                              10K 10K             1SMA4744A
                                                                                                                                                                                                                    1SMA4744A

                      R38 R37 D22                D23                                                                       R55 R56 D31        D30                                               MOTOR_DGND

                                                                     Q2                                                                                    Q6
                                                                                                                                                           NCE4953
                               1SMA4744A                             NCE4953                                                          1SMA4744A
                               1SMA4744A                                                                                              1SMA4744A
                      10K 10K                                  1  S1     D1  8                                             10K 10K                   1  S1  D1  8
                                                               2  G1     D1  7                                                                       2  G1  D1  7
B  MOTOR_X3 R36  10K                                           3  S2     D2  6      X3         MOTOR_X11R57           10K                            3  S2  D2  6      X11                      MOTOR_VDD_24V                                                                  B
                                                               4  G2     D2  5      X4                                                               4  G2  D2  5      X12
   MOTOR_X4 R35  10K                                                                           MOTOR_X12 R58          10K

                                                                                                                                                                                                R74 R73                                  Q10
                                                                                                                                                                                                                                         NCE6005AS

                                                                                                                                                                                                           10K 10K                1  S2      D2  8  Y3
                                                                                                                                                                                      MOTOR_Y3                                    2  G2      D2  7  Y4
                                                                                                                                                                                                                                  3  S1      D1  6
                                                            MOTOR_VDD_24V                                                                            MOTOR_VDD_24V                    MOTOR_Y4                                    4  G1      D1  5

                                                                                                                                                                                                R70 R69             D37  D36

                      R39 R40 D25                D24                                                                       R59 R60 D33        D32

                                                 1SMA4744A              Q3                                                            1SMA4744A             Q7                                  10K 10K             1SMA4744A
                                                 1SMA4744A              NCE4953                                                       1SMA4744A             NCE4953                                                 1SMA4744A

                      10K 10K                                     1  S1  D1  8                                             10K 10K                   1  S1     D1  8
                                                                  2  G1  D1  7                                                                       2  G1     D1  7
   MOTOR_X5 R42  10K                                              3  S2  D2  6      X5         MOTOR_X13R61           10K                            3  S2     D2  6   X13
                                                                  4  G2  D2  5      X6                                                               4  G2     D2  5   X14
   MOTOR_X6 R43  10K                                                                           MOTOR_X14 R62          10K

C                                                                                                                                                                                               MOTOR_DGND                                                                     C

                                                                                                                                                                                                MOTOR_VDD_24V

                                                               MOTOR_VDD_24V                                                                         MOTOR_VDD_24V

                                                                                                                                                                                                R78 R77                                  Q11
                                                                                                                                                                                                                                         NCE6005AS
                      R44 R46 D27                D26                                                                       R63 R64 D35        D34

                                                 1SMA4744A               Q4                                                               1SMA4744A         Q8                                             10K 10K                1  S2      D2  8  Y5
                                                 1SMA4744A               NCE4953                                                          1SMA4744A         NCE4953                   MOTOR_Y5                                    2  G2      D2  7  Y6
                                                                                                                                                                                                                                  3  S1      D1  6
                      10K 10K                                        1  S1   D1  8                                         10K 10K                      1  S1   D1  8                                                             4  G1      D1  5
                                                                     2  G1   D1  7                                                                      2  G1   D1  7
   MOTOR_X7 R47  10K                                                 3  S2   D2  6      X7             MOTOR_X15R65   10K                               3  S2   D2  6     X15         MOTOR_Y6
                                                                     4  G2   D2  5      X8                                                              4  G2   D2  5     X16
   MOTOR_X8 R48  10K                                                                                   MOTOR_X16 R66  10K                                                                       R76 R75             D39  D38

                                                                                                                                                                                                10K 10K             1SMA4744A

D                                                                            X()                                                                                                                                    1SMA4744A                                                  D

                                                                                                                                                                                                MOTOR_DGND

                                                                                                                                                                                                MOTOR_VDD_24V

                  VCC_24V MOTOR_VDD_24V                                                                                                                                                         R82 R81                                  Q12
                                                                                                                                                                                                                                         NCE6005AS
                                            F2                                                                                    J6
                                       JK30-050                                                                                   5557S-2*8P                                                    10K 10K                           1  S2      D2  8
                                                                                                                                                                                                                                  2  G2      D2  7
E                                                                 VDD_3V3                                                  X1 1   1    2  2   X2                       J7             MOTOR_Y7                                    3  S1      D1  6  Y7
                                                                     DGND                                                  X3 3   3    4  4   X4                       5557S-2*4P     MOTOR_Y8                                    4  G1      D1  5  Y8
                                                                                                                           X5 5   5    6  6   X6
                                                                                                                           X7 7   7    8  8   X8            Y1  1   1  2  2    Y2               R80 R79             D41  D40
                                                                                                                           X9 9   9   10  10  X10           Y3  3   3  4  4    Y4
                                                                                                                           X1111  11  12  12  X12           Y5  5   5  6  6    Y6                                                                                              E
                                                                                                                           X1313  13  14  14  X14           Y7  7   7  8  8    Y8
                                                                                                                           X1515  15  16  16  X16
                                                              D5                                                                                                                                10K 10K             1SMA4744A
                                                   BAT54S,215                                                                                                                                                       1SMA4744A
                                                                                                                                                            Y()
   MOTOR_CURRENT_ADC_PB0                         R49 1K                                    MOTOR_DGND                      X()

                                                                                 R50                                                                                                            MOTOR_DGND
                                                                                 0.5
                                                                                                                                                                                                Y()
                                                                             DGND

                                                                                                                                                                                                TITLE:                                                             REV: 1.0

                                                                                                                                                                                                             04-

                                                                                                                                                                                                                               Company: HX-SMJ01                   Sheet: 1/1

                                                                                                                                                                                                                               Date: 2021-10-19 Drawn By: 423857A

   1                                                        2                               3                                         4                                        5   6                                           7                        8
   1                                  2                                      3                                 4                    5

                                                                                     U9

                                                                         74HC237D,653                                 U11

   MOTOR_CTL_X_A0_PD3                                                 1  A0              Y0   15               1  1B     1C  16     MOTOR_X1
   MOTOR_CTL_X_A1_PD4                                                 2  A1              Y1   14               2  2B     2C  15     MOTOR_X2
   MOTOR_CTL_X_A2_PD5                                                                                          3  3B     3C  14     MOTOR_X3
                                                                      3 A2               Y2   13               4  4B     4C  13     MOTOR_X4
                                                                                         Y3   12               5  5B     5C  12     MOTOR_X5
A  MOTOR_CTL_X_LE_PD6                                                 4  LE#             Y4   11               6  6B     6C  11     MOTOR_X6                                        A
    MOTOR_CTL_X_E_PB5                                                 5  E1#             Y5   10               7  7B     7C  10     MOTOR_X7
   MOTOR_CTL_X_EN_PD7                                                 6  E2              Y6   9                8  E   COM    9
                                                                                                                                        MOTOR_VDD_24V
                                                                                         Y7 7

                                                              VDD_5V 16 VCC GND 8                              ULN2003AIDR
                                                                                                                 C48 100nF

                                                                         C45 100nF

                                                                                                               DGND

                                                                                                DGND

                                                                   VDD_5V                                             U12

                                                              U7              C44                              1  1B     1C  16     MOTOR_X8
                                                                              100nF                            2  2B     2C  15     MOTOR_X9
                                         DGND              1  N.C                                              3  3B     3C  14     MOTOR_X10
                                         VDD_5V            2  A                                                4  4B     4C  13     MOTOR_X11
                                                           3  GND                                              5  5B     5C  12     MOTOR_X12
                                                           4  Y                                                6  6B     6C  11     MOTOR_X13
                                                           5  VCC                                              7  7B     7C  10     MOTOR_X14
                                                                                                               8  E   COM    9
                                         74HC1G04GV,125 DGND                                                                          MOTOR_VDD_24V
B                                                                                                                                                                                   B

                                                                                U10                            ULN2003AIDR
                                                                         74HC237D,653                            C49 100nF

                                                                      1 A0               Y0 15
                                                                      2                       14               DGND
                                                                      3  A1              Y1   13
                                                                         A2              Y2   12
                                                                                         Y3   11
                                                                      4  LE#             Y4   10                      U13
                                                                      5  E1#             Y5

                                                                      6 E2               Y6   9                1  1B     1C  16     MOTOR_X15
                                                                                         Y7   7                2  2B     2C  15     MOTOR_X16
                                                                                                               3  3B     3C  14
                                                              VDD_5V  16 VCC             GND 8                 4  4B     4C  13     MOTOR_Y1
                                                                                                               5  5B     5C  12
                                                                         C46 100nF                             6  6B     6C  11       MOTOR_VDD_24V
                                                                                                               7  7B     7C  10
                                                                                                               8  E   COM    9

                                                                                                DGND           ULN2003AIDR

C                                                                                        VDD_5V                   C50 100nF                                                         C

                                                                                     U8           C47

                                                                         74HC137D,653             100nF        DGND

                                      MOTOR_CTL_Y_LE_PC12             4 LE# VCC 16                       DGND

                                      MOTOR_CTL_Y_A0_PD2              1  A0              Y0#  15                      U14
                                      MOTOR_CTL_Y_A1_PD1              2  A1              Y1#  14
                                      MOTOR_CTL_Y_A2_PD0                                                       1  1B     1C  16     MOTOR_Y2
                                                                      3 A2               Y2#  13               2  2B     2C  15     MOTOR_Y3
                                      MOTOR_CTL_Y_EN_PC11                                Y3#  12               3  3B     3C  14     MOTOR_Y4
                                                                      6  E1#             Y4#  11               4  4B     4C  13     MOTOR_Y5
                                                                      5  E2              Y5#  10               5  5B     5C  12     MOTOR_Y6
                                                                                         Y6#  9                6  6B     6C  11     MOTOR_Y7
                                                                                                               7  7B     7C  10     MOTOR_Y8
                                                                      8 GND              Y7# 7                 8  E   COM    9
                                                                                                                                      MOTOR_VDD_24V

                                                                   DGND                                        ULN2003AIDR
                                                                                                                 C51 100nF

D                                                                                                              DGND                                                                 D
                                   1
                                                                                                                  TITLE:                                                REV: 1.0

                                                                                                                               05-

                                                                                                                                    Company: HX-SMJ01                   Sheet: 1/1

                                                                                                                                    Date: 2021-10-19 Drawn By: 423857A

                                      2                                      3                                 4                    5
                     1                                2                                          3                              4                                      5
                                                                                                                                                                                RN18 1K
                                            PNP2_24V                           5.1V                                                           U17                                 RN191K
                                            PNP1_24V
   VDD_24V                                  PNP_IR                                                                                     1  1B          1C  16                         RN20  PNP2_PE8
                                                                                                                                       2  2B          2C  15                         1K    PNP1_PE9
   PNP2_24V              1  1                            RN4                   RN9                  C72 C74 C76                        3  3B          3C  14                               SIG2_INFRA_DETECT_PE10
   PNP1_24V              2  2                             10K                  2.7K                 100nF 100nF 100nF                  4  4B          4C  13                 RN14          SIG1_INFRA_DETECT_PE11
   PNP_IR                3  3                                                                                                          5  5B          5C  12                 1K
A  NPN_IR                4  4                                                                                                          6  6B          6C  11  VDD_3V3                                                                     A
   NPN2_24V              5  5                                                                                                          7  7B          7C  10                RN15
   NPN1_24V              6  6                                                                                                          8  E        COM    9                   1K                  NPN2_PE12
                         7  7                                                                                                                                                                     NPN1_PE13
                         8  8                                                                                                             ULN2003AIDR
                                                                                                                                                                                                  SW1_DETECT_PE14
                         VH3.96-8P     VDD_5V                                                                                                  C82 100nF                                          SW2_DETECT_PE15
                         J1                                                                                                                                                                       SW3_DETECT_PB13
                                                                         DGND                                                      DGND                                                           SW4_DETECT_PB14
                                                                                                                                                                                                  SW5_DETECT_PB15
                               R84 1K  R85          10K NPN_IR                                                                                                                                     SW6_DETECT_PD8

          Q13                     R83  RN2          10K NPN2_24V                                                                500mA                                                                                                     B
   NCE3400                        10K                     NPN1_24V
                                                          SW1_DETECT_IN                                                                                                                    MOTOR_DETECT_Y1_PD9
                                                          SW2_DETECT_IN                                                                       U18                                          MOTOR_DETECT_Y2_PD10
                                                          SW3_DETECT_IN                                                                                                                    MOTOR_DETECT_Y3_PD11
            DGND                                          SW4_DETECT_IN                                                                1  1B          1C  16                               MOTOR_DETECT_Y4_PD12
                                                          SW5_DETECT_IN                                                                2  2B          2C  15                               MOTOR_DETECT_Y5_PD13
                                                          SW6_DETECT_IN                                                                3  3B          3C  14                               MOTOR_DETECT_Y6_PD14
                                                                                                                                       4  4B          4C  13                               MOTOR_DETECT_Y7_PD15
         INFRARED_PW_EN_PB1                    RN3                       C68 C69 C70 C71 C73 C75 C77 C78 C79                           5  5B          5C  12  VDD_3V3                      MOTOR_DETECT_Y8_PC6
                                               10K                       100nF 100nF 100nF 100nF 100nF 100nF 100nF 100nF 100nF         6  6B          6C  11
B                                                                                                                                      7  7B          7C  10                                                                              C
                                                                                                                                       8  E        COM    9

                                                                                                                                          ULN2003AIDR

   J2                                                                                                                                     C83 100nF

   VH3.96-7P                                                    DGND

       7       7     SW6_DETECT_IN                                       RN5                                                       DGND
               6     SW5_DETECT_IN
       6       5     SW4_DETECT_IN                       Y1 24V          10K   5.1V
       5       4     SW3_DETECT_IN
       4       3     SW2_DETECT_IN           C52 100nF   Y2                                            RN10                                   U15
       3       2     SW1_DETECT_IN           C53 100nF                                                 2.7K
       2       1                             C54 100nF   Y3                                                                            1  1B     1C  16
       1              DGND                   C55 100nF                                                                                 2  2B     2C  15
                                             C56 100nF   Y4                                                                            3  3B     3C  14
                                             C57 100nF                                                                                 4  4B     4C  13
                                             C58 100nF   Y5                                                                            5  5B     5C  12
                                             C59 100nF                                                                                 6  6B     6C  11
                                                         Y6                                                                            7  7B     7C  10
                                       DGND                                                                                            8  E   COM    9
                                                         Y7

                                                         Y8

                                                                         RN6                                                                                  VDD_3V3
                                                                         10K

                                                                                                                       RN12            ULN2003AIDR
                                                                                                                       2.7K
C                                                                                                                                         C80 100nF

                                                                         RN7                                                       DGND                                   RN16
                                                                         10K                                                                                              1K
                                       C60 100nF         SW8 24V               5.1V                 DGND                                      U16                                          MOTOR_SW8_PC7
                                       C61 100nF                         RN8                                                                                              RN17
                     J5                C62 100nF         SW7              10K                        RN11                              1  1B     1C  16                     1K             MOTOR_SW7_PC8
                                       C63 100nF         SW6                                         2.7K                              2  2B     2C  15                                    MOTOR_SW6_PC9
                  5557S-2*4P           C64 100nF         SW5                                                                           3  3B     3C  14                                    MOTOR_SW5_PA8
                                       C65 100nF         SW4                                        DGND                               4  4B     4C  13                                    MOTOR_SW4_PA9
   SW1         1  1         2  2  SW2  C66 100nF         SW3                                                                           5  5B     5C  12                                    MOTOR_SW3_PA10
   SW3         3  3         4  4  SW4  C67 100nF         SW2                                                                           6  6B     6C  11                                    MOTOR_SW2_PA11
   SW5         5  5         6  6  SW6                    SW1                                                                           7  7B     7C  10                                    MOTOR_SW1_PA12
   SW7         7  7         8  8  SW8                                                                                                  8  E   COM    9

                                                                                                                                                              VDD_3V3

                                                                                                                                       ULN2003AIDR

                                       DGND                                                                            RN13               C81 100nF
                                                                                                                       2.7K

D                                                                                                                                  DGND                                                                    D

                                                                                                                                TITLE:                                                        REV: 1.0

                                                                                                                                             06-

                                                                                                                                                          Company: HX-SMJ01                   Sheet: 1/1

                                                                                                                                                          Date: 2021-10-19 Drawn By: 423857A

                     1                              2                                3                                          4                                      5
   1                                                                            2                      3                     4                                               5

A                                                         U19                                                                                                                                                         A

                  1                                              16                                                                     VDD_24V                           VDD_24V_LED
                  2                                              15
   REALY_R6_PC2   3   1B                                     1C  14  REALY_R6                                                                                          Q16
   REALY_R5_PC1   4   2B                                     2C  13  REALY_R5                                                                                          NCE3007S
   REALY_R4_PC0   5   3B                                     3C  12  REALY_R4
                  6   4B                                     4C  11  REALY_R3                                                      R95   R98                     1  S  D  8      C87                   2  2
   REALY_R3_PC15  7   5B                                     5C  10  REALY_R2                                                      10K   10K              D10 2     S  D  7                            1  1
   REALY_R2_PC14  8   6B                                     6C  9   REALY_R1                                                                                       S  D  6
   REALY_R1_PC13      7B                                     7C                                                                                                  3  G  D  5                 D13           VH3.96-2P
                      E                                   COM          VDD_24V                                                                                                                            J10
                                                                                                                                                                 4               100uF/50V  M7
                                                                                                                                                 1SMA4744A

                  ULN2003AIDR                                                                                LED_PC3
                     C84 100nF

                                                                                                                             Q14                                                      DGND
                                                                                                                             MMUN2233LT1G
                  DGND

   VDD_24V                                                                                                                   DGND                              LED

B                                                         LED10                                                                                                                                                       B

   R105               10K

                      D14 REALY_R6

                  M7

   VDD_24V                   LED9
                      10K
          R102        D12 REALY_R5

                  M7

                                                                                                    J12                                          VDD_12V                         VDD_12V_Lock

   VDD_24V                                                  LED8                       REALY_R6  7  7                                                                  Q17                                J13
                                                     10K                               REALY_R5  6                                                                     NCE3007S                           VH3.96-3A
          R96                                        D9 REALY_R4                       REALY_R4  5  6
                                                                                       REALY_R3  4  5
                  M7                                                                   REALY_R2  3  4                                                  R99     1    S  D  8      C88                      1  1
                                                                                       REALY_R1  2  3                                                     10K  2    S  D  7      100uF/50V                2  2
                                                                                                 1  2                                                          3    S  D  6                       D15     3  3
                                                                                   VDD_24V          1                                   R97 1K                 4    G  D  5                       M7
C  VDD_24V                                                                                                                                                                                                            C

                                                          LED7

      R94                                            10K                                                     12V_PWM_EN_PB6

                                                     D8 REALY_R3                                 A3963WV-7P                             Q15
                                                                                                                                        MMUN2233LT1G
                                                                                                                                                                                            DGND
                  M7

   VDD_24V                                                                                                                                                     INFRARED_PW_EN_PB1     R103      1K           Q18
                                                                                                                                                                                                             NCE3400
            R93                                             LED6                                                                   DGND
                                                     10K
                                                     D7 REALY_R2                                                                                                                            R104
                                                                                                                                                                                             10K

                  M7

   VDD_24V                                                                                                                                                                                             DGND

          R86                                              LED5
                                                     10K
                                                     D6 REALY_R1

                                                 M7                                                                                                                                                                   D
D

                                                                                                                             TITLE:                                                                    REV: 1.0

                                                                                                                                          07-

                                                                                                                                                               Company: HX-SMJ01                       Sheet: 1/1

                                                                                                                                                               Date: 2021-10-19 Drawn By: 423857A

   1                                                                            2                      3                     4                                               5
                                   1           2                              3                                           4                  5
A
B                                                                                                                                                                                            A
C
D                                                                                           VDD_3V3

                                   1                                 J3                                 R127
                                                                        1                               10K
                                                                        2
                                      10K3950                              1                            R131  1K               ADC1_PC5
                                                                           2

                                                                              D16                       R128      C92
                                                                              BAT54S,215                300K         1nF

                                                                                                                                                                                             B

                                                                              DGND VDD_3V3  DGND                  DGND

                                                                                            VDD_3V3

                                                                                                        R129

                                                                     J4                                 10K
                                                                        1
                                      10K3950                           2  1                            R132  1K               ADC2_PC4
                                                                           2
                                                                  2                                                                                                                          C

                                                                                            D17         R130            C93
                                                                                            BAT54S,215  300K              1nF

                                                                              DGND VDD_3V3  DGND                  DGND

                                                                              NTC                                                                                                            D

                                                                                         3                                 TITLE:                                                REV: 1.0

                                                                                                                                        08-  Company: HX-SMJ01                   Sheet: 1/1

                                                                                                                          4                  Date: 2021-10-19 Drawn By: 423857A

                                                                                                                                                                          5
