import os,glob,sys,re
inputdir= sys.argv[1]
outputfile= sys.argv[2]

try:
   foname=open(outputfile,'w')
   for root, dirs, files in os.walk(inputdir):
       files.sort()
       for file in files:
         if glob.fnmatch.fnmatch(file, '*.txt'):
            #name=file.split('.')
            #foname.write(name[0])
            #foname.write(' ')
            try:
             inputfile=os.path.join(root,file)
             finame=open(inputfile,'r',encoding='UTF-8',errors='ignore')
             for line in iter(finame):
                line=re.sub('\*+','',line)
                line=re.sub('\n','',line)
                line=re.sub('\s+',' ',line)
                #line=line.strip('\n\t')
                foname.write(line)
                foname.write(' ')
             foname.write('\n')
            except IOError:
             print ('Error while reading from file') 
            finally:
             finame.close()

except IOError:
     print ('Error while writing into file') 
finally:
 foname.close()
 
