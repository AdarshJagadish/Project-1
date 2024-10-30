numbers={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# print(numbers)
num=int(input("Enter a Number: "))
value=''
while (num>0):
        b=num%10
        demo=numbers[b]
        value=demo+value
        num=num//10
        # print(b)
print(value)