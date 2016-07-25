#!/usr/bin/python
import sys
import time

import Adafruit_DHT

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.AM2302

# Example of sensor connected to Raspberry Pi pin 23
CABIN_DHT_PIN  = 'P9_23'
UTILITY_DHT_PIN = 'P8_12'
#CONEX_DHT_PIN = 'P8_11'

now=time.localtime(time.time())
currentmonth=now.tm_mon
currentday=now.tm_mday
currentyear=now.tm_year
filename = "{0}_{1}_{2}_env-monitor.csv".format(currentyear, currentmonth, currentday)

#### informative messaging for starting storage file
print "Opening ",filename, " for appending..."
print "reading inputs and storing data..."
file=open(filename,"a")
file.write("Time,Location,Temp,Humidity\n")
file.close()

while True:
    try:
        #get current time
        now=time.localtime(time.time())
        pt=time.asctime(now)  #formatted time for file
        currentmonth=now.tm_mon
        currentday=now.tm_mday
        currentyear=now.tm_year

        # How long to wait (in seconds) between measurements.
        FREQUENCY_SECONDS = 300

        # Attempt to get sensor reading in cabin
        humidity, temp = Adafruit_DHT.read_retry(DHT_TYPE, CABIN_DHT_PIN)

        # Skip to the next reading if a valid measurement couldn't be taken.
        # This might happen if the CPU is under a lot of load and the sensor
        # can't be reliably read (timing is critical to read the sensor).
        if humidity is not None and temp is not None:
            print('-------Cabin-------')
            print('Temperature: {0:0.1f} C'.format(temp))
            print('Humidity:    {0:0.1f} %'.format(humidity))
            #open file to append
            file=open(filename,"a")
            #add first column date/time stamp
            file.write(pt)
            #add next columns with raw reading, and converted voltage
            file.write(",%s,%f,%f\n" % ('Cabin',temp,humidity))
            file.close()
            #if MM/DD/YR changes, update filename
            #this translates to a new file every day
            ##!!!!header row is dropped from subsequent days
            filename = "{0}_{1}_{2}_env-monitor.csv".format(currentyear, currentmonth, currentday)
        else:
            print('Failed to get reading from Cabin. Try again!')

        # Attempt to get sensor reading in utility connection.
        humidity, temp = Adafruit_DHT.read_retry(DHT_TYPE, UTILITY_DHT_PIN)

        # Skip to the next reading if a valid measurement couldn't be taken.
        # This might happen if the CPU is under a lot of load and the sensor
        # can't be reliably read (timing is critical to read the sensor).
        if humidity is not None and temp is not None:
            print('------Utility------')
            print('Temperature: {0:0.1f} C'.format(temp))
            print('Humidity:    {0:0.1f} %'.format(humidity))
            #open file to append
            file=open(filename,"a")
            #add first column date/time stamp
            file.write(pt)
            #add next columns with raw reading, and converted voltage
            file.write(",%s,%f,%f\n" % ('Utility',temp,humidity))
            file.close()
            #if MM/DD/YR changes, update filename
            #this translates to a new file every day
            ##!!!!header row is dropped from subsequent days
            filename = "{0}_{1}_{2}_env-monitor.csv".format(currentyear, currentmonth, currentday)
        else:
            print('Failed to get reading from Utility. Try again!')

        # Attempt to get sensor reading in conex connection.
#        humidity, temp = Adafruit_DHT.read_retry(DHT_TYPE, CONEX_DHT_PIN)

        # Skip to the next reading if a valid measurement couldn't be taken.
        # This might happen if the CPU is under a lot of load and the sensor
        # can't be reliably read (timing is critical to read the sensor).
#        if humidity is not None and temp is not None:
#            print('-------Conex-------')
#            print('Temperature: {0:0.1f} C'.format(temp))
#            print('Humidity:    {0:0.1f} %'.format(humidity))
            #open file to append
#            file=open(filename,"a")
            #add first column date/time stamp
#            file.write(pt)
            #add next columns with raw reading, and converted voltage
#            file.write(",%s,%f,%f\n" % ('Conex',temp,humidity))
#            file.close()
            #if MM/DD/YR changes, update filename
            #this translates to a new file every day
            ##!!!!header row is dropped from subsequent days
#            filename = "{0}_{1}_{2}_env-monitor.csv".format(currentyear, currentmonth, currentday)
#        else:
#            print('Failed to get reading from Conex. Try again!')

        # Wait 30 seconds before continuing
        time.sleep(FREQUENCY_SECONDS)

    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        sys.exit()
