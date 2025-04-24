# Terminal 1: Middleware
`cd middleware && docker-compose up -d`

# Terminal 2: Gateway
`python gateway/gateway.py`

# Terminal 3: Sensor Simulator
`python sensor_simulator/sensor.py`

# Terminal 4: Actuator Simulator
`python sensor_simulator/actuator.py `

# Terminal 5: Serviço gRPC
`python microservices/storage_service/storage_server.py`

# Terminal 6: Client gRPC (para testar)
`python microservices/storage_service/storage_client.py  `

# Terminal 7: Dashboard
`python dashboard/app.py`