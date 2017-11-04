import scrapy
from amazon.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
  		name = "AmazonDeals"
  		#allowed_domains = ["amazon.com"]
  
  #Use working product URL below
  		start_urls = ["https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes"]
 
  		def parse(self, response):
  			items = AmazonItem()
  			title = response.xpath('//a[@class ="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@title').extract()
  			sale_price = response.xpath('//span[@class ="a-size-base a-color-price s-price a-text-bold"]/@text').extract()
  			items['product_name'] = ''.join(title).strip()
  			items['product_sale_price'] = ''.join(sale_price).strip()
  			yield items