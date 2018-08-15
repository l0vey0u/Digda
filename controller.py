import core.xss
import core.sqli
import core.dirlist
import json

class Controller:
    def __init__(self):
        self.__key = sys.argv[1]
        self.fuzzData = {}
        self.atkFlag = 0

    def readQueue(self):
        try:
            __sheet = open("./queue/"+self.__key+".json")
        except IOError as ferr:
            print(ferr)
        except Exception as err:
            print(err)
        else:
            dump = json.load(__sheet)
            atkList = dump.pop('atkType')
            atkFlag = 0
            if(atkList.contains('xss'))
                atkFlag += 1
            if(atkList.contains('sqli'))
                atkFlag += 2
            if(atkList.contains('dirlist'))
                atkFlag += 4
            self.atkFlag = atkFlag
            self.fuzzData = dump
    
    def checkStatus(self):
        # 추가 입력값에 대하여 판단후 크롤러에게 정보 넘김
        stat = 0 
        dump = self.fuzzData
        tag = list(dump.keys())
        if tag.contains('url'):
            if tag.contains('method'):
                stat += 2
            if tag.contains('param'):
                stat += 1
        else:
            raise Exception("URL Data Missing")

        return stat
    
    def fuzzIt(self):
        # 실제 fuzz 컨트롤
        try:
            stat = self.checkStatus()
        except Exception as err:
            print(err)
        atkFlag = self.atkFlag

        if stat < 2:
            self.fuzzData['method'] = 'post'
        else:
            stat -= 2
        
        if stat < 1:
            url = self.fuzzData['url']
            self.fuzzData['param'] = Crawler(url).crawlParam()
            
        else:
            print("Status Error")

        # Fuzz!
        if atkFlag >= 4:
            dirl = DirList(self.__key, json.dumps(self.fuzzData))
            atkFlag -= 4
        if atkFlag >= 2:
            sqli = SQLi(self.__key, json.dumps(self.fuzzData))
            atkFlag -= 2
        if atkFlag >=1:
            xss = XSS(self.__key, json.dumps(self.fuzzData))
            atkFlag -=1