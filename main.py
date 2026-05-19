from scrapy.crawler import CrawlerProcess
from scrapy_spiders.books_spider import BooksSpider

process = CrawlerProcess(settings={
    "FEEDS": {
        "cleaned_data/products.json": {
            "format": "json",
            "overwrite": True,
        },
    },
})

process.crawl(BooksSpider)
process.start()