import scrapy
import re

from typing import Iterator


class PsstoreSpider(scrapy.Spider):
    name = "psstore"
    custom_settings = {"ITEM_PIPELINES": {"psplus.pipelines.PsStorePipeline": 300}}
    allowed_domains = ["store.playstation.com"]

    # N should be equal to number of pages in psstore
    N = 349

    start_urls = [
        f"https://store.playstation.com/en-us/pages/browse/{n}" for n in range(1, N + 1)
    ]

    def parse(self, response):
        img_urls = filter(
            lambda link: not re.search("(ratings|thumb=true)", link),
            response.css("div.psw-game-art__container img::attr(src)").getall(),
        )
        titles = response.css("div.psw-product-tile span.psw-t-body::text").getall()
        titles = map(
            lambda title: "".join(c.lower() for c in title if c.isalnum()), titles
        )

        yield {"image_urls": [next(img_urls)], "title": next(titles)}
