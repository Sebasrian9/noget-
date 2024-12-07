import paho.mqtt.client as mqtt
import time

# MQTT-konfiguration for ThingsBoard demo-serveren
server = "demo.thingsboard.io"  # Korrekt serveradresse
port = 1883  # Porten for MQTT
access_token = "l4XSur6mlYJGQzZuMAnP"  # Din enheds access token

# Callback-funktion når tilslutning er etableret
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Callback-funktion når data er publiceret
def on_publish(client, userdata, mid):
    print(f"Data successfully published with mid: {mid}")

# Opret MQTT-klient
client = mqtt.Client()

# Sæt access token som klient-id
client.username_pw_set(access_token, "")

# Tilslut callback-funktioner
client.on_connect = on_connect
client.on_publish = on_publish

# Forbind til ThingsBoard demo-serveren
client.connect(server, port, 60)

# Start MQTT-loop
client.loop_start()

# Simuler sending af telemetri i en løkke
while True:
    # Første sæt af telemetri (stationær position)
    telemetry = {"latitude": 55.6762, "longitude": 12.5683, "speed": 0.0}
    client.publish("v1/devices/me/telemetry", str(telemetry))
    print(f"Sent telemetry: {telemetry}")

    time.sleep(9)  # Vent i 4 sekunder før næste data

    # Andet sæt af telemetri (ændret position)
    telemetry = {"latitude": 55.689690, "longitude": 12.555693, "speed": 0.0}
    client.publish("v1/devices/me/telemetry", str(telemetry))
    print(f"Sent telemetry: {telemetry}")

    time.sleep(4)  # Vent i 4 sekunder før næste iteration

# Vent og afslut forbindelsen
time.sleep(4)
client.loop_stop()
client.disconnect()
