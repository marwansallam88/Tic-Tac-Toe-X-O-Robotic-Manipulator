// Import libraries
#include <Servo.h>

// Define pins
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
int i;
int magnet = 3;
int theta1 = 95;
int theta2 = 180;
int theta3 = 90;
int theta4 = 0;

void setup() {
  Serial.begin(9600);
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);
  servo4.attach(6);

  pinMode(magnet, OUTPUT);
  digitalWrite(magnet, LOW);

  servo1.write(95);
  delay(1000);
  servo2.write(180);
  delay(1000);
  servo3.write(95);
  delay(1000);
  servo4.write(0);
  delay(1000);
}

void loop() {
  // Communication part
  while (!Serial.available());
  char pos = Serial.read();
  Serial.flush();

  // Arm Logic
  switch (pos) {
      digitalWrite(magnet, LOW);
      delay(500);
    case 'A':
      for (i = 0; i < 125; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(95);
      delay(100);
      for (i = 180; i > 120; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      servo3.write(95);
      delay(100);
      theta1 = 95;
      theta2 = 120;
      theta3 = 95;
      theta4 = 125;
      break;

    case 'B':
      for (i = 0; i < 135; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(95);
      delay(100);
      for (i = 180; i > 45; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      servo3.write(100);
      delay(100);
      theta1 = 95;
      theta2 = 45;
      theta3 = 100;
      theta4 = 135;
      break;

    case 'C':
      servo1.write(100);
      delay(100);
      for (i = 0; i < 120; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      for (i = 180; i > 0; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      for (i = 95; i > 85; i = i - 5) {
        servo3.write(i);
        delay(100);
      }
      theta1 = 95;
      theta2 = 0;
      theta3 = 85;
      theta4 = 120;
      break;

    case 'D':
      for (i = 0; i < 85; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(95);
      delay(100);
      for (i = 180; i > 105; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      servo3.write(95);
      delay(100);
      theta1 = 95;
      theta2 = 105;
      theta3 = 95;
      theta4 = 85;
      break;

    case 'E':
      for (i = 0; i < 100; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(100);
      delay(100);
      for (i = 180; i > 65; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      for (i = 95; i > 85; i = i - 5) {
        servo3.write(i);
        delay(100);
      }
      theta1 = 100;
      theta2 = 65;
      theta3 = 85;
      theta4 = 100;
      break;

    case 'F':
      for (i = 0; i < 80; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(100);
      delay(100);
      for (i = 180; i > 45; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      for (i = 95; i > 85; i = i - 5) {
        servo3.write(i);
        delay(100);
      }
      theta1 = 100;
      theta2 = 45;
      theta3 = 85;
      theta4 = 80;
      break;

    case 'G':
      servo1.write(95);
      delay(100);
      for (i = 180; i > 135; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      servo4.write(0);
      delay(100);
      servo3.write(95);
      delay(100);
      theta1 = 95;
      theta2 = 135;
      theta3 = 95;
      theta4 = 0;
      break;

    case 'H':
      for (i = 0; i < 90; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(100);
      delay(100);
      for (i = 180; i > 105; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      for (i = 95; i > 80; i = i - 5) {
        servo3.write(i);
        delay(100);
      }
      for (i = 90; i > 0; i = i - 5) {
        servo4.write(i);
        delay(100);
      }
      theta1 = 100;
      theta2 = 105;
      theta3 = 80;
      theta4 = 0;
      break;

    case 'I':
      for (i = 0; i < 90; i = i + 5) {
        servo4.write(i);
        delay(100);
      }
      servo1.write(100);
      delay(100);
      for (i = 180; i > 90; i = i - 5) {
        servo2.write(i);
        delay(100);
      }
      for (i = 90; i > 0; i = i - 5) {
        servo4.write(i);
        delay(100);
      }
      for (i = 95; i > 85; i = i - 5) {
        servo3.write(i);
        delay(100);
      }
      servo2.write(92);
      delay(100);
      theta1 = 100;
      theta2 = 92;
      theta3 = 85;
      theta4 = 0;
      break;
  }
  digitalWrite(magnet, HIGH);
  delay(2000);
  for (i = theta2; i < 180; i = i + 5) {
    servo2.write(i);
    delay(100);
  }
  for (i = theta4; i > 0; i = i - 5) {
    servo4.write(i);
    delay(100);
  }
  for (i = theta1; i > 95; i = i - 5) {
    servo1.write(i);
    delay(100);
  }
  for (i = theta1; i < 95; i = i + 5) {
    servo1.write(i);
    delay(100);
  }
  for (i = theta3; i > 95; i = i - 5) {
    servo3.write(i);
    delay(100);
  }
  for (i = theta3; i < 95; i = i + 5) {
    servo3.write(i);
    delay(100);
  }
  digitalWrite(magnet, LOW);
  delay(5000);
  Serial.print('H');
}
