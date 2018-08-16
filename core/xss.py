import core.fuzzer

class XSS(core.fuzzer.Fuzzer):
    
    def __init__(self, fuzzData):
        super().__init__(fuzzData, 'xss')
    
    def checkVuln(self):   
        pass

