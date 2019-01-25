'''
-------
pattern:
	python3 trimming_general_using_threading.py <<wuxiaworld.co/ ((argv))/>>
-------

'''

import sys
import threading
import time
from urllib.request import Request, urlopen

import certifi
from bs4 import BeautifulSoup

link = sys.argv[1]
link1 = Request(link + "all.html", headers={'User-Agent': 'Mozilla Firefox 64.0'})
page = urlopen(link1, cafile=certifi.where()).read()
soup = BeautifulSoup(page, "lxml")
soup = soup.find("div", {"id": "chapterlist"})
soup = soup.find_all('a')
print(soup)
string = [""] * len(soup)
incomplete = []
file = open("output files/" + sys.argv[1][sys.argv[1][:-1].rfind("/") + 1:-1] + ".txt", 'w')


# print(soup[0].get('href'))
def thread(a, b):
    try:
        for link_number in range(a, b):
            link2 = Request(link + soup[link_number].get('href'), headers={'User-Agent': 'Mozilla Firefox 64.0'})
            # print(soup[link_number])
            global num
            page = urlopen(link2, cafile=certifi.where()).read()
            soup2 = BeautifulSoup(page, "lxml")
            soup2 = soup2.find("div", {"id": "chaptercontent"})
            #	for script in soup2(["script", "style"]):
            #		    script.extract()    # rip it out
            #	text = soup2.get_text()
            #	lines = (line.strip() for line in text.splitlines())
            #	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            #	text = '\n'.join(chunk for chunk in chunks if chunk)
            #	text=text+'\n\n\n\n\n\n\n'
            print(str(soup[link_number]) + "end" + str(link_number))
            string[a] = (''.join(str(soup2)))
    finally:
        incomplete.append(a)


jobs = []
for i in range(1, len(soup)):
    out_list = list()
    threads = threading.Thread(target=thread, args=(i, i + 1))
    # process = multiprocessing.Process(target=thread,args=(i,i+1))
    jobs.append(threads)

# Start the threads (i.e. calculate the random number lists)
for j in jobs:
    j.start()

# Ensure all of the threads have finished
'''for j in jobs:
	print("end")
	j.join()
'''
print("List processing complete.")

## wait until all threads finish

try_number = 0
flag = 1
while (flag == 1):
    try_number += 1
    time.sleep(3)
    flag = 0
    for chapter_number in range(1, len(soup)):
        if (string[chapter_number] == ''):
            print("incomplete " + str(chapter_number) + "try:" + str(try_number))
            threads = threading.Thread(target=thread, args=(chapter_number, chapter_number + 1))
            threads.start()
            jobs.append(threads)
            flag = 1
            continue

for chapter_number in range(0, len(soup)):
    file.write(string[chapter_number] + "\n\n\n")
file.close()
sys.exit()
'''Traceback (most recent call last):
  File "/usr/lib/python3.6/multiprocessing/process.py", line 258, in _bootstrap
    self.run()
  File "/usr/lib/python3.6/multiprocessing/process.py", line 93, in run
    self._target(*self._args, **self._kwargs)
  File "trimming-Ze-Tian-Ji.py", line 26, in thread
    page=urlopen(link2).read()
  File "/usr/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.6/urllib/request.py", line 526, in open
    response = self._open(req, data)
  File "/usr/lib/python3.6/urllib/request.py", line 544, in _open
    '_open', req)
  File "/usr/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.6/urllib/request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/usr/lib/python3.6/urllib/request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)>

TO REMOVE THIS ERROR I HAVE USED certifi
'''
