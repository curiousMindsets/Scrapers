import scrapy


class SearchResultsSpiderSpider(scrapy.Spider):
    name = "search_results_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=bluetooth+speaker"]

    def parse(self, response):
        pass
