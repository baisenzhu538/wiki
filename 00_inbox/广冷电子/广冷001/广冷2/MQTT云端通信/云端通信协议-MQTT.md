# 云端通信协议-MQTT

(02H)

(02H)
jumi/deviceconn

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"02",

"Ack":"00",

"data":{

          "DevType":"xx",      //

          "Ver":"xxx",         //

          "ContainNum":xx //

          "LayNum":"xx", //

          "MotoNum":"xx", //

          }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

          }

}

02H
jumi/00000000000000000000000000000000()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"02",

"Ack":"00",

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

          }

}

(08H)
(08H)

10min
08H
jumi/devicecomm0000000000000001(20H)

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"08",

"Ack":"00",

"data":{

   "List":[

             {

                           "contain":0,       //

                           "rackwidth":6, //

                           "rackheight":6, //

                           "current":[

                                        [1,1,1,1,1,1],

                                        [1,1,1,1,1,1],

                                        [1,1,1,1,1,1],

                                        [1,1,1,1,1,1],

                                        [1,1,1,1,1,1],

                                        [0,0,0,0,0,0]

                                           ]  //
                           "temp":25,         //
                           "IrErr":102000,

             }

             ,

             ... //

             ]

          "Rssi":"135",        //

          "NET":"LTE",         //

          "PowerStatus":xx, // 1  0 

          "BatteryLevel":xx, //

          "longitude":"xx", //

          "latitude":"xx"      //

   }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

          }

}

08H
08H
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"08",

"Ack":"00",

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

   }

}

(03H)

(03H)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"03",

"Ack":"00",

"data":{                       //
             "ContainNum":xx,

   }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

   }

}

(03H)
jumi/devicecomm0000000000000001(20H)

    {
    "ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"03",

"Ack":"00",

"data":{

          "List":[

                           {

                               "contain":0, //
                               "rackwidth":6, //
                               "rackheight":6, //

                              "current":[

                                           [1,1,1,1,1,1],

                                           [1,1,1,1,1,1],

                                           [1,1,1,1,1,1],

                                           [1,1,1,1,1,1],

                                           [1,1,1,1,1,1],

                                           [0,0,0,0,0,0]

                                              ]

                              "temp" :xx, //
                              "IrErr" :102000, //

                           }

             ]

          "Rssi":"135",           //

          "NET":"LTE",            //

          "PowerStatus":xx, // 1  0 

          "BatteryLevel":xx //

          "longitude":"xx", //

          "latitude":"xx"         //

          }

"Time":{                      //
             "year":xx,       //
             "month":xx,      //
             "day":xx,        //
             "hour":xx,       //
             "minute":xx,     //
             "second":xx,

          }

}

(01H)

(01H)

jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

    {
    "ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "SN":"xxxxxxxxxxxxxxxx",
    "Cmd":"01",
    "Ack":"01",
    "data":{

                 "List":[
                                  {
                           "ContainNum":x,   //
                                            //
                           "MotoNum":x,     //

                           "LayNum":x,       //
                                            //
                },                          //

                {

                           "ContainNum":x,

                           "MotoNum":x,

                           "LayNum":x,

                },

                ...

             ]

         }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

         }

}

(01H,ACK:00)
jumi/servercomm0000000000000001(20H)

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"01",                //
"Ack":"00",

"data":

   {                       //113000 
   "AckError":xxxxxx       //113301 
                           //113302 
                           //113303 
                           //113304 

   }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

         }

}

(01H,ACK:01)
jumi/servercomm0000000000000001(20H)
{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"01",                      //
"Ack":"01",

"data":{                         //
             "ContainNum":0,     //
             "MotoNum":1,        //
             "LayNum":1,         //
             "Status":"xx",      //
             "MotorErr":101000,  //
             "IrErr":102000,

   }

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

      }

}

(04H)

(04H)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"04",

"Ack":"00",

"data":{                         //
              "ContainNum":0,    //
              "En":"xx",         //
              "Mod":"xx",        //
              "Temp":xx,

   }

"Time":{                         //
             "year":xx,          //
             "month":xx,         //
             "day":xx,           //
             "hour":xx,          //
             "minute":xx,        //
             "second":xx,

      }

}



jumi/devicecomm0000000000000001(20H)

{

"ID":"xx xx xx xx xx xx xx xx",

"Cmd":"04",

"SN":"xx xx xx xx xx xx xx xx",

"Ack":"00",

"data":{

        "ContainNum":0, //

   }

"Time":{                        //
             "year":xx,         //
             "month":xx,        //
             "day":xx,          //
             "hour":xx,         //
             "minute":xx,       //
             "second":xx,

   }

}

(09H)

(09H)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"09",

"Ack":"00",

"data":{                        //
              "ContainNum":xx,  //
              "En":"xx",

   }

"Time":{                        //
             "year":xx,         //
             "month":xx,        //
             "day":xx,          //
             "hour":xx,         //
             "minute":xx,       //
             "second":xx,

   }

}

(09H,ACK00)

jumi/devicecomm0000000000000001(20H)
jumi/devicecomm0000000000000001(20H)

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"09",                     //
"Ack":"00"

"data":{                        //
              "ContainNum":xx,  //01 02
              "Status":"xx",

   }

"Time":{                        //
             "year":xx,         //
             "month":xx,        //
             "day":xx,          //
             "hour":xx,         //
             "minute":xx,       //
             "second":xx,

   }

}

(09H,ACK01)
jumi/devicecomm0000000000000001(20H)

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"09",                     //
"Ack":"01",

"data":{                        //
              "ContainNum":xx,  //
              "Status":"xx",

   }

"Time":{                        //
             "year":xx,         //
             "month":xx,        //
             "day":xx,          //
             "hour":xx,         //
             "minute":xx,       //
             "second":xx,

   }

}

(20H)

   
(20H)
jumi/deviceconn
jumi/deviceconn

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"20",

"Ack":"00",

"Time":{                   //
             "year":xx,    //
             "month":xx,   //
             "day":xx,     //
             "hour":xx,    //
             "minute":xx,  //
             "second":xx,

   }

}

(20H)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",

"Cmd":"20",

"Ack":"00",

"data":{

          "DeviceTopic" : "xx", // (jumi/devicecomm0000000000000001)
          "ServerTopic" : "xx", //(jumi/servercomm0000000000000001)

   }

"Time":{                       //
             "year":xx,        //
             "month":xx,       //
             "day":xx,         //
             "hour":xx,        //
             "minute":xx,      //
             "second":xx,

   }

}

(21H)

30s
jumi/deviceconn

    {
    "ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "SN":"xxxxxxxxxxxxxxxx",
"Cmd":"21",                    //
"Ack":"00",                    //
"Time":{                       //
                               //
             "year":xx,        //
             "month":xx,       //
             "day":xx,
             "hour":xx,
             "minute":xx,
             "second":xx,
             }
}

109H

(109H)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx",       //16

"Cmd":"109",

"Ack":"00",

"data":{                       //
             "ContainNum":xx,  // 255 (0XFF)
             "LayNum":xx,

   }

"Time":{                       //
             "year":xx,        //
             "month":xx,       //
             "day":xx,         //
             "hour":xx,        //
             "minute":xx,      //
             "second":xx,

   }

}

(109H)
jumi/devicecomm0000000000000001(20H)

{

"ID":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",

"SN":"xxxxxxxxxxxxxxxx", //16

"Cmd":"109",

"Ack":"00",

"data":{                       //01 02
             "Status":"xx",    //
             "ContainNum":xx,  // 255 (0XFF)
             "LayNum":xx,
             }                //
"Time":{                      //
                              //
             "year":xx,       //
             "month":xx,      //
             "day":xx,        //
             "hour":xx,
             "minute":xx,
             "second":xx,
             }
}

(0AH)

(0AH)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

   "ID":"xxxxxxxxxxxxxxxxx"

   "Cmd":"0A"

   "Ack":"00"

   "SN":"xxxxxxxxxxxxxxxxxx"

   "data":{                        //(jumi/deviceupgrade)
                "PubTopic":"xx",   //(jumi/upgrade)
                "SubTopic":"xx",   //
                "Host":"xxxxx",    //
                "URL":"xxxxx",     //
                "FwVer":"Vx.x.x",  //
                "FwSize":xx,       //MD5
                "FwMD5":"xxxxx"

   }

   "Time":{                        //
                "year":xx,         //
                "month":xx,        //
                "day":xx,          //
                "hour":xx,         //
                "minute":xx,       //
                "second":xx,

   }

}

(0AH,ACK00)

jumi/devicecomm0000000000000001(20H)

    {
          "ID":"xxxxxxxxxxxxxxxxx"
          "Cmd":"0A"
          "Ack":"00"
          "SN":"xxxxxxxxxxxxxxxxxx"
      "Time":{                   //
                   "year":xx,    //
                   "month":xx,   //
                   "day":xx,     //
                   "hour":xx,    //
                   "minute":xx,  //
                   "second":xx,
                   }

}

(0AH,ACK01)
jumi/devicecomm0000000000000001(20H)

{

   "ID":"xxxxxxxxxxxxxxxxx"

   "Cmd":"0A"

   "Ack":"01"

   "SN":"xxxxxxxxxxxxxxxxxx"

   "data":{

             "Ratio":xx,

                 //

             "Status":xx,

                 //0 
                 //1 
                 //2 

             "Err":xx ,

                 //120000 
                 //120101 
                 //120102 
                 //120103 
                 //120104 
                 //120105 
                 //120406 

             }

   "Time":{                      //
                "year":xx,       //
                "month":xx,      //
                "day":xx,        //
                "hour":xx,       //
                "minute":xx,     //
                "second":xx,

             }

}

(0BH & 1BH)

(0BH)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()


{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0B",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

   }

}

(0BH)
jumi/devicecomm0000000000000001(20H)

{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0B",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

   }

}

(1BH) !!

(1BH)

jumi/devicecomm0000000000000001(20H)

    {
          "ID":"xxxxxxxxxxxxxxxxx",
          "Cmd":"1B",
          "Ack":"00",
          "SN":"xxxxxxxxxxxxxxxxxx",
          "Time":{

                                           
   "year":xx,                  //
   "month":xx,                 //
   "day":xx,                   //
   "hour":xx,                  //
   "minute":xx,                //
   "second":xx,                //

   }

}

(1BH)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"1B",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

   }

}

(0CH)

(0CH)
jumi/146xxxxxxxxxxxxxxxxxxxxxxxxxxxxx()

{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0C",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "data":{                    //
         "DownTime":xx,

   }

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,
                   }
}

(0CH)
jumi/devicecomm0000000000000001(20H)

{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0C",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

             }

}

4G

7S44G02AIR720


{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0D",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "data":{

             "IPaddress":"xxxxxxxxx",  // IP  
                                       //
             "port":xxxx,              // "TCP"  "UDP"

             "mode":"xxx",

             }

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

             }

}




{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0D",

   "Ack":"00",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

   }

}



{

   "ID":"xxxxxxxxxxxxxxxxx",

   "Cmd":"0D",

   "Ack":"01",

   "SN":"xxxxxxxxxxxxxxxxxx",

   "data":{"Status":xx},       //00  01 

   "Time":{                    //
                "year":xx,     //
                "month":xx,    //
                "day":xx,      //
                "hour":xx,     //
                "minute":xx,   //
                "second":xx,

   }

}
