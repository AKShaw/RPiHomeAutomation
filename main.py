from bottle import *
from config import GetConfig
import platform
import sys
import json
import urllib.request


#Initilize config class
config = GetConfig()

#Set static path for files
if (platform.system() == "Windows"):
    #obviosuly Windows wont work for the GPIO inputs, just for testing template files and general non-linux
    #constrained stuff etc
    print("Running on Windows...")
    @route("/static/<filepath:path>")
    def server_static(filepath):
        return static_file(filepath, root='C:/Users/ashaw/RPiHomeAutomation/www')
    print("Static path set!")
elif (platform.system() == "Linux"):
    try:
        import RPi.GPIO as GPIO
        print("Running on Raspberry Pi...")
        @route("/static/<filepath:path>")
        def server_static(filepath):
            return static_file(filepath, root='/home/pi/RPiHomeAutomation/www')
        print("Static path set!")
    except ImportError:	
        print("Running on Linux...")
        @route("/static/<filepath:path>")
        def server_static(filepath):
            return static_file(filepath, root='/home/alex/RPiHomeAutomation/www')
        print("Static path set!")
else:	
    print("Operating system not supported for development! Please use Windows or Linux")
    sys.exit()
	

@route('/<area>')
@route('/')
def index(area="Home"):
    return template("www/index.tpl", area=area, nums=[0,1,2,3])

def createWeatherJson(lat, long):
    url="http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(long)+"&APPID=18c319fbdc2695c31d05763b053e1753"
    print("Getting weather data...")
    response = urllib.request.urlopen(url)
    print("Data collected, parsing to JSON...")
    data = json.loads(response.read())
    print("Parsing complete!")
    return data

def start():
    weatherData = createWeatherJson(config.getLat, config.getLong)
    print (weatherData)
    run(host='0.0.0.0', port=8080)

start()

#TODO: Fix invalid API call error (even though key is correct?)
