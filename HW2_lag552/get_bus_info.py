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
for i in stopinfo:
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    stop_name = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    stop_status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    onward_calls = i['MonitoredVehicleJourney']['OnwardCalls']
    if len(onward_calls) == 0:
        stop_name == 'N/A'
        stop_status == 'N/A'
#How to return N/A from blank values in python: from http://stackoverflow.com/questions/17551427/how-to-return-n-a-given-blank-values-in-python-and-scraperwiki
    print (latitude, ',', longitude, ',', stop_name, ',', stop_status)
    ii = ii + 1
