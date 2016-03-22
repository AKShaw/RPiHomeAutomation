class GetConfig():
    def __init__(self):
        self.lines=self.loadConfigFile()
        self.lat=self.findCoords(self.lines)[0]
        self.long=self.findCoords(self.lines)[1]
                            
    def loadConfigFile(self):
        f = open("config", "r")
        lines=f.readlines()
        f.close()
        return lines
            
    def findCoords(self, lines):
        s1 = lines[0]
        lat = s1[s1.index("lat=") + len("lat="):]
        s2 = lines[1]
        long = s2[s2.index("long=") + len("long="):]
        lat = lat[0:len(lat)-2] #cut \n off
        return lat, long
        
    @property
    def getLat(self):
        return self.lat
            
    @property
    def getLong(self):
        return self.long

class SaveConfig():
    def __init__(self, lat, long):
        self.createData(lat, long)

    def writeConfigFile(self, data):
        f = open("config", "w")
        f.write(data)
        f.close()

    def createData(self, lat, long):
        data = "lat="+str(lat)+"\nlong="+str(long)
        self.writeConfigFile(data)
        

    
	
		
