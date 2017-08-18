import scrapy
from scrapytest.CourseItems import CourseItem

class MySpider(scrapy.Spider):

	name = "MySpider"
	allowed_domains = ['imooc.com']
	start_urls = ['http://www.imooc.com/course/list']

	def parse_item(self, response):
		item = CourseItem()
		for box in response.xpath("//div[@class='course-card-container']/a"):
			item['title'] = box.xpath(".//h3[@class='course-card-name']/text()").extract()[0]
			item['student'] = box.xpath(".//div[@class='course-card-info']/span[2]/text()").extract()[0]
			item['img_url'] = box.xpath(".//div[@class='course-card-top']/img[@src]").extract()[0]
			item['introduction'] = box.xpath(".//p[@class='course-card-desc']/text()").extract()[0]
			yield item

		#url跟进 获取下一页url信息
		url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
		if url:
			#将信息组合成下一页的url
			page = 'http://www.imooc.com' + url[0]
			yield scrapy.Request(page, callback=self.parse_item)



