const socket = io();

socket.on('sensor_update', function(data) {
    const container = document.getElementById('sensor-data');
    const id = data.sensor_id;
    const type = data.type;
    const value = data.value;
    const time = new Date(data.timestamp * 1000).toLocaleTimeString();

    let element = document.getElementById(id);
    if (!element) {
        element = document.createElement('div');
        element.id = id;
        container.appendChild(element);
    }
    element.innerHTML = `<strong>${id} (${type})</strong>: ${value} - ${time}`;
});
