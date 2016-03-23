class Thermostat():
    def __init__(self, target, roomTemp, heatingStatus):
        self.target=target
        self.roomTemp=roomTemp
        self.heatingStatus = heatingStatus


    @property
    def getTarget(self):
        return self.target

    def setTarget(self, value):
        self.updateHeating(self.roomTemp, value)
        self.target = value

    @property
    def getRoomTemp(self):
        return self.roomTemp

    def setRoomTemp(self, value):
        self.updateHeating(value, self.target)
        self.roomTemp = value

    @property
    def getHeatingStatus(self):
        return self.heatingStatus

    def updateHeating(self, room, target):
        if (room >= target):
            self.heatingStatus = "OFF"
        elif (room < target):
            self.heatingStatus = "ON"
