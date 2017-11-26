import sensor as sensor
import communication as com
import schedule
import time

def doAll():
    sensor.getTempAndHumidityFromSensor()
    com.printTempAndHumidity()
    com.sendToThingsPeak()

def scheduleAndDoAll():
    schedule.every(15).minutes.do(doAll)
    while 1:
        schedule.run_pending()
        time.sleep(1)

scheduleAndDoAll()
#doAll()