#include <TimerOne.h>
int randomVal = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3, OUTPUT);
 

}

void vibrate(){
  if(Serial.available()>0){
    if(Serial.read()== 1){
      randomVal = random(70, 256);
      analogWrite(3, randomVal);
      
    }
    else{
      analogWrite(3, 0);
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  vibrate();

}
