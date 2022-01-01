import json
import os

class RouteDAL:
    def __init__(self):
        self.isWindows = None
        try:
            fs = open('/Data/DataREADME.txt', 'r')
            fs.close()
            self.isWindows = True
            self.SetWindowsPath()
        except IOError:
            self.isWindows = False
            self.SetLinuxPath()

    def SetWindowsPath(self):
        self.jsonPath = '/Data/Routes.json'
    
    def SetLinuxPath(self):
        self.jsonPath = os.getcwd() + '/../../Data/Routes.json'
    
    def IsRoutesJsonCreated(self):
        try:
            fs = open(self.jsonPath, 'r')
            fs.close()
        except:
            return False
        return True

    def WriteRoutesToJson(self, routesList):
        #delete the file if it exists so that data is not duplicated
        if(self.IsRoutesJsonCreated()):
            os.remove(self.jsonPath)
        fs = open(self.jsonPath, 'a')
        fs.write(json.dumps(routesList))

    def GetRoutesFromJson(self):
        if(self.IsRoutesJsonCreated()):
            fs = open(self.jsonPath, 'r')

            #need to separate things out after loading data so that we can close the data stream in context
            stringData = fs.read()
            parsedData = json.loads(stringData)
            fs.close()
            return parsedData
        else:
            return []
    
