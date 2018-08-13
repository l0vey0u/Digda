# Abstract Base Class
from abc import *
import sys
import json

class Fuzzer(metaclass=ABCMeta):
    __key = 0
    __reqInfo = {}
    _atkType = ''
    __fuzzList = []
    def __init__(self, _atkType):
        self.__key = sys.argv[1]
        self.readQueue()

    def readQueue(self):
        __sheet = open("./queue/"+self.__key+".json")
        self.__reqInfo = json.load(__sheet)  

    def loadDict(self):
        __dictPath = os.getcwd()+"./core/dict/"+self._atkType
        try:
            for item in os.scandir(__dictPath):
                __dictFile = open("./core/dict/"+item.name) 
                self.__fuzzList += __dictFile.read().splitlines()
                # Remove Duplicated Payload
                self.__fuzzList = list(set(self.__fuzzList))
        except IOError as ferr:
            print(ferr)
        except Exception as err:
            print(err)
        print(self.__fuzzList)

    @abstractmethod
    def parseReq(self):
        pass

    @abstractmethod
    def fuzz(self):
        pass

    @abstractmethod
    def checkVuln(self):
        pass
    
    def exportResult(self):
        # TO DO : Implement
        pass
