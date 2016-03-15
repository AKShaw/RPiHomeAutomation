from bottle import *
import time

@route("/static/<filepath:path>")
def server_static(filepath):
	return static_file(filepath, root='C:/Users/ashaw/RPiHomeAutomation/www')

@route('/<area>')
def index(area):
    return template("www/index.tpl", area=area)
	
@route("/")
def noRoute():
	return index("")

run(host='localhost', port=8080)


#TODO: generate body content dependent on area etc