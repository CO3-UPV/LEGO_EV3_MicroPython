void setup() {
  Serial.begin(115200);
  Serial3.begin(115200);
}

void loop() {
  while(Serial.available()) Serial3.write(Serial.read());
  while(Serial3.available()) Serial.write(Serial3.read());
}
