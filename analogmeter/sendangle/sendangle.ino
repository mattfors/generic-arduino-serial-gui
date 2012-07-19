
void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);
  //Serial.println("Arduino Initialized");
  delay(200);

}
int output;
int degree;
int val;


void loop()
{
  degree =0;
  if (Serial.available() > 0)
  {
    while(1)
    {  
      
      val = analogRead(A0);
      degree = val*(180/1023.0);
      Serial.println(degree);
      delay(10);
    }
  }

}


