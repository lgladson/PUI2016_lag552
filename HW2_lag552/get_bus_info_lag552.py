from __future__ import print_function
import pylab as pl
import json
import urllib as urllib
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

stopinfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

ii = 0
fname = sys.argv[3]
r = open(fname, 'w')
r.write('Latitude, Longitude, Stop Name, Stop Status, ')
print ('Latitude, Longitude, Stop Name, Stop Status')

for i in stopinfo:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    onward_calls = i['MonitoredVehicleJourney']['OnwardCalls']
    if len(onward_calls) is 0:
        stop_name = 'N/A'
        stop_status = 'N/A'
    else:
        stop_name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
#How to return N/A from blank values in python: from http://stackoverflow.com/questions/17551427/how-to-return-n-a-given-blank-values-in-python-and-scraperwiki
    print (latitude, ',', longitude, ',', stop_name, ',', stop_status)
    r.write(str(latitude) + ',' + str(longitude) + ',' + str(stop_name) + ',' + str(stop_status) + ',')
    ii = ii + 1
