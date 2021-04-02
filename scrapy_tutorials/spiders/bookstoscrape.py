from scrapy import Spider, Request

class BooksSpider(Spider):
    name = "books"
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for entry in response.css("article.product_pod"):
            title = entry.css("h3 a::attr(title)").get()
            url = entry.css("a::attr(href)").get()
            stars = entry.css("p.star-rating::attr(class)").get()
            price = entry.css("p.price_color::text").get()
            in_stock = entry.css("p.instock::text").extract()[1].strip()
            yield {
                "title": title,
                "url": url,
                "stars": stars,
                "price": price,
                "in_stock": in_stock
            }

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield Request(url=next_page_url, callback=self.parse)