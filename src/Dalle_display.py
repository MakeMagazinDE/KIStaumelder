import RPi.GPIO as GPIO
import time
import subprocess

import pygame
from pygame.locals import*
pygame.init()

SENSOR_PIN = 23
BUTTON_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

subprocess.run(["/usr/bin/vcgencmd", "display_power", "0"])

def mein_callback(channel):
    print('Es gab eine Bewegung!')
    subprocess.run(["/usr/bin/vcgencmd", "display_power", "1"])
    img = pygame.image.load('/home/pi/Desktop/Ergebnis.jpg')
    black = (0, 0, 0)

    # Hier die Größe des Bilds einstellen
    img = pygame.transform.scale(img, (400, 400))
    w = 400
    h = 400    
    screen = pygame.display.set_mode((w, h))
    #Sobald alles läuft, Zeile oben mit Zeile unten ersetzen
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    pygame.event.get()
    pygame.mouse.set_visible(False)

    # Anzeigedauer verlängern wie gewünscht z.B. von 10 auf 60 Sekunden:
    t_end = time.time() + 10

    while time.time() < t_end:
        screen.fill((black))

	# Hier die Position auf dem Display einstellen
        screen.blit(img,(0,0))
        pygame.display.flip()

        # Bei Tastendruck per VNC das Programm beenden
        for event in pygame.event.get():
            print(event.type)
            if event.type == 2:
                subprocess.run(['pm2', 'stop', '0'])
                subprocess.run(["/usr/bin/vcgencmd", "display_power", "1"])
        
	# Button
        input_state = GPIO.input(24)
        if input_state == False:
            pygame.quit()
            print('Button Pressed')
            exec(open("/home/pi/Desktop/Dalle_generate.py").read())
    
    print("Ende Display")
    pygame.quit()

    # Nach der Anzeige des Bilds wird noch kurz der Desktop angezeigt, und dann erst das 
    # Display ausgeschaltet. Das kann gelöscht werden, wenn alles gut läuft.
    time.sleep(5)
    subprocess.run(["/usr/bin/vcgencmd", "display_power", "0"])
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    subprocess.run(["/usr/bin/vcgencmd", "display_power", "1"])
GPIO.cleanup()