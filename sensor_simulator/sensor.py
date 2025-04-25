import random
import time
import json
import socket
import threading
import multiprocessing
SENSOR_TYPES = {
    'temperature': lambda: round(random.uniform(18.0, 32.0), 2),
    'humidity':    lambda: round(random.uniform(30.0, 80.0)),
    'co2':         lambda: random.randint(400, 2000),
    'noise':       lambda: random.randint(30, 90),
    'motion':      lambda: random.choice([True, False]),
    'light':       lambda: round(random.uniform(0.0, 1000.0), 1),  # luminosidade em lux
    'pressure':    lambda: round(random.uniform(950.0, 1050.0), 2) # pressão em hPa
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

    from multiprocessing import Process

    sensors = [
        ("sensor_001", "temperature"),
        ("sensor_002", "humidity"),
        ("sensor_003", "noise"),
        ("sensor_004", "light"),         # <-- Novo sensor aqui!
        ("sensor_005", "motion")         # <-- Pode adicionar outros também!
    ]

    for sensor_id, sensor_type in sensors:
        p = Process(target=simulate_sensor, args=(sensor_id, sensor_type))
        p.start()