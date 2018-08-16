import core.fuzzer

class XSS(core.fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(fuzzData, 'xss')
    
    def checkVuln(self, respList):
        for respSet in respList:
            isVuln = False
            for payl, resp in respSet.items():
                if payl in resp.text:
                    isVuln = True
            respSet['isVuln'] = isVuln
        return respList


