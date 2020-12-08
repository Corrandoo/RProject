#include <TimerOne.h>
int randomVal = 0;
char inByte = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3, OUTPUT); //vibration pin
  pinMode(5, OUTPUT); //light pin
 

}

void vibrate(){
  if(Serial.available()>0){
    inByte = Serial.read();
    if(inByte == 1){
      randomVal = random(70, 150);
      analogWrite(3, randomVal);
      analogWrite(5, 255);
      
    }
    else if(inByte == 2){
      analogWrite(3, 0);
      analogWrite(5, 255);
    }
    else{
      analogWrite(3, 0);
      analogWrite(5, 0);
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  vibrate();

}
