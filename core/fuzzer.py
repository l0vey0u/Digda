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

    def __init__(self, key, fuzzData, _atkType):
        self.__key = key
        self.fuzzData = json.loads(fuzzData)
        self._atkType = _atkType
        self.loadDict()

    def loadDict(self):
        __dictPath = os.getcwd()+"/core/dict/"+self._atkType
        try:
            for item in os.scandir(__dictPath):
                __dictFile = open("./core/dict/"+self._atkType+"/"+item.name, errors='ignore') 
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
        cookie = self.fuzzData['cookie']
        header = self.fuzzData['header']
        sess = requests.Session()
        respList = []
        for form in formSet:
            for method, paramDict in form.items():
                for fuzzPayl in self.__fuzzList:
                    payl = {}
                    for k, v in paramDict.items():
                        postfix = v.index('Dig')
                        payl[k] = v[:postfix] + fuzzPayl
                    try:
                        resp = self.req(method, sess, url, payl, cookie, header)
                        respList.append({fuzzPayl:resp})
                    except Exception as err:
                        print(err)
        return respList


    def req(self, method, sess, url, payl, cookie, header):
        if method == 'get':
            return sess.get(url=url, params=payl, cookies=cookie, headers=header)
        elif method == 'post':
            return sess.post(url=url, data=payl, cookies=cookie, headers=header)
        else:
            raise Exception("Method is NOT GET or POST")

    @abstractmethod
    def checkVuln(self, respList):
        pass
    
    def exportResult(self, result):
        __destPath = os.getcwd()+"/result/"+str(self.__key)
        if not os.path.exists('result'):
            os.mkdir('./result')
        if not os.path.exists('result/'+str(self.__key)):
            os.mkdir('./result/'+str(self.__key))
        with open(__destPath+"/"+self._atkType+'.json', 'w') as out:
            json.dump(result, out)
        if not os.path.exists('./result/'+str(self.__key)+'/queueInfo.txt'):
            infoFile = open(__destPath+"/queueInfo.txt", "w")
            infoFile.write("URL="+self.fuzzData['url'])
