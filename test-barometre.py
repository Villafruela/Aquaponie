import machine
import utime as t
from bmp2802 import BMP280

P2 = machine.Pin(2) # Data
P3 = machine.Pin(3) # Clock

i2c = machine.I2C(1, sda=P2, scl=P3, freq=400000)

print(i2c.scan())

sensor =  BMP280(i2c)
sensor.get()

#returns a list of temp float and barometric pressure int
while True :
    print(sensor.getTemp(),'°C')
    #returns float temp in Celcius 

    print(sensor.getPress(),'Pa')
    #returns int pressure in Pascals

    #print(sensor.getAltitude(),'m')
    #returns float calculated altitude in metres
    t.sleep(60)
