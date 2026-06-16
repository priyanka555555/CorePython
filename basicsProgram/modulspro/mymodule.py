def fun():
    print("hello world")

dictp={
    "name":"priya",
    "age":40
} 

def ad(a,b):
    print(a+b)
def sb(a,b):
    print(a-b)    

import copy
a=[[1,2],[3,4]]
b=copy.copy(a) 
b[0][0]=99
print(a) 
print(b)

a=[[1,2],[3,4]]
b=copy.deepcopy(a)
b[0][0]=9
print(a)
print(b)
