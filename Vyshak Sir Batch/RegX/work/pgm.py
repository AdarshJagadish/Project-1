import re
a="Welcome To The World Of Proramming"
txt1=re.split('\s',a)
print(txt1)
upper=0
for i in txt1:
    # print(i)
    for j in i:
        if j==isupper():
            upper+=1