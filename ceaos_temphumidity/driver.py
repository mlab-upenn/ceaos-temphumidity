from time import sleep
import zmq
import json
from .temphumidity import TempHumiditySensor

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:23267")
    sensor = TempHumiditySensor()

    while True:
        payload = sensor.read_value()
        if payload == "error":
            socket.send('Error: sensor read failed')
            #print('Temp: {:.2f} C Humidity: {:.2f}'.format(s.temperature(), s.humidity()))
        else:
            socket.send_json(payload)
        sleep(3)
