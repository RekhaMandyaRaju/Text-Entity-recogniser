from nltk import word_tokenize
import nltk
import sys,re
import itertools

i=0
dict_new={}
trainfile= sys.argv[1]
outfile= sys.argv[2]

foname=open(outfile,'w')
finame=open(trainfile,'r')

for line in finame:
 line=line.decode('utf-8').strip()
 list1=line.split() 
 dict_new=dict(nltk.pos_tag(list1)) 
 for key,value in dict_new.items():
  foname.write(key)
  foname.write("/")
  foname.write(value)
  foname.write(" ")
finame.close()
foname.close()


