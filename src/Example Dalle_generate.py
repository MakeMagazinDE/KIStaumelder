import random
pic_style = random.choice(["photo realistic", "superhero comic", "Picasso", "Claude Monet", "Vincent van Gogh", "Rembrandt"])
pic_object = random.choice(["panda", "elephant", "frog", "buddha", "star wars character"])    
pic_location = random.choice(["on a ship deck", "in space", "on times square", "on the beach", "under water"])

print("Generiere Bild:")
print(f"Stil: {pic_style}")
print(f"Objekt: {pic_object}")
print(f"Lokation: {pic_location}")

import openai
openai.api_key = 'Hier den eigenen OpenAI-API-Key eintragen' 
response = openai.Image.create(
    prompt= 'Style is ' + pic_style + ', add a ' + pic_object + ' ' + pic_location,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
import urllib.request
urllib.request.urlretrieve(image_url, "/home/pi/Desktop/Bild.jpg")