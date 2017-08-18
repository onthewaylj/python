#encoding:utf-8
import urllib
import re

def getHtml(url):
	f = urllib.urlopen(url)
	html = f.read()
	return html

def getImage(html):
	pattern = r'src="(.+?\.gif)"'
	imglist = re.findall(pattern, html)
	num = 0
	for i in imglist:

		urllib.urlretrieve(i, './ceshi/%s.jpg' % num)#是个相对路径需转为绝对路径
		num += 1;


html = getHtml("http://www.cnblogs.com/SeekHit/p/6089397.html")
print getImage(html)



