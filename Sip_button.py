import subprocess

#import RPi.GPIO as GPIO

# Set up the GPIO pin for the buttonw
button_pin = 18
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

command = "linphonecsh init; sleep 1; linphonecsh register --host 192.168.0.36 --username 1008 --password Bloemenland2431a; sleep 1; linphonecsh dial \"sip:1006@192.168.0.36\"; sleep 28; linphonecsh hangup; sleep 1; linphonecsh exit"

while True:
    # Wait for the button to be pressed
    #while GPIO.input(button_pin):
        #time.sleep(0.1)

    subprocess.run(command, shell=True)