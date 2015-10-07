import sys,copy,pickle
import codecs,re

inputfile= sys.argv[1]
outputfile= sys.argv[2]
main_dict={}
new_dict={}
finame=open(inputfile,'rb')
foname=open(outputfile,'w')
main_dict=pickle.load(finame)
sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

for line in sys.stdin:
  str2=''
  list1=[]
  list3=["its","it's","they're","their","you're","your","to","too","loose","lose","It's","Its","They're","Their","To","Too","Loose","Lose"]

  line=''.join(('START ',line.rstrip(), ' END'));
  list1=line.split()
  for i in range(1,len(list1)-1):
   word=list1[i]
   pre="prev_"+list1[i-1]
   nex="nex_"+list1[i+1]
   if(len(list1) > 2):
    suffix3=list1[-3:]
   else:
    suffix3=0
   if(len(list1) > 1):
    suffix2=list1[-2:]
   else:
    suffix2=0
   suf3="suf3_"+str(suffix3)
   suf2="suf2_"+str(suffix2) 
   
   wshape=re.sub('[A-Z]+','A',list1[0])
   wshape=re.sub('[a-z]+','a',wshape)
   wshape=re.sub('[0-9]+','9',wshape)
   wshape=re.sub(r'[^\w_]+','-',wshape)
   ws="wshape_"+wshape  
   
   if list1[i] in list3:
    str1=pre+"  "+nex+"  "+suf3+"  "+suf2+"  "+ws
    dict_clas={}
    list_new=[]
    list2=str1.split()
    if list1[i] == "its" or list1[i] == "it's" or list1[i] == "Its" or list1[i] == "It's":
     list_new=["its","it's","It's"]
    elif list1[i] == "you're" or list1[i] == "You're" or list1[i] == "Your" or list1[i] == "your":
     list_new=["your","you're"]
    elif list1[i] == "loose" or list1[i] == "Loose" or list1[i] == "lose" or list1[i] == "Lose":
     list_new=["lose","loose","Lose","Loose"]
    elif list1[i] == "to" or list1[i] == "too" or list1[i] == "Too" or list1[i] == "To":
     list_new=["to","too","To","Too"]
    elif list1[i] == "their" or list1[i] == "they're" or list1[i] == "Their" or list1[i] == "They're":
     list_new=["their","Their","they're","They're"]
    for k in range(0,len(list_new)):
     total=0
     for j in range(0,len(list2)):
       if list2[j] in main_dict[list_new[k]]:
         total+=main_dict[list_new[k]][list2[j]] 
     dict_clas[list_new[k]]=total    
    pred_class = max(dict_clas,key=dict_clas.get)
    foname.write(pred_class)
    foname.write(" ")
   elif list1[i] not in list3:
    foname.write(list1[i])
    foname.write(" ")
  foname.write("\n") 
finame.close()
foname.close()




