#define pot A0

#define BUTTON1 2
#define BUTTON2 3
#define BUTTON3 4

void setup() {
  Serial.begin(9600);

}

void loop() {

  // if(digitalRead(BUTTON1)==1){
  //   Serial.print("button1");
  // }

  // if(digitalRead(BUTTON2)==1){
  //   Serial.print("button2");
  // }

  // if(digitalRead(BUTTON3)==1){
  //   Serial.print("button3");
  // }


  Serial.print(digitalRead(BUTTON1));
  Serial.print("+");
  Serial.print(digitalRead(BUTTON2));
  Serial.print("+");
  Serial.print(digitalRead(BUTTON3));
  Serial.print("+");
  Serial.println(analogRead(pot));

}
