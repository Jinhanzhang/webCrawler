import scrapy

from product_scraper.items import Product
from scrapy.spiders import SitemapSpider, Rule

class SitemapSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = ['https://www.allrecipes.com/sitemap.xml']
    sitemap_rules = [
        ('/recipe/', 'parse_product')
    ]

    def parse_product(self, response):
        item = Product()
        item['name'] = response.xpath("//h1[contains(@class,'headline') and contains(@class,'heading-content')]/text()").get()
        ingredients = response.xpath("//input[@data-tracking-label='ingredient clicked']")
        ingredients_obj = []
        ingredients_list = ''
        for ingredient in ingredients:
            ingredient_obj = {
                'name': ingredient.xpath(".//@data-ingredient").get(),
                'qty': ingredient.xpath(".//@data-quantity").get(),
                'unit': ingredient.xpath(".//@data-unit").get(),
            }
            ingredients_obj.append(ingredient_obj)
            ingredients_list = ingredients_list + ingredient_obj['name'] + ','
        item['ingredients'] = ingredients_obj
        item['ingredients_list'] = ingredients_list
        item['description'] = response.xpath("//li[contains(@class,'instructions-section-item')]//div//p/text()").getall()
        item['img_url'] = response.xpath("//div[contains(@class,'primary-media-with-filmstrip')]//div//noscript//img/@src").get(0)
        item['label'] = response.xpath("//li[@class='breadcrumbs__item'][3]//a/span/text()").get()
        # item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        # item['title'] = response.xpath('//section[1]//h2/text()').get()
        # item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        return item