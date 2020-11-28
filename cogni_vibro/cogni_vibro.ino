#include <TimerOne.h>
int val = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode(11, OUTPUT);
  /*while(!Serial){
    Timer1.initialize(500000);
    Timer1.attachInterrupt(vibrate);
  }*/

}

void vibrate(){
  if(Serial.available()>0){
    if(Serial.read()== 1){
      analogWrite(A0, 255);
      
    }
    else{
      analogWrite(A0, 0);
      //analogWrite(A1, 0);
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  vibrate();

}
