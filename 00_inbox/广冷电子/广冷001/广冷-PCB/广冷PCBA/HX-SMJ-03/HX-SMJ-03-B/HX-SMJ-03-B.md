# HX-SMJ-03-B

1                                               2                                            3                                                    4                                              5              6                                          7                                            8

   VCC                                                                                                             VCC

        R2                                                                                             R1               R62                                                                                         R61
                                                                                                                                                                                                                 8.2K
   C1 8.2K                                          U1                                     8.2K                    C25 8.2K                                      U7                                           C26 1uF

                                                    8              1  X0 R3 100K R4 1K C2 1uF                                                                      8               1  X12R63 100K     R64 1K
                                                    7              2                                                                                            X137               2
   100nF C3      1uF R5 1K R6             100K  X1     V+   OUT    3                                               100nF C27     1uF   R65 1K        R66  100K        V+    OUT    3
            D18                                        OUT   -IN   4                                                        D30                                       OUT    -IN   4
A                       R9                          6  -IN  +IN       IN_U1                       R8                                  R69                        6    -IN   +IN       IN_U7                       R68                                                                                                                               A
                        100K R10                       +IN     V-         R7                                                          100K R70                        +IN      V-         R67
                                          IN_U1 5                              24K VCC                                                                    IN_U7 5                              24K VCC
                                   3K                                                                                                            3K
                                          C4                                               100K D17                                                       C28                                                 100K D29

                                                       LM358PWR                                                                                                       LM358PWR

                                          100nF                                                                                                           100nF

   GND                                                                                                             GND
   VCC                                                                                                             VCC

        R12                                                                                            R11              R72                                                                                         R71
                                                                                                                                                                                                                 8.2K
   C5 8.2K                                          U2                                     8.2K                    C29 8.2K                                      U8                                           C30 1uF

                                                    8              1  X2 R13 100K R14 1K C6 1uF                                                                    8               1  X14R73 100K     R74 1K
                                                    7              2                                                                                            X157               2
   100nF C7      1uF   R15  1K       R16  100K  X3     V+   OUT    3                                               100nF C31     1uF   R75 1K        R76  100K        V+    OUT    3
            D20                                        OUT   -IN   4                                                        D32                                       OUT    -IN   4
                      R19      R20                  6  -IN  +IN       IN_U2                       R18                                 R79                        6    -IN   +IN       IN_U8                       R78
                      100K     3K                      +IN     V-         R17                                                         100K R80                        +IN      V-         R77
                                          IN_U2 5                              24K VCC                                                                    IN_U8 5                              24K VCC
                                                                                                                                                 3K
B                                         C8                                               100K D19                                                       C32                                                 100K D31                                                                                                                              B

                                                       LM358PWR                                                                                                       LM358PWR

                                          100nF                                                                                                           100nF

   GND                                                                                                             GND                                                                                                                                    U10                    VCC                          U11                   VCC
   VCC                                                                                                                                                                                                                                                    SN74LV4051APWR                                      SN74LV4051APWR
                                                                                                                                                                                                                                                                                        C34                                                C35
                                                                                                                                                                                                                                      X4        1    Y4   VCC         16  X2            100nF  X12    1  Y4   VCC   16  X10                100nF
                                                                                                                                                                                                                                      X6        2    Y6     Y2        15  X1                   X14    2  Y6     Y2  15  X9
                                                                                                                                                                                                                                      X_IN3     3    COM    Y1        14  X0     GND           X_IN4  3  COM    Y1  14  X8          GND
                                                                                                                                                                                                                                      X7        4    Y7                   X3                   X15    4  Y7             X11
        R22                                                                                            R21              VCC                                      Q1                   VCC                              Q17            X5        5    Y5        Y0     13  A                    X13    5  Y5   Y0    13  A
                                                                                                                                                                 S9014                                                 S9014                    6    INH       Y3     12  B                           6  INH  Y3    12  B
   C9 8.2K                                          U3                                                       8.2K               R81                                                           R105                                              7    GND              11  C                           7  GND        11  C
                                                                      X4 R23 100K R24 1K C10 1uF                                91 D1                                                         91 D9                                                             A     10                                       A    10
                                                                                                                                                                                                                                                                B                                              B
                                                    8              1                                                                                      Q2          R82                                     Q18         R106                  8 GND          C9                                     8 GND     C9
                                                    7              2                                                                                                                                          S9014       1K
   100nF C11     1uF   R25 1K        R26  100K  X5     V+   OUT    3                                                                                      S9014       1K
            D22                                        OUT   -IN   4
                      R29                           6  -IN  +IN       IN_U3                       R28                                  R83                                                           R107
                      100K R30                         +IN     V-         R27
                                          IN_U3 5                              24K VCC                                           X01   22K                                 GND        X09            22K                      GND
                                 3K
                                          C12                                              100K D21                     VCC                                                           VCC                                             GND                                                   GND

                                                       LM358PWR                                                                 R84                              Q3                           R108                     Q19
                                                                                                                                91 D2                            S9014                        91 D10                   S9014
                                          100nF

C                                                                                                                                                         Q4          R85                                     Q20         R109                                                                                                                      C
                                                                                                                                                                                                              S9014       1K
   GND                                                                                                                                                    S9014       1K
   VCC
                                                                                                                                       R86                                                           R110                                                 U12                    VCC
                                                                                                                                                                                                     22K
                                                                                                                                 X02   22K                                 GND        X010                                    GND                         SN74HC595PWR

        R32                                                                                      R31                    VCC                                      Q5                   VCC                              Q21                 X02  1    QB         VCC   16  X01    C36
                                                                                              8.2K                                                               S9014                                                 S9014               X03  2    QC           QA  15  QD3    100nF
   C13 8.2K                                         U4                                     C14 1uF                              R87                                                           R111                                         X04  3    QD               14
                                                                                                                                91 D3                                                         91 D11                                       X05  4    QE         SER   13  RCLK
                                                                                                                                                                                                                                           X06  5    QF        OE#    12
                                                    8              1  X6 R33 100K  R34 1K                                                                 Q6          R88                                     Q22         R112             X07  6    QG       RCLK    11
                                                    7              2                                                                                                                                          S9014       1K               X08  7    QH     SRCLK     10
   100nF C15     1uF   R35 1K        R36  100K  X7     V+   OUT    3                                                                                      S9014       1K                                                                        8    GND  SRCLR#      9   SRCLK
            D24                                        OUT   -IN   4                                                                                                                                                                                             QH'
                      R39                           6  -IN  +IN       IN_U4                       R38                                  R89                                                           R113                                                                 VQDC4C
                      100K R40                         +IN     V-         R37                                                                                                                        22K                                                                        GND
                                          IN_U4 5                              24K VCC                                           X03   22K                                 GND        X011                                    GND
                                 3K
                                          C16                                              100K D23                     VCC                                                           VCC                                             GND                                        VCC

                                                       LM358PWR                                                                 R90                              Q7                           R114                     Q23                                U13
                                                                                                                                91 D4                            S9014                        91 D12                   S9014                              SN74HC595PWR
                                          100nF

                                                                                                                                                          Q8          R91                                     Q24         R115             X010 1    QB         VCC   16  X09
                                                                                                                                                                                                              S9014       1K               X011 2    QC           QA  15
   GND                                                                                                                                                    S9014       1K                                                                   X012 3    QD               14  QD4
   VCC                                                                                                                                                                                                                                     X013 4    QE         SER   13
D                                                                                                                                      R92                                                           R116                                  X014 5    QF        OE#    12         C37                                                                D
                                                                                                                                                                                                     22K                                   X015 6    QG       RCLK    11
                                                                                                                                 X04   22K                                            X012                                                 X016 7    QH     SRCLK     10  RCLK   100nF
                                                                                                                                                                                                                                                     GND  SRCLR#      9   SRCLK
                                                                                                                                                                           GND                                                GND                 8              QH'

        R42                                                                                      R41                    VCC                                      Q9                   VCC                              Q25                                                VCC
                                                                                              8.2K                                                               S9014                                                 S9014
   C17 8.2K                                         U5                                     C18 1uF                              R93                                                           R117                                                                               GND
                                                                                                                                91 D5                                                         91 D13

                                                    8              1  X8 R43 100K  R44 1K                                                                 Q10         R94                                     Q26         R118        GND
                                                    7              2                                                                                                                                          S9014       1K
   100nF C19     1uF   R45 1K        R46  100K  X9     V+   OUT    3                                                                                      S9014       1K
            D26                                        OUT   -IN   4
                      R49                          6   -IN  +IN       IN_U5                       R48                                  R95                                                           R119
                      100K R50            IN_U5 5      +IN     V-         R47                                                                                                                        22K
                                                                               24K VCC                                           X05   22K                                 GND        X013                                    GND
                                 3K
                                          C20                                              100K D25                     VCC R96                                                       VCC R120

                                                       LM358PWR                                                                 91 D6                            Q11                          91 D14                   Q27
                                                                                                                                                                 S9014                                                 S9014
                                          100nF

                                                                                                                                                          Q12         R97                                     Q28         R121
                                                                                                                                                                                                              S9014       1K
   GND                                                                                                                                                    S9014       1K                                                                                                                                                            J1
   VCC
                                                                                                                                       R98                                                           R122                                                                      VCC                                      PHB-2*5AW
                                                                                                                                                                                                     22K
                                                                                                                                 X06   22K                                 GND        X014                                    GND                                                     C38                                  9     9  10  10 X_IN4
                                                                                                                                                                                                                                                                                      47uF                                 7     7   8  8 X_IN3
E                                                                                                                       VCC R99                                                       VCC R123                                                                                                                VCC RCLK     5     5   6  6C          E
                                                                                                                                                                                                                                                                               GND                                         3     3   4  4B
        R52                                                                                      R51                            91 D7                            Q13                          91 D15                   Q29                                                                               GND        SRCLK            2  2A
                                                                                              8.2K                                                               S9014                                                 S9014                                                                                        QD3
   C21 8.2K                                         U6                                     C22 1uF                                                                                                                                                                                                                         11

                                                   8               1  X10R53 100K  R54 1K                                                                 Q14         R100                                    Q30         R124
                                                X117               2                                                                                      S9014       1K                                      S9014       1K
   100nF C23     1uF   R55 1K        R56  100K         V+   OUT    3
            D28                                        OUT   -IN   4
                      R59                           6  -IN  +IN       IN_U6                       R58                                  R101                                                          R125
                      100K R60                         +IN     V-         R57                                                                                                                        22K
                                          IN_U6 5                              24K VCC                                           X07   22K                                 GND        X015                                       GND
                                 3K
                                          C24                                              100K D27                     VCC R102                                                      VCC R126                         Q31

                                                       LM358PWR                                                                 91 D8                            Q15                          91 D16
                                                                                                                                                                 S9014
                                          100nF

   GND                                                                                                                                                    Q16         R103                                    Q32         R127
                                                                                                                                                          S9014       1K                                      S9014       1K

                                                                                                                                       R104                                                          R128
                                                                                                                                                                                                     22K
                                                                                                                                 X08   22K                                 GND        X016                             S9014 GND

                                                                                                                                                                                                                                                               TITLE:                                                                   REV: 1.0

                                                                                                                                                                                                                                                                            HX-SMJ-03-B

                                                                                                                                                                                                                                                                                            Company: HX-SMJ-03                          Sheet: 1/1

                                                                                                                                                                                                                                                                                            Date: 2021-10-19 Drawn By: 423857A

                      1                                               2                                            3                                                    4                                              5              6                                          7                                            8
