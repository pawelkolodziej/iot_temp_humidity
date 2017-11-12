# https://www.rototron.info/dht22-tutorial-for-raspberry-pi/
import Adafruit_DHT as dht

#global variables
humidity = 0
temp = 0

#get temp and humidity from sensor DHT22
def getTempAndHumidityFromSensor():
    global humidity, temp
    humidity,temp = dht.read_retry(dht.DHT22, 4)
