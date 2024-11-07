# limit=int(input('Enter Limit: '))
# try:
#     f=open('Vyshak Sir Batch\FileHandling\students.txt','x')
# except:
#     pass
# for i in range(limit):
#     name=input('Enter name: ')
#     f=open('Vyshak Sir Batch\FileHandling\students.txt','a')
#     f.write(name+'\n')
f=open('Vyshak Sir Batch\FileHandling\students.txt','r')
print(f.read())
# print(f.read(13))
# f.seek(0)
# print(f.tell())
