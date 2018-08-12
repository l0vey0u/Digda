# Abstract Base Class
from abc import *
import sys
import json

class Fuzzer(metaclass=ABCMeta):
    __key = 0
    __reqInfo = {}
    def __init__(self):
        self.__key = sys.argv[1]
        self.readQueue()
        print(self.__reqInfo)
    @abstractmethod
    def fuzz(self):
        pass

    def readQueue(self):
        __sheet = open("./queue/"+self.__key+".json")
        self.__reqInfo = json.load(__sheet)  

    @abstractmethod
    def parseReq(self):
        pass

    @abstractmethod
    def checkVuln(self):
        pass
    
    def exportResult(self):
        # TO DO : Implement
        pass

class Test(Fuzzer):
    def fuzz(self):
        pass
    def parseReq(self):
        pass
    def checkVuln(self):
        pass

fuzz = Test()
