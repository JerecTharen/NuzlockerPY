try:
    from DAL.JSON.RouteDAL import RouteDAL
except:
    #My Ubuntu environment needs this
    import sys
    import os
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.getcwd() + '/DAL/JSON')
    from RouteDAL import RouteDAL

class RouteTracker:
    def __init__(self):
        self.routeDAL = RouteDAL()
        self.routeList = self.routeDAL.GetRoutesFromJson()
        #initialize routelist if not created yet
        if(type(self.routeList) != type([])):
            self.routeList = []
    
    def AddRoute(self):
        routeName = str(input('What is the route name: '))
        isDuplicate = self.DetectRoute(routeName)
        if(self.DetectRoute(routeName)):
            print('That route has already been added!')
        else:
            self.routeList.append(routeName)
            self.routeDAL.WriteRoutesToJson(self.routeList)
            print('Added route - ', routeName)

    def FindRoute(self):
        routeName = input('What route are you looking for: ')
        if(self.DetectRoute(routeName)):
            print('Route found!')
        else:
            print('Route not found . . .')
    
    def DetectRoute(self, routeName):
        self.routeList = self.routeDAL.GetRoutesFromJson()
        try:
            self.routeList.index(routeName) > -1
        except:
            return False
        return True

    def ListRoutes(self):
        routeListString = 'These routes have been added: \n'
        for route in self.routeList:
            routeListString += (route + ',\n')
        print(routeListString)
        
    def ResetRoutes(self):
        self.routeList = []
        self.routeDAL.WriteRoutesToJson(self.routeList)
        print('Routes have been reset.')
