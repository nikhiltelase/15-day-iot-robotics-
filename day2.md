**<div align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx7L3QXZeJ5gtlP5Qi728ZyvGvRBfYz-_mrA&s" alt="Connect Shiksha Logo" width="200"/>
  
  # Connect Shiksha IoT Academy
  ## 🔧 15-Day IoT & Robotics Program
  
  <p align="center" style="font-size: 1.2em; color: #666;">
    Transforming Engineering Students into IoT Professionals
  </p>
</div>

# Programming a NodeMCU ESP8266 using the Arduino IDE :

---

### ✅ Step 1: **Install Arduino IDE**

If you haven’t already, download and install the [Arduino IDE](https://www.arduino.cc/en/software).

---

### ✅ Step 2: **Add ESP8266 Board to Arduino IDE**

1. Open Arduino IDE.
2. Go to **File > Preferences**.
3. In the **"Additional Board Manager URLs"** field, paste this URL:

   ```
   http://arduino.esp8266.com/stable/package_esp8266com_index.json
   ```
4. Click **OK**.

---

### ✅ Step 3: **Install the ESP8266 Board**

1. Go to **Tools > Board > Boards Manager**.
2. Search for **"esp8266"**.
3. Click **Install** on the package named *esp8266 by ESP8266 Community*.

---

### ✅ Step 4: **Select the NodeMCU Board**

1. Go to **Tools > Board**.
2. Select **NodeMCU 1.0 (ESP-12E Module)**.

---

### ✅ Step 5: **Connect the NodeMCU**

* Use a **micro USB cable** to connect the NodeMCU to your PC.
* Go to **Tools > Port**, and select the COM port corresponding to your NodeMCU.

> If no port shows, make sure you have the **CH340 or CP210x USB driver** installed (depending on your board).

---

### ✅ Step 6: **Write or Load a Sketch**

Example: Blink the onboard LED (usually on GPIO 2 / D4):

```cpp
void setup() {
  pinMode(2, OUTPUT); // D4
}

void loop() {
  digitalWrite(2, HIGH);
  delay(500);
  digitalWrite(2, LOW);
  delay(500);
}
```

---

### ✅ Step 7: **Upload the Code**

1. Click the **Upload** button (right arrow icon).
2. Wait for it to compile and upload.
3. You’ll see “Done uploading” when successful.

---

### ✅ Optional: **Open Serial Monitor**

* Go to **Tools > Serial Monitor**.
* Set the baud rate to **115200** (common default for NodeMCU).

---

Would you like help writing code for a specific project using the NodeMCU (e.g., controlling LEDs, reading sensors, or IoT tasks)?
