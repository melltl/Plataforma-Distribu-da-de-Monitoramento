const socket = io();

socket.on('sensor_update', (data) => {
    const div = document.getElementById('sensor-data');
    div.innerHTML = `
        <p>Sensor ID: ${data.sensor_id}</p>
        <p>Tipo: ${data.type}</p>
        <p>Valor: ${data.value}</p>
        <p>Timestamp: ${new Date(data.timestamp * 1000)}</p>
    `;
});