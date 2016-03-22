#DEPENDENCIES:
#   bottle
#   pyowm

from bottle import *
from config import *
from board import Board
from led import SetLED
from datetime import date
import platform
import sys
import calendar
import pyowm

board = Board()
led = SetLED("", "", board)


#Initilize config class
def setConfig():
    global config
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
    configObj = {}
    configObj["lat"] = config.getLat
    configObj["long"] = config.getLong

    ledScreenObj = {}
    ledSreenObj["firstLine"] = led.getLine1
    ledScreenObj["secondLine"] = led.getLine2
    
    return template("www/index.tpl", area=area, weather=getWeatherData(pyowm.OWM("18c319fbdc2695c31d05763b053e1753"), float(config.getLat), float(config.getLong)), config=configObj)

@route("/saveConfig", method="POST")
def writeConfig():
    lat=request.forms.get("lat")
    long=request.forms.get("long")
    valid = checkLatLong(lat, long)
    if valid==True:
        print("Saving...")
        saveConfig = SaveConfig(lat, long)
        print("Saved!")
        setConfig()
        redirect("/Config")
    elif valid==False:
        return "<p>Latitude or Longtitude invalid!</p>"

@route("/setLEDScreen")
def setLEDScreen():
    firstLine = request.forms.get("line1")
    secondLine = request.forms.get("line2")
    led = SetLED(firstLine, secondLine, board)
    redirect("/LEDScreen")


def checkLatLong(lat, long):
    try:
        if (-90 <= float(lat) <= 90 and -180 <= float(long) <= 180):
            return True
        else:
            return False
    except ValueError:
        return False
    

def getWeatherData(owm, lat, long):
    owm = owm
    weather = owm.weather_at_coords(lat, long) #returns observation obj
    currentDate = date.today()
    date_day_name = calendar.day_name[date.today().weekday()] #get day name
    date_day_num = date.today().day # get day num
    currentDate = [date_day_name, date_day_num] #create date variable
    location = weather.get_location().get_name() #get location name e.g Salisbury
    weather = weather.get_weather() #returns weather obj
    temp = weather.get_temperature(unit="celsius") #returns temp obj
    icon = weather.get_weather_icon_name()
    minTemp = temp["temp_min"]
    maxTemp = temp["temp_max"]
    currentTemp = temp["temp"]
    temp = [currentTemp, minTemp, maxTemp]
    humidity = weather.get_humidity()   #Gets humidity
    windSpeed = weather.get_wind()["speed"] #gets wind speed m/s
    status = weather.get_status() #gets quick weather status
    sunTime = [weather.get_sunrise_time(), weather.get_sunset_time()]

    #Select background colors:
    if (time.time() <= sunTime[0] or time.time() > sunTime[1]):
        color = ["1A237E", "212121"]    #night
    elif (time.time() > sunTime[0] and time.time() <= sunTime[1]):
        color = ["B3E5FC", "29B6F6"]  #day
    else:
        color = ["FFFFFF", "FFFFFF"]    #blank
    
    weather = {}
    weather["date"] = currentDate
    weather["location"] = location
    weather["temps"] = temp
    weather["humidity"] = humidity
    weather["windSpeed"] = windSpeed
    weather["status"] = status
    weather["icon"] = icon
    weather["color"] = color
   
    return weather


def start():
    setConfig()
    run(host='0.0.0.0', port=8080)

start()

#TODO: write gpio class that sets up the board, pins etc
#   Finish setLED method
