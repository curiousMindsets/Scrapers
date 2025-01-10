import scrapy


class SingleItemSpiderSpider(scrapy.Spider):
    name = "single_item_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/JBL-Ultra-Portable-Waterproof-Dustproof-Built/dp/B0CTNWBT1Z/"]

    def parse(self, response):
        product_name = response.css('span#productTitle::text').get().strip()
        price = response.css('.aok-offscreen::text').get().strip()
        images = response.css('#altImages img::attr(src)').getall()
        description_items = response.css('#feature-bullets .a-list-item::text ').getall()
        description = ' '.join([item.strip() for item in description_items if item.strip()])
        reviews = response.css('ul#cm-cr-dp-review-list li.review')
        reviews_list = []

        for review in reviews:
            rating = review.css('.review-rating ::text').get().strip()
            title = review.css('.review-title span:nth-of-type(2) ::text').get().strip()
            body = review.css('.review-text span ::text').get().strip()
            review_dict = {
                "Rating" : rating,
                "Title" : title,
                "Body" : body,
            }

            reviews_list.append(review_dict)


        yield {
            'Product Name' : product_name,
            'Price' : price,
            'Images' : images,
            'Description' : description,
            'Reviews' : reviews_list,
        }