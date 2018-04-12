import sys

#taking as command line argument
argument = sys.argv[1]

#opening file 
f = open(argument, "r")

#reading all lines
lines = f.readlines()

#again opening file from different pointer
fp = open(argument,"r")

#counting total number of lines
num_lines = sum(1 for line in fp)
 
tags=list()   #list in which all the tags will be stored 
checktags=list()    #list in which all the opening tags will be stored and when closing tags come these are compared
ok=0
notok=0     #variable which will tell if the tags like <abc/> are in the range a-z or A-Z.
#Loop to store all the tags in the list named 'tags'
for pp in range(2,num_lines+1):                 #reading every line
	linelen = len(lines[pp-1])
	
	for ll in range(1,linelen+1):           #reading through all the words in a line
		if(lines[pp-1][ll-1]=='<'):     #when we encounter opening < then-
			donot=0		#variable to store if we need to add the tag to list or not -> like <xyz/> will not be added.
			notadd=0	#variable to store if we need to add more character or not->like <abc id=1> will add only abc.
			name = list()		#list to store the tags and then appended to main list 'tags'
			br = ll-1
			br=br+1
			ch = lines[pp-1][br]     
			
			if(ch=='/'):                    #if it is a closing tag
				name.append(ch)
				br=br+1
				ch=lines[pp-1][br]				
             #run the loop till we do not encounter '>'
			while (ch!='>'):
				if(ch=='/'):                 #condition to deal with case like <xyz/>  
					donot=donot+1				
				if(ch==' '):		     #condition to deal	with case like <xyz id=1>
					notadd=notadd+1	
				if(notadd==0):
					name.append(ch)
				br=br+1
				ch = lines[pp-1][br]
			if donot==0:			
				newname=''.join(name)		#making the character array a string
				tags.append(newname)		#appending to the main list
			else:
				newname=''.join(name)
				if (newname.isalpha()):
					ok=1
				else:
					notok=1

totaltags=len(tags)  #total number of tags in the list

def2=0   #check for the condition 2 given in the question
def3=0  #check for the condition 3 given in question

elem1=tags[0]
elem2=tags[totaltags-1][1:]

if(elem1!=elem2):                           #if there is no single root that contains all the elements then condition 3 is violated
	def3=1

#Loop to check if the tag name contains only a-z or A-Z
for pp in range(1,totaltags+1):
	notletters=0     #variable to store if all are letter or not
	letters=0
	taglen=len(tags[pp-1])
	
	if(tags[pp-1][0]=='/'):                #if it is closing tag
		newstri = tags[pp-1]
		newstr = newstri[1:]
		if newstr.isalpha(): 		#isalpha return 1 if all are between a-z or A-z
			letters=1
		else:
			notletters=notletters+1 	#updating notletters variable to 1
	else:
		if tags[pp-1].isalpha():
			letters=1
		else:
			notletters=notletters+1

	if (notletters!=0):  #if not letters
		def2=1       #violating condition 2
		break

ind=0
def1=0  #check for the condition 1 given in question

if(notok==1):
	def1=1

#loop to check the nesting , overlapping and missing of any begin,end and empty element tags.
for pp in range(1,totaltags+1):
	if(tags[pp-1][0]=='/'):
		newstr=tags[pp-1][1:]
		
		if(len(checktags)==0):     #if the begin tags ended before the end tags
			def1=1             #condition 1 is violated
			break	
#if both the begin and end tag of element matched then remove the begin tag from checklist
		if(newstr==checktags[ind-1]):
			checktags.pop()
			ind=ind-1
		else:			#condition 3 is violated
			def1=1
			break
		
	else:
		checktags.append(tags[pp-1])
		ind=ind+1

#if all the three are not violated then print 'well formed' otherwise 'not well formed'.
if (def1==0 and def2==0 and def3==0):
	print "well formed"

else:
	print "Not well formed"
	if(def1==1 or def2==1):
		print "\nReason : Either of Condition 1 or 2 is violated"
	if(def3==1):
		print "\nReason : There is no single root element"
	if(notok==1):
		print "The empty element contains character out of range of a-z or A-Z\n"
