class ConsoleCommander:
    cmd = None
    def __init__(self, cmdDict):
        self.cmdDict = cmdDict
        self.cmd = ''
        self.PromptCommand()
    
    def PromptCommand(self):
        try:
            self.cmd = input('\nPlease enter a command: ').lower()
        except NameError:#only applies to linux environment
            print('You did not enter \" before and after your command. Try again.')
            self.PromptCommand()
        print('You entered - ', self.cmd)
        self.ProcessCommand()
    
    def ProcessCommand(self):
        if(self.cmd == 'exit'):
            print('Have a great day!')
        elif(self.cmd == 'help'):
            for key in self.cmdDict.keys():
                print('\n\r' + key + ',')
            self.PromptCommand()
        else:
            try:
                self.cmdDict[self.cmd]()
                self.PromptCommand()
            except KeyError:
                print('Command not recognized. Please try again.')
                self.PromptCommand()