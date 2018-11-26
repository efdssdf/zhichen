# coding=utf-8

import scrapy
from scrapy.selector import Selector

headers = {
    'Host': 't25097.jiangsuyinhang.com',
    'Connection':'keep-alive',
    'Content-Length':43,
    'Accept':'*/*',
    'Origin':'http://t25097.jiangsuyinhang.com',
    'User-Agent':'Mozilla/5.0(Linux;Android 7.1.1;OPPO R11s Build/NMF26X;wv)AppleWebKit/537.36(KHTML,like Gecko)Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044307 Mobile Safari/537.36 MMWEBID/8365 MicroMessenger/6.7.3.1360(0x2607033A) NetType/WIFI Language/zh_CN Process/toolsContent-Type: application/x-www-form-urlencoded;charset=UTF-8',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Referer':'http://t25097.jiangsuyinhang.com/index.php/cms/index/booklist/?from=groupmessage&isappinstalled=0',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,en-US;q=0.8',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'PHPSESSID=5nb0isk8a4b8k33oagjaur9vs2;UM_distinctid=1674d8b9f0c134-0b7dd71b1a92eb-27485c58-3f480-1674d8b9f0d135;CNZZDATA1253007811=1227586348-1543193919-%7C1543193919;CNZZDATA1275441066=1270912696-1543193739-%7C1543193739'
}
l = []
res = ""

class QuotesSpider(scrapy.Spider):
    name = "zhichen"

    def start_requests(self):
        global token
        global headers
        global l

        yield scrapy.FormRequest(
            url = "http://t25097.jiangsuyinhang.com/index.php/cms/api/getbook",
            headers = headers,
            formdata = {'start':'0','limit':'10','fenlei':'0','order':'zhishu+desc'},
            callback = self.parse
        )
        # url = 'http://t25097.jiangsuyinhang.com/index.php/cms/index/booklist/?from=groupmessage&isappinstalled=1'
        # url = 'http://t25097.jiangsuyinhang.com/index.php/cms/index/detail/id/191020.html'
        # yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print(response.body)
        # global res

        # data = response.body
        # content = Selector(text=data).xpath('//body/div[@class="read_body read_body_fontsize_"]/div[@class="read_content_list"]/div[@class="read_main_box"]/div[@class="read_main_p"]').extract()
        # c = content[0].replace("<br>\xa0\xa0\xa0\xa0","\r\n")
        # res = "###"+c[c.find('</p>')+20:c.find('</div>')]+"\r\n"
        # print(res)
        # fiename = './test.txt'
        # with open(fiename, 'a') as f:
        #     f.write(res)
        # next_url = Selector(text=data).xpath('//body/div[@class="read_body read_body_fontsize_"]/div[@class="read_content_list"]/div[@class="read_main_other_box"]/a/@data-url').extract()
        # url = 'http://t25097.jiangsuyinhang.com'+next_url[0]
        # yield scrapy.Request(url=url,callback=self.parse)


