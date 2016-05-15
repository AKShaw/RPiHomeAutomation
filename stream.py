import picamera

class Stream():
    def __init__(self):
        pass

    def getData(self):
        with picamera.PiCamera() as camera:
            im = open("image", "w+b")
            camera.resolution=(640,480)
            camera.capture(im, format="jpeg")
            print (im.read())
            return im.read()
            
        
