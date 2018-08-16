import fuzzer

class SQLi(fuzzer.Fuzzer):
    
    def __init__(self, fuzzData):
        super().__init__(fuzzData, 'sqli')
    
    def checkVuln(self):
        pass
