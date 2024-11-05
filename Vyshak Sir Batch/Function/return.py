# def math():     # fn with arguments
#     a=1
#     b=2
#     c=3
#     return a,b,c
# number=math()
# x,y,z=math()
# print(x)
# print(y)
# print(z)
# print(number)

# def std(name,age):                       # position argument
#     print(name,age)
# std('Abhi',24)

# def std(*arg):             # fn with arbitary arg
#     print(arg)
# std('jerrin',22,"thrissur")
# std('abhinav',"kozhikode")

# def std(name,age,course='Python'):           # FN with default parameter
#     print(name,age,course)
# std('Abhi',24,'java')
# std('Adarsh',21)


def std(**arg):             # fn with arbitory keyword arg,output as dictionary
    print(arg)
std(name='jerrin',age=22,place="thrissur")
std(name='abhinav',place="kozhikode")
std(name='jose',age=52,place="thrissur")