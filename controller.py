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

    def fuzzIt(self):
        # 실제 fuzz 컨트롤

