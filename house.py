#coding:utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import json


def generate_allurl(user_in_number): #生成url
	url = "https://bj.lianjia.com/zufang/changping/pg{}l2/"
	for url_next in range(1,int(user_in_number)):
		yield url.format(url_next)   #返回生成的所有url


def get_allurl(generate_allurl): #分析url解析出每一页的详细url
	get_url = requests.get(generate_allurl, 'lxml',allow_redirects=False)#? lxml
	if get_url.status_code == 200:
		re_set = re.compile('<li.*?class="info-panel".*?<a.*?href="(.*?)"')
		re_get = re_set.findall(get_url.text)
		return re_get  #返回urllist 


def open_url(re_get): #分析详细url获取信息
	res = requests.get(re_get)
	if res.status_code == 200:
		info = {}
		soup = BeautifulSoup(res.text, 'lxml')

		info['价钱'] = soup.select(".total")[0].text# + soup.select(".unit")[0].text
		info['描述'] = soup.select("span[class='tips decoration']")[0].text #soup.find("span",_class="tips decoration")[0].text
		re_pat = re.compile('</?\w+[^>]*?>') 
		details = soup.select(".zf-room p")
		for detail in details:
			detail = str(detail)# 转类型 bs4.element.Tag ==>str
			if '</i>' in detail: 
			    key, value = detail.split('</i>')
			    info[re_pat.sub('',key)] = re_pat.sub('',value) # 去掉html标签
			    
			 
		
		return info

def pandas_to_xlsx(info):
	pd_look = pd.DataFrame(info)
	# 表名等前面不加u会提示 ValueError:worksheet titles must be unicode
	pd_look.sort_values(by=['价钱','时间：'])#待验证？？
	pd_look.to_excel(u'链家昌平二居室租房信息.xlsx', sheet_name=u'链家昌平二居室')

def write_to_text(info): #中文无法正常显示
	with open('链家租房.txt','a') as f:
		f.write(json.dumps(info))

def main():
 	user_in_number = input("输入页数：")
 	infos = []
 	for get_url in generate_allurl(user_in_number):
 		re_get = get_allurl(get_url)	
 		for perurl in re_get:
 			info = open_url(perurl) #解析每个详情页
 			infos.append(info)


 	pandas_to_xlsx(infos)
 	#write_to_text(infos)

if __name__ == '__main__':
	 main()
#proxy = {'http:':''}
## request.get('url',headers=,proxies=proxy)
