import json
import os

class RouteDAL:
    def __init__(self):
        self.jsonPath = './Data/Routes.json'
    
    def IsRoutesJsonCreated(self):
        try:
            fs = open(self.jsonPath, 'r')
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
            return json.loads(fs.read())
        else:
            return []
    
