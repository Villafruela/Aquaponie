import machine
import ssd1306

#Donner l'addresse des GPIO qui pilotent les données (data (sda)) et l'horloge (clock (scl))
sda=machine.Pin(0)
scl=machine.Pin(1)

i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

#Scanne le port i2c et donne les addresses de tous les objets connectés
#print(i2c.scan())

#0x3C address = 60 en Hexadecimal
# On définit la taille de l'affichage (128x32 ou 128x64), le protocole d'accès (i2c ou spi), puis l'addresse de l'écran
oled = ssd1306.SSD1306_I2C(128,32,i2c,0x3c)

#oled.fill(1)
#oled.text ("Coucou Sophie", 30,25,1)
#oled.show()
# 128 x 32 > Affichage de 3 lignes de 16 caractères
# oled.text ("abcdefghijklmnop", 0,0,1)
# oled.show()
# oled.text ("abcdefghijklmnop", 0,12,1)
# oled.show()
# oled.text ("abcdefghijklmnop", 0,24,1)
# oled.show()

oled.text ("Salut Eloan", 0,0,1)
oled.show()
oled.text ("Ca roule ", 0,12,1)
oled.show()
oled.text ("ma poule ?", 0,24,1)
oled.show()


# pour effacer l'écran :
#oled.fill(0)
#oled.show()

