from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
link="https://m.wuxiaworld.co/Paradise-of-Demonic-Gods/"
link1=Request(link+"all.html",headers={'User-Agent': 'Mozilla Firefox 64.0'})
page=urlopen(link1).read()
soup=BeautifulSoup(page,"lxml")
soup=soup.find("div" , {"id":"chapterlist"})
soup=soup.find_all('a')
print(soup)
file=open("Paradise-of-Demonic-Gods.txt",'w')
#print(soup[0].get('href'))
for link_number in range (1,len(soup)):
	print(soup[link_number])
	time.sleep(2)
	link2=Request(link+soup[link_number].get('href'),headers={'User-Agent': 'Mozilla Firefox 64.0'})


	page=urlopen(link2).read()
	soup2=BeautifulSoup(page,"lxml")
	soup2=soup2.find("div",{"id":"chaptercontent"})
#	for script in soup2(["script", "style"]):
#		    script.extract()    # rip it out
#	text = soup2.get_text()
#	lines = (line.strip() for line in text.splitlines())
#	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#	text = '\n'.join(chunk for chunk in chunks if chunk)
#	text=text+'\n\n\n\n\n\n\n'
	file.write(''.join(str(soup2)))
file.close()

