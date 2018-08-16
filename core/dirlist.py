import fuzzer

class DirList(fuzzer.Fuzzer):
    
    def __init__(self, fuzzData):
        super().__init__(fuzzData, 'dirl')
    
    def checkVuln(self, respList):
        pass
