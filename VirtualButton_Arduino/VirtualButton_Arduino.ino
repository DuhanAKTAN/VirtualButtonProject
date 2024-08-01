void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');
    
    if (data == "green")
    {
      digitalWrite(2,1);
      
    }else if (data == "blue")
    {
      digitalWrite(3,1);
    }
    else if (data == "red")
    {
      digitalWrite(4,1);
    }
    else
    {
      digitalWrite(2,0);
      digitalWrite(3,0);
      digitalWrite(4,0);
    }          
  }
}
