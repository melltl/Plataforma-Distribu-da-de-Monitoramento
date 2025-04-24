from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer
import json

app = Flask(__name__, template_folder='templates')  # Adicione esta linha
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def kafka_consumer():
    consumer = KafkaConsumer(
        'sensor-data',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        socketio.emit('sensor_update', message.value)
@socketio.on('control')
def handle_control(command):
    from gateway.gateway import handle_control_command
    handle_control_command(command)
if __name__ == '__main__':
    socketio.start_background_task(kafka_consumer)
    socketio.run(app, debug=True)