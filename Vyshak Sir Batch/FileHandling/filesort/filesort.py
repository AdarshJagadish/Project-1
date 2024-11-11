try:
    f=open('Vyshak Sir Batch/FileHandling/filesort/textfile.txt','x')
except:
    pass
# f=open('Vyshak Sir Batch/FileHandling/filesort/textfile.txt','w')
# f.write(input('enter a paragraph: '))
f=open('Vyshak Sir Batch/FileHandling/filesort/textfile.txt','r')
content=f.readlines()
# print(content)
for i in content:
    hgjh