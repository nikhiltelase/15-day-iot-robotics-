<div style="display: flex; justify-content: space-between; align-items: center; padding: 1px 8px;">
<h1>Iot & Robotics</h1>
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx7L3QXZeJ5gtlP5Qi728ZyvGvRBfYz-_mrA&s" alt="Connect Shiksha Logo" width="200"/>
 
</div>

## 📝 **Day 2 – Programming NodeMCU ESP8266 with Python (MicroPython)**

---

### 📌 **Objective:**

Learn how to install drivers, flash MicroPython firmware to NodeMCU ESP8266, and write your first program (blink LED) using **Thonny IDE** and **Python**.

---

### ⚙️ **Step 1: Install CH340 USB Driver**

**Why?**
The NodeMCU ESP8266 board uses the **CH340 USB-to-Serial chip** to connect with the computer. We need its driver so the board is detected.

**How to Install:**

1. Download the CH340 driver from trusted sources like [gogo.co](https://sparks.gogo.co.nz/ch340.html?srsltid=AfmBOormbl2iYCKWMg7DCX-8LWkwvtjy7SFPc4o5LS1dZQ_1tUuXwslT).
2. Extract the zip file and run the installer.
3. After successful installation, **restart your computer** (if required).

---

### 🔌 **Step 2: Connect NodeMCU to Laptop/PC**

* Use a **Micro USB cable** to connect the NodeMCU ESP8266 to your laptop.
* Make sure the cable supports **data transfer** (some cables are charge-only).

---

### 🖥️ **Step 3: Check Device in Device Manager**

1. Press `Windows + X` → Click on **Device Manager**.
2. Look under **Ports (COM & LPT)**.
3. You should see something like **“USB-SERIAL CH340 (COMX)”**.

   * If yes: Board is connected successfully.
   * If not: Recheck your driver and USB cable.

---

### 📁 **Step 4: Create a Project Folder**

1. Make a new folder (e.g., `esp8266_project`).
2. Open this folder in **VS Code** (optional, just for organizing files).

---

### 💻 **Step 5: Install esptool (Python Library)**

**What is esptool?**
`esptool` is a Python tool used to erase and flash firmware to ESP boards.

**How to Install:**

1. Open Terminal / Command Prompt.
2. Run:

   ```bash
   pip install esptool
   ```

---

### 🔄 **Step 6: Erase the Board (Clear Old Data)**

**Command:**

```bash
esptool --port COMX erase_flash
```

* Replace `COMX` with your actual port (e.g., COM4).
* This will **wipe existing data** from the board.

---

### 📥 **Step 7: Download MicroPython Firmware**

* Go to the official site: [https://micropython.org/download/esp8266/](https://micropython.org/download/esp8266/)
* Download the latest **`.bin` firmware file** for NodeMCU ESP8266.

---

### 📤 **Step 8: Flash Firmware to NodeMCU**

**Command:**

```bash
esptool --port COMX --baud 460800 write_flash --flash_size=detect 0 firmware_file_name.bin
```

* Replace:

  * `COMX` with your actual COM port
  * `firmware_file_name.bin` with your downloaded firmware filename or file path

Example:

```bash
esptool --port COM4 --baud 460800 write_flash --flash_size=detect 0 "C:\Users\Lenovo\Downloads\ESP8266_GENERIC-20250415-v1.25.0.bin"
```

This step will take a few seconds and install MicroPython on your board.

---

### 🧠 **MicroPython = Python for Microcontrollers**

Now your ESP8266 can be programmed using Python instead of C/C++.

---

### 🧑‍💻 **Step 9: Install Thonny IDE**

**Why Thonny?**
It is a beginner-friendly IDE that supports **MicroPython** and lets us write, run, and upload code easily.

**Download from:**
[https://thonny.org/](https://thonny.org/)

**After Installation:**

1. Open Thonny
2. Go to: **Tools → Options → Interpreter**
3. Select:

   * **Interpreter:** MicroPython (ESP8266)
   * **Port:** Select the correct COM port

---

### 💡 **Step 10: Write First Python Program (LED Blink)**

**NodeMCU has a built-in LED on Pin D4 (GPIO2)**

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

**How to Run:**

1. Paste the code in Thonny editor.
2. Click **“Run”** or press `F5`.
3. Watch the blue LED on the NodeMCU start blinking!

---

### ✅ **Summary of Steps:**

| Step | Task                                     |
| ---- | ---------------------------------------- |
| 1    | Install CH340 driver                     |
| 2    | Connect board via USB                    |
| 3    | Check COM port in Device Manager         |
| 4    | Create a project folder                  |
| 5    | Install `esptool`                        |
| 6    | Erase flash on board                     |
| 7    | Download MicroPython firmware            |
| 8    | Flash firmware using `esptool`           |
| 9    | Install and configure Thonny IDE         |
| 10   | Write and upload Python code (Blink LED) |

---

### 📌 **Tips for Students:**

* Always check the correct COM port before running any esptool commands.
* If the LED doesn't blink, try resetting the board using the RST button.
* Be patient while flashing firmware; don’t disconnect the board.
* You can connect sensors and actuators later using MicroPython code.

---

