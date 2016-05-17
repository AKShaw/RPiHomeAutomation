class GetConfig():
    def __init__(self):
        self.lines=self.loadConfigFile()
        self.lat=self.findCoords(self.lines)[0]
        self.long=self.findCoords(self.lines)[1]
                            
    def loadConfigFile(self):
        f = open("config.txt", "r")
        lines=f.readlines()
        f.close()
        return lines
            
    def findCoords(self, lines):
        s1 = lines[0]
        lat = s1[s1.index("lat=") + len("lat="):]
        s2 = lines[1]
        long = s2[s2.index("long=") + len("long="):]
        return lat, long
        
    @property
    def getLat(self):
        return self.lat
            
    @property
    def getLong(self):
        return self.long

class SaveConfig():
    def __init__(self, lat, long):
        print("Saving config")
        self.createData(lat, long)

    def writeConfigFile(self, data):
        f = open("config.txt", "w")
        f.write(data)
        print("Data wrote")
        f.close()

    def createData(self, lat, long):
        data = "lat="+str(lat)+"\nlong="+str(long)
        print("Writing Data")
        self.writeConfigFile(data)
        

    
	
		
