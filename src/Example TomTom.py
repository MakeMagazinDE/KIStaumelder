#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import configparser 
import requests 
import json 
import sys 
import time 
import datetime 
from urllib.request import urlopen 
# URL to the tomtom api 
apiURL = "https://api.tomtom.com/routing/1/calculateRoute/" 
# apiKey 
apiKey = "TomTom-API-Key" 
# Start- und Zielkoordinaten:
sourceLat = 48.xxxxxxx 
sourceLon = 11.xxxxxxx 
destLat = 48.xxxxxxx 
destLon = 11.xxxxxxx 
tomtomURL = "%s/%s,%s:%s,%s/json?key=%s&traffic=true" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey) 
getData = urlopen(tomtomURL).read() 
jsonTomTomString = json.loads(getData) 
print(jsonTomTomString) 
totalTime = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']/60
delayTime = jsonTomTomString['routes'][0]['summary']['trafficDelayInSeconds']/60
print ("Fahrzeit: ", round(totalTime,1), " Minuten.")
print ("Verzögerung: ", round(delayTime,1), " Minuten.")