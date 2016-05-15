import picamera

class Stream():
    def __init__(self):
        pass

    def getData(self):
        with picamera.PiCamera() as camera:
            im = open("image", "w+")
            camera.resolution=(640,480)
            camera.capture(im, format="jpeg")
            return im.read()
            
        
