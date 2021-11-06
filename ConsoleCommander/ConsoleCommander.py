class ConsoleCommander:
    cmd = None
    def __init__(self, cmdDict):
        self.cmdDict = cmdDict
        self.PromptCommand()
    
    def PromptCommand(self):
        self.cmd = input('Please enter a command: ').lower()
        print('You entered - ', self.cmd)
        self.ProcessCommand()
    
    def ProcessCommand(self):
        if(self.cmd == 'exit'):
            print('Have a great day!')
        else:
            try:
                self.cmdDict[self.cmd]()
                self.PromptCommand()
            except:
                print('Command not recognized. Please try again.')
                self.PromptCommand()