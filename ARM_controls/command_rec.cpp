#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    pinMode(2, OUTPUT);  // X_P not exact to finish later
    pinMode(4, OUTPUT);  // X_N
    // to add other pins for other commands
  }
  
  String readCommand() {
    static String cmd = "";
    while (Serial.available()) {
      char c = Serial.read();
      if (c == '\n') {
        String msg = cmd;
        cmd = "";
        return msg;
      }
      else if (c >= 32 && c <= 126) {
        cmd += c;
      }
    }
    return String();
  }
  
  void loop() {
    String cmd = readCommand();
    if (cmd.length() > 0) {
      Serial.print("Received: ");
      Serial.println(cmd);
  
      if (cmd == "X_P") {
        digitalWrite(2, HIGH); //only an example
        delay(100);
        digitalWrite(2, LOW);
      }
      else if (cmd == "X_N") {
        digitalWrite(4, HIGH);
        delay(100);
        digitalWrite(4, LOW);
      }
      // to continue
      else {
        Serial.println("Unknown command");
      }
    }
  }
  