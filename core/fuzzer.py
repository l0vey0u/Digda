# Abstract Base Class
from abc import *
import sys
import json
import os

class Fuzzer(metaclass=ABCMeta):
    __key = 0
    __fuzzList = []
    _atkType = ''

    def __init__(self, key, fuzzData, _atkType):
        self.__key = key
        self.fuzzData = json.load(fuzzData)
        self.loadDict()

    def loadDict(self):
        __dictPath = os.getcwd()+"/core/dict/"+self._atkType
        try:
            for item in os.scandir(__dictPath):
                __dictFile = open("./core/dict/"+self._atkType+"/"+item.name) 
                self.__fuzzList += __dictFile.read().splitlines()
                # Remove Duplicated Payload
                self.__fuzzList = list(set(self.__fuzzList))
        except IOError as ferr:
            print(ferr)
        except Exception as err:
            print(err)

    @abstractmethod
    def fuzz(self):
        pass

    @abstractmethod
    def checkVuln(self):
        pass
    
    def exportResult(self):
        # TO DO : Implement
        pass
