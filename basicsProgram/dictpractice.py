# # Keys associated with Values
## Print anagrams together
#test_list = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']
#Check if binary representations of two numbers are anagram
#Counter to find size of largest subset of anagram word
#Count of groups having largest size while grouping according to sum of its digits


#Sort by Key or Value
d={'apple': 5, 'banana': 2, 'cherry': 7}
sor={}
for value in sorted(d.values()):
    for key in d:
        if d[key]==value:
            sor[key]=value
print(sor) 

#2.Handling missing keys
# program to find the sum of all items in a dictionary
d = {'a': 100, 'b': 200, 'c': 300}
sum=0
for i in d.values():
   sum=sum+i
print(sum) 

# Find size of a Dictionary
import sys
d = {'a': 100, 'b': 200, 'c': 300}
size=sys.getsizeof(d)
print(size)

# Merging two Dictionaries
d1 = {'x': 1, 'y': 2} 
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)

# Common elements in sorted arrays by dictionary intersection
"""
Input:      ar1 = [1, 5, 10, 20, 40, 80]
            ar2 = [6, 7, 20, 80, 100]
            ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output:  [80, 20]
"""
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
l = []

for i in ar1:
   if i in ar2 and i in ar3:
       l.append(i)
print(l) 

"""
nput: [ "john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john" ]      
Output: John
"""
"""
l=[ "johmmmn", "johnny", "jackie", "johnny", "johmmmn", "jackie", "jamie", "jamie", "johmmmn", "johnny", "jamie", "johnny", "johmmmn" ]
for i in l:
    l=[]
    if l.count(i)<=len(i):
        l.append(i)
print(l)        
"""
      

d = {"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]}
d1 = {}
# output {"is": [6, 7, 4, 3, 3]}
# Part 1: Remove duplicates
for key in d:
    l = []
    for num in d[key]:
        if num not in l:
            l.append(num)
    d1[key] = l

# Part 2: Find the key with the longest list of unique numbers
max_key = ""
max_len = 0
for key in d1:
    if len(d1[key]) > max_len:
        max_len = len(d1[key])
        max_key = key

print(f"Cleaned Dictionary: {d1}")
print(f"Key with most unique values: {max_key}")

# Find all duplicate characters in string

s = "GeeksforGeeks"
dup = []
seen = []

for i in s:
    if i in seen:
        if i not in dup:
            dup.append(i)
    else:
        seen.append(i) 

print(dup) 
# Output: ['e', 'G', 'k', 's']
# Group Similar items to Dictionary Values List    
a = ['apple', 'banana', 'apple', 'orange', 'banana']
d = {}

for fruit in a:
    if fruit in d:
        d[fruit].append(fruit)
    else:
        d[fruit] = [fruit] 

print(d)
# Output: {'apple': ['apple', 'apple'], 'banana': ['banana', 'banana'], 'orange': ['orange']}
# Output: "r"
s = "geeksforgeeks"
k = 3
l = []

# Step 1: Find all characters that appear only once
for i in s:
    if s.count(i) == 1:
        l.append(i)
print(l)
print(l[-1])

"""
est_list = ["Gfg", "is", "Best"], subs_dict = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}, K = 0 
Output : [5, 7, "Best"] 
Explanation : "Gfg" and "is" is replaced by 5, 7 as 0th index in dictionary value list. 
"""
list = ["Gfg", "is", "Best"]
d = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
K = 0
l=[] 
for word in list:
    if word in d:
        l.append(d[word][K])
    else:
        l.append(word)
print(l)

lst = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
l=[]
# Output : [4, 3]
for i in lst:
    if lst.count(i)>=K and  i not in l:
        l.append(i)
print(l)  
"""
li = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
# {1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
d={}
for i in li:
  if i in d:
      d[i]=d[i]+1
  else:
      d[i]=1
print(d)
""" 
lst = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]    
dict = {}

for index, val in enumerate(lst, 1):
  dict[index] = val

print(dict)

lst = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]    
dict = {}
c = 1 
for i in lst:
    dict[c] = i
    c = c + 1 
print(dict)
        
a = ['apple', 'banana', 'apple', 'orange', 'banana']
#{'apple': ['apple', 'apple'], 'banana': ['banana', 'banana'], 'orange': ['orange']}
d={}

for key in a:
    if key in d:
        d[key].append(key)
    else:
        d[key] =[key]  
print(d)
     
       
s = "hello world, have a great day"
r_dict = {"hello": "hi", "world": "earth", "great": "wonderful"}
words = s.split()
result = []

for word in words:
    clean_word = word.strip(",")
    
    if clean_word in r_dict:
        replaced = word.replace(clean_word, r_dict[clean_word])
        result.append(replaced)
    else:
       result.append(word)


# Join the list back into a sentence
print(" ".join(result))


a = ["a", "b"]
b = [1, 2]
l=[]
#output : [('a',1),('a',2),('b',1),('b',2)]
for i in a:
    for j in b:
          l.append((i,j))
         
print(l)            

# remove duplicate
s = "Geeks for Geeks"
s1 = s.split()
seen = set()
duplicates = set()

for i in s1:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates) 
print(seen)

s = "Geeks for Geeks"
s1 = s.split()
res=[]
for word in s1:
    if word not in res:
        res.append(word) 
print(res)        


s = "GeeksforGeeks"
dup = []
seen = []

for i in s:
    if i in seen:
        if i not in dup:
            dup.append(i)
    else:
        seen.append(i) 

print(dup) 

a = ['Gfg', 'is', 'best']
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
#output : ['Gfg', 'is', 'best', 'is', 'Gfg', 'Gfg', 'Gfg', 'best', 'is', 'is', 'best', 'Gfg']
l=[]
for i in b:
     if i not in a:
      l.append(a[i]) # gfg ,is best
print(l)        

a = ['Gfg', 'is', 'best']
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
l = []

for i in b:
    word = a[i]
    l.append(word)
print(l)
# Output: ['Gfg', 'is', 'best', 'is', 'Gfg', 'Gfg', 'Gfg', 'best', 'is', 'is', 'best', 'Gfg']

print("Remove duplicate values across Values")

d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
d1={}
s=set()
for key,value in d.items():
    l=[]
    for va in value:
       if va not in s: 
        l.append(va)
        s.add(va)
    d1[key]=l
print(d1)    

d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
# {'a': [1, 2, 3], 'b': [4, 5], 'c': [6]}
d1={}
s=[]
for key in d:
    l=[]
    for value in d[key]:
          if value not in s:
           l.append(value)
           s.append(value)
        
    d1[key]=l
print(d1) 

# Counting the Frequencies in a List Using Dictionary
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# {'apple': 2, 'banana': 3, 'orange': 1}         
d={}
for key in a:
     c=a.count(key)
     d[key]= c
print(d) 
###############################################################
###############################################################
#Conversion of dictionary
#Convert Key-Value list Dictionary to List of Lists
a = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
# [['name', 'Alice'], ['age', 25], ['city', 'New York']]
result=[]
for key,value in a.items():
    result.append([key,value])
print(result)

#Convert List to List of dictionaries

a = ["name", "age", "city"]  
b = ["Alice", 25, "New York"] 

# output [{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}]
"""
d={}
for key in a:
    for value in b:
        if key not in d:
            d[key]=d[value] 
        else:
            d[key]=value
print(d)
"""
############333
# Create Nested Dictionary using List
a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]
# {8: {'Gfg': 4}, 3: {'is': 5}, 2: {'best': 9}}
d={}
c=0
for i ,j in a.items():
    d[b[c]]={(i,j)}
    c=c+1
print(d)

a = {'Gfg': 4, 'is': 5, 'best': 9}

# This will process 'best' first, then 'is', then 'Gfg'
d={}
for key, value in reversed(a.items()):
    d[key]=value
print(d)    
# Swapping Hierarchy in Nested Dictionaries
test = {'Gfg': { 'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}}
# 'a': {'Gfg': [1, 3, 7, 8]}, 'b': {'Gfg': [4, 9]}, 'c': {'Gfg': [0, 7]}}
d = {}

for key, value in test.items():
   for k, v in value.items():
       if k not in d:
           d[k] = {}
       
       d[k][key] = v

print(d)

# Inversion in nested dictionary
dst= {"a" : {"b" : {}}, "d" : {"e" : {}}, "f" : {"g" : {}}}
# Output : {'b': {'a': {}}, 'e': {'d': {}}, 'g': {'f': {}}
#  Explanation : Nested dictionaries inverted as outer dictionary keys and viz-a-vis
d={}
for key,value in dst.items():
    for k,v in value.items():
       if k not in d:
          d[k]={}  
       d[k][key]=v
print(d)

# Reverse Dictionary Keys Order
dst={'gfg': 4, 'is': 2, 'best': 5}
#OrderedDict({'best': 5, 'is': 2, 'gfg': 4})
d={}
for key,value in reversed(dst.items()):
    d[key]=value
print(d)    

##############################################33
#Extract Key’s Value, if Key Present in List and Dictionary
"""
a = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg": 5, "Best": 6}
K = "Gfg"
output 5
"""
a = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg": 5, "Best": 6}
K = "Gfg"
s=""

for key,value in d.items():
    if key in a:
        s=s+ str(value)
print(s)

a = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg": 5, "Best": 6}
K = "Gfg"
if K in a and K in d:  
    print(d[K])

#Remove keys with Values Greater than K ( Including mixed values )
d = {'a': 1, 'b': 5, 'c': 'hello', 'd': [1, 2, 3]}
# {'a': 1, 'c': 'hello', 'd': [1, 2, 3]}
d1={}
del d['b']
print(d) 

# Remove keys with substring values
d = {'name1': 'hello world', 'name2': 'python code', 'name3': 'world peace'}
substring = 'world'
d1={}
# {'name2': 'python code'}
for i ,j in d.items():
    j1=j.split()
    if substring not in j1:
        d1[i] =j
print(d1)           










# Dictionary with maximum count of pairs
test_list = [{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}]
#Output : 4
d={}
c=0
for i in test_list:
 for key , value in i.items():
   if key not in d:
      d[key]=value 
      c=c+1
  
print(c)   

test_list = [{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}]
max_keys = 0
for d in test_list:
    if len(d) > max_keys:
        max_keys = len(d)# 4

print(max_keys) # Output: 4

# Append Dictionary Keys and Values
dst=["name", "age", "city"]
values = ["Harry", 30, "New York"]
#Output: {'name': 'Harry', 'age': 30, 'city': 'New York'}
d={}
for i in range(len(dst)):
    if key not in d:
        d[dst[i]] =values[i]
print(d)

# Extract Unique values
data = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
#Output: [1, 2, 5, 6, 7, 8, 10, 11, 12]
l=[]
for key ,value in data.items():
    for v in value:
        if v not in l:
            l.append(v)
l.sort()            
print(l)  

# Filter dictionary values in heterogeneous
test= {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}
k=3
d={}
for key,value in test.items():
     if type(value)!=int or value>3:
       d[key]=value
print(d)

# Sort Dictionary key and values List
dst= {'c': [3], 'b': [12, 10], 'a': [19, 4]} 
#Output: {'a': [4, 19], 'b': [10, 12], 'c': [3]} 
d={}
for i,j in reversed(dst.items()):
    d[i]=sorted(j)
print(d)

# Sort Dictionary by Values Summation
"""
Input : test_dict = {'Gfg' : [6, 7, 4], 'best' : [7, 6, 5]} 
Output : {'Gfg': 17, 'best': 18} 
Explanation : Sorted by sum, and replaced. 
"""
test_dict = {'Gfg' : [6, 7, 4], 'best' : [7, 6, 5]} 
# Output : {'Gfg': 17, 'best': 18} 
d={}
s=0
for key,value in test_dict.items():
    for v in value:
       s=s+v
    d[key]=s
print(d)

# Sort dictionaries list by Key’s Value list index
"""
Input : [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19}, {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}],
 K = "Gfg", idx = 0 
Output : [{'Gfg': [2, 0, 3], 'is': 11, 'best': 19}, {'Gfg': [4, 6, 9], 'is': 16, 'best': 1}, {'Gfg': [6, 7, 8], 'is': 9, 'best': 10}] 
Explanation : 2<4<6, hence dictionary ordered in that way by 0th index of Key. 

"""
dst = [
    {"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
    {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19}, 
    {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]

K = "Gfg"
idx = 0 

x = sorted(dst, key=lambda d: d[K][idx])
print(x)

############################33
#Output: 2
"""
arr = [1, 5, 3, 4, 3, 5, 6]


for i in range(len(arr)):
    result = 0
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            result = result+1 

    if result==1:
      print(i) 
      break
"""
d = {"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]}
#is

d1={}
for i,j in d.items():
    l=[]
    for j1 in j:

        if j1 not in l:
            l.append(j1)

    if i not in d1:
        d1[i]=l

max_key = ""
max_len = 0

for i, j in d1.items():
    if len(j) > max_len:
        max_len = len(j)
        max_key = i

print(max_key)

#############3
l=['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
#Output: {'apple': 2, 'banana': 3, 'orange': 1}
d={}
for i in l:
  if i in d:
      d[i]=d[i]+1
  else:
      d[i]=[i]
print(d)
arr = [1, 5, 3, 4, 3, 5, 6]
min_index = float('inf')
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            if (i + 1) < min_index:
                min_index = i + 1
            break 


if min_index == float('inf'):
    print(-1)
else:
    print(min_index)






