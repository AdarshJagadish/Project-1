try:
    f=open('Vyshak Sir Batch\FileHandling\sample.txt','x')
except:
    pass
# f=open('Vyshak Sir Batch\FileHandling\sample.txt','r')
# line=f.readline()
# print(line)
# rline=f.readline()
# print(rline)
# print(type(line))

f=open('Vyshak Sir Batch\FileHandling\sample.txt','r')
line=f.readlines()
print(line)
print(type(line))
for i in line:
    print(i)
    for j in i:
        print(j)