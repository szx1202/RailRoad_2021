// ver 2.0 --> servopos shortened from 4 to 3 Byte i.e. fw12 to f12)
// ver 2.1 --> added 3rd servo series
//ver 2.2 --| added single turnout servos
//ver 3.0 --> created Turn_FW and Turn_BW funtion for servo rotation control
// CAUTION > Servo in slot 1 is mounted in reverse direction

#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif
BluetoothSerial SerialBT;

#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
//SDA (default is GPIO 21) SCL (default is GPIO 22)
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
const int numItems=8; //number of servo's to manage

#define SERVOMIN  150 //set 150 300  this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  180 //set 175 600  this is the 'maximum' pulse length count (out of 4096)

int pinLed=17; //Led to check BT Connection
char servopos[3]; //4 is the string leght for Bluethooth command (F12, R12,...)

void setup()
{
  //Setup usb serial connection to computer
  Serial.begin(115200);
  
  Serial.println("Led on"); 
  pinMode(pinLed, OUTPUT);
  digitalWrite(pinLed, LOW); 
  
 SerialBT.begin("ESP32Track"); //Bluetooth device name
 Serial.println("The device started, now you can pair it with bluetooth!");

  pwm.begin();
  delay(10);
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
 
  
  for(int i=0; i<numItems; i++)
    {
     Turn_FW(i);     
     delay(100);
  }
}

void loop()
{
  //Read from bluetooth and write to usb serial 
  while (SerialBT.available())
  {
    Serial.println ("BT OK");
    digitalWrite(pinLed, LOW); 
    for (int i=0;i<3;i++){
      servopos[i] = SerialBT.read();
      Serial.print(servopos[i]);
     }
     
  SerialBT.flush();
    
    if ((servopos[0] == 'f') && (servopos[1]=='2')) {                     //if (realservo >= 1000 && realservo <1180) in case of sliders
        Serial.println("fw23");
        Turn_FW(2);
        Turn_FW(2);
        digitalWrite(pinLed, LOW); 
        
      }
    if ((servopos[0] == 'r') && (servopos[1]=='2')){
       Serial.println("rw23");
       Turn_BW(2);
       Turn_BW(2);
       digitalWrite(pinLed, HIGH); 
      }
      
    if ((servopos[0] == 'f') && (servopos[1]=='4')) {                     //if (realservo >= 1000 && realservo <1180) in case of sliders
        Serial.println("fw45");
        Turn_FW(4);
        Turn_FW(5);
        digitalWrite(pinLed, LOW); 
        }
        
    if ((servopos[0] == 'r') && (servopos[1]=='4')){
       Serial.println("bw45");
       Turn_BW(4);
       Turn_BW(5);
       digitalWrite(pinLed, HIGH); 
      }
      
     if ((servopos[0] == 'f') && (servopos[1]=='7')) {                     //if (realservo >= 1000 && realservo <1180) in case of sliders
        Serial.println("f77");
        Turn_FW(7);
        digitalWrite(pinLed, LOW);
      }

     if ((servopos[0] == 'r') && (servopos[1]=='7')) {                     //if (realservo >= 1000 && realservo <1180) in case of sliders
        Serial.println("f77");
        Turn_BW(7);
        digitalWrite(pinLed, LOW);
      }
      
    if (servopos[0] == 't') {
      Serial.println("TestBT");
      SerialBT.write('k');
    }
    
    if (servopos[0] == 'i') {
      Serial.println("reset");
       for(int i=0; i<numItems; i++)
      {
        Serial.println(i);
        Turn_FW(i);
       }
       digitalWrite(pinLed, LOW);
    }
  }
//delay(100);
}

void Turn_BW(uint16_t servonum) {
  //Serial.println(servonum);
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
    pwm.setPWM(servonum, 0, pulselen);
    delay (5);
  }
}

void Turn_FW(uint16_t servonum) {
 //Serial.println(servonum);
 for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--) {
    pwm.setPWM(servonum, 0, pulselen);
    delay (5);
  }
}
