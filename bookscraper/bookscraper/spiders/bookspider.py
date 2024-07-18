import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            yield{
                'name':book.css('h3 a::text').get(),
                'price':book.css('p.price_color::text').get(),
                'url':book.css('h3 a::attr(href)').get(),
            }
        next_page = response.css('.next a::attr(href)').get()

        if next_page is not None:
            if next_page[0:9] == 'catalogue':
                next_page_url = 'https://books.toscrape.com/'+ next_page 
                yield response.follow(next_page_url,callback = self.parse)
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/'+next_page
                yield response.follow(next_page_url,callback = self.parse)
        