import sys
import os
try:
    #Windows can run this without issue
    from ConsoleCommander.ConsoleCommander import ConsoleCommander
    from CmdController.CmdController import CmdController
    from DAL.JSON.RouteDAL import RouteDAL
    from AppModules.RouteTracker.RouteTracker import RouteTracker
    from ConsoleHelpers.PrintHelper import PrintHelper
except:
    #My Ubuntu environment needs this
    print('The application is being run on a Linux environment.')
    print('It must be run as \"python ./index.py\" instead of \"python index.py\"')
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.getcwd() + '/ConsoleHelpers')
    from PrintHelper import PrintHelper
    sys.path.append(os.getcwd() + '/ConsoleCommander')
    from ConsoleCommander import ConsoleCommander
    sys.path.append(os.getcwd() + '/CmdController')
    from CmdController import CmdController
    sys.path.append(os.getcwd() + '/DAL/JSON')
    from RouteDAL import RouteDAL
    sys.path.append(os.getcwd() + '/AppModules/RouteTracker')
    from RouteTracker import RouteTracker
    print('All inputs must begin and end with a \" or it will crash.')



# pylint: disable=expected
PrintHelper.PrintBanner('Hello There. Welcome to PokeNucklockerPy!')
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
cmdController.RegisterCmd('reset routes', routeTracker.ResetRoutes)


#Stand handling input
consoleCommander = ConsoleCommander(cmdController.GetCmdDict())


#this is a test comment