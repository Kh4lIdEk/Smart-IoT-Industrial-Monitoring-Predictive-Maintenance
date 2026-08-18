//Controlling servo motors using digital pins :

//Includes :
#include <ESP32Servo.h>

//Declarations : 
Servo myservo[6]; 

//Initializations : 
volatile int servoPulses[NUM_SERVOS] = {1500, 1500, 1500, 1500, 1500, 1500};  // (us)
volatile int servoIndex = 0;

uint16 ServoPwmDuty[8] = {1500,1500,1500,1500,1500,1500,1500,1500};     //Actual positions
uint16 ServoPwmDutySet[8] = {1500,1500,1500,1500,1500,1500,1500,1500};  //Target positions 

//This is like a flag that turn True when we have a move (in other words ServoPwmDuty and ServoPwmDutySet are different) -> That flag is used in comparison as a first cdt
bool ServoPwmDutyHaveChange = FALSE;

//This gives the Step : 
ServoPwmDutyInc[i]


void setup() {
  InitPWM();

  //should replace it with the function that set the servos smoothly 
  for (int i = 0; i < 6; i++) {
    myservo[i].write(90); // center position
  }
}

void loop() {

}


//Functions : 

void InitPWM(void)
{
  myservo[0].attach(4,500,2500);
  myservo[1].attach(5,500,2500);
  myservo[2].attach(18,500,2500);
  myservo[3].attach(19,500,2500);
  myservo[4].attach(13,500,2500);
  myservo[5].attach(12,500,2500);
}

void InitTimer(void)		//100us@12.000MHz    <- Something is wrong : make your own 
{

}

//Servo Time handles speed of our servo movements, it results of the step (ServoPwmDutyInc) and How much time we'll that step to get the target value : 
//ServoPwmDutyIncTimes = ServoTime/20; 
uint16 ServoTime = 0;

//this function set the ServoDutySet values to give a reference to ServoPwmDutyCompare function 
void ServoSetPluseAndTime(uint8 id,uint16 p,uint16 time) 
{
  if(id >= 0 && id <= 7 && p >= 500 && p <= 2500)
  {
    if(time < 20)
      time = 20;
    if(time > 30000)
      time = 30000;
    ServoPwmDutySet[id] = p;
    ServoTime = time;
    ServoPwmDutyHaveChange = TRUE;      //A flag to know we have a move 
  } 
}

//Comparing the ServoPwmDutyset with ServoPwmDuty to make the suitables moves :
void ServoPwmDutyCompare(void)
{
  static uint16 ServoPwmDutyIncTimes;
  static bool ServoRunning = FALSE;

  if(ServoPwmDutyHaveChange)
  {
    ServoPwmDutyHaveChange = FALSE;
    ServoPwmDutyIncTimes = ServoTime/20; 

    for(i=0; i<8; i++){
      ServoPwmDutyInc[i] = ServoPwmDutySet[i] - ServoPwmDuty[i] ;
    }
    ServoPwmDutyInc[i] /= ServoPwmDutyIncTimes;
  }

}
