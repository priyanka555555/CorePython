def fun(a,b,c):
  return a,b,c
l=[1,2,3]
print(*fun(*l))
print(fun(*l))
#print(type(*fun(*l)))
# fun(1,2,3)