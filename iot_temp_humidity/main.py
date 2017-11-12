import sensor as sensor
import communication as com

sensor.getTempAndHumidityFromSensor()
com.printTempAndHumidity()
com.sendToThingsPeak()