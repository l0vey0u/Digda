import fuzzer

class XSS(fuzzer.Fuzzer):
    
    def __init__(self, fuzzData):
        super().__init__(fuzzData, 'xss')
    
    def checkVuln(self):
        pass

xss = XSS()
print(xss.fuzz())
