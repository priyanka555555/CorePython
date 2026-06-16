"""
l=["hello",1,2,3]
print(l[0])
l1=len(l)
for i in range(l1):
    print(l[i])
    """
#tuple is immutable
"""
t=(1,2,3,4,6)
t1=len(t)
for i in range(t1):
    print(t[i])
"""
"""
# in set
s={1,2,3,4}
for i in s:
  print(i)
#in dict  
d={
  "name":"priya",
  "age":40
}
for key,value in d.items():
  print(key,":",value)
for key in d.keys():
  print(key)
for value in d.values():
  print(value)  
"""
"""
st="hello"
for i in st:
    print(i)
"""
"""
l=[1,3,4,5,8,5,6]
l1=len(l)
for i in range(l1):
    print(l[i])
    if i==4:
         break
"""
"""
l=[1,3,4,5,8,5,6]
for i in l:
    if i==3:
     continue
    print(i)
 """
"""
l=[1,3,4,5,8,5,6]
for i in l:
    print(i) 
    if i==5:
        break    
"""
"""
for i in range(1,6,2):
    print(i)
else:
    print("loop is finished")    

"""
for i in range(6):
    if i==3:
        break
    print(i)
"""   
for x in range(6):
  if x == 3:
    break
  print(x)
else:
  print("Finally finished!")    
  """
## nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
