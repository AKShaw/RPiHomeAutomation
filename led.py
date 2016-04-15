class RGBLED():
    def __init__(self, red, green, blue, status):
        self.red = red
        self.green = green
        self.blue = blue
        self.status = status

    @property
    def getRed(self):
        return self.red

    def setRed(self, value):
        self.red = value

    @property
    def getBlue(self):
        return self.Blue

    def setBlue(self, value):
        self.Blue = value

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
