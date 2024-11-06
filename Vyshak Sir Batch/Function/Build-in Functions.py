# # 1.Map
# # map(function,iterable)
# l=[1,2,3,4]
# res=map(lambda a:a*a,l)
# print(list(res))                # must define result as list

l=[1,2,3,4,5,6,7,8,9,10]
# def mapfn(a):
#     return a*a                    # Using def
# result=list(map(mapfn,l))
# print(result)

# 2.filter
# even=list(filter(lambda a:a%2==0,l))
# print(even)

# def fil(a):
#     return(a%2==0)
# result=list(filter(fil,l))
# print(result)

def fact(a,s):
    s=0
    return a=a+1
res=reduce(fact,l)
print(res)