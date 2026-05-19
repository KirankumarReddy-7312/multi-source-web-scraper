import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        books = response.css("article.product_pod")

        for book in books:

            title = book.css("h3 a::attr(title)").get()
            price = book.css(".price_color::text").get()

            yield {
                "title": title,
                "price": price
            }