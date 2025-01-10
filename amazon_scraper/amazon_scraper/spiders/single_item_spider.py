import scrapy


class SingleItemSpiderSpider(scrapy.Spider):
    name = "single_item_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/JBL-Ultra-Portable-Waterproof-Dustproof-Built/dp/B0CTNWBT1Z/"]

    def parse(self, response):
        pass
