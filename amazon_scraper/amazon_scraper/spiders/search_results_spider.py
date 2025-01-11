import scrapy
from amazon_scraper.items import AmazonSearchResultItem

class SearchResultsSpiderSpider(scrapy.Spider):
    def __init__(self, search_term="Dog toy", *args, **kwargs):
        self.search_term = search_term
        super(SearchResultsSpiderSpider,self).__init__(*args, **kwargs)

    name = "search_results_spider"
    # Check for user-defined search term
    

    allowed_domains = ["amazon.com"]
#    start_urls = [f"https://www.amazon.com/s?k={self.search_term}"]

    def start_requests(self):
        search_url =f"https://www.amazon.com/s?k={self.search_term}"
        yield scrapy.Request(search_url, self.parse)

    def parse(self, response):
        single_search_result = AmazonSearchResultItem()
        results = response.css('.s-result-item')
        for result in results:
            product_name = result.css('.a-link-normal h2 span ::text').get()
            rating = result.css('i[data-cy="reviews-ratings-slot"] span ::text').get()
            price = result.css('span.a-offscreen ::text').get()

            if product_name and rating and price:
                single_search_result['product_name'] = product_name.strip()
                single_search_result['rating'] = rating.strip()
                single_search_result['price'] = price.strip()
                yield single_search_result
        
        next_page = response.css('a.s-pagination-next ::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

