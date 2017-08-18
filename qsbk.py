# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import lxml
import re

class QSBK:
	"""抓取糗事百科热门段子
	
	每按enter一次显示一条，q/Q退出
	"""

	#定义一些变量
	def __init__(self):
	     self.pageIndex = 1
	     #存储段子，元素为每页的段子列表
	     self.stories = []
	     #存放程序是否继续运行的变量
	     self.enable = False
	     self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	


	def getPageContent(self,pageIndex):
		"""
		返回指定页的所有段子序列
		"""
		url = "https://www.qiushibaike.com/8hr/page/{pageIndex}/"
		response = requests.get(url, self.headers)
		if response.status_code != 200:
			print '页面加载失败。。。'
			return None
		soup = BeautifulSoup(response.text, 'lxml')
		infos = []
		details = soup.select('#content-left .article')	#段子列表	
		for detail in details:
			detail = str(detail)
			soup = BeautifulSoup(detail, 'lxml')
			
			if soup.find('.thumb'):#带图片的
				continue
			elif soup.find('.contentForAll'):#字太多，内容在详情页
				continue
			else:
				info = {}# 写成[]就变成序列了，序列的键值只能为数字
				info['nickname'] = re.sub('\s','',soup.select('.author h2')[0].text)#去掉空格等\t\n
				info['content'] = re.sub('\s','',soup.select('.content span')[0].text)# 要追踪到文字的上层标签
				info['vote'] = soup.select('.stats-vote .number')[0].text
				infos.append(info)
		return infos
	

	def loadPage(self):
		"""加载并提取页面的内容，加入到列表中

		"""
		if self.enable == True:
			#如果当前未看的页数少于两页，加载新一页
			if len(self.stories) < 2:
				#获取新一页
				pageStories = self.getPageContent(self.pageIndex)
				
				if pageStories:
					self.stories.append(pageStories)
					#页码加一
					self.pageIndex += 1




	def getOneStory(self,pageStories,page):
		"""
		每次显示一条段子
		"""
		for story in pageStories:
			userin = raw_input()
			#用户输入后，判断是否要加载新页面
			self.loadPage()
			if userin.lower() == 'q':#输入q/Q退出
				self.enable = False
				return
			print u"第{0}页\t发布人：{nickname}\t 内容：{content}\t点赞数：{vote}".format(page,**story)

	def start(self):
		print(u"正在读取糗事百科，按回车键查看段子，Q键退出")
		self.enable = True
		#先加载一页内容 类里面调用方法要写self.
		self.loadPage() 
		#局部变量 控制当前读到第几页
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:				
				nowPage += 1
				#删除第一个元素，并将其返回
				pageStories =  self.stories.pop(0)
				self.getOneStory(pageStories,nowPage)
		





spider = QSBK()
spider.start()			
