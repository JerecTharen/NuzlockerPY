from ConsoleCommander.ConsoleCommander import ConsoleCommander

print('Hello There. Welcome to PokeNucklockerPy!')
def testFunc():
    print('Test successful')
cmdDict = {"test": testFunc}

consoleCommander = ConsoleCommander(cmdDict)