import sensor as sensor
import communication as com
import schedule
import time

def doAll():
    sensor.getTempAndHumidityFromSensor()
    com.printTempAndHumidity()
    com.sendToThingsPeak()

def scheduleAndDoAll():
    print "temp and humidity scheduleAndDoAll"
    schedule.every(15).minutes.do(doAll)
    while 1:
        schedule.run_pending()
        time.sleep(1)

<<<<<<< HEAD
scheduleAndDoAll()
#doAll()
=======
if __name__ == '__main__':
    scheduleAndDoAll()
#doAll()
>>>>>>> bfa85d89b06150ae7ec66ee47b4deedb1b844fb9
