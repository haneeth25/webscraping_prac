import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css('h3 a::attr(href)').get()
            if 'catalogue' in relative_url:
                book_url = 'https://books.toscrape.com/'+relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/'+relative_url
                
            yield response.follow(book_url,callback = self.parse_book_page)


        
        next_page = response.css('.next a::attr(href)').get()

        if next_page is not None:
            if next_page[0:9] == 'catalogue':
                next_page_url = 'https://books.toscrape.com/'+ next_page 
                yield response.follow(next_page_url,callback = self.parse)
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/'+next_page
                yield response.follow(next_page_url,callback = self.parse)

    
    def parse_book_page(self,response):
        table_rows = response.css('.table.table-striped tr')
        book_item = BookItem()
        book_item['url'] = response.url,
        book_item['title']=response.css('.product_main h1::text').get(),
        book_item['product_type']=table_rows[1].css('td::text').get(),
        book_item['price']=table_rows[3].css('td::text').get(),
        book_item['availability'] = table_rows[5].css('td::text').get(),
        book_item['no_of_reviews'] = table_rows[6].css('td::text').get(),
        book_item['rating'] = response.css('.star-rating').attrib['class'],
        book_item['description']= response.xpath("//div[@id = 'product_description']/following-sibling::p/text()").get(),
        yield book_item

        
        
        