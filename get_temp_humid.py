# https://www.rototron.info/dht22-tutorial-for-raspberry-pi/
import Adafruit_DHT as dht
import time
import datetime
import os
import urllib2

# get current time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#get temp and humidity
h,t = dht.read_retry(dht.DHT22, 4)
print st,'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)

#send it to thingspeak.com
myAPI = "DALZ4ZCKJ03P9GHY"
baseURL = baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (t, h))

# Open a file and save as html
#fo = open("pi_temp_humid.html", "ab")

#filename = "/var/www/html/pi_temp_humid.html"
#if not os.path.exists(os.path.dirname(filename)):
#    try:
#        os.makedirs(os.path.dirname(filename))
#    except OSError as exc: # Guard against race condition
#        if exc.errno != errno.EEXIST:
#            raise

#with open(filename, "ab") as fo:
#	fo.write(st + ', Temp={0:0.1f}*C,  Humidity={1:0.1f}% <br />'.format(t, h) );
#fo.close()
