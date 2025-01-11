from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# Spaces are urlencoded automatically 
process.crawl("search_results_spider", search_term="Bluetooth headset")
process.start()  # the script will block here until the crawling is finished