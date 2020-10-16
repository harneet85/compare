import os
import sys

file1=sys.argv[1]
file2=sys.argv[2]

common=[]
uncommon=[]


def comparefiles(file1,file2):
	f2=open(file2,"r")
	with open(file1,"r") as f1:
		for lines in f1:
			for lines2 in f2:
				if lines2.find(lines)==0:
				#	print(file1+":"+lines.strip("\n")+" :in "+file2+":Found")
					found=True
					common.append(lines)

			if not found:
				#print(file1+":"+lines.strip("\n")+" :in "+file2+":NOT")
				uncommon.append(lines)
			found=False
			f2.seek(0)
		f1.seek(0)
	
		for lines2 in f2:
			found2=False
			for lines in f1:
				if lines.find(lines2)==0:
					found2=True		
				
			if not found2:
				#print(file2+":"+lines2.strip("\n")+" :in "+file1+":NOT")
				uncommon.append(lines2)
			f1.seek(0)



comparefiles(file1,file2)


print("\nCommon ones"+str(len(common)))
for i in common:
	print(i.strip("\n"))


print("\nUn-common ones "+str(len(uncommon)))
for i in uncommon:
	print(i.strip("\n"))
