import picamera

class Stream():
    def __init__(self):
        pass

    def getData(self):
        with picamera.PiCamera() as camera:
            with open("image", "w+b") as im:
                #camera.resolution=(640,480)
                #camera.capture(im, format="jpeg")
                im.write("test")
                print("Printing image file...")
                print (im.read())
                return im.read()
            
        
