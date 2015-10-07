from nltk import word_tokenize
import nltk
import sys,re
import itertools
from nltk.corpus import brown

list2=["its","it's","they're","their","you're","your","to","too","loose","lose","It's","Its","They're","Their","To","Too","Loose","Lose"]
i=0
list_new=[]
outfile= sys.argv[1]

foname=open(outfile,'w')
list_new=brown.tagged_words() 
for i in range(0,len(list_new)):
 l1= list(list_new[i])
 #if l1[0] in list2:
 foname.write(l1[0])
 foname.write("/")
 foname.write(l1[1])
 foname.write(" ")
 
foname.close()


