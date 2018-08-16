import fuzzer

class DirList(fuzzer.Fuzzer):
    
    def __init__(self, fuzzData):
        super().__init__(fuzzData, 'dirl')
    
    def fuzz(self):
        pass
    
    def checkVuln(self):
        pass
