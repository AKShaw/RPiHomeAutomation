class RGBLED():
    def __init__(self, red, green, blue, status, sense):
        self.red = red
        self.green = green
        self.blue = blue
        self.status = status
        self.sense = sense
        self.updateLight(red, green, blue, status)

    @property
    def getRed(self):
        return self.red

    def setRed(self, value):
        self.red = value

    @property
    def getBlue(self):
        return self.blue

    def setBlue(self, value):
        self.blue = value

    @property
    def getGreen(self):
        return self.green

    def setGreen(self, value):
        self.green = value

    @property
    def getStatus(self):
        return self.status

    def setStatus(self, value):
        self.status = value

    def updateLight(self, red, green, blue, status):
        rgb = [red, green, blue]
        if status==1:
            self.sense.clear(rgb)
        elif status==0:
            self.sense.clear(0,0,0)
