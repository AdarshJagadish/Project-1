import os
foldername=input('enter folder name')
filename=input('enter file name')
os.mkdir(foldername)
f=open(foldername+'/'+filename,'x')