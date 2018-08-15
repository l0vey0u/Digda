import requests
from bs4 import BeautifulSoup
import json

class Crawler:
    paramList = []
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        try:
            self.parsedHtml, self.header = self.parseHtml(self.url, self.session)
        except Exception as err:
            print(err)
            
    def parseHtml(self, url, session):
        res = session.post(url)
        # Reload Page
        if not res.ok:
            res = session.post(url)
        if not res.ok:
            raise Exception('Can\'t load website :: '+str(res.status_code))
        res.encoding = 'utf-8'
        html = res.text
        parsedHtml = BeautifulSoup(html, 'html.parser')
        if parsedHtml.find('meta', attrs={'http-equiv':'refresh'}):
            metaTag = parsedHtml.find('meta', attrs={'http-equiv':'refresh'})
            prefix = metaTag['content'].index('url') + 4
            urlPostFix = metaTag['content'][prefix:]
            return self.parseHtml(url+urlPostFix, session)
        return parsedHtml, res.headers
        
    def crawlParam(self):
        formSet = []
        formDump = self.parsedHtml.find_all('form')
        for form in formDump:
            method = form.get('method')
            if method is None:
                method = 'post'
            inputDump = form.find_all('input')
            param = {}
            for inputElem in inputDump:
                input_type = inputElem.get('type')
                nameTag = inputElem.get('name')
                # TODO radio같은 애들 처리를 어떻게 해주지
                if input_type is None or input_type == 'submit':
                    continue
                if name is None : continue
                nameTag = nameTag.encode("utf-8")
                param[nameTag]='Dig'
            formSet.append({method:param})
        return formSet
            

        