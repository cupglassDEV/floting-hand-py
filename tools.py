import os
import platform as pf

class osTools():
    def __init__(self):
        self.onOs = None
        self.edition = None
    
    def getSys(self):
        self.onOs = pf.system()
        return self.onOs
    
    def clearConsole(self):
        systems = self.getSys()
        def funcClear():
            if systems == "Windows":
                return os.system("cls")
            elif systems == "Linux":
                return os.system("clear")
            elif systems == "Darwin":
                return os.system("printf '\\33c\\e[3J'")
            
        clear = lambda: funcClear()
        clear()