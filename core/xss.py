import core.fuzzer

class XSS(core.fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(key, fuzzData, 'xss')
    
    def checkVuln(self, respList):
        report = []
        for respSet in respList:
            isVuln = False
            for payl, resp in respSet.items():
                if payl in resp.text:
                    isVuln = True
            duration = int(resp.elapsed.total_seconds()*1000)
            report.append({'payl':payl,'resInfo':[resp.status_code, duration, isVuln, resp.text]})
        return report
