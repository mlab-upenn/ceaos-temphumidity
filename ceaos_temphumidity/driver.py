from time import sleep
import zmq
import json
from temphumidity import TempHumiditySensor

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://158.130.113.109:23267")    # Replace with your IP address
    sensor = TempHumiditySensor()

    while True:
        payload = sensor.read_value()
        if payload == "error":
            socket.send('Error: sensor read failed')
        else:
            socket.send_string(payload)
        
        reply = socket.recv()
        reply = json.loads(reply)
        print(reply)
        sleep(600)
