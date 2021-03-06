#DEPENDENCIES:
#   bottle
#   pyowm
#   sensehat
#   jquery
#   bootstrap
#   cherrypy
#   picamera
#   test

#Special imports
from bottle import *
from sense_hat import SenseHat
import pyowm

#general imports
import platform
import sys
import os
import calendar
import time
import threading
from datetime import date

#Imports from classes written by myself
from config import *
from board import Board
from lcd import SetLCD
from led import RGBLED
from pir_buzzer import PirBuzzer
from btn_buzzer import BtnBuzzer
from thermostat import Thermostat
from photoresistor import PhotoResistor
from stream import Stream

#Initilize all the required classes and create an instance
"""Setting up all of the instances of classes, this is an example of OOP"""
board = Board()
sense = SenseHat()
lcd = SetLCD("", "", board)
therm = Thermostat(20, 0, 0, 0, "OFF")
rgbled = RGBLED(128, 128, 128, 1, sense)
luxSensor = PhotoResistor(22, board)
camStream = Stream()
btnbuzz = BtnBuzzer(board, 12, 6)
pirbuzz = PirBuzzer(board, 5, 14)

#Initilize config
def initConfig():
    global config
    config = GetConfig()

#Set static path for files
@route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root='/home/pi/RPiHomeAutomation/www')
    print("Static path set!")
	
"""Routing methods"""
"""These are all event driven as they are only ran when the server receives a request for the routes"""
@route('/<area>')
@route('/')
def index(area="Home"):
    objects = updateObj()
    return template("www/index.tpl", rgb=objects[3], area=area, weather=getWeatherData(pyowm.OWM("18c319fbdc2695c31d05763b053e1753"), float(config.getLat), float(config.getLong)), config=objects[0], lcd=objects[2], temp=objects[1])

@route("/saveConfig", method="POST")
def writeConfig():
    """This gets the lat/long and calls the instance of the writing class"""
    lat=request.forms.get("lat")
    long=request.forms.get("long")
    valid = checkLatLong(lat, long)
    if valid==True:
        saveConfig = SaveConfig(lat, long)
        initConfig()
        redirect("/Config")
    elif valid==False:
        return "<p>Latitude or Longtitude invalid!</p>"

@route("/setLCDScreen", method="POST")
def setLCDScreen():
    """This gets the lines and sets the text on the LCD through the lcd instance (OOP)"""
    firstLine = request.forms.get("line1")
    secondLine = request.forms.get("line2")
    lcd.setLine1(firstLine)
    lcd.setLine2(secondLine)
    redirect("/LCDScreen")

@route("/setTargetTemp", method="POST")
def setTargetTemp():
    """This gets the target temp from the slider, and sets the target property of the therm instance to it. This is an example of OOP"""
    target = request.forms.get("targetSlider")
    therm.setTarget(float(target))
    redirect("/Temperature")

@route("/setLEDs", method="POST")
def setLEDs():
    """This gets the RGB values and the status of the LED panel from the web interface, before setting
    the propertys (OOP) and running the updateLight method which actually sets the new values"""
    red = int(request.forms.get("redSlider"))
    green = int(request.forms.get("greenSlider"))
    blue = int(request.forms.get("blueSlider"))
    status = int(request.params.get("onOff"))
    rgbled.setRed(red)
    rgbled.setGreen(green)
    rgbled.setBlue(blue)
    rgbled.setStatus(status)
    rgbled.updateLight(red, green, blue, status)
    redirect("/Lighting")

@route("/camFeed")
def camFeed():
    """This gets the image from the getData method of the camStream instance (OOP)"""
    im = camStream.getData()
    return im

"""End of routing methods"""

"""Normal methods"""
def updateObj():
    """This method is responsable for updating all the sensor information.
    This is ran every time a new page is requested from the server (Event driven) and this makes sure
    the data displayed on the web interface is always up to date (with the last refresh/page load).
    This method creates a blank array before populating it directly from the instance properties."""
    configObj = {}
    configObj["lat"] = config.getLat
    configObj["long"] = config.getLong

    updateRoom()
    tempObj = {}
    tempObj["target"]= therm.getTarget
    tempObj["roomTemp"] = therm.getRoomTemp
    tempObj["roomPressure"] = therm.getRoomPressure
    tempObj["roomHumidity"] = therm.getRoomHumidity
    tempObj["heating"] = therm.getHeatingStatus

    lcdScreenObj = {}
    lcdScreenObj["firstLine"] = lcd.getLine1
    lcdScreenObj["secondLine"] = lcd.getLine2

    rgbObj = {}
    rgbObj["red"]=rgbled.getRed
    rgbObj["green"]=rgbled.getGreen
    rgbObj["blue"]=rgbled.getBlue
    rgbObj["status"]=rgbled.getStatus
    rgbObj["lux"]=luxSensor.getLux()

    return [configObj, tempObj, lcdScreenObj, rgbObj]

def checkLatLong(lat, long):
    """This checks the lattitude and longtidude are valid, which prevents my weather
    API calls returning an error and breaking the program."""
    try:
        if (-90 <= float(lat) <= 90 and -180 <= float(long) <= 180):
            return True
        else:
            return False
    except ValueError:
        return False
    

def getWeatherData(owm, lat, long):
    """This creates a weather object at the specified lat/long containing date, location, temp,
    pressure, humidity, windspeed etc."""
    weather = owm.weather_at_coords(lat, long) #returns observation obj
    date_day_name = calendar.day_name[date.today().weekday()] #get day name
    date_day_num = date.today().day # get day num
    currentDate = [date_day_name, date_day_num] #create date variable
    location = weather.get_location().get_name() #get location name e.g Salisbury
    weather = weather.get_weather() #returns weather obj
    temp = weather.get_temperature(unit="celsius") #returns temp obj
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
    weather["color"] = color
   
    return weather

def checkBtn():
    """This is ran in a thread and is constantly checking if the button is pressed.
    If it is pressed, it runs the buzzer on method."""
    while True:
        if btnbuzz.getBtn():
            btnbuzz.buzz_off()
        else:
            btnbuzz.buzz_on()

def updateRoom():
    """This method gets the data from the sensehat and sets the propertys of the therm
    instance to them."""
    therm.setRoomTemp(int(sense.temp))
    therm.setRoomHumidity(int(sense.humidity))
    therm.setRoomPressure(int(sense.get_pressure()))

def start():
    """This method starts the whole program. It creates the global config variable, updates the room,
    starts the button/buzzer thread and starts the server."""
    initConfig()
    updateRoom()
    print("Starting button thread...")
    t = threading.Thread(target=checkBtn)
    t.start()
    print("Starting server...")
    run(host='0.0.0.0', port=8080, server="cherrypy")
    print("All started")

start()
