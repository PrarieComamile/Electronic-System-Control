#define pot A0

#define BUTTON1 2
#define BUTTON2 3
#define BUTTON3 4

void setup() {
  Serial.begin(9600);

}

void loop() {

  Serial.print(digitalRead(BUTTON1));
  Serial.print("+");
  Serial.print(digitalRead(BUTTON2));
  Serial.print("+");
  Serial.print(digitalRead(BUTTON3));
  Serial.print("+");
  Serial.println(analogRead(pot));

}
