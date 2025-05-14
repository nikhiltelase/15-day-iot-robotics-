#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "RelayControl";
const char* password = "12345678";

ESP8266WebServer server(80);

#define RELAY_PIN D6
bool relayState = false;

void handleRoot() {
  String html = R"rawliteral(
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #1e1e1e;
          color: white;
          text-align: center;
          padding: 20px;
        }
        h2 {
          color: #00ffcc;
        }
        .status {
          font-size: 1.5em;
          margin: 20px 0;
        }
        .btn {
          display: inline-block;
          padding: 15px 30px;
          font-size: 18px;
          margin: 10px;
          border: none;
          border-radius: 8px;
          cursor: pointer;
          text-decoration: none;
          transition: background-color 0.3s ease;
        }
        .on {
          background-color: #4CAF50;
          color: white;
        }
        .on:hover {
          background-color: #45a049;
        }
        .off {
          background-color: #f44336;
          color: white;
        }
        .off:hover {
          background-color: #da190b;
        }
        .footer {
          margin-top: 40px;
          font-size: 0.9em;
          color: #888;
        }
      </style>
    </head>
    <body>
      <h2>🔌 Relay Control Panel</h2>
      <p class="status">Relay is currently: <strong>)rawliteral";

  html += relayState ? "ON" : "OFF";

  html += R"rawliteral(</strong></p>
      <a class="btn on" href="/on">Turn ON</a>
      <a class="btn off" href="/off">Turn OFF</a>
      <div class="footer">ESP8266 Web Server</div>
    </body>
    </html>
  )rawliteral";

  server.send(200, "text/html", html);
}

void handleOn() {
  relayState = true;
  digitalWrite(RELAY_PIN, LOW); // LOW = ON for relay
  handleRoot();
}

void handleOff() {
  relayState = false;
  digitalWrite(RELAY_PIN, HIGH); // HIGH = OFF for relay
  handleRoot();
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH); // Start with relay off

  WiFi.softAP(ssid, password);
  Serial.println("Access Point Started");
  Serial.println("IP Address: ");
  Serial.println(WiFi.softAPIP());

  server.on("/", handleRoot);
  server.on("/on", handleOn);
  server.on("/off", handleOff);
  server.begin();
  Serial.println("Web server started");
}

void loop() {
  server.handleClient();
}




// then opne