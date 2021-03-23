from sense_emu import SenseHat
import time
sense = SenseHat()

def medida():

    temp = sense.temp
    presion = sense.pressure
    humedad = sense.humidity
    medidas = [humedad, temp, presion] 
    return medidas

