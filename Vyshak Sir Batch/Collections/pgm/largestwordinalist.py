l=['apple','kiwi','orange','watermelon']
largest=l[0]
# print(largest)
for i in l:
    if len(i)>len(largest):
        largest=i
print(largest)