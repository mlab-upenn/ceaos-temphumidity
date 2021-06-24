import sys
import time
os.chdir('pigpio_dht22')
sys.path.append("/home/pi/pigpio_dht22")
import pigpio
import DHT22

#s is sensor made in config file, must be passed
def driver(s, pollrate):
    while True:
        if s.humidity is not None and s.temperature is not None:
            #send to cea-os using zeromq Api
            print('Temp: {:.2f} C Humidity: {:.2f}'.format(s.temperature(), s.humidity()))
        else:
            print('Error: sensor read failed')
        time.sleep(pollrate)
