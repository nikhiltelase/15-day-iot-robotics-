

# 📘 **Day-4 – Wireless Control**

---

## 🧠 **What You Will Learn Today**

1. What is Wireless Control in IoT?
2. Different Wireless Control Methods
3. How to Control a Light using Wi-Fi (AP Mode)
4. Hands-on: Turn ON/OFF LED using NodeMCU Web Page

---

## 📡 **1. What is Wireless Control?**

> Wireless control ka matlab hai bina wires ke kisi bhi device (light, fan, motor) ko **remotely control karna**.

IoT ka main power yehi hota hai – automation without touching things!

---

## 🚀 **2. Wireless Control Methods in IoT/Robotics**

| Method         | Use Case Example       | Range        | Notes                              |
| -------------- | ---------------------- | ------------ | ---------------------------------- |
| **IR Remote**  | TV, AC, old toys       | Few meters   | Works only in direct line of sight |
| **Bluetooth**  | Mobile controlled cars | 10–30 meters | Fast, but short range              |
| **Wi-Fi**      | Home automation        | 100+ meters  | Fast + long range + internet-based |
| **RF (Radio)** | RC cars, RF switches   | 100+ meters  | Cheap but not secure               |
| **LoRa**        | Remote sensors, agriculture | 2–15 km      | Ultra long range, low power, slow data |

---

## 💡 **3. Today’s Practical: LED Control using NodeMCU + Wi-Fi (AP Mode)**

---

### 📌 **AP Mode (Access Point Mode) kya hota hai?**

> NodeMCU khud hi ek **Wi-Fi hotspot (Access Point)** banata hai.
> Mobile/Computer us hotspot se connect hota hai, fir webpage se LED control hoti hai.

📶 *No need of internet or router!*

---

## 🔧 **4. Step-by-Step Practical**

---

### ✅ **Step 1: Connect External LED**

| Component | NodeMCU Pin             |
| --------- | ----------------------- |
| LED (+)   | D2 (GPIO4)              |
| LED (–)   | GND (via 220Ω resistor) |

---

### ✅ **Step 2: MicroPython Code to Create Web Server (AP Mode)**

```python
import network
from machine import Pin
import socket

# Create Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="IoT_LED", password="12345678")  # Wi-Fi name & password

# Setup LED pin
led = Pin(4, Pin.OUT)  # D2 = GPIO4

# HTML for Webpage
html = """<!DOCTYPE html>
<html>
<head><title>LED Control</title></head>
<body style="text-align:center; font-family:sans-serif;">
    <h2>Control LED</h2>
    <a href="/on"><button style="padding:20px; font-size:20px;">Turn ON</button></a>
    <a href="/off"><button style="padding:20px; font-size:20px;">Turn OFF</button></a>
</body>
</html>
"""

# Create Socket Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Access Point IP:", ap.ifconfig()[0])

while True:
    conn, addr = s.accept()
    print("Client connected from", addr)
    request = conn.recv(1024)
    request = str(request)

    if '/on' in request:
        led.on()
    elif '/off' in request:
        led.off()

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(html)
    conn.close()
```

---

### 📱 **Step 3: How to Use**

1. NodeMCU ko power do (Thonny IDE se code run karo)
2. Phone/laptop se connect karo:
   **Wi-Fi Name**: `IoT_LED`
   **Password**: `12345678`
3. Open browser and go to IP:
   👉 `192.168.4.1`
4. Webpage open hogi – button dabao to LED on/off hogi ✅

---

## 🎯 **Result**

* LED will turn **ON** or **OFF** wirelessly from your mobile browser!
* No internet or router needed – NodeMCU ne khud Wi-Fi banaya.

---

## 🧠 **Summary of Learning**

| Topic               | What We Did                             |
| ------------------- | --------------------------------------- |
| Wireless Control    | Discussed IR, Bluetooth, Wi-Fi, RF etc. |
| Wi-Fi AP Mode       | NodeMCU created a local hotspot         |
| LED Control Project | LED ON/OFF using browser webpage        |
| Code Understanding  | Web server + socket + GPIO control      |

---

## 🏠 **Task**

1. Try changing Wi-Fi name and password in code.
2. Try adding another LED on different GPIO.
3. Make webpage better using HTML styles.

---
