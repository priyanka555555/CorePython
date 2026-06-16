"""
Input : test_list1 = ["Gfg", "is", "not", "best", "and", "not", "CS"], 
test_list2 = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "thats ok"], sub_str = "ok" 
Output : ['Gfg', 'is', 'best', 'and', 'CS'] 
Explanation : All retained contain "ok" as substring in corresponding idx, e.g : Gfg -> Its ok ( has ok ) as substr.
"""
#5. First Non-Repeating Character - Find the first character that does not repeat.

st2 = "aabbccd"

for i in range(len(st2)):
    count = 0
    
    for j in range(len(st2)):
        if st2[i] == st2[j]:
            count =count+ 1
    
    if count == 1:
        print("First non-repeating character:", st2[i])

l=[1,1,1,2,2,3,3,4,4,4,6,6,6,7,8,7]
#output{1:[1,1,1]:[2,2],3:[3,3],4:[4,4,4],6:[6,6,6],7:7,8:[8,8,8]}
d={}
for i in l:
    if i in d:
        d[i].append(i) 
    else: 
     d[i]=[i] 
print(d)     

for i in d: 
    print(i)
    ln=len(d[i])
    #print(ln)
    if ln==1:
     d[i]= i
print(d) 

a= [10, 20, 30, 40, 50]
#b= [50, 40, 30, 20, 10]
a.reverse()
print(a)

a= [10, 20, 30, 40, 50]
l=[]
for i in range(len(a) -1, -1 ,-1):
   l.append(a[i])
print(l)

# Count element in a List
a = [1, 3, 2, 6, 3, 2, 8, 3, 9, 2, 7, 3]
c=3
count=0
for i in a:
   if c==i:
      count=count+1
print(count)   

# Smallest number in a List
l=[8, 3, 1, 9, 5] 
s=l[0]
for i in l:
   if i<s:
      s=i
print("smallest ",s)   

#Largest number in a List
l=[8, 3, 1, 9, 5] 
m=l[0]
for i in l:
   if i>m:
      m=i
print("max number ",m) 

#Second largest number in a List
l=[8, 3, 1, 9, 5] 
for i in range(len(l)):
   for j in range(len(l)):
      if l[i]>l[j]:
         t=l[i]
         l[i]=l[j]
         l[j]=t
print(l[1])  

# Even numbers in a List
l=[8, 3, 1, 9, 5] 
l1=[]
for i in l:
   if i%2==0:
      l1.append(i)
print(l1)      
# Positive numbers in a List
a = [-10, 15, 0, 20, -5, 30, -2] 
#Positive numbers = 15, 20, 30
l1=[]
for i in a:
   if i>=0:
      l1.append(i)
print(l1)  

# Count positive and negative numbers in a List
a = [-10, 15, 0, 20, -5, 30, -2] 
cp=0
cn=0
for i in a:
   if i>0:
      cp=cp+1
   else:
      cn=cn+1
print("count postive ",cp)         
print("count negative ",cn)   

# Remove multiple elements from a List
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
l=[]
for  i in a:
   if i not in remove:
      l.append(i)
print(l)  

# Remove empty tuples from a List
t=[(1, 2), (), (3, 4), (), (5,)]
#Output: [(1, 2), (3, 4), (5,)]
l=[]
for i in t:
   ln=len(i)
   if ln>0:
      l.append(i)
print(l)

# Print duplicates from a list of integers
l=[1, 2, 3, 1, 2, 4, 5, 6, 5,1]
#Output: [1, 2, 5].
dup=set()
seen=[]
for i in l:
   if i in seen:
      dup.add(i)# 1
   else:
      seen.append(i) # 2 3    
print(dup) 

#Remove first element from List
# Remove duplicates from List
l=[1, 2, 2, 3, 4, 4, 5]
#Output: [1, 2, 3, 4, 5].
l1=[]
for i in l:
   if i not in l1:
      l1.append(i)
print(l1) 

#  Merge Two Lists

l=[1, 2, 2, 3, 4, 4, 5]
l.insert(0,5)
print(l)

# Intersection of two Lists
A = [4, 9, 1, 17, 11]
B = [9, 74, 21, 45]
#Output: [9]
l=[]
for i in A:
   if i in B:
      l.append(i)
print(l) 
# Select random value from a List
"""
import random
A = [4, 9, 1, 17, 11]
b=random.randint(0,len(A))
print(A[b])  
"""
a = [1, 2, 3, 4, 5]
b = [4, 5, 6]
#Output: [4, 5]
l=[]
for i in a:
   if i in b:
      l.append(i)
print(l)  

#Max and Min element's position in a List
a = [1, 2, 3, 4, 5]
max=a[0]
min=a[0]
for i in a:
   if i>max:
      max=i
   elif i<min:
      min=i
print("max elemennt ",max)
print("min elemennt ",min) 

# Union of two or more Lists
a = [1, 2, 3]
b = [3, 4, 5]
#Output: [1, 2, 3, 4, 5]
l=[]
for i in a:
   if i not in b:
      l.append(i)
      
print(l+b) 

#Move All Zeroes To End
l= [1, 2, 0, 4, 3, 0, 5, 0]
#Output: [1, 2, 4, 3, 5, 0, 0, 0]
l1=[]
l2=[]
for i in l:
   if i!=0:
      l1.append(i)
   elif i==0:
      l2.append(i)  
print(l1+l2)  

# Plus One
l=[5, 6, 7, 8]
#Output: [5, 6, 7, 9]
l[-1]=l[-1]+1
print(l)
arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
#Output: 7
l=[]
for i in arr:
   if i not in l:
      l.append(i)
print(len(l)) 

# Union of Arrays with Duplicates 
a= [1, 2, 3, 2, 1]
b= [3, 2, 2, 3, 3, 2]

#Output: [1, 2, 3] 
c=a+b
dup=set()
seen=[]
print(c)
for i in c:
   if  i not in seen:
      dup.add(i)
      
   else:
      seen.append(i)

print(list(dup))

###############################################3333
#Programs on List of Strings
#Swap elements in String list
s=['Gfg', 'is', 'best', 'for', 'Geeks']
#['efg', 'is', 'bGst', 'for', 'eGGks']
s[0],s[-1]=s[-1],s[0]
print(s)

#Convert List to String
a = ['Geeks', 'for', 'Geeks']
#Geeks for Geeks
j=""
for i in a:
   j=j+"".join(i)+" "
print(j)


# Reverse All Strings in String List
a = ["apple", "banana", "cherry", "date"]
# ['elppa', 'ananab', 'yrrehc', 'etad']
l=[]
for i in a:
   rev=""
   for j in i:
    rev= j+rev
   if j not in l:
      l.append(rev) 
print(l)      

a = ["apple", "banana", "cherry", "date"]
res = []
for s in a:
    res.append(s[::-1])

print(res)

# Character position of Kth word
"""
nput : test_list = ["geekforgeeks", "is", "best", "for", "geeks"], K = 21 
Output : 0
Explanation : 21st index occurs in "geeks" and point to "g" which is 0th element of word.

"""
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
K = 21 
current_pos = 0
for word in test_list:
    
    if current_pos + len(word) > K:
        print(K - current_pos)
        break
    current_pos += len(word)

# Prefix frequency in string List
a = ["geeks", "geeksforgeeks", "geeky", "geek", "apple", "banana"]
#The prefix 'geeks' appears 2 times.
prefix="geeks"
c=0
for i in a:
    if i.startswith(prefix):
       c=c+1
print("The prefix 'geeks' appears ",c)       

# Remove words containing list characters

a = ['gfg', 'is', 'best', 'for', 'geeks']
remove_chars = ['g', 'e']
l = []

for word in a:
    for char in remove_chars:
        if char in word:
            break  
    else:
        l.append(word)

print(l)
# Output: ['is', 'for']

# Remove multiple empty spaces from String List

li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]
l= []
for i in li:
    
    s= " ".join(i.split())
    l.append(s)

print(l)
# Output: ['Hello world', 'Python is great', 'Extra spaces here']

# Add Space between Potential Words
test_list = ["gfgBest", "forGeeks", "andComputerScience"]
l=[]
for i in test_list:
   for j in i:
      if j.isupper():
         i=i.replace(j," "+j)
   l.append(i)  
print(l) 

# Convert Character Matrix to single String
a = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# gfgisbest
s=""
for i in a:
   for j in i:
      s=s+"".join(j)
print(s)  

# Filter strings by substring match in second List
"""
nput : test_list1 = ["Gfg", "is", "not", "best", "and", "not", "CS"], 
test_list2 = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "thats ok"], sub_str = "ok" 
Output : ['Gfg', 'is', 'best', 'and', 'CS'] 
Explanation : All retained contain "ok" as substring in corresponding idx, e.g : Gfg -> Its ok ( has ok ) as substr.
"""
# Replace all chars in list except given one
"""
Input : test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T'], repl_chr = '*', ret_chr = 'G' 
Output : ['G', '*', 'G', '*', '*', '*', '*', '*', '*'] 
Explanation : All characters except G replaced by *
"""
test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G' 
#['G', '*', 'G', '*', '*', '*', '*', '*', '*'] 
l=[]
for i in test_list:
   if i==ret_chr:
      l.append(i)
      
   else:
      l.append(repl_chr)

print(l)
##########
#Converting all Strings in a list to integers
a = ['2', '4', '6', '8']
for i in range(len(a)):
  a[i] = int(a[i])

print(a)

# Convert String Representation of a List into List
#########################################33333
################################################3
#Programs on List of Lists
#Remove empty List from List
a = [[1, 2], [], [3, 4], [], [5]]
#Resulting list = [[1, 2], [3, 4], [5]]
l=[]
for i in a:
   ln=len(i)
   if ln!=0:
     l.append(i)  
print(l)  

#Convert List to List of dictionaries
a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 
# [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}]

l=[1, 2, 8, 7, 9, 10, 23, 24, 26, 25, 27]
# 5
for i in range(len(l)):
   for j in range(len(l)):
      if l[i]<l[j]:
         t=l[i]
         l[i]=l[j]
         l[j]=t 
print(l)# [1, 2, 7, 8, 9, 10, 23, 24, 25, 26, 27]
res=[]
i=l[0]
r=[]
for num in l:
  if i==num:
   res.append(num)
   i=i+1
  else:
   r.append(res)
   res = [num]
   i=num+1

r.append(res)
print(r)# # output: [[1, 2], [7, 8, 9, 10], [23, 24, 25, 26, 27]]  
#print(max(r))
max_len=0
max_list=[]
for i in r:
   ln=len(i)
   if ln>max_len:
      max_len=ln
      max_list=i
print(max_list,max_len)      

"""

if len(l2)>len(l1):
   print(l2,"lenth is= ",len(l2))
else:
   print(l1,"lenth is= ",len(l1))
 """ 
a = [1, 2, 2, 2, 3, 4, 5]
s=""
for i in a:
   s=s+"".join((str(i)))
print(s)
print(type(s)) 
l = l1=[1,2,3,[3,4],[5,3],6]
i = 0
x=len(l)
print(x)
while i < len(l):
    if type(l[i]) == list:
        l[i:i+1] = l[i] 
    else:
        i=i+1        
print(l)  

t= ["gfgBest", "forGeeks", "andComputerScience"]
l=[]
for i in t:
   for j in i:
      if j.isupper():
         i=i.replace(j," "+j)

   l.append(i)
print(l)




