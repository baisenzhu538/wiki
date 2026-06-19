# 红外光栅（主控）原理图_HX-SMJ-03-A_V1.1

1                                                           2                        3                                              4                                           5

   IN24V                                 D33 VDD_24V

                                        SS24

   J2                                                  C39                                            5V@3A(max) output

A  1   1  Out                            D34           22uF/50V                                                                                                           VCC_5V                                                                  A
   2   2                                P6SMB33CA
   3   3                                                                        VCC_24V               C40                               L1
                                                                                                      100nF/50V                   15uH/6.25A

   HY2.0-3AW                                       GND

                                                                                                      U14                           D35              C41 C38                                                               J1         VCC_5V
                                                                                                                                  B560C              47uF 47uF
                                                                                                      TPS54360                                                      R133                R129                               PHB-2*5AW
                                                                                                                                  FB                            FB
                                                                                                   1  BOOT SW      8                                    DGND        53.6K/1% 2K                     A  2      2                1  1  QD3
                                                                                                   2  VIN GND      7                                                                                          4                3  3  SRCLK
                                                                                                   3  EN COMP      6                                                                                B  4      6                5  5  RCLK
                                                                                                                                                                                                              8                7  7
                                                                                                                                                                                                    C  6      10               9  9

                                        VCC_5V                                                     4 RT/CLK FB 5                                                                                    X_IN3 8
                                                                                                      9 EP
                                                                                C42                                                                                                        LED3     X_IN4 10
                                                                                22uF
                 R135                        NCE3401(NC)                                    R143                                  13.3K/1% R141                     R132
                 1K(NC)                                                                 523K/1%                                                                     10.2K/1%
                                                  Q36
                                                                    R138                                     DGND                                                                                                                     GND
                                                                    10K(NC)
                                                                                                   R131                                              C78
                                                                                            R142   162K/1%                         C79               39pF           DGND
                                                                                        37.4K/1%                                  8.2nF
B                                                      Out                                                                                                                                                                                        B

                                  R134           Q37        R139
               Level Out 1K                      NCE3400    10K(NC)

                                                                                DGND                                                             DGND

                                        GND

                                                                                    U9                                                                                                                                         VCC_5V

C                                                                                   STM8AF6213PDU                                                                                                                                                                   C

            A          A                      1  [LINUART_CK]TIM5_CH1/BEEP/(HS)PD4      PD3(HS)/AIN4/TIM5_CH2/ADC_ETR         20  Level Out
            B          B                      2                                                                               19  LED Out
            C          C                      3  AIN5/LINUART_TX/(HS)PD5                           PD2(HS)/AIN3[TIM5_CH3]     18  SWITCH                            VCC_5V                                                           R130
                       NRST                   4                                                                               17  X_IN2                                                                                              2K
   GND                 X_IN3                  5  AIN6/LINUART_RX/(HS)PD6                              PD1(HS)/SWIM            16  X_IN1                                                CN1
   VCC_5V              X_IN4                  6                                                                               15                                                                                                         LED4
                                              7  NRST                                             PC7(HS)/SPI_MISO[TIM1_CH2]  14  QD3        X_IN2
                 C75 1uF                      8                                                                               13  QD1         X_IN1                                                                                     Q38
                                              9  OSCIN/PA1                                        PC6(HS)/SPI_MOSI[TIM1_CH1]  12  RCLK                                                  5  5                         R137               NCE3400
                                             10                                                                               11  SRCLK      QD1                                        4  4         LED Out 1K
                                                 OSCOUT/PA2                                       PC5(HS)/SPI_SCK[TIM5_CH1]                  RCLK                              SWITCH   3  3
                                                                                                                                             SRCLK                                      2  2                         R136
                                                 VSS                            PC4(HS)/TIM1_CH4/CLK_CCO/AIN2[TIM1_CH2N]                                                          NRST  1  1        Level Out 1K

                                                 VCAP                                   PC3(HS)/TIM1_CH3[TLI][TIM1_CH1N]                                            DGND

                                                 VDD                                              PB4(T)/I2C_SCL[ADC_ETR]

                                                 [SPI_NSS]TIM5_CH3/(HS)PA3                        PB5(T)/I2C_SDA[TIM1_BKIN]

                                                                                                                                                                                        XH-5A

                    VCC_5V

   VCC_5V                                                                                                                                                                                                                      GND

                                        R140

D         C33                           10K NRST                                                                                                                                                                                                               D

          100nF                         C76                                                                                                                                                                                           REV: 1.0

                                        100nF                                                                                                          TITLE:

       GND                                                                                                                                                          01-

                                        GND                                                                                                                               Company: HX-SMJ-03                                          Sheet: 1/1

                                                                                                                                                                          Date: 2021-10-19 Drawn By: 423857A

                 1                                                           2                        3                                              4                                           5
                           1                                                       2                                                 3                                      4                            5                                                6                                                           7                                         8

   VCC_5V                                                                                      VCC_5V                                                                                            VCC_5V                                                               VCC_5V

                                                            R3 100K                                               R2                                  R6 100K                                                                           R43 100K                                             R42                                          R46 100K

   R1                                               U1.1 VCC_5V                                                   8.2K                                U1.2                                         R41                                  U5.1 VCC_5V                                          8.2K                                         U5.2
                                                                                                                                                                                                 8.2K
   8.2K

                C2 1uF        R4 1K                 2-           8  GND +V                                            C3 1uF               R5 1K 6 -                                                    C18 1uF       R44 1K            2-     8  GND +V                                     C19 1uF                           R45 1K 6 -

                                                                            1 X1                                                                                7 X2                                                                                      1 X9                                                                                      7 X10

A                             VCC_5V 3 +                                                                                       R9    C43   IN_U1 5 +                                                                             VCC_5V 3 +                                                           R49                 C51      IN_U5 5 +                                     A

                                                                 4          LMV358IPWR                                                                          LMV358IPWR                                                                     4          LMV358IPWR                                                                                LMV358IPWR
                                                                                                              D2                                                                                                                                                                        D10
                                                                                                                               100K 11pF                                                                                                                                                              100K 11pF

                           R8 C44             R7                                                                                                                                                                      R48 C52    R47
                                             8.2K                                                                                                                                                                                8.2K

                                             IN_U1                                             GND                                                                                                                               IN_U5                                GND

   D1                      100K 11pF                C4                      0.54V                                                                                                                D9                   100K 11pF         C20

                              R10                                                                                                                                                                                     R50

                              1K                    100nF                                                                                                                                                             1K                100nF

   GND                                                                                         VCC_5V                                                                                            GND                                                                  VCC_5V
   VCC_5V                                                                                                                                                                                        VCC_5V

                                                            R13 100K                                              R12                                 R16 100K                                                                          R53 100K                                             R52                                          R56 100K

          R11                                       U2.1 VCC_5V                                                   8.2K                                U2.2                                         R51                                  U6.1 VCC_5V                                          8.2K                                         U6.2
B 8.2K                                                                                                                                                                                           8.2K
                                                                                                                                                                                                                                                                                                                                                                                 B
                              R14 1K                                                                                                                                                                                  R54 1K
                C6 1uF                              2-           8  GND +V                                            C7 1uF               R15 1K 6 -                                                   C22 1uF                         2-     8  GND +V                                     C23 1uF                           R55 1K 6 -

                                                                            1 X3                                                                                7 X4                                                                                      1 X11                                                                                     7 X12

                              VCC_5V 3 +                                                                                       R19   C45   IN_U2 5 +                                                                  VCC_5V 3 +                                                                                          C53      IN_U6 5 +

                                                                 4          LMV358IPWR                                                                          LMV358IPWR                                                                     4          LMV358IPWR                                  R59                                           LMV358IPWR

                                                                                               D4                              100K 11pF                                                                                                                                                               100K 11pF
                                                                                                                                                                                                                                                                      D12
                           R18 C46           R17                                                                                                                                                                      R58 C54    R57
                                             8.2K                                                                                                                                                                                8.2K

                                             IN_U2                                             GND                                                                                                                               IN_U6                                GND

   D3                      100K 11pF                C8                                                                                                                                           D11                  100K 11pF         C24

                              R20                                                                                                                                                                                     R60

                              1K                    100nF                                                                                                                                                             1K                100nF

   GND                                                                                                                                                                                           GND

          VCC_5V                                                                               VCC_5V                                                                                            VCC_5V                                                               VCC_5V

C                                                           R23 100K                                R22                                               R26 100K                                                                          R63 100K                                             R62                                          R66 100K                               C

    R21                                             U3.1 VCC_5V                                                   8.2K                                U3.2                                         R61                                  U7.1 VCC_5V                                          8.2K                                         U7.2
   8.2K                                                                                                                                                                                          8.2K

                C10 1uF       R24 1K                2-           8  GND +V                                            C11 1uF              R25 1K 6 -                                                   C26 1uF       R64 1K            2-     8  GND +V                                     C27 1uF                           R65 1K     6-
                                                    3+                                                                                                                                                                                  3+                                                                       R69                      5+
                              VCC_5V                                        1 X5                                               R29   C47   IN_U3 5 +             7 X6                                                 VCC_5V                              1 X13                                                           C55      IN_U7            7 X14
                                                                            LMV358IPWR                                                                          LMV358IPWR                                                                                LMV358IPWR                                                                                LMV358IPWR
                                                                 4                                                                                                                                                                             4

                                                                                               D6                              100K 11pF                                                                                                                              D14                             100K 11pF

                           R28 C48           R27                                                                                                                                                                      R68 C56    R67
                                             8.2K                                                                                                                                                                                8.2K

                                             IN_U3                                             GND                                                                                                                               IN_U7                                GND

   D5                      100K 11pF                C12                                                                                                                                          D13                  100K 11pF         C28

                              R30                                                                                                                                                                                     R70

                              1K                    100nF                                                                                                                                                             1K                100nF

D                                                                                                                                                                                                                                                                                                                                                                                                                                                                        D

          GND                                                                                                                                                                                    GND
          VCC_5V
                                                                                               VCC_5V                                                                                            VCC_5V                                                               VCC_5V
          R31
         8.2K                                               R33 100K                                  R32                                             R36 100K                                                                          R73 100K                                             R72                                          R76 100K
                                                                                                      8.2K                                                                                                                                                                                                                                U8.2
                  C14 1uF                           U4.1         VCC_5V                                                                               U4.2                                         R71                                  U8.1 VCC_5V                                          8.2K
                                                         2                                              C15 1uF                                                                                  8.2K
                                                         3
                              R34 1K                             8  GND +V                     D8                                          R35 1K     6-                                                C30 1uF       R74 1K            2-     8  GND +V                                     C31 1uF                           R75 1K 6 -
                                                                                                                                                      5+
                              VCC_5V                          -             1 X7                                                                                   7 X8                                                                                   1 X15                                                                                     7 X16
                                                                                                                                                              LMV358IPWR
                                                              +                                                                R39   C49   IN_U4                                                                      VCC_5V 3 +                                                                      R79                 C57      IN_U8 5 +
                                                                                                                               100K
                                                                             LMV358IPWR4                                                                                                                                                       4          LMV358IPWR                                                                                LMV358IPWR

                                                                                                                                     11pF                                                                                                                                                             100K 11pF

                            R38 C50          R37                                                                                                                                                                      R78 C58    R77                                  D16
                                             8.2K                                                                                                                                                                                8.2K
                           100K 11pF         IN_U4
                                        R40                                                    GND                                                                                                                               IN_U8                                GND
                                        1K              C16
            D7                                                                                                                                                                                   D15                  100K 11pF         C32
E                                                      100nF
                                                                                                                                                                                                                      R80

                                                                                                                                                                                                                      1K                100nF                                                                                                                                    E

   GND                                                                                                                                                                                           GND                                                                                                  VCC_5V

                                                                            U10                                   VCC_5V                                       U11                       VCC_5V                    5                                                                                                  C1       C5  C9     C13 C17 C21 C25 C29
                                                                            CD4051BPWR
                                                                                                                                                          CD4051BPWR                                                                                                                                                  100nF 100nF 100nF 100nF 100nF 100nF 100nF 100nF

                              C59 11pF X5                   1    Y4         VCC    16  X3 C63  11pF                                     C67 11pF X13  1   Y4    VCC    16  X11C71  11pF
                              C60 11pF X7                   2    Y6           Y2   15  X2 C64  11pF                                     C68 11pF X15  2   Y6      Y2   15  X10C72  11pF
                                                                              Y1   14  X1 C65  11pF                                     C69 11pF X16              Y1   14  X9 C73  11pF
                              C61 11pF X8                   3    COM          Y0   13  X4 C66  11pF                   C34               C70 11pF X14  3   COM     Y0   13  X12C74  11pF    C35                                                                                                        GND
                              C62 11pF X6                   4    Y7           Y3   12                                 100nF                           4   Y7      Y3   12                100nF
                                                            5    Y5             A  11                                                         GND     5   Y5        A  11
                                                            6    INH                                                                                  6   INH

                                                            7    GND        B      10                             GND                                 7   GND       B  10                                                                                                                    TITLE:
                                                            8    GND        C      9                                                                  8   GND       C  9
                                                                                                                                                                                                                                                                                                          02-
                                             GND                                               A                                                                                      GND                                                                                                                                                                              REV: 1.0
                                                                                               B
                                                                                               C                                                                                   A                                                                                                                                      Company: Your Company                    Sheet: 1/1
                                                                                                                                                                                   B
                                                                                               X_IN1                                                                               C
                                                                                                                                                                                   X_IN2

                                                                                                                                                                                                                                                                                                                          Date: 2021-12-11 Drawn By: ncount0

                           1                                                       2                                                 3                                      4                                                                             6                                                           7                                         8
   1                                 2                                               3       4                                       5

   VCC_5V                               VCC_5V

      R81             Q1                R105                                  Q17
      91 D17          S9014             91 D25                                S9014

                 Q2        R82                                           Q18       R106
                                                                         S9014     1K
                 S9014     1K

A          R83                                  R107                                                                                                                      A
                                                22K
      X01  22K                  GND     X09                                             GND                       U12                                       VCC_5V

   VCC_5V                               VCC_5V                                                                    SN74LV595APWR                                    C36
                                                                                                                                                                   100nF
      R84             Q3                R108                                  Q19                    X02  1  QB         VCC   16     X01
      91 D18          S9014             91 D26                                S9014                  X03  2  QC           QA  15     QD1                    GND
                                                                                                     X04  3  QD               14
                 Q4        R85                                           Q20       R109              X05  4  QE         SER   13     RCLK            QD1
                                                                         S9014     1K                X06  5  QF        OE#    12     SRCLK
                 S9014     1K                                                                        X07  6  QG       RCLK    11                     RCLK
                                                                                                     X08  7  QH     SRCLK     10             VCC_5V  SRCLK
           R86                                                   R110                                     8  GND  SRCLR#      9
                                                     X010 22K                                                            QH'         QD2
      X02  22K                  GND                                                     GND
                                        VCC_5V
   VCC_5V
                                                    R111
      R87             Q5                            91 D27                    Q21
                      S9014                                                   S9014
      91 D19                                                                                    GND

                 Q6        R88                                           Q22       R112
                                                                         S9014     1K
                 S9014     1K

           R89                                  R113

      X03  22K                  GND     X011 22K                                        GND

B  VCC_5V                               VCC_5V                                                                                                                            B

      R90             Q7                R114                                  Q23
      91 D20          S9014             91 D28                                S9014

                 Q8        R91                                           Q24       R115
                                                                         S9014     1K
                 S9014     1K                                                                                                                               VCC_5V

           R92                                                     R116                                              U13
                                                       X012 22K
           22K                                                                                                       SN74LV595APWR
                                        VCC_5V
      X04                       GND                                                     GND          X010 1     QB         VCC   16
                                                      R117                                           X011 2     QC           QA  15
   VCC_5V                                             91 D29                                         X012 3     QD               14  X09
                                                                                                     X013 4     QE         SER   13  QD2
      R93             Q9                                                      Q25                    X014 5     QF        OE#    12                                C37
                      S9014                                                   S9014                  X015 6     QG       RCLK    11  RCLK                          100nF
      91 D21                                                                                         X016 7     QH     SRCLK     10  SRCLK
                                                                                                                GND  SRCLR#      9                   RCLK   GND
                 Q10       R94                                           Q26       R118                     8               QH'         VCC_5V       SRCLK
                                                                         S9014     1K
                 S9014     1K

           R95                                  R119

      X05  22K                  GND     X013 22K                                        GND

   VCC_5V                               VCC_5V                                                  GND

      R96             Q11               R120                                  Q27

C     91 D22          S9014             91 D30                                S9014                                                                                       C

                 Q12       R97                                           Q28       R121
                                                                         S9014     1K
                 S9014     1K

           R98                                                     R122
                                                       X014 22K
      X06  22K                  GND                                                     GND
                                        VCC_5V
   VCC_5V
                                                      R123
      R99             Q13                             91 D31                  Q29
                      S9014                                                   S9014
      91 D23

                 Q14       R100                                          Q30       R124
                 S9014     1K                                            S9014     1K

           R101                                 R125

      X07  22K                  GND     X015 22K                                        GND

   VCC_5V                               VCC_5V

      R102            Q15               R126                                  Q31
      91 D24          S9014
                                        91 D32

                 Q16       R103                                          Q32       R127

D                S9014     1K                                            S9014     1K                                                                                     D

           R104                                 R128

      X08  22K                  GND     X016 22K                              S9014 GND

                                                                                              TITLE:                                                        REV: 1.0

                                                                                                           03-       Company: Your Company                  Sheet: 1/1

   1                                 2                                               3       4                       Date: 2021-12-11 Drawn By: ncount0

                                                                                                                                                  5
