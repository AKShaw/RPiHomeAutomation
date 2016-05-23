import picamera

class Stream():
    """This class gets the data from the camera and returns it as bytes"""
    def __init__(self):
        pass

    def getData(self):
        """This sets up the pi cam and automatically closes it"""
        with picamera.PiCamera() as camera:
            """This sets the IM class to the im object"""
            im = IM()
            camera.resolution=(640,480)
            """Writes the image to the im instance"""
            camera.capture(im, format="jpeg")
            print("Printing image file...")
            return im.read()

class IM:
    """This class is used to mimic a file handler without actually writing to and from the disk"""
    def __init__(self):
        """Sets the file attribute to a bytes type"""
        self.file = bytes()

    def write(self, data):
        """Writes the data parsed in (from the cam) to file"""
        self.file = data

    def read(self):
        """Returns the cam data as bytes""" 
        return self.file

    
            
        
