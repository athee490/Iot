import urequests
import machine
import time
import sounddevice as sd
import numpy as np

# Define the audio callback function
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_data.append(indata.copy())

# Set up the audio stream
audio_data = []
with sd.InputStream(callback=audio_callback):
    sd.sleep(5000)  # Record audio for 5 seconds (adjust as needed)

# Combine all audio frames into a single array
audio_data = np.concatenate(audio_data)

# Convert the audio data to a string for sending
audio_data_str = ','.join(map(str, audio_data))

# Now you can use `audio_data_str` as the payload in your HTTP request
print("Audio data ready for sending:", audio_data_str)

# Replace with your Wi-Fi credentials
SSID = "YourSSID"
PASSWORD = "YourPassword"

# Replace with the URL where you want to send the data
URL = "http://example.com/upload_audio_data"

# Initialize the Wi-Fi connection
def connect_wifi():
    import network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)
    while not station.isconnected():
        pass

def send_data(audio_data_str):
    payload = "audio_data=" + str(audio_data_str)
    try:
        response = urequests.post(URL, data=payload)
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error sending data. Status code:", response.status_code)
        response.close()
    except Exception as e:
        print("Error:", e)

# Main program
connect_wifi()

while True:
    # Read audio data from the microphone (you'll need to implement this)
    # Replace audio_data with actual audio data

    send_data(audio_data_str)

    # Add a delay before sending the next request (if needed)
    time.sleep(5)


