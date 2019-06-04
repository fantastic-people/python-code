from urllib import request

class Spider():
    url= 'https://www.douyu.com/topic/xyb01?rid=272065'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding =('utf-8'))
        print(htmls)

    def analy(parameter_list):
        pass

    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()