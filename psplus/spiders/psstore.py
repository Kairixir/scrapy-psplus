import scrapy


class PsstoreSpider(scrapy.Spider):
    name = "psstore"
    allowed_domains = ["store.playstation.com"]
    start_urls = ["https://store.playstation.com/en-us/pages/browse/1"]

    def parse(self, response):
        pass
