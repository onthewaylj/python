import scrapy
from scrapy import Item, Field
class CourseItem(Item):
	#课程标题
	title = Field()
	#课程url
	url = Field()
	#课程标题图片
	image_url = Field()
	#课程描述
	introduction = Field()
	#学习人数
	student = Field()
	#图片地址
	image_path = Field()


