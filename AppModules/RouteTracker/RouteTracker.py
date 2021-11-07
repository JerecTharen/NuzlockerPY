from DAL.JSON.RouteDAL import RouteDAL

class RouteTracker:
    def __init__(self):
        self.routeDAL = RouteDAL()
        self.routeList = self.routeDAL.GetRoutesFromJson()
        #initialize routelist if not created yet
        if(type(self.routeList) != type([])):
            self.routeList = []
    
    def AddRoute(self):
        routeName = input('What is the route name: ')
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
        return self.routeList.index(routeName) > -1

    def ListRoutes(self):
        routeListString = 'These routes have been added: \n\r'
        for route in self.routeList:
            routeListString += (route + ',\n\r')
        print(routeListString)
