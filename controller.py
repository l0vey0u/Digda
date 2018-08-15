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
            if atkList.contains('xss'):
                atkFlag += 1
            if atkList.contains('sqli'):
                atkFlag += 2
            if atkList.contains('dirlist'):
                atkFlag += 4
            self.atkFlag = atkFlag
            self.fuzzData = dump
        print(dump)
    
    def needCrawl(self):
        dump = self.fuzzData
        if dump['url']:
            if dump['param']:
                return False
            else:
                return True
        else:
            raise Exception("URL Data Missing")
        return True
    
    def fuzzIt(self):
        dump = self.fuzzData
        try:
            if self.needCrawl():
                dump['formSet'] = Crawler(url).crawlParam()
                dump.pop('method')
                dump.pop('param')
            else
                dump['formSet'] = [{dump.pop('method'):dump.pop('param')}]
        except Exception as err:
            print(err)

        atkFlag = self.atkFlag
        print(dump)
        return
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
c = Controller()
c.readQueue()
c.fuzzIt()