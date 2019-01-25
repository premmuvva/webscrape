"""

give_number is a program to give the chapter name to the text where it is missing 
either due to author or improper trimming of website 

FORMAT:
python3 give_number.py <<file_name>> <<chapter separating text or string>>
python3 give_number.py <<file_name>> <<new_file_name>> <<chapter separating text or string>>

"""
"""
progress:
edit 1: ackword naming of type file.txt(new)
edit 2: currently not able to print , dont know where the error is
edit 3: 
"""
import sys

def main():

	f = open(sys.argv[1], "r")
	if(len(sys.argv)<4):
		fi = open(sys.argv[1][:-4]+"(new).txt", "w")
		seperator=sys.argv[2]
	else:
		fi=open(sys.argv[2],'w')
		seperator=sys.argv[3]
	num=1
	for line in f.readlines():
		if(seperator in line):
			print(line)
			line.replace(seperator,(seperator+"\n\n\nchapter : "+str(num)+"\n"))
			num+=1
			fi.write(line)
			continue
		fi.write(line)

	"""# dig = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	    # if (not (("www.asianovel.com"in line or "Translator Notes" in line or "NOTES:" in line or line[0] == '-' or (line[0] == '[' and (line[2] == ']'or line[3] == ']')) or "Notes:" in line or "Footnotes:" in line) or (line[0] in dig and ':' not in line))):
	    #     fi.write(line)

	    # if (not(#("Chapter" in line and len(line)<15) )):or
	    # 	 ("					 					 						    " in line and len(line)==25))) :
	    # 	fi.write(line)

	    # if(line[i][len(line[i])-2] == '.' or line[i][len(line[i])-2]=='"'or line[i][len(line[i])-2]=='?'):
	    # 	fi.write(line[i])
	    # 	continue

	    # fi.write(line[i][:len(line[i])-1])
	    # while line[i+1]=='\n':
	    # 	i=i+1
	    # fi.write(line[i])

	    if(not("  " in line[i] and len(line[i])<=6)):
		fi.write(line[i])

	    # if(not("Chapter " in line[i] and len(line[i])<=12)):
	    #     fi.write(line[i])

	    # if ((line[i][0]>='a'and line[i][0]<='z')or(line[i][0]>='A'and line[i][0]<='Z')or line[i][0]==' 'or line[i][0]=='"'or line[i][0]=='\n'or line[i][0]=='*'):
	    #     fi.write(line[i])

	     # if(line[0]=='-'||line[0]=='['||"Notes:"in line||"Footnotes:"in line||"Previous Chapter | Project Page | Next Chapter" in line||"Bringing A Farm To Mess Around In Another World" in line):
	     # 	continue
	     # f1.write(''.join( c for c in line if  c not in '?:./.' ))
	"""
	f.close()
	fi.close()

if __name__ == "__main__":
   main()
