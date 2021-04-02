from scrapy import Spider, Request

class QuotesSpider(Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for entry in response.css("div.quote"):
            text = entry.css("span.text::text").get()
            author = entry.css("small.author::text").get()
            author_url = entry.css("span a::attr(href)").get()
            tags = entry.css("a.tag::text").getall()
            yield {
                "text": text[1:-1],
                "author": author,
                "author_url": author_url,
                "tags": tags
            }

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield Request(url=next_page_url, callback=self.parse)