# -*- coding: utf-8 -*-
import scrapy
from car.items import CarItem

class CarSpiderSpider(scrapy.Spider):
    name = 'car_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/4851.html#pvareaid=3454438']

    def parse(self, response):
        datas = response.xpath("//div[@class='column grid-16']/div[@class='uibox']")[1:]
        for data in datas:
            cate = data.xpath(".//div[@class='uibox-title']/a[1]/text()").get().strip()
            urls = data.xpath(".//ul/li/a/img/@src").getall()
            urls = list(map(lambda url:response.urljoin(url),urls))

            print("=" * 30)
            print(cate)
            print("=" * 30)
            item = CarItem(cate=cate,urls=urls)
            yield item
