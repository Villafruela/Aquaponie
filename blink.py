import machine
import utime
#Onboard pin = 25 for RPi Pico
led_onboard = machine.Pin(15, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(0.3)