from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import threading 
import multiprocessing
import certifi
import sys

link="https://www.wuxiaworld.co/Hail-the-King/"
link1=Request(link,headers={'User-Agent': 'Mozilla Firefox 64.0'})
page=urlopen(link1, cafile=certifi.where()).read()
soup=BeautifulSoup(page,"lxml")
soup=soup.find("div" , {"id":"list"})
soup=soup.find_all('a')
print(soup)
string=[""]*len(soup)
incomplete=[]
file=open("Hail-the-King.txt",'w')
#print(soup[0].get('href'))
def thread(a,b):
	try:
		for link_number in range (a,b):
			
			link2=Request(link+soup[link_number].get('href'),headers={'User-Agent': 'Mozilla Firefox 64.0'})
			#print(soup[link_number])
			global num
			page=urlopen(link2, cafile=certifi.where()).read()
			soup2=BeautifulSoup(page,"lxml")
			soup2=soup2.find("div",{"id":"content"})
		#	for script in soup2(["script", "style"]):
		#		    script.extract()    # rip it out
		#	text = soup2.get_text()
		#	lines = (line.strip() for line in text.splitlines())
		#	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		#	text = '\n'.join(chunk for chunk in chunks if chunk)
		#	text=text+'\n\n\n\n\n\n\n'
			print(str(soup[link_number])+"end"+str(link_number))
			string[a]=(''.join(str(soup2)))
	finally:
		incomplete.append(a)
jobs = []
for i in range(len(soup)):
	out_list = list()
	threads = threading.Thread(target=thread,args=(i,i+1)) 
	#process = multiprocessing.Process(target=thread,args=(i,i+1))
	jobs.append(threads)

# Start the threads (i.e. calculate the random number lists)
for j in jobs:
	j.start()

# Ensure all of the threads have finished
'''for j in jobs:
	print("end")
	j.join()
'''
print ("List processing complete.")

## wait until all threads finish 

try_number=0
flag=1
while (flag==1):
	try_number+=1
	time.sleep(10)
	flag=0
	for chapter_number in range (1,len(soup)):
		if(string[chapter_number]==''):
			print("incomplete "+str(chapter_number)+"try:"+str(try_number))
			threads = threading.Thread(target=thread,args=(chapter_number,chapter_number+1)) 
			threads.start()
			jobs.append(threads)	 
			flag=1
			continue
	
for chapter_number in range (1,len(soup)):
	file.write(string[chapter_number]+"\n\n\n")
file.close()
sys.exit()