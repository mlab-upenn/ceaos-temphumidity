import os
import json
import pigpio
import DHT22
os.chdir("pigpio_dht22")  # so that new module is in the right path


class TempHumiditySensor():
    def __init__(self, gpio=4):
        self.gpio = gpio
        self.pi = pigpio.pi()
        self.s = DHT22.sensor(self.pi, self.gpio)

    def read_value(self):
        self.s.trigger()
        if self.s.humidity is not None and self.s.temperature is not None:
            farenheit = (self.s.temperature() * 1.8) + 32
            payload = json.dumps(
                {
                    "action": "recv_value",
                    "cea-addr": "farm1.env1.bed1.air",
                    "payload": {
                        "air temperature": farenheit,
                        "humidity": self.s.humidity
                    }
                }
            )
        else:
            return "error"

    def calibrate(self, calib_val_humidity, calib_val_temperature):
        humidity, temperature = self.read_value()
        self.calib_humidity = calib_val_humidity - humidity
        self.calib_temperature = calib_val_temperature - temperature
        pass
