import network
import socket
from machine import Pin, PWM

# PWM pins for motor
in1 = PWM(Pin(5), freq=1000)   # D1
in2 = PWM(Pin(4), freq=1000)   # D2
in3 = PWM(Pin(14), freq=1000)  # D5
in4 = PWM(Pin(12), freq=1000)  # D6

# Default speed
speed_pwm = 600

# Movement mode
current_action = 'stop'

# Motor control logic
def move(action):
    global current_action
    current_action = action
    if action == 'forward':
        in1.duty(speed_pwm); in2.duty(0)
        in3.duty(speed_pwm); in4.duty(0)
    elif action == 'backward':
        in1.duty(0); in2.duty(speed_pwm)
        in3.duty(0); in4.duty(speed_pwm)
    elif action == 'left':
        in1.duty(0); in2.duty(speed_pwm)
        in3.duty(speed_pwm); in4.duty(0)
    elif action == 'right':
        in1.duty(speed_pwm); in2.duty(0)
        in3.duty(0); in4.duty(speed_pwm)
    else:
        in1.duty(0); in2.duty(0)
        in3.duty(0); in4.duty(0)

# Wi-Fi AP setup
ssid = 'WiFi_Car'
password = '12345678'
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
while not ap.active():
    pass
print('WiFi started at', ap.ifconfig()[0])

# HTML for interface
html = """<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>WiFi Car</title>
  <style>
    body { font-family: sans-serif; text-align: center; background: #f0f0f0; padding: 20px; }
    button { padding: 15px 25px; font-size: 20px; margin: 10px; border-radius: 10px; }
    .slider { width: 90%%; max-width: 400px; }
    h2, h3 { color: #333; }
    .controls { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
  </style>
</head>
<body>
  <h2>WiFi Car Control</h2>
  <div class="controls">
    <button onclick="sendCmd('forward')">↑</button><br>
    <button onclick="sendCmd('left')">←</button>
    <button onclick="sendCmd('stop')">■</button>
    <button onclick="sendCmd('right')">→</button><br>
    <button onclick="sendCmd('backward')">↓</button>
  </div>
  <h3>Speed: <span id="spd">600</span></h3>
  <input type="range" min="0" max="1023" value="600" class="slider" id="speedSlider" oninput="updateSpeed(this.value)">
  <script>
    let currentSpeed = 600;
    let lastSentSpeed = 600;

    function sendCmd(cmd) {
      fetch('/' + cmd);
    }

    function updateSpeed(val) {
      currentSpeed = val;
      document.getElementById("spd").innerText = val;
      fetch('/speed?val=' + val);
    }
  </script>
</body>
</html>
"""

# Start web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Server listening on", addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024).decode()
    print('Request:', request)

    if 'GET /forward' in request:
        move('forward')
    elif 'GET /backward' in request:
        move('backward')
    elif 'GET /left' in request:
        move('left')
    elif 'GET /right' in request:
        move('right')
    elif 'GET /stop' in request:
        move('stop')
    elif 'GET /speed?val=' in request:
        try:
            val_str = request.split('GET /speed?val=')[1].split(' ')[0]
            speed_pwm = int(val_str)
            print("Speed set to:", speed_pwm)
            if current_action != 'stop':
                move(current_action)  # Re-apply movement with new speed
        except:
            pass

    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.sendall(html)
    cl.close()