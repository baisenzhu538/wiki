# HX_SMJ-03_红外光栅板设计分析

1
      2
            (1)  A B 

      
            (2) MCU 

      
            (3) 
             MCU  IO  SN74LV595APWR 
                  SN74LV595APWR 
                    940nm 
            (4) 
              LMV358IPWR 
                  CD4051BPWR  8  1  MCU IO 
                    940nm 
            (5) 
                    50mA 5%
            

24V 
1
2
      1 SS24 
      2 P6SMB30CA 

3
      1P6SMB30CA
            1)
                  1) 
                  2) Vrwm25.6V
                  3) 28.5V
                  4) Ipp@10/1000us14.5A
                  5) 41.4V
            2) 45VTPS54340DDAR
             24V
            
            3)P6SMB30CA (TVS)
            
      2SS24
            
                  140V
                  22A
                  3550mV 2A

24V  5V  DCDC 
1

3 24V  JW5026  5V1A
4

      (1) 
              VOUT=0.8V*(R2/R3+1) R132  10.2K R133  53.6K

      (2)
