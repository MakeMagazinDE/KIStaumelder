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
apiKey = "Dein TomTom-API-Key" 
# Deine Start- und Zielkoordinaten hier einsetzen:
sourceLat = 48.xxxxxxx 
sourceLon = 11.yyyyyyy 
destLat = 48.zzzzzzz 
destLon = 11.vvvvvvv 

tomtomURL = "%s/%s,%s:%s,%s/json?key=%s&traffic=true" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey) 
getData = urlopen(tomtomURL).read() 
jsonTomTomString = json.loads(getData) 
print(jsonTomTomString) 
totalTime = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']/60
delayTime = jsonTomTomString['routes'][0]['summary']['trafficDelayInSeconds']/60
print ("Fahrzeit: ", round(totalTime,1), " Minuten.")
print ("Verzögerung: ", round(delayTime,1), " Minuten.")

import random
if totalTime <= 15:
    pic_object = random.choice(["dolphin", "fighter jet"])    
if 15 < totalTime <= 20:
    pic_object = random.choice(["dog", "star wars villain"])    
if 20 < totalTime <= 25:
    pic_object = random.choice(["panda", "muppet"])    
if totalTime > 25:
    pic_object = random.choice(["buddha", "snail"])  
pic_style = random.choice(["photo realistic", "superhero comic", "Picasso", "Claude Monet", "Vincent van Gogh", "Rembrandt"])
pic_location = random.choice(["on a ship deck", "in the street", "on times square", "on the beach"])

api_key = "Hier den eigenen OWM-API-Key eintragen" 
root_url = "http://api.openweathermap.org/data/2.5/forecast?" 
# Name des Ortes für die Vorhersage → siehe Orte bei OWM
city_name = "Munich" 
# url für den API call zusammenstellen
url = f"{root_url}appid={api_key}&q={city_name}&cnt=3" 
r = requests.get(url) 
#print(r.json()) 
data = r.json() 
# Vorhersagewerte einlesen
descr = data["list"][1]['weather'][0]['description'] 
print("Generiere Bild:")
print(f"Stil: {pic_style}")
print(f"Objekt: {pic_object}")
print(f"Lokation: {pic_location}")
print(f"Wetter: {descr}")

import openai
openai.api_key = 'Hier den eigenen OpenAI-API-Key eintragen' 
response = openai.Image.create(
    prompt= 'Weather is ' + descr + 'Style is ' + pic_style + ', add a ' + pic_object + ' ' + pic_location,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
import urllib.request
urllib.request.urlretrieve(image_url, "/home/pi/Desktop/Ergebnis.jpg")
