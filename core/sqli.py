import fuzzer

class SQLi(fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(key, fuzzData, 'sqli')
    
    def fuzz(self):
        pass
    
    def checkVuln(self):
        pass
