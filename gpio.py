import RPi.GPIO as GPIO
import time

# GPIO-pinnen instellen
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

try:
    while True:
        # Lees de status van de GPIO-pinnen
        pin4_status = GPIO.input(4)
        pin17_status = GPIO.input(17)
        pin27_status = GPIO.input(27)

        # Toon de status in de terminal
        print(f"GPIO 4: {pin4_status}")
        print(f"GPIO 17: {pin17_status}")
        print(f"GPIO 27: {pin27_status}")
        time.sleep(1.5)

except KeyboardInterrupt:
    # GPIO-cleanup bij het afsluiten van het programma
    GPIO.cleanup()