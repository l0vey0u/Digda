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
        paramList = []
        formDump = self.parsedHtml.find_all('form')
        for form in formDump:
            method = form.get('method')
            if method is None:
                method = 'post'
            

        