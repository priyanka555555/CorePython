def fun(x):#30
   x=10# create new object
   return x
a=fun(20) 
print(a)  





def priyanka(*num,**name):
   #  if name:
   #     print(num,name)
   #  else:
   #     print(num)
   if num:
      print(num)
   if name:
      print(name)

priyanka(1)                 
priyanka(1,2)              
priyanka(1,2,3)           
priyanka(1,2,3,A="Ram")  
"""
def priyanka(*num,**name):
    if name:
       return num,name
    else:
      return num

p=priyanka(1)
print(p)                 
p1=priyanka(1,2) 
print(p1)             
p2=priyanka(1,2,3)   
print(p2)       
p3=priyanka(1,2,3,A="Ram")  
print(p3)
"""
def fun(*l):
   return l
l1=[1,2,3]
l2=[2,3,4]
print(*fun(l1+l2))



