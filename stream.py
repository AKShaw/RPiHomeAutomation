import picamera

class Stream():
    def __init__(self):
        pass

    def getData(self):
        with picamera.PiCamera() as camera:
            with IM()as im:
                camera.resolution=(640,480)
                camera.capture(im, format="jpeg")
                print("Printing image file...")
                return im.read()

class IM:
    def __init__(self):
        self.file = bytes()

    @property
    def write(self, data):
        self.file = data

    def read(self):
        return self.file

    
            
        
