# Abstract Base Class
from abc import *
import sys
import json
import os
import requests

class Fuzzer(metaclass=ABCMeta):
    __key = 0
    __fuzzList = []
    _atkType = ''

    def __init__(self, fuzzData, _atkType):
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

    def fuzz(self):
        formSet = self.fuzzData['formSet']
        url = self.fuzzData['url']
        sess = requests.Session()

        respList = []
        for form in formSet:
            for method, paramDict in form.items():
                for k, v in paramDict.items():
                    postfix = v.index('Dig')
                    for fuzzPayl in self.__fuzzList:
                        payl = v[:postfix] + fuzzPayl
                        try:
                            resp = self.req(method, sess, url, payl)
                            respList.append({payl:resp})
                        except Exception as err:
                            print(err)
        return respList


    def req(self, method, sess, url, payl):
        if method == 'get':
            return sess.get(url=url, params=payl)
        elif method == 'post':
            return sess.post(url=url, data=payl)
        else:
            raise Exception("Method is NOT GET or POST")

    @abstractmethod
    def checkVuln(self):
        pass
    
    def exportResult(self):
        # TO DO : Implement
        pass
