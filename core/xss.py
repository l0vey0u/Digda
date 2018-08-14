import fuzzer

class XSS(fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(key, fuzzData, 'xss')

    def fuzz(self):
        pass
    
    def checkVuln(self):
        pass
