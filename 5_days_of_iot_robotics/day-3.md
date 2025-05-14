

# 📘 **Day-3 – Introduction to Sensors & Ultrasonic Sensor with LED Project**

---

## ✨ **What You Will Learn Today**

1. What is a sensor?
2. Types of sensors in IoT & Robotics
3. What are GPIO pins?
4. How to blink external LED using GPIO
5. How to connect an Ultrasonic sensor
6. How to control LED using distance

---

## 🔍 **1. What is a Sensor?**

> A **sensor** is a device that **detects or measures** something in the environment and sends data to the microcontroller.

### 🧠 **Example Sensors:**

| Sensor Name       | What it Detects        |
| ----------------- | ---------------------- |
| Ultrasonic Sensor | Distance               |
| DHT11             | Temperature & Humidity |
| LDR               | Light                  |
| Gas Sensor (MQ-2) | Smoke or Gas level     |

---

## 🧩 **2. What are GPIO Pins?**

> GPIO = General Purpose Input/Output
> Ye pins hoti hain jo **input (sensor)** ya **output (LED, motor)** ke liye use hoti hain.

### 📌 **ESP8266 NodeMCU Common GPIO Pins**

| NodeMCU Pin | GPIO Number | Common Use  |
| ----------- | ----------- | ----------- |
| D0          | GPIO16      | Output only |
| D1          | GPIO5       | I/O         |
| D2          | GPIO4       | I/O         |
| D5          | GPIO14      | I/O         |
| D6          | GPIO12      | I/O         |

⚠️ **Important**: Kuch pins sirf output ke liye ache hote hain, jaise D0. But D1, D2, D5, D6 normally safe hote hain.

---

## 💡 **3. Step-by-Step Practical**

---

### ✅ **Step 1: Blink an External LED**

### 📌 Connections:

| Component | NodeMCU Pin             |
| --------- | ----------------------- |
| LED (+)   | D2 (GPIO4)              |
| LED (–)   | GND (via 220Ω resistor) |

### 🧑‍💻 Code:

```python
from machine import Pin
from time import sleep

led = Pin(4, Pin.OUT)  # GPIO4 = D2

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

### 🎯 Result:

LED blink karega har 1 second baad.

---

### ✅ **Step 2: Read Distance from Ultrasonic Sensor**

### 📌 Sensor Pins:

| Ultrasonic Pin | Use           | ESP8266 Pin |
| -------------- | ------------- | ----------- |
| VCC            | Power (3.3V)  | VV        |
| GND            | Ground        | GND         |
| Trig           | Trigger Pulse | D5 (GPIO14) |
| Echo           | Echo Signal   | D6 (GPIO12) |

### 🧑‍💻 Code:

```python
from machine import Pin, time_pulse_us
from time import sleep

trigger = Pin(14, Pin.OUT)
echo = Pin(12, Pin.IN)

def get_distance():
    trigger.off()
    sleep(0.01)
    trigger.on()
    sleep(0.00001)
    trigger.off()

    duration = time_pulse_us(echo, 1)
    distance = (duration * 0.0343) / 2
    return distance

while True:
    d = get_distance()
    print("Distance:", d, "cm")
    sleep(1)
```

### 🎯 Result:

Thonny terminal me distance print hoti rahegi.

---

### ✅ **Step 3: Control LED Based on Distance**

#### 📌 Final Connections (Ultrasonic + LED):

| Component     | ESP8266 Pin |
| ------------- | ----------- |
| LED (+)       | D2 (GPIO4)  |
| LED (–)       | GND         |
| Trig (Sensor) | D5 (GPIO14) |
| Echo (Sensor) | D6 (GPIO12) |

### 🧑‍💻 Code:

```python
from machine import Pin, time_pulse_us
from time import sleep

trigger = Pin(14, Pin.OUT)   # Trig = D5
echo = Pin(12, Pin.IN)       # Echo = D6
led = Pin(4, Pin.OUT)        # LED = D2

def get_distance():
    trigger.off()
    sleep(0.01)
    trigger.on()
    sleep(0.00001)
    trigger.off()

    duration = time_pulse_us(echo, 1)
    distance = (duration * 0.0343) / 2
    return distance

while True:
    d = get_distance()
    print("Distance:", d, "cm")

    if d < 20:
        led.on()
    else:
        led.off()

    sleep(1)
```

### 🎯 Result:

* Agar object 20cm se paas hoga ➜ **LED ON**
* Door hoga ➜ **LED OFF**

---

## 🧠 Summary of Learning

| Topic                  | What We Learned                     |
| ---------------------- | ----------------------------------- |
| Sensors                | Detect real-world changes (input)   |
| GPIO                   | Pins to connect sensors/outputs     |
| LED Blinking           | Output example using GPIO           |
| Ultrasonic Sensor      | Input example using GPIO            |
| Distance-based Project | LED ON/OFF based on object distance |

---

Agar aap chahen to mai iske liye ek **homework task**, **circuit diagram**, ya **quiz** bhi bana sakta hoon. Bataiye!
