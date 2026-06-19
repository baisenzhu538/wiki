# 红外光栅（外设）原理图_HX-SMJ-03-B_V1.1

1                                                      2                                      3                                    4                                5                                                    6                               7                                8

   VCC_5V                                         R3                        VCC_5V                                           R6                                        VCC_5V                                                                 VCC_5V

                                                  100K                           R2                                          100K                                                                             R43 100K                             R42                                   R46 100K
                                                                                                                                                                                                                                                                                         U5.2
   R1                                    U1.1 VCC_5V                             8.2K                                   U1.2                                            R41                                   U5.1 VCC_5V                          8.2K
                                                                                                                                                                       8.2K
   8.2K

         C2 1uF              R4 1K           2-      8  GND +V                            C3 1uF                R5 1K   6-                                                   C18 1uF       R44 1K             2-       8  GND +V                   C19 1uF                    R45 1K     6-
                                                                                                                        5+                                                                                    3+                                                                  IN_U5  5+
A                                                               1 X1                                                                  7 X2                                                    VCC_5V                              1 X9                                                             7 X10                   A

                             VCC_5V 3 +                                                                   C33   IN_U1

                                                     4          LMV358IPWR                         R9                                 LMV358IPWR                                                                       4          LMV358IPWR                      R49                              LMV358IPWR
                                                                                                                                                                                                                                                                  100K 11pF
                                                                                                   100K 11pF

                        R8 C39     R7                                       D18                                                                                                       R48 C47           R47                                   D26
                                   8.2K                                                                                                                                                                 8.2K

   D17                  100K 11pF  IN_U1                              0.54V GND                                                                                        D25            100K 11pF         IN_U5                                 GND
                                             C4                                                                                                                                                    R50            C20

                             R10

                             1K          100nF                                                                                                                                             1K                 100nF

   GND                                                                      VCC_5V                                                                                     GND                                                                    VCC_5V
   VCC_5V                                                                                                                                                              VCC_5V

                                                 R13 100K                        R12                                    R16 100K                                                                              R53 100K                             R52                                   R56 100K
                                                                                                                        U2.2
   R11                                   U2.1 VCC_5V                             8.2K                                                                                   R51                                   U6.1 VCC_5V                          8.2K                                  U6.2
                                                                                                                                                                       8.2K
B  8.2K                                                                                                                                                                                                                                                                                                                    B

         C6 1uF              R14 1K          2-      8  GND +V                         C7 1uF                   R15 1K  6-                                                   C22 1uF       R54 1K             2-       8  GND +V                         C23 1uF              R55 1K     6-
                                             3+                                  D20                                    5+                                                                                    3+                              D28                                 IN_U6  5+
                             VCC_5V                             1 X3                                      C40   IN_U2                  7 X4                                                VCC_5V                                 1 X11                                                             7 X12
                                                                LMV358IPWR                                                            LMV358IPWR                                                                                  LMV358IPWR                                                       LMV358IPWR
                                                     4                                             R19                                                                                                                 4                                          R59
                                                                                                   100K                                                                                                                                                           100K
                                                                                                          11pF                                                                                                                                                          11pF

                        R18 C41    R17                                                                                                                                                R58               R57
                                   8.2K
                                                                                                                                                                                                        8.2K

   D19                  100K 11pF  IN_U2                                    GND                                                                                        D27            100K 11pF         IN_U6                                 GND
                                             C8                                                                                                                                                                   C24

                             R20                                                                                                                                                           R60

                             1K          100nF                                                                                                                                             1K                 100nF

                GND                                                         VCC_5V                                                                                     GND                                                                    VCC_5V
                VCC_5V                                                                                                                                                 VCC_5V
                                                                                 R22                                                                                                                                                                                                                                       C
C                                               R23 100K                         8.2K                                   R26 100K                                                                              R63 100K                                                                   R66 100K
                                                                                                                        U3.2                                                                                                                       R62
                  R21                    U3.1 VCC_5V
                 8.2K                                                                                                                                                   R61                                   U7.1 VCC_5V                          8.2K                                  U7.2
                                                                                                                                                                       8.2K

         C10 1uF             R24 1K          2-      8  GND +V                            C11 1uF               R25 1K 6 -                                                   C26 1uF       R64 1K             2-       8  GND +V                         C27 1uF              R65 1K     6-
                                             3+                                                                                                                                                               3+                              D30                                        5+
                             VCC_5V                             1 X5                                      C42   IN_U3 5 +              7 X6                                                VCC_5V                                 1 X13                                 C50   IN_U7                7 X14
                                                                LMV358IPWR                                                            LMV358IPWR                                                                                  LMV358IPWR                                                       LMV358IPWR
                                                     4                                             R29                                                                                                                 4                                          R69
                                                                                                                                                                                                                                                                  100K
                                                                                                   100K 11pF                                                                                                                                                            11pF

                        R28 C43    R27                                      D22                                                                                                       R68 C51           R67
                                   8.2K                                                                                                                                                                 8.2K

   D21                  100K 11pF  IN_U3                                    GND                                                                                        D29            100K 11pF         IN_U7                                 GND
                                             C12                                                                                                                                                                  C28

                             R30                                                                                                                                                           R70

                             1K          100nF                                                                                                                                             1K                 100nF

D                                                                                                                                                                                                                                                                                                                          D

   GND                                                                      VCC_5V                                                                                     GND                                                                    VCC_5V
   VCC_5V                                                                                                                                                              VCC_5V

                                                 R33 100K                        R32                                    R36 100K                                                                              R73 100K                             R72                                   R76 100K
                                                                                                                        U4.2                                                                                                                                                             U8.2
    R31                                  U4.1 VCC_5V                             8.2K                                                                                   R71                                   U8.1 VCC_5V                          8.2K
   8.2K                                                                                                                                                                8.2K

         C14 1uF             R34 1K          2-      8  GND +V                   C15 1uF                        R35 1K 6 -                                                   C30 1uF       R74 1K             2-       8  GND +V                   C31 1uF                    R75 1K     6-

                                                                1 X7                                                                  7 X8                                                                                        1 X15                                                            7 X16

                             VCC_5V 3 +                                                                         IN_U4 5 +                                                                  VCC_5V 3 +                                                                   C52   IN_U8 5 +

                                                     4          LMV358IPWR                         R39                             LMV358IPWR                                                                          4          LMV358IPWR                      R79                              LMV358IPWR

                                                                                                   100K 11pF                                                                                                                                                      100K 11pF

                        R38 C45    R37                                      D24                                                                                                       R78 C53           R77                                   D32
                                   8.2K                                                                                                                                                                 8.2K

   D23                  100K 11pF  IN_U4                                    GND                                                                                        D31            100K 11pF         IN_U8                                 GND
                                             C16                                                                                                                                                                  C32

E                            R40                                                                                                                                                           R80                                                                                                                             E

                             1K          100nF                                                                                                                                             1K                 100nF

   GND                                                                                                                                                                 GND                                                                               VCC_5V

                                        U10                                 VCC_5V                                           U11                         VCC_5V                                                                                               C1 C5 C9 C13 C17 C21 C25 C29
                                        CD4051BPWR                                                                           CD4051BPWR                                                                                                                      100nF 100nF 100nF 100nF 100nF 100nF 100nF 100nF
                                                                                   C34                                                                          C35
         C54 11pF       X5   1 Y4        VCC 16         X3      C58 11pF           100nF           C69 11pF X13  1 Y4         VCC 16      X11 C65 11pF          100nF                                                                                    GND
         C55 11pF       X7   2                   15     X2      C59 11pF                           C68 11pF X15  2                    15  X10 C64 11pF
                             3     Y6    Y2      14     X1      C60 11pF    GND                    C66 11pF X16  3      Y6       Y2   14  X9 C63 11pF    GND
         C57 11pF       X8   4     COM   Y1      13     X4      C61 11pF                           C67 11pF X14  4      COM      Y1   13  X12 C62 11pF
         C56 11pF       X6   5     Y7    Y0      12                                                              5      Y7       Y0   12
                                   Y5    Y3                                                               GND           Y5       Y3
                             6                   11                                                              6                    11
                             7     INH   A       10                                                              7      INH        A  10                                                                                                      TITLE:
                             8     GND   B       9                                                               8      GND        B  9
                                   GND   C                                                                              GND        C                                                                                                                       01-
                                                                                                                                                                                                                                                                                                               REV: 1.0

                        GND                                        A                                                                              A                                                                                                               Company: HX-SMJ-03                           Sheet: 1/1
                                                                   B                                                                              B
                                                                   C                                                                              C                                                                                                               Date: 2021-10-19 Drawn By: 423857A

                                                                   X_IN3                                                                          X_IN4

         1                                                      2                                      3                                    4                                5                                                    6                               7                                8
   1                               2                                    3                  4                                            5

   VCC_5V                              VCC_5V

      R81               Q1             R105                                  Q17                                   J1                 VCC_5V
      91 D1             S9014          91 D9                                 S9014

                   Q2        R82                                        Q18       R106                             PHB-2*5AW

                   S9014     1K                                         S9014     1K             A  A         2    2    1  1   QD3
                                                                                                 B                 4    3  3   SRCLK
A            R83                               R107                                              C  B         4    6    5  5   RCLK                                       A
                                                                                           X_IN3                   8    7  7
             22K                               22K                                         X_IN4    C         6    10   9  9

      X01                         GND  X09                                            GND           X_IN3 8

   VCC_5V                              VCC_5V                                                       X_IN4 10

      R84               Q3             R108                                  Q19                                                           C38
      91 D2             S9014          91 D10                                S9014
                                                                                                                                           47uF

                   Q4        R85                                        Q20       R109
                                                                        S9014     1K
                   S9014     1K

             R86                                                  R110                                                             GND
                                                      X010 22K
      X02    22K                  GND                                                 GND
                                       VCC_5V
   VCC_5V
                                                     R111
      R87               Q5                           91 D11                  Q21
                        S9014                                                S9014
      91 D3

                   Q6        R88                                        Q22       R112
                                                                        S9014     1K
                   S9014     1K

             R89                               R113

      X03    22K                  GND                 X011 22K                        GND

B  VCC_5V                              VCC_5V                                                                                                   VCC_5V                    B

      R90               Q7             R114                                  Q23                                   U12
      91 D4             S9014          91 D12                                S9014
                                                                                                                   SN74LV595APWR

                                                                                                    X02  1    QB         VCC   16
                                                                                                    X03  2    QC           QA
                   Q8        R91                                        Q24       R115              X04  3    QD               15 X01
                                                                        S9014     1K                X05  4    QE         SER
                   S9014     1K                                                                     X06  5    QF        OE#    14 QD3                  C36
                                                                                                    X07  6    QG       RCLK                            100nF
             R92                                                  R116                              X08  7    QH     SRCLK     13
                                                      X012 22K                                           8    GND  SRCLR#                       GND
             22K                                                                                                          QH'  12 RCLK
                                       VCC_5V
      X04                         GND                                                 GND                                      11 SRCLK
                                                     R117
   VCC_5V                                            91 D13                                                                    10     VCC_5V
                                                                                                                               9 QD4
      R93               Q9                                                   Q25
                        S9014                                                S9014
      91 D5

                   Q10       R94                                        Q26       R118        GND
                                                                        S9014     1K
                   S9014     1K

             R95                               R119

      X05    22K                  GND                 X013 22K                        GND

   VCC_5V                              VCC_5V                                                                      U13                          VCC_5V

      R96               Q11            R120                                  Q27                                   SN74LV595APWR

C     91 D6             S9014          91 D14                                S9014                  X010 1    QB         VCC   16                                         C
                                                                                                    X011 2    QC           QA  15
                             R97                                                  R121              X012 3    QD               14  X09
                                                                                  1K                X013 4    QE         SER   13
                   Q12       1K                                         Q28                         X014 5    QF        OE#    12  QD4           C37
                                                                        S9014                       X015 6    QG       RCLK    11
                   S9014                                                                            X016 7    QH     SRCLK     10
                                                                                                              GND  SRCLR#      9
             R98                                                  R122                                     8              QH'      RCLK          100nF
                                                      X014 22K                                                                     SRCLK
      X06    22K                  GND                                                 GND
                                       VCC_5V
   VCC_5V                                                                                                                             VCC_5V
                                                     R123
      R99               Q13                          91 D15                  Q29                                                                GND
                        S9014                                                S9014
      91 D7
                                                                                              GND
                   Q14       R100                                       Q30       R124
                   S9014     1K                                         S9014     1K

             R101                              R125

      X07    22K                  GND                 X015 22K                        GND

   VCC_5V                              VCC_5V

      R102              Q15            R126                                  Q31
      91 D8             S9014
                                       91 D16

                   Q16       R103                                       Q32       R127

D                  S9014     1K                                         S9014     1K                                                                                      D

             R104                              R128
                                               22K
      X08    22K                  GND  X016                                  S9014 GND

                                                                                            TITLE:                                                            REV: 1.0

                                                                                                         02-       Company: Your Company                      Sheet: 1/1

   1                               2                                    3                  4                       Date: 2021-12-11 Drawn By: ncount0

                                                                                                                                                5
