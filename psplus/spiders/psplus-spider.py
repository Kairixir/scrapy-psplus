import re
import scrapy

from urllib.parse import urlparse, urljoin


class PsplusSpider(scrapy.Spider):
    name = "psplus"

    start_urls = [
        "https://www.playstation.com/en-us/ps-plus/games/",
    ]

    def parse(self, response):
        selector = "div.tabs__tab-content div.txt-block-paragraph p.txt-style-base a::attr(href)"
        yield from response.follow_all(css=selector, callback=self.parse_images)

    def parse_images(self, response):
        img_urls = [
            urljoin(response.url, link) if not urlparse(link).scheme else link
            for link in filter(
                lambda link: not re.search("(ratings|thumb=true)", link),
                response.css("img::attr(src)").getall(),
            )
        ]
        title = "".join(
            s.lower()
            for s in response.css("title::text").get(default="").strip()
            if s.isalnum()
        )

        yield {"image_urls": img_urls, "unique_prefix": title}
