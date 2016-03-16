from bottle import *
import platform, sys

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
        return template("www/index.tpl", area=area)

run(host='0.0.0.0', port=80)


#TODO: generate body content dependent on area etc
#       Maybe a seperate .tpl file for each area that is concatenated as a var into the main template?
#       Need to try tomorrow
