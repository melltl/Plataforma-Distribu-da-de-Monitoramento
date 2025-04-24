from confluent_kafka import Producer
import socket
import threading
import json
import socket as udp_socket

# Configuração do produtor Kafka
producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Função de callback para monitorar a entrega das mensagens. """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def handle_client(conn):
    """ Função para tratar os dados recebidos de cada cliente. """
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = json.loads(data.decode())
        # Enviar a mensagem para o Kafka
        producer.produce('sensor-data', json.dumps(message).encode('utf-8'), callback=delivery_report)
        producer.flush()
    conn.close()

def start_gateway():
    """ Função para iniciar o servidor de gateway TCP. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 65432))
        s.listen()
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn,))
            thread.start()

def send_to_actuator(command):
    """ Função para enviar comandos para o atuador via UDP. """
    with udp_socket.socket(udp_socket.AF_INET, udp_socket.SOCK_DGRAM) as s:
        s.sendto(json.dumps(command).encode(), ('localhost', 65433))
def handle_control_command(command):
    """Envia comandos para atuadores via UDP"""
    if command['type'] == 'light_control':
        control_msg = {
            'actuator_id': f"light_{command['room']}",
            'action': 'toggle'
        }
    elif command['type'] == 'ac_control':
        control_msg = {
            'actuator_id': f"ac_{command['room']}",
            'action': 'set_temp',
            'value': command['temperature']
        }
    
    send_to_actuator(control_msg)  # Usa a função existente
if __name__ == "__main__":
    start_gateway()
