import fuzzer

class XSS(fuzzer.Fuzzer):
    
    def __init__(self):
        super().__init__('xss')

    def fuzz(self):
        pass
    
    def parseReq(self):
        pass
    
    def checkVuln(self):
        pass

xss = XSS()
