soup.a  
soup.p.attrs 
soup.p.name
soup.p.get('class')
soup.p['class']
soup.p.string

soup.p.contents
soup.head.children
soup.descendants
soup.strings
soup.stripped_strings

soup.find_all(href=re.compile("elsi"),id='link1')
soup.find_all("a",class_="sister",limit = 2, recursive = False) #返回列表
soup.find_all(attrs={"data-foo":"value"})
soup.find_all(text=re.compile('dormouse'))


soup.select('title')#return:list
soup.select('p #link1')
soup.select('p a[href=""]')
soup.select('.transaction li')
soup.select('.content li')


