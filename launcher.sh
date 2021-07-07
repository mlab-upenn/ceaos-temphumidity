#!/bin/sh
#launcher.sh

cd /
cd home/pi/ceaos-temphumidity
sudo python3 setup.py install
cd ceaos_temphumidity
sudo python3 driver.py
cd /
