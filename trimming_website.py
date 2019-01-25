from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def write_into(book,temp):
	file=open(book,'a')
	for script in temp(["script", "style"]):
	    script.extract()    # rip it out
	text = temp.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	text=text+'\n\n\n\n\n\n\n'
	file.write(text)
	file.close()

def extract_and_write(link,book):
	page=urlopen(link).read()
	soup = BeautifulSoup(page, "lxml")
	# temp=BeautifulSoup("")
	if ("moonbunnycafe" in link):
		soup=(soup.find("div", {"id": "content"}))
		soup=soup.find("div", {"class" : "entry-content"})
	else:		
		soup=soup.find("table" , {"id":"myTable"})
		soup=soup.find_all('a',{"class":"chp-release"})
	write_into(book,temp)
	

#basic link struture of the bringing-the-farm-to-live-in-another-world novelupdates 
basic_link_novelupdates="https://www.novelupdates.com/series/bringing-the-farm-to-live-in-another-world/?pg="

#from chapter 1 to 41 from moonbunnycafe by Armored Raven 
basic_link_chap_1_to_41="http://moonbunnycafe.com/bringing-a-farm-to-mess-around-in-another-world/bringing-a-farm-to-mess-around-in-another-world-chapter-"



for chapter in range(1,42):
	page_link=basic_link_chap_1_to_41+str(chapter)+"/"
	link=Request(page_link, headers={'User-Agent': 'Mozilla Firefox 64.0'})	
	extract_and_write(link,"bringing_the_farm_to_live_in_another_world.txt")



# file=open("bringing_the_farm_to_live_in_another_world.txt",'a')
#from chapters 42 to 49 from Trung Nguyen
link=Request(basic_link_novelupdates+str(26),headers={'User-Agent': 'Mozilla Firefox 64.0'})
page=urlopen(link).read()
soup=BeautifulSoup(page,"lxml")
#print(soup[0].get('href'))
for link_number in range (7,-1,-1):
	link2=Request("https:"+soup[link_number].get('href'),headers={'User-Agent': 'Mozilla Firefox 64.0'})
	extract_and_write(link2,"bringing_the_farm_to_live_in_another_world.txt")
	# page=urlopen(link2).read()
	# soup2=BeautifulSoup(page,"lxml")
	# soup2=soup2.find("div",{"class":"post-body entry-content"})
	# for script in soup2(["script", "style"]):
	# 	    script.extract()    # rip it out
	# text = soup2.get_text()
	# lines = (line.strip() for line in text.splitlines())
	# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# text = '\n'.join(chunk for chunk in chunks if chunk)
	# text=text+'\n\n\n\n\n\n\n'
	# file.write(text)

# file.close()

#from chapters 49 to 124 from Trung Nguyen


# file=open("bringing_the_farm_to_live_in_another_world.txt",'a')
initial_page_novelupdates=25
final_page_novelupdates=20
for page in range (initial_page_novelupdates,final_page_novelupdates,-1):
	link=Request(basic_link_novelupdates+str(page),headers={'User-Agent': 'Mozilla Firefox 64.0'})
	page=urlopen(link).read()
	soup=BeautifulSoup(page,"lxml")
	soup=soup.find("table" , {"id":"myTable"})
	soup=soup.find_all('a',{"class":"chp-release"})
	#print(soup[0].get('href'))
	for link_number in range (len(soup)-1,-1,-1):
		link2=Request("https:"+soup[link_number].get('href'),headers={'User-Agent': 'Mozilla Firefox 64.0'})
		extract_and_write(link2,"bringing_the_farm_to_live_in_another_world.txt")

# 		page=urlopen(link2).read()
# 		soup2=BeautifulSoup(page,"lxml")
# 		soup2=soup2.find("div",{"class":"post-body entry-content"})
# 		for script in soup2(["script", "style"]):
# 			    script.extract()    # rip it out
# 		text = soup2.get_text()
# 		lines = (line.strip() for line in text.splitlines())
# 		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# 		text = '\n'.join(chunk for chunk in chunks if chunk)
# 		text=text+'\n\n\n\n\n\n\n'
# 		file.write(text)

# file.close()
