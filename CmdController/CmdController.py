class CmdController:
    def __init__(self):
        self.cmdDict = {}
    
    def RegisterCmd(self, cmdName, cmd):
        self.cmdDict[cmdName] = cmd

    def GetCmdDict(self):
        return self.cmdDict