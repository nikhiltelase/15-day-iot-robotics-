

## 🔦 **Day 7 – IR + Relay + WiFi Control in AP Mode**

### 🧰 **Components Needed**:

* NodeMCU (ESP8266)
* IR Receiver (e.g., TSOP1838)
* TV Remote
* 1-Channel Relay Module
* Electrical Appliance (Bulb via plug/socket board – take proper safety)
* Jumper wires
* Breadboard
* 5V Power supply (Relay ke liye)

---

### ✅ **Step 1: Relay Module Connection**

**Wiring (NodeMCU to Relay):**

* **IN** → **D6**
* **VCC** → **3.3V ya 5V** (Check your relay, some need 5V)
* **GND** → **GND**

**Relay to AC Appliance:** (⚠️ *High Voltage: Take help from adult or use plug board safely*)

* Live wire cut → One end to **Common (COM)**
* Other end to **Normally Open (NO)**
* Neutral directly connected

---

### ✅ **Step 2: IR + Relay Code (Relay ON/OFF with Remote)**

```cpp
#include <IRremoteESP8266.h>
#include <IRrecv.h>
#include <IRutils.h>

const uint16_t RECV_PIN = D5;
IRrecv irrecv(RECV_PIN);
decode_results results;

#define RELAY_PIN D6
#define BUTTON_RELAY 0xFFA25D  // Replace with your remote button HEX

bool relayState = false;

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn();
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, relayState);
}

void loop() {
  if (irrecv.decode(&results)) {
    if (results.value == BUTTON_RELAY) {
      relayState = !relayState;
      digitalWrite(RELAY_PIN, relayState);
      Serial.println(relayState ? "Relay ON" : "Relay OFF");
    }
    irrecv.resume();
  }
}
```

---

### ✅ **Step 3: WiFi Control via Access Point + Webpage**

📶 NodeMCU khud ek WiFi hotspot banayega aur webpage se relay ko control kar sakoge.

```cpp
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "RelayControl";
const char* password = "12345678";

ESP8266WebServer server(80);

#define RELAY_PIN D6

bool relayState = false;

void handleRoot() {
  String html = "<h2>Relay Control</h2>";
  html += "<p>Relay is: " + String(relayState ? "ON" : "OFF") + "</p>";
  html += "<a href=\"/on\">ON</a> | <a href=\"/off\">OFF</a>";
  server.send(200, "text/html", html);
}

void handleOn() {
  relayState = true;
  digitalWrite(RELAY_PIN, HIGH);
  handleRoot();
}

void handleOff() {
  relayState = false;
  digitalWrite(RELAY_PIN, LOW);
  handleRoot();
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  WiFi.softAP(ssid, password);
  Serial.println("Access Point Started");

  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.begin();
  Serial.println("Web server started");
}

void loop() {
  server.handleClient();
}
```

---

### ✅ **Step 4: Combine IR + WiFi Control**

Dono features ek code me combine karo (Remote aur Mobile dono se control):

* IR se toggle
* Webpage se ON/OFF

```cpp
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <IRremoteESP8266.h>
#include <IRrecv.h>
#include <IRutils.h>

// WiFi AP Config
const char* ssid = "RelayControl";
const char* password = "12345678";
ESP8266WebServer server(80);

// IR Config
const uint16_t RECV_PIN = D5;
IRrecv irrecv(RECV_PIN);
decode_results results;
#define BUTTON_RELAY 0xFFA25D  // Update with your button code

// Relay
#define RELAY_PIN D6
bool relayState = false;

void toggleRelay() {
  relayState = !relayState;
  digitalWrite(RELAY_PIN, relayState);
}

// Web Handlers
void handleRoot() {
  String html = "<h2>Relay Control</h2>";
  html += "<p>Relay is: " + String(relayState ? "ON" : "OFF") + "</p>";
  html += "<a href=\"/on\">ON</a> | <a href=\"/off\">OFF</a>";
  server.send(200, "text/html", html);
}

void handleOn() {
  relayState = true;
  digitalWrite(RELAY_PIN, HIGH);
  handleRoot();
}

void handleOff() {
  relayState = false;
  digitalWrite(RELAY_PIN, LOW);
  handleRoot();
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, relayState);

  irrecv.enableIRIn();

  WiFi.softAP(ssid, password);
  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.begin();

  Serial.println("Access Point started. Connect to: RelayControl");
}

void loop() {
  server.handleClient();

  if (irrecv.decode(&results)) {
    if (results.value == BUTTON_RELAY) {
      toggleRelay();
      Serial.println(relayState ? "Relay ON" : "Relay OFF");
    }
    irrecv.resume();
  }
}
```

---

## 🎯 Final Outcome:

* 📱 **Mobile Se Control**: Connect to hotspot → Open `192.168.4.1` → ON/OFF buttons
* 🕹️ **Remote Se Control**: Press assigned button → Relay toggles ON/OFF

---

### 💡 Bonus Idea:

Agle din ke liye:

* Voice Assistant (Python + Speech Recognition + ESP8266) se "Turn on light" bole to relay ON ho!

Agar chaho to main uska bhi code aur UI bana ke de sakta hoon.

---

Aaj ka kaam complete ho jaane ke baad batana, next level automation ke liye ready ho jaayein 💪
