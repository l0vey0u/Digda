import core.fuzzer

class SQLi(core.fuzzer.Fuzzer):
    
    def __init__(self, key, fuzzData):
        super().__init__(key, fuzzData, 'sqli')
    
    def checkVuln(self, respList):
        report = []
        for respSet in respList:
            isVuln = False
            # sql 은 뭘 체크하지..?
            for payl, resp in respSet.items():
                if payl in resp.text:
                    isVuln = True
            report.append({'payl':payl,'resInfo':[resp.status_code, isVuln]})
        return report

