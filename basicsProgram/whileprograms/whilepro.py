num = 5
count = 0
i = 1

while i <= num:
    if num % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print("prime number")
else:
    print("not prime number")   
#########
"""
i=1
while i<=5:
    print(i)
    if i==4:
        break
    i=i+1
"""
###########3
"""
i = 0
while i < 6:
  i=i+ 1
  if i == 3:
    break
  print(i) 
"""
########continue
"""
i=1
while i<5:
   i=i+1
   if i==2:
      continue
   print(i)       
 """ 
"""
i=0
while i<=5:
   i=i+1
   if i==3:
       continue
   print(i)
"""
"""
i=0
while i<=5:
    i=i+1
    if i==3:
        break
    print(i)   
"""
"""
i=1
while i<=10:
    print(i)
    i=i+1
else:
    print("i is no longer less then 10")    

""" 
##########
""" 
i=0
while i<=5:
    i=i+1
    if i==4:
        #continue
        break
    print(i)
""" 
""" 
l=[1,11,3,4,5]
i=0
while i<len(l):
    print(l[i])
    i=i+1
""" 
""" 
t=(2,8,4,5)
i=0
while i<len(t):
    print(t[i])
    i=i+1
"""     
"""
s = {1, 9, 3, 4}

lst = list(s)
i = 0

while i < len(lst):
    print(lst[i])
    i += 1

    """
d ={
    "name": "priya",
    "age": 25
}

keys = list(d.keys())

i = 0
while i < len(keys):
    key = keys[i]
    print(key, d[key])
    i = i + 1
    
 