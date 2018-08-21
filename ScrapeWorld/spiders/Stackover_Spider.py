from scrapy import Spider
from scrapy.selector import Selector
from ScrapeWorld.items import ScrapeworldItem

class StackoverSpider(Spider):
    name = "StackOverFlow"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?pagesize=50&sort=newest"]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = ScrapeworldItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = f"""www.stackoverflow.com{question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]}"""
            yield item
