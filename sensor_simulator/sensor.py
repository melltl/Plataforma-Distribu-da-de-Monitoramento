import random
import time
import json
import socket

SENSOR_TYPES = {
    'temperature': lambda: round(random.uniform(18.0, 32.0), 2),
    'humidity': lambda: round(random.uniform(30.0, 80.0)), 
    'co2': lambda: random.randint(400, 2000),
    'noise': lambda: random.randint(30, 90),
    'motion': lambda: random.choice([True, False])
}

def simulate_sensor(sensor_id, sensor_type, interval=5):
    while True:
        data = {
            'sensor_id': sensor_id,
            'type': sensor_type,
            'value': SENSOR_TYPES[sensor_type](),
            'timestamp': time.time()
        }
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 65432))
            s.sendall(json.dumps(data).encode())
        time.sleep(interval)

if __name__ == "__main__":
    # Exemplo para iniciar múltiplos sensores
    simulate_sensor("sensor_001", "temperature")
    # Adicione mais instâncias conforme necessário