import machine as pico
import utime as t

pin6 = pico.Pin(6, pico.Pin.OUT)

while True:
    pin6.value(1)
    t.sleep(3)
    pin6.value(0)
    t.sleep(3)