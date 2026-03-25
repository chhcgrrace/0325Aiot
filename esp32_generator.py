import requests
import time
import random

SERVER_URL = "http://127.0.0.1:5000/sensor"

def generate_data():
    temp = round(random.uniform(20.0, 35.0), 2)
    humid = round(random.uniform(40.0, 80.0), 2)
    
    # Metadata includes simulated WiFi connection state
    metadata = {
        "device": "ESP32_Demo_Unit",
        "wifi_connected": True,
        "wifi_rssi": random.randint(-80, -40),
        "ip": "192.168.1.100"
    }
    
    return {
        "temp": temp,
        "humid": humid,
        "metadata": metadata
    }

if __name__ == "__main__":
    print("Starting ESP32 Data Generator...")
    print(f"Target URL: {SERVER_URL}")
    while True:
        data = generate_data()
        try:
            response = requests.post(SERVER_URL, json=data, timeout=5)
            print(f"[{time.strftime('%X')}] Sent: {data} -> Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{time.strftime('%X')}] Request Failed: {e}")
        
        # Send fake DHT11 data every 2 seconds exactly
        time.sleep(2)
