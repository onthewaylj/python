#encoding:utf-8
#######  test 1 ###### 
# x = int(raw_input("please enter an integer: "))
# if x<0:
# 	x=0
# 	print 'negative changed to zero'
# elif x==0:
# 	print 'zero'
# elif x==1:
# 	print 'single'
# else:
# 	print 'more'


####### test 2 for ###### 
# words = ['cat','window','avdfsesw']
# for w in words[:]:
# 	if len(w) > 6 :
# 		words.insert(0,w)

# print words


###### test3 break; 连接符号 逗号###### 
# for n in range(2,10):
# 	for i in range(2,n):
# 		if n% i == 0:
# 			print n,' equals ',i,' * ',n/i
# 			break;

# 	else:
# 		print n ,'is a prime number'


###### test4 continue  末尾加分号也可以，写成else也可以###### 
# for i in range(2,10):
# 	if i%2 == 0:
# 		print i ,' is an even number'
# 		continue
# 	print "find a number",i

####函数##########
# def fib(n):
# 	a,b = 0,1
# 	result = []
# 	while a<n:
# 		result.append(a)
# 		a,b = b,a+b
# 	return result


# print fib(10)

# def ask_ok(prompt,retries=4,complaint='yes or no,please!'):
# 	while True:
# 		ok = raw_input(prompt)
# 		if ok in ('y', 'ye', 'yes'):
# 			return True
# 		if ok in ('n', 'no', 'nope', 'nop'):
# 			return False
# 		retries = retries -1
# 		if retries<0:
# 			raise IOError('refusenik user')
# 		print complaint

# #ask_ok('Do you really want to quit?')
# ask_ok('Ok to overwrite the file?',2,'come on ,only yes or no')


####参数 可以使用 ** 操作符分拆关键字参数为字典##########
# def parrot(voltage,state='a stiff', action='voom'):
# 	print "-- This parrot wouldn't",action,
# 	print "if you put ",voltage,"wolts through it.",
# 	print "E's",state,"!"

# d  = {"voltage":"param1","state":"param2","action":'param3'}
# parrot(**d)

##############**name *name 参数################################
# def cheeseshop(kind,*arguments, **keywords):
# 	print "-- Do you have any",kind,"?"
# 	print "-- I'm sorry,we're all out of ",kind
# 	for arg in arguments:
# 		print arg
# 	print "-" * 40
# 	keys = sorted(keywords.keys())
# 	for kw in keys:
# 		print kw,":", keywords[kw]

# cheeseshop("orange","It's a param","It's a param too",a="hhh",b='jjj',c='kkk')

#################参数####################
# for x in range(1,11):
# 	print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)

# print 'the {food} is {good}'.format(food='egg',good='goodvalue')



################自定义异常####################
# class MyError(Exception):
# 	def __init__(self, value):
# 		self.value = value
# 	def __str__(self):
# 		return repr(self.value)

# try:
# 	raise MyError(2*2)
# except MyError as e:
# 	print 'my exception occurred,value:',e.value

##########除法异常###########
# def divide(x, y):
# 	try:
# 		result = x / y
# 	except ZeroDivisionError:
# 		print 'division by zero'
# 	else:
# 		print 'result is ',result
# 	finally:
# 		print("executing finally clause")

############类##############
# class MyClass:
# 	""" A simple example class"""
# 	i = 123
# 	def __init__(self, realpart, imagpart):
# 		self.r = realpart
# 		self.i = imagpart
# 	def f(self):
# 		return 'hello world'

#########urllib2 smtplib###################
# import urllib2
# for line in urllib2.urlopen('http://www.baidu.com')
# 	line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#     	print line

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('fromll@qq.com','toll@qq.com',
# 	"""To:toll@qq.com
# 	From:fromll@qq.com

# 	beware the ides of march
	
# 	""")
# server.quit()


######################
# def average(values):
# 	"""computes the arithmetic mean of a list of numbers.

# 	>>>print average([20,30,70])
# 	40
# 	"""
# 	return sum(values,0.0) / len(values)


##########template############
# import pprint
# t = [[[['black','cyan'],'white',['green','red']],[['magent','yellow'],'blue']]]
# pprint.pprint(t,width=40)

######textwrap######
# import textwrap
# doc=""" The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines.
# """
# print textwrap.fill(doc,width=40)
###########substitute safe_substitute##########
# from string import Template
# t = Template('${village}folk send $$10 to $cause')
# t.substitute(village='Notting', cause='the ditch fund')


#######更改图片名#######
# import time,os.path
# photefiles = ['img_100.jpg','img_101.jpg','img_102.jpg']
# class BatchRename(Template):
# 	delimiter = '%'

# fmt = input('enter rename style (%d-date %n-seqnum %f-format):')
# t = BatchRename(fmt)
# data = time.strftime('%d%b%y')#'24Jul17'
# for i, filename in enumerate(photefiles):#0, img_100.jpg
# 	base, ext = os.path.splitext(filename)#img_100 , .jpg
# 	newname = t.substitute(d=date, n=i,f=ext)
# 	print('{0}---------->{1}'.format(filename,newname))


##########os模块########
# import os
# print os.getcwd() #获得当前路径
# print os.listdir('/home/show')
# print os.mkdir('hhh')
# print os.rmdir('c')
# print os.rename('abc.txt','readme.txt')

##########sys模块########
# import sys
# print 'Name is :',sys.argv[0]
# print "path has ",sys.path #查找模块所在目录的目录名列表。

# 使用sys模块查找内建模块

# def dump(module):
# 	print module, '=>',
# 	if module in sys.builtin_module_names:
# 		print "内建模块"
# 	else:
# 		module = __import__(module)
# 		print module.__file__

# dump('os')
# dump('sys')
# dump('string')
# dump('zlib')
