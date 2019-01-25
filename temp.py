from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

file=open("bringing_the_farm_to_live_in_another_world1.txt",'w')
basic_link_novelupdates="https://wuxiaworld.online/bringing-the-farm-to-live-in-another-world/chapter-"


for page_no in range (180,919):
	link=Request(basic_link_novelupdates+str(page_no),headers={'User-Agent': 'Mozilla Firefox 64.0'})
	page=urlopen(link).read()
	soup=BeautifulSoup(page,"lxml")
	soup=(soup.find("div", {"id": "content"}))
	# for script in soup(["script", "style"]):
	# 	    script.extract()    # rip it out
	text=''.join(str(s) for s in soup.contents)
	text='\n'.join(text.split('<br/>'))
	# text = soup.get_text()
	# lines = (line.strip() for line in text.splitlines())
	# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# text = '\n'.join(chunk for chunk in chunks if chunk)
	text="c"+str(page_no) + " : \n" +text+'\n\n\n\n\n\n\n'
	file.write(text)

file.close()
