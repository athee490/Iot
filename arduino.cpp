#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
const char* server = "http://yourserver.com/endpoint";

int microphonePin = A0;
int ledPin = 13;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  int sensorValue = analogRead(microphonePin);
  float percentage = map(sensorValue, 0, 1023, 0, 100);

  Serial.print("Percentage: ");
  Serial.println(percentage);

  // Send data as JSON
  WiFiClient client;
  if (client.connect(server, 80)) {
    String jsonData = "{\"VALUE\":\"" + String(percentage, 0) + "\"}";
    client.println("POST / HTTP/1.1");
    client.println("Host: yourserver.com");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(jsonData.length());
    client.println();
    client.println(jsonData);
    delay(10);
    client.stop();
  }

  delay(1000); // Adjust delay as needed
}