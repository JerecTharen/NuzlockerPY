from ConsoleCommander.ConsoleCommander import ConsoleCommander
from CmdController.CmdController import CmdController
from DAL.JSON.RouteDAL import RouteDAL
from AppModules.RouteTracker.RouteTracker import RouteTracker

# pylint: disable=expected
print('Hello There. Welcome to PokeNucklockerPy!')
cmdController = CmdController()
routeTracker = RouteTracker()

#Command Handlers
def testFunc():
    print('Test successful')

#Registered Routes
cmdController.RegisterCmd('test', testFunc)
cmdController.RegisterCmd('add route', routeTracker.AddRoute)
cmdController.RegisterCmd('find route', routeTracker.FindRoute)
cmdController.RegisterCmd('list routes', routeTracker.ListRoutes)


#Stand handling input
consoleCommander = ConsoleCommander(cmdController.GetCmdDict())