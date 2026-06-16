"""
list=[1,4,6,8,7]
list.sort(reverse=True)
print(list)
"""
"""
# remove duplicate
list=[1,4,6,8,7,4]
s=set(list)
print(s)
"""

"""
# print duplicate
data_list = [1, 4, 6, 8, 7, 4]
store = set()
duplicates = set()

for item in data_list:
    if item in store:#
        duplicates.add(item)# 1
    else:
        store.add(item)

print(list(duplicates))
"""
"""
2.data_list = [4, 6, 8, 7, 4, 9,9]
n=len(data_list)
for i in range(n):
    for j in range(i):
     if data_list[i]==data_list[j]:
        print(data_list[i])
"""
"""
# unique element
data_list = [1, 4, 6, 8, 7, 4]
store = set()
duplicates = set()

for item in data_list:
    if item  not in store:
        duplicates.add(item)
    else:
        store.add(item)

print(list(duplicates))
"""

# max element
     
"""
data_list = [4, 6, 8, 7, 4, 9]

n = len(data_list)
for i in range(n):
    for j in range(n):
      
        if data_list[i] < data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = temp

print(data_list[i])
"""

# smallest element
"""
data_list = [4, 6, 8, 7, 4, 9]

n = len(data_list)
for i in range(n):
    for j in range(n):
      
        if data_list[i] >data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = temp

print(data_list[i])   
"""
"""
# assending order

data_list = [4, 6, 8, 7, 4, 9]

n = len(data_list)
for i in range(n):
    for j in range(i+1,n):
      
        if data_list[i] >data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = temp


print(data_list)
"""

# dessending order
"""
data_list = [4, 6, 8, 7, 4, 9]

n = len(data_list)
for i in range(n):
    for j in range(i+1,n):
      
        if data_list[i] < data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = temp


print(data_list)
"""
"""
# second highest

data_list = [4, 6, 8, 7, 4, 9]
n = len(data_list)

for i in range(n):  
   # print(i)
    for j in range(i + 1, n):
        if data_list[i] < data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = temp
#  6,8,4,7,4,9
print("Second highest:", data_list[1])
"""
# sum of the list
"""
list=[1,2,3,4,5] 
sum=0 
for i in list:
    sum=sum+i
print(sum)    
"""
#Decrement List Values



#Interchange first and last element
"""
list=[10,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)
"""
#Check if element exists
"""
list=[10,2,3,4,5]
if 10 in list:
    print(" 10 is exist")
else:
     print(" 10 is  not exist")
"""
#Reverse a List
"""
list=[10,2,3,4,5]
list.sort(reverse=True)
print(list)
"""
"""
#Cloning or Copying a List
list=[10,2,3,4,5]
list1=list.copy()
print(list1)
"""
#Sum and avg
"""
list=[10,2,3,4,5]
sum=0 
for i in list:
    sum=sum+i
print(sum)    
avg=sum/len(list) 
print(avg)  
"""
"""
list=[10,2,3,4,5]
s=min(list)
print(s)
"""
#smallest element
"""
list=[10,2,3,4,5]
s=list[0]
for i in list:
    if i<s:
        s=i
print(s)
#largest element
"""
"""
list = [10, 24, 76, 23, 12]

res = list[0]
for i in list:
    if i > res:
        res = i
print(res)
"""
# sum of even and odd
"""
list = [10, 24, 76, 23, 12]
even=0
odd=0

for i in list:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i    
print(" sum of even number",even)
print(" sum of odd number",odd)
""" 
# Count Even and Odd Numbers in a List
"""
list = [10, 24, 76, 23, 12]
even=0
odd=0

for i in list:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1    
print(" sum of even number",even)
print(" sum of odd number",odd)     
  """
#Positive numbers in a List
"""
list = [-10, 24, -76, 23, 12] 
for i in list:
    if i>0:
        print(i) 
""" 
#Negative numbers in a List  
"""
list = [-10, 24, -76, 23, 12] 
for i in list:
    if i<0:
        print(i) 
"""
# Count positive and negative numbers in a List 
"""
list = [-10, 24, -76, 23, 12] 
pn=0
nn=0
for i in list:
    if i<0:
        pn=pn+1
    else:
        nn=nn+1    
print("count negative number",pn)   
print("count postive number",nn)         
"""
# Remove multiple elements from a List
"""
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
res=[]
for i in a:
    if i not in remove:
        res.append(i)
print(res)        
"""
#Remove empty tuples from a List
"""
t=[(1,2),(),(2,3),()]
res=list(filter(None,t))
print(res)
"""
#Remove first element from List
"""
a = [10, 20, 30, 40, 50, 60, 70]
a.pop(0)
print(a)
"""
#Remove duplicates from List
"""
a = [10, 20, 30, 40, 50, 50, 70]
store=set()
duplicate=set()

for i in a:
    if i not in store:
        duplicate.add(i)
    else:
        store.add(i)
print(duplicate)
"""
#3Get Unique values from a List
"""
a = [10, 20, 30, 40, 50, 50, 70]
res=[]
for x in a:
    if x not in res:
        res.append(x)
print(res)         
""" 
#Print common elements of two lists
""" 
a = [10, 20, 40, 50 ,70] 
b = [10, 20, 30, 40, 50, 50, 70] 
c=[] 
for i in a:
    if i in b:
        c.append(i)
    print(i)   
"""      
# Max and Min element's position in a List
"""
a = [10, 5, 2, 50 ,70] 
m=a[0]
s=a[0]

for i in a:
    if i>m:
        m=i
    else:
        s=i    
print(m)
print(s)
"""
#Union of two or more Lists unique
"""
a = [10, 20, 40, 50 ,70] 
b = [10, 20, 30, 40, 50, 50, 70] 
c=list(set(a).union(b))
print(c)
"""
#moves all zeroes to end of list
"""
arr = [1, 2, 0, 4, 3, 0, 5, 0]

zero = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[zero] = arr[i]
        zero=zero+1

for i in range(zero, len(arr)):
    arr[i] = 0

print(arr)
"""

# Plus One
"""
arr= [5, 6, 7, 8]
arr[-1]=arr[-1]+1
print(arr)
"""
#Convert List to String
"""
a=['Geeks', 'for', 'Geeks']
rs=' '.join(a)

print(rs)
"""
#Reverse All Strings in String List
"""
a=['Geeks', 'for', 'Geeks']
res=[]
for s in a:
    res.append(s[::-1])
print(res)    
"""
#Extract words starting with K
"""
a = ["Kite", "Apple", "King", "Banana", "Kangaroo", "cat"]
K = 'K'
res = []
for word in a:
    if word.startswith(K): 
        res.append(word)

print(f"Words starting with '{K}':", res)
"""
"""
li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]

# Remove multiple spaces in each string using split and join
c = [' '.join(string.split()) for string in li]

print(c)
"""
"""
a = [[1, 2], [], [3, 4], [], [5]]
s=list(filter(lambda b:b,a))
print(s)
"""
"""
a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 
c=[dict(zip(a.value)) for i in b]
print(c)
"""
#Smallest Missing Positive Number
"""
a = [2, -3, 4, 1, 1, 7]
s=a[0]

for i in a:
    if i<s:
       s=abs(i)
       break  
print(s)
"""

#Alternate Positive Negative
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]

pos = []
neg = []

# separate positives (and zero) and negatives
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(pos) 
print(neg)       

result = []
i=0
j=0

# alternate positive and negative
while i < len(pos) and j < len(neg):
    result.append(pos[i])# 9,-2,4
    result.append(neg[j])# 9,-2,4,-1
    i += 1
    j += 1

# append remaining elements
result.extend(pos[i:])
result.extend(neg[j:])
print(result)

a = [10, 5, 2, 50 ,70] 
m=a[0]
s=a[0]

for i in a:
    if i>m:
        m=i
    else:
        s=i    
print(m)
print(s)

l= [1, 2, 0, 4, 3, 0, 5, 0]
#output [1,2,3,4,5,0,0,0]
for i in l:
    if i==0:
        l.remove(i)
        l.append(0)
l1 = []
for i in l:
    if i > 0:
        l1.append(i)
l1.sort()
l2=[]
for i in l:
 if i==0:
   l2.append(i)
   l1.extend(l2)
print(l1)

s="priyanka patel"
# output "PrIyaNkA pAtEl"
s1=""
for i in range(len(s)):
    if i%2==0:
        s1=s1+s[i].upper()
    else:
        s1=s1+s[i].lower() 
print(s1)   
       
s="hello"
s1=s.find('l')
print(s1)





