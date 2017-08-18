from scrapy.exceptions import DropItem
import json

class MyPipeline(object):
	def __init__(self):
		self.file = open('data.json','w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line)
		return item

	def open_spider(self, spider):
		pass

	def close_spider(self, spider):
		pass
