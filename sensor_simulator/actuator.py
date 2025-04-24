import socket
import json

ACTUATORS = {
    'ac_001': {'status': False, 'temp_setpoint': 24.0},
    'light_001': {'status': False},
    'alarm_001': {'status': False}
}

def actuator_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('localhost', 65433))
        print("Actuator service running...")
        while True:
            data, addr = s.recvfrom(1024)
            command = json.loads(data.decode())
            
            actuator_id = command['actuator_id']
            action = command['action']
            
            if actuator_id in ACTUATORS:
                if action == 'toggle':
                    ACTUATORS[actuator_id]['status'] = not ACTUATORS[actuator_id]['status']
                elif action == 'set_temp' and 'temp_setpoint' in ACTUATORS[actuator_id]:
                    ACTUATORS[actuator_id]['temp_setpoint'] = command['value']
                
                print(f"Actuator {actuator_id} updated: {ACTUATORS[actuator_id]}")
            else:
                print(f"Unknown actuator: {actuator_id}")

if __name__ == "__main__":
    actuator_listener()