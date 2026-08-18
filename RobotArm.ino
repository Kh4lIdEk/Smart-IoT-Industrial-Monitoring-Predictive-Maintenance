#include <HardwareSerial.h>
#include <ESP32Servo.h>
#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define SELECT_HEX        0x0001
#define L3_HEX            0x0002
#define R3_HEX            0x0004
#define START_HEX         0x0008

#define TRIANGLE_HEX      0x1000
#define CIRCLE_HEX        0x2000
#define CROSS_HEX         0x3000
#define SQUARE_HEX        0x4000

#define L2_HEX            0x5000
#define R2_HEX            0x6000
#define L1_HEX            0x7000
#define R1_HEX            0x8000

#define LEFT_STICK_UP      0X0100
#define LEFT_STICK_DOWN    0X0200
#define LEFT_STICK_RIGHT   0X0300
#define LEFT_STICK_LEFT    0X0400

#define RIGHT_STICK_UP     0X0500
#define RIGHT_STICK_DOWN   0X0600
#define RIGHT_STICK_RIGHT  0X0700     
#define RIGHT_STICK_LEFT   0X0800


#define Pin_Motor_A                     14
#define Pin_Motor_B                     2
#define Pin_Motor_C                     23
#define Pin_Motor_D                     21
#define Pin_Motor_E                     5
#define Pin_Motor_F                     4

#define Pin_LED                         13
#define Pin_BUZZER                      12

unsigned long is_pressed   =            0x00000;

Servo myservo[6];  // create servo object to control a servo
// 16 servo objects can be created on the ESP32
Servo buzzer;

String interpretedSymbol;


#define Servo_Init_POS                  90
#define Min_Angle                       0
#define Max_Angle                       180 
#define Step                            2

int POS_A = Servo_Init_POS;
int POS_B = Servo_Init_POS;
int POS_C = Servo_Init_POS;
int POS_D = Servo_Init_POS;
int POS_E = Servo_Init_POS;
int POS_F = Servo_Init_POS;

HardwareSerial mySerial(2); // Use UART2 (RX2/TX2)

void InitServos(void){
	myservo[0].attach( Pin_Motor_A, 500 ,2500 );
  myservo[1].attach( Pin_Motor_B, 500 ,2500 );
  myservo[2].attach( Pin_Motor_C , 500 , 2500 ); 
  myservo[3].attach( Pin_Motor_D , 500 , 2500 );
  myservo[4].attach( Pin_Motor_E , 500, 2500 );
  myservo[5].attach( Pin_Motor_F , 500 , 2500 );
	
  myservo[0].write(90);
	myservo[1].write(90);
	myservo[2].write(90);
	myservo[3].write(90);
	myservo[4].write(90); 
	myservo[5].write(90);
}

void ResetServos(void){
	myservo[0].write(90);
	myservo[1].write(90);
	myservo[2].write(90);
	myservo[3].write(90);
	myservo[4].write(90); 
	myservo[5].write(90);
}

void command(char receivedSymbol){
	// Compare received character with 6 cases using if-else
    if (receivedSymbol == 'A') {
      Serial.println("Received character is: A");
      if ((POS_A + Step) <= Max_Angle){
        POS_A += Step;
      }
			myservo[0].write(POS_A);
    }
    else if (receivedSymbol == 'a') {
      Serial.println("Received character is: a");
      if ((POS_A - Step) >= Min_Angle){
        POS_A -= Step;
      }
			myservo[0].write(POS_A);
    }

    //////////////////////////////////////////////


    else if (receivedSymbol == 'B') {
      Serial.println("Received character is: B ");
      if ((POS_B + Step) <= Max_Angle){
        POS_B += Step;
      }
			myservo[1].write(POS_B);
    }
    else if (receivedSymbol == 'b') {
      Serial.println("Received character is: b");
      if ((POS_B - Step) >= Min_Angle){
        POS_B -= Step;
      }
			myservo[1].write(POS_B);
    }

    //////////////////////////////////////////////


    else if (receivedSymbol == 'C') {
      Serial.println("Received character is: C ");
      if ((POS_C + Step) <= Max_Angle){
        POS_C += Step;
      }
			myservo[2].write(POS_C);
    }
    else if (receivedSymbol == 'c') {
      Serial.println("Received character is: c");
      if ((POS_C - Step) >= Min_Angle){
        POS_C -= Step;
      }
			myservo[2].write(POS_C);
    }

    //////////////////////////////////////////////


    else  if (receivedSymbol == 'D') {
      Serial.println("Received character is: D ");
      if ((POS_D + Step) <= Max_Angle){
        POS_D += Step;
      }
			myservo[3].write(POS_D);
    }
    else if (receivedSymbol == 'd') {
      Serial.println("Received character is: d");
      if ((POS_D - Step) >= Min_Angle){
        POS_D -= Step;
      }
			myservo[3].write(POS_D);
    }

    //////////////////////////////////////////////


    else if (receivedSymbol == 'E') {
      Serial.println("Received character is: E ");
      if ((POS_E + Step) <= Max_Angle){
        POS_E += Step;
      }
			myservo[4].write(POS_E);
    }
    else if (receivedSymbol == 'e') {
      Serial.println("Received character is: e");
      if ((POS_E - Step) >= Min_Angle){
        POS_E -= Step;
      }
			myservo[4].write(POS_E);
    }

    //////////////////////////////////////////////


    else if (receivedSymbol == 'F') {
      Serial.println("Received character is: F ");
      if ((POS_F + Step) <= Max_Angle){
        POS_F += Step;
      }
			myservo[5].write(POS_F);
    }
    else if (receivedSymbol == 'f') {
      Serial.println("Received character is: f");
      if ((POS_F - Step) >= Min_Angle){
        POS_F -= Step;
      }
			myservo[5].write(POS_F);
    }

    ///////////////////////////////////////////////
    
		else if (receivedSymbol == '1') {
      Serial.println("Received character is: Led");
			digitalWrite(Pin_LED, HIGH);
    }

    ///////////////////////////////////////////////

		else if (receivedSymbol == '2') {
      Serial.println("Received character is: Buzzer");
			buzzer.write(100);
    }
    
}


void setup() {

	Serial.begin(115200);
	InitServos();

	pinMode(Pin_LED, OUTPUT);
	buzzer.attach(Pin_BUZZER, 1000, 2000);

  ResetServos();

	Serial.println("Servos initiated to position 0");
	Serial.println("Ready to receive a character...");

  mySerial.begin(112500, SERIAL_8N1, 16, 17); // RX2 on GPIO 16, TX2 on GPIO 17
  Serial.println("Serial 2 is Ready");

}

void loop() {
  
  char incomingByte;
  
  if (mySerial.available()) {
    // Read the data from Serial2
    char incomingByte = mySerial.read();
    
    // Print the received byte to Serial0 (Serial Monitor)
    Serial.write((char)incomingByte);

    command(incomingByte);
    
    // Optionally, send the same byte back to Serial2
    //mySerial.write((byte)incomingByte);
  }

  
  // Check if data is available on Serial0
  if (Serial.available() > 0) {
    // Read the data from Serial0
    char incomingByte = (char) Serial.read();
    
    // Print the received byte to Serial Monitor
    Serial.println(incomingByte);
    
    // Call the command function with the received character
    command(incomingByte);
  }
}

