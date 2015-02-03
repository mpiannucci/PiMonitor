PiMonitor
=================

A simple interface for remote home monitoring.

The project consists of two parts. The first is the **Collector**, which grabs the current data. The second is the **Reporter** which displays the latest data in a meaningful way. 

Required Hardware
-----------------
* [Raspberry Pi](http://www.raspberrypi.org)
* [DHT11](http://www.adafruit.com/product/386)
* 10k resistor
* Breadboard

Required Software
-----------------
* [Adafruit DHT11 Python Library](https://github.com/adafruit/Adafruit_Python_DHT)
* [Google App Engine](https://cloud.google.com/appengine/docs)
* [web.py](http://webpy.org)

##### Get Adafruit Python Library
On the Raspberry Pi...
```bash
sudo apt-get update
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/
sudo python setup.py install
```

##### Get the Google App Engine SDK
On a host laptop...
Install the Python SDK [from Google](https://cloud.google.com/appengine/downloads)

##### Get Web.py
On a host laptop... 
```bash
cd Reporter/
pip install web.py -t .
rm -rf web.*
```