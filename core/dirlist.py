import fuzzer

class DirList(fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(key, fuzzData, 'dirl')
    
    def fuzz(self):
        pass
    
    def checkVuln(self):
        pass
