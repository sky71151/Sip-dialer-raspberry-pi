import pexpect
import time
#import RPi.GPIO as GPIO

# Set up the GPIO pin for the button
button_pin = 18
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Start linphone in interactive mode
linphone = pexpect.spawn('linphonec')

# Wait for linphone to start
time.sleep(2)

# Register a SIP account
sip_username = "1005"
sip_password = "12345678"
sip_domain = "192.168.0.36"
linphone.sendline(f'register {sip_username} {sip_password} sip:{sip_domain}')

# Wait for the registration to complete
time.sleep(2)

# Loop forever
while True:
    # Wait for the button to be pressed
    #while GPIO.input(button_pin):
        #time.sleep(0.1)

    # Make a call to extension 1005
    linphone.sendline('call 1005')

    # Wait for the call to connect
    time.sleep(25)

    # Hang up the call
    linphone.sendline('terminate')

    # Wait for a few seconds before the next iteration
    time.sleep(2)