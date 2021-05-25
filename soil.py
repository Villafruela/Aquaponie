import machine as pico
import utime as t
adc = pico.ADC(pico.Pin(27))
maxEchantillonage = 65535 #0% d'humidité
minEchantillonage = 25862 #100% humidité

def humiditePlante():
    mesure = adc.read_u16()
    #print('mesure brute : %s',mesure)
    plage = maxEchantillonage-minEchantillonage
    mesure = abs(minEchantillonage-mesure)
    humidite = int(100-((mesure * 100)/plage))
    print('Humidite :%i %',humidite)
    
while True:
    humiditePlante()
    t.sleep(5)

    