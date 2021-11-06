from DAL.JSON.RouteDAL import RouteDAL

class RouteTracker:
    def __init__(self):
        self.routeDAL = RouteDAL()
        test = RouteDAL()
        self.routeList = test.GetRoutesFromJson()
        #initialize routelist if not created yet
        if(type(self.routeList) != type([])):
            self.routeList = []
    
    def AddRoute(self):
        routeName = input('What is the route name: ')
        self.routeList.append(routeName)
        self.routeDAL.WriteRoutesToJson(self.routeList)

    def FindRoute(self):
        routeName = input('What route are you looking for: ')
        if(self.routeList.index(routeName) > -1):
            print('Route found!')
        else:
            print('Route not found . . .')