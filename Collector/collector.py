#!/usr/bin/python
# Copyright 2015 Matthew Iannucci
# 
# collector.py 
# The main collector script. Interfaces all of the sensors and packages 
# the data for the reporter. Because this is a low level interface with
# the GPIO pins, root access is REQUIRED. 
import sys
import json
import requests
import datetime
import Adafruit_DHT
import config


class Collector():

    def __init__(self, api_url):
        ''' Constructor '''
        self.api_url = api_url
        read_success = self._readTemperature()
        if not read_success:
            print "Failed to read from Temperature sensor!"

    def _readTemperature(self):
        ''' Read temperature data from the DHT11 sensor
        You must set up the pin in the config module for this 
        to work. This method reads the data and sets the class
        variables that should be retrieved with a getter or setter. 
        This method is PRIVATE and should not be called directly.

        @return True if successful. 
        '''
        self.humidity, self.temperature = Adafruit_DHT.read_retry(config.TEMP_SENSOR, config.TEMP_PIN)

        # Make sure there is data
        if self.humidity is not None and self.temperature is not None:
            return True
        else:
            return False

    def getTemperatureF(self):
        ''' Get the latest temperature reading in Fahrenheit. 

        @return The temperature in Fahrenheit
        '''
        return ((self.temperature * 9) / 5) + 32

    def getTemperatureC(self):
        ''' Get the latest temperature reading in Celsius. 

        @return The temperature in Celsius
        '''
        return self.temperature

    def getHumidity(self):
        ''' Get the latest humidity reading

        @return The percent humidity
        '''
        return self.humidity

    def sendReport(self):
        ''' Send the data off to the reporter '''
        rawData = {
            "date": str(datetime.datetime.now()),
            "temp": self.getTemperatureF(),
            "humidity": self.getHumidity()
        }
        packedData = json.dumps(rawData)
        
        try:
            resp = requests.post(self.api_url, data=packedData, headers={"Accept":"*/*", "Content-Type": "application/json"})
            return resp.json()
        except Exception as e:
                print e

if __name__ == "__main__":
    collector = Collector(config.ADDRESS)
    print collector.getHumidity()
