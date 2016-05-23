class GetConfig():
    """This class reads the config.txt file and returns the latitude and longtitude"""
    def __init__(self):
        self.lines=self.loadConfigFile()
        self.lat=self.findCoords(self.lines)[0]
        self.long=self.findCoords(self.lines)[1]
                            
    def loadConfigFile(self):
        """This opens the file and returns an array which each entry containing 1 line"""
        f = open("config.txt", "r")
        lines=f.readlines()
        f.close()
        return lines
            
    def findCoords(self, lines):
        """This splits the lines and isolates the latitude and longtitude floats"""
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
    """This class creates rhe data and writes it to the config file"""
    def __init__(self, lat, long):
        self.createData(lat, long)

    def writeConfigFile(self, data):
        """Writes the data to the config file"""
        f = open("config.txt", "w")
        f.write(data)
        f.close()

    def createData(self, lat, long):
        """This method takes the lat/long floats and creates a string out of them, before writing it"""
        data = "lat="+str(lat)+"\nlong="+str(long)
        self.writeConfigFile(data)
        

    
	
		
