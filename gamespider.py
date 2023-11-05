import scrapy
class GamingSpider(scrapy.Spider):
    name = "Game"
    page_number = 2
    start_urls = ["https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1"]

    def parse(self, response):
        total_pages = response.css("span.psw-fill-x::text").getall()
        for products in response.css("section.psw-product-tile__details.psw-m-t-2"):
            yield{
                "Title": products.css("span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text").get(),
                "Price (Rp)": products.css("span.psw-m-r-3::text").get().replace("Rp\xa0",""),
            }

        next_page = "https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/" + str(self.page_number) + "/"
        if self.page_number <= int(total_pages[-1]):
            self.page_number += 1
            yield response.follow(next_page, self.parse)