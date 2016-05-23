class Thermostat():
    """This class stores the temp, target temp, humidity, pressure and heating status"""
    def __init__(self, target, roomTemp, roomHumidity, roomPressure, heatingStatus):
        self.target=target
        self.roomTemp=roomTemp
        self.heatingStatus = heatingStatus
        self.roomHumidity = roomHumidity
        self.roomPressure = roomPressure

    @property
    def getTarget(self):
        return self.target

    def setTarget(self, value):
        self.updateHeating()
        self.target = value

    @property
    def getRoomHumidity(self):
        return self.roomHumidity

    def setRoomHumidity(self, value):
        self.roomHumidity = value

    @property
    def getRoomPressure(self):
        return self.roomPressure

    def setRoomPressure(self, value):
        self.roomPressure = value

    @property
    def getRoomTemp(self):
        return self.roomTemp

    def setRoomTemp(self, value):
        self.updateHeating()
        self.roomTemp = value

    @property
    def getHeatingStatus(self):
        return self.heatingStatus

    def updateHeating(self):
        """This method decides if the heating should be on or off, dependent on the room temp and target temp"""
        if (self.roomTemp >= self.target):
            self.heatingStatus = "OFF"
        elif (self.roomTemp < self.target):
            self.heatingStatus = "ON"
