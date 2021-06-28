import sys
import os
import time
import zmq
os.chdir('pigpio_dht22')
sys.path.append("/home/pi/pigpio_dht22")
import pigpio
import DHT22

#s is sensor made in config file, must be passed
def driver():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:23267")
    pi = pigpio.pi()
    s = DHT22.sensor(pi, 4)
    while True:
        if s.humidity is not None and s.temperature is not None:
            #send to cea-os using zeromq Api
            farenheit = (s.temperature() * 1.8) + 32
            payload = {
                "action": "temp.read",
                "cea-addr": "farm1.env1.airtemp",
                "payload": [farenheit, s.humidity()]
            }
            socket.send_json(payload)
            #print('Temp: {:.2f} C Humidity: {:.2f}'.format(s.temperature(), s.humidity()))
        else:
            socket.send('Error: sensor read failed')
        time.sleep(3)
