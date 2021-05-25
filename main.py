# Librairies
###################################################
import machine as pico
import ssd1306
import utime as t
from bmp280 import BMP280

# INITIALISATIONS
###################################################
# Mode de fonctionnement du système
mode = "demo" # mode de fonctionement 2 etats = demo / reel
timing = 0 # temps d'attente entre 2 mesures de l'humidité plante

# Set des entrées/sorties
P0 = pico.Pin(0) # sda oled
P1 = pico.Pin(1) # scl oled
P2 = pico.Pin(2) # Data baro
P3 = pico.Pin(3) # Clock baro
P6 = pico.Pin(6, pico.Pin.OUT) # Pin Moteur

# Set du capteur d'humidité
adc = pico.ADC(pico.Pin(27)) # détecteur humidité du sol
maxEchantillonage = 65535 #0% d'humidité
minEchantillonage = 25862 #100% humidité

# Set de l'affichage oled
i2c_oled=pico.I2C(0,sda=P0, scl=P1, freq=400000)
i2c_baro = pico.I2C(1, sda=P2, scl=P3, freq=400000)
#print(i2c.scan())
#test
oled = ssd1306.SSD1306_I2C(128,32,i2c_oled,0x3c)

# Set du baromètre (T°, Pression, Altitude)
sensor =  BMP280(i2c_baro)
sensor.get()


# FONCTIONS 
###################################################
def getTemp ():
    return sensor.getTemp()

def getPressure ():
    return sensor.getPress()

def getAltitude ():
    return sensor.getAltitude()

def affichage (message):
    taille = len(message)
    nbEcrans = int(taille / 48)
    #print (nbEcrans)
    if (taille%48) != 0 :
        nbEcrans+=1
    position = 0
    for i in range(nbEcrans):
        for j in range(3):
            oled.text (message[position:position+16], 0,j*12,1)
            oled.show()
            position += 16
        t.sleep(3)
        oled.fill(0)
        oled.show()

def afficheTempPre ():
    temp = str(round(getTemp(),1)) + " C"
    pressure = str(int(getPressure())) + " Pa"
    affichage(temp+"          "+pressure)
    t.sleep(3)

def moteur(etat):
    if (etat=="on") :
        P6.value(1)
        t.sleep(3)
        P6.value(0)
    elif (etat=="off") :
        P6.value(0)
    else :
        P6.value(0)
    
}

def humiditePlante():
    mesure = adc.read_u16()
    #print('mesure brute : %s',mesure)
    plage = maxEchantillonage-minEchantillonage
    mesure = abs(minEchantillonage-mesure)
    humidite = int(100-((mesure * 100)/plage))
    affichage('Humidite :%i %',humidite)
    return humidite

while True :
    afficheTempPre ()
    if (mode == "demo"){
        timing = 15
    } elif (mode == "reel"){
        timing = 900
    }
    t.sleep(timing)
    humidite = humiditePlante()
    if (humidite < 50):
        moteur(on) 