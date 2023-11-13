import re
import scrapy


class PsplusSpider(scrapy.Spider):
    name = "psplus"

    start_urls = [
        "https://www.playstation.com/en-us/ps-plus/games/",
    ]

    def parse(self, response):
        selector = "div.tabs__tab-content div.txt-block-paragraph p.txt-style-base a::attr(href)"
        yield from response.follow_all(selector, callback=self.parse_images)

    def parse_images(self, response):
        img_urls = list(
            filter(
                lambda link: not re.search("(ratings|thumb=true)", link),
                response.css("img::attr(src)").getall(),
            )
        )
