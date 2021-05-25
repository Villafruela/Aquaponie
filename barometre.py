import machine
import utime as t
from bmp280 import BMP280
#import adafruit_bmp280



P2 = machine.Pin(2) # Data
P3 = machine.Pin(3) # Clock

bus = machine.I2C(1, sda=P2, scl=P3, freq=400000)
#print(bus.scan())
bmp = BMP280(bus, addr=0x76)

#i2c = machine.I2C(1, sda=P2, scl=P3, freq=400000)
#sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

while True :
    print(round(bmp.temperature,1),'°C')
    print(round(bmp.pressure/100,1),'hPa')
    t.sleep(10)