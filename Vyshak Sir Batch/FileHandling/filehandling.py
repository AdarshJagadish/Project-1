# f=open('sample.txt','x')

# try:
#     f=open('Vyshak Sir Batch\FileHandling\sample.txt','x')             #to create in a specific path 
# except:
#     pass

# f=open('Vyshak Sir Batch\FileHandling\sample.txt','w')                   # To write or overwrite in the file
# f.write('Hello World')

# f=open('Vyshak Sir Batch\FileHandling\sample.txt','a')                   # To append in a file
# f.write(' ,Welcome to Sample')

f=open('Vyshak Sir Batch\FileHandling\sample.txt','r')                   # To read a file
print(f.read())