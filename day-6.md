## 🔦 **Day 6 – IR Receiver + TV Remote + Multiple LEDs Control**

### 🧰 Components Needed:

* NodeMCU (ESP8266)
* IR Receiver (e.g., TSOP1838)
* TV Remote (any IR remote)
* Jumper wires
* Breadboard
* External LEDs (1 to 3) + 220Ω resistors

---

### ✅ **Step 1: Connect IR Receiver Sensor**

**Connections:**

* IR VCC → 3.3V
* IR GND → GND
* IR OUT → D5 (GPIO 14)

---

### ✅ **Step 2: Print Remote Values in Serial Monitor**

```cpp
#include <IRremoteESP8266.h>
#include <IRrecv.h>
#include <IRutils.h>

const uint16_t RECV_PIN = D5;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn();  // Start IR receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);  // Print HEX code
    irrecv.resume();  // Ready for next signal
  }
}
```

🟢 **Upload and press any remote button** → Check HEX codes in Serial Monitor.

---

### ✅ **Step 3: Control Built-in LED (D4)**

🟢 Note down one HEX code from remote (for toggle)

```cpp
#include <IRremoteESP8266.h>
#include <IRrecv.h>
#include <IRutils.h>

const uint16_t RECV_PIN = D5;
IRrecv irrecv(RECV_PIN);
decode_results results;

#define BUTTON_CODE 0xFFA25D  // Replace with your button code

const int ledPin = D4;
bool ledState = false;

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn();
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
}

void loop() {
  if (irrecv.decode(&results)) {
    if (results.value == BUTTON_CODE) {
      ledState = !ledState;
      digitalWrite(ledPin, ledState);
    }
    irrecv.resume();
  }
}
```

---

### ✅ **Step 4: Add 1 External LED**

**Connection:**

* LED Anode (+) → D6
* LED Cathode (–) → GND (via 220Ω resistor)

Use same logic and new HEX codes for that LED.

---

### ✅ **Step 5: Add Multiple LEDs (e.g., 3)**

```cpp
#include <IRremoteESP8266.h>
#include <IRrecv.h>
#include <IRutils.h>

const uint16_t RECV_PIN = D5;
IRrecv irrecv(RECV_PIN);
decode_results results;

#define LED1 D6
#define LED2 D7
#define LED3 D8

// Single button code for each LED
#define BUTTON1 0xFFA25D  // Button for LED1
#define BUTTON2 0xFF629D  // Button for LED2
#define BUTTON3 0xFFE21D  // Button for LED3

bool ledStates[] = {false, false, false};
const int leds[] = {LED1, LED2, LED3};

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn();

  for(int i = 0; i < 3; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], ledStates[i]);
  }
}

void loop() {
  if (irrecv.decode(&results)) {
    long code = results.value;
    
    if(code == BUTTON1) toggleLED(0);
    else if(code == BUTTON2) toggleLED(1);
    else if(code == BUTTON3) toggleLED(2);
    
    irrecv.resume();
  }
}

void toggleLED(int index) {
  ledStates[index] = !ledStates[index];
  digitalWrite(leds[index], ledStates[index]);
}
```

✅ Each button independently toggles its LED ON/OFF:
- Button 1: Press to toggle LED 1
- Button 2: Press to toggle LED 2
- Button 3: Press to toggle LED 3

---

### 🧠 Concepts:

* IR Receiver: Decode TV remote signals.
* Serial Monitor: Helps find HEX code of each button.
* LED Toggle: `digitalRead()` + `!` is used to switch ON/OFF.

---


