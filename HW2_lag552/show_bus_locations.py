from __future__ import print_function
import pylab as pl
import json
import urllib as urllib
import sys

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=ef750fed-f2ee-44e0-88f7-3adbc4466614&VehicleMonitoringDetailLevel=calls&LineRef=B52" 
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busline = 'Bus line : ' + sys.argv[2]
numberofbuses = len(location)
print (busline)
print ('Number of Active Buses :' , numberofbuses)

ii = 0
for i in location:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', ii, 'is at latitude', latitude, 'and longitude', longitude)
    ii = ii + 1
