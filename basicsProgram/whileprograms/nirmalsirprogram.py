#1.Count the frequency of each character in a string.
s= "banana"
#Output: {'b': 1, 'a': 3, 'n': 2}
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d) 
#Q2. Find the second largest element in a list.
#Input: [10, 5, 20, 8]
#Output: 10   
l=[10, 5, 20, 8]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t 
    print(l[i])
print("second largest element is:",l[-2])    

#3. Find common elements between two lists.
#Input: [1, 2, 3, 4], [3, 4, 5, 6]
#Output: [3, 4]
l1=[1, 2, 3, 4]
l2=[3, 4, 5, 6]
ls=[]
for i in l1:
    if i in l2:
        ls.append(i)
print(ls) 

#Q4. Merge two dictionaries and sum values of common keys.
#Input: {'a': 2, 'b': 3}, {'b': 4, 'c': 5}
#Output: {'a': 2, 'b': 7, 'c': 5}
d1={'a': 2, 'b': 3}
d2={'b': 4, 'c': 5}
d3={}
for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
print(d3)
for i in d2:
    if i not in d1:
        d3[i]=d2[i] 
print(d3)

##########################
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
l1=[1, 2, 3, 4]
l2=[3, 4, 5, 6]
# [3, 4]
ls=[]
for i in l1:
    if i in l2:
        ls.append(i)
print(ls)        
d1={'a': 2, 'b': 3}
d2={'b': 4, 'c': 5} 
# {'a': 2, 'b': 7, 'c': 5}
d={}
for i in d1:
    if i in d2:
        d[i]=d1[i]+d2[i]
    else:
        d[i]=d1[i]
print(d)        
for i in d2:
    if i not in d1:
        d[i]=d2[i]
print(d) 

l= [1, [2, [3, 4], 5], 6]
#Output: [1, 2, 3, 4, 5, 6]
l1=[]
for i in range(len(l)):
    if type(l[i])==list:
        l[i:i+1]=l[i]
    else:
        i=i+1
print(l)  
#Q1. Remove duplicate characters from a string while preserving order.
s="programming"
#Output: "progamin"
s1=""
for i in s:
    if i not in s1:
        s1=s1+i
print(s1)  

#Q2. Check if a given number is prime.
num= 17
c=0
#Output: True
for i in range(1,num+1):
    if num%i==0:
        c=c+1
if c==2:
  print("true")
else:
    print("false")
#Q3. Group words that are anagrams.
l=["eat", "tea", "tan", "ate", "nat", "bat"]
#Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] 
d={}
for i in l:
    key= ''.join(sorted(i))
    if key in d:
        d[key].append(i)
    else:
        d[key]=[i]#aet:[eat]
        
print(list(d.values()))   

#Q4. Rotate a list by k positions.
l=[1, 2, 3, 4, 5]
k = 2
l1=[]
#Output: [4, 5, 1, 2, 3]
for i in range(len(l)):
    if i>k:
     l1.append(l[i])
    
for i in range(len(l)):
    if i<=k:
      l1.append(l[i])  
         
print(l1) 
#Q5. Flatten a nested list of any depth.
l= [1, [2, [3, 4], 5], 6]
#Output: [1, 2, 3, 4, 5, 6]
l1=[]
for i in range(len(l)):
    if type(l[i])==list:
        l[i:i+1]=l[i]
    else:
        i=i+1
print(l)  
l = [1, [2, [3, [4]]]]
flat_list = []

for item in l:
    if type(item) == list:
        flat_list.extend(item)
    else:
        flat_list.append(item)
        

l = [1, [2, [3, [4]]]]

flat_list = []

for item in l:
    if isinstance(item, list):
        l.extend(item)
    else:
       flat_list.append(item)

print(flat_list) 
# Output: [1, 2, 3, 4]
# set C low
#1
#Count the frequency of each word in a sentence.
s="this is a test this is"
#Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1}
d={}
for i in s.split():
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d) 
"""
Q2. Check if two strings are anagrams.
Input: "listen", "silent"
Output: True
"""
s= "listen"
s1="silent"
if sorted(s)==sorted(s1):
    print("true this is anagram")
else:
    print("false this is not anagram") 
    
"""
Medium
Q3. Group words by their length.
Input: ["one", "two", "three", "four"]
Output: {3: ['one', 'two'], 5: ['three'], 4: ['four']}
""" 
l=["one", "two", "three", "four"] 
d={}
l1=[]
for i in l:
    for j in l:
      if len(i)==len(j):
          if i not in d:
              d[len(i)]=[i]
        
          
          
print(d)                
l = ["one", "two", "three", "four"] 
d = {}
for i in l:
    length = len(i)
    if length not in d:
        d[length] = [i]
    else:
       d[length].append(i)
print(d)

l=[1,2,3,4,5]
print(l.count(1))# returns the number of elements
l1=[1,2,3,4,5]
l.extend(l1)# extend method add list elemnts to the end of the current list
print(l)
l.append(l1)
print(l)
l.insert(1,"hello")
print(l)
print(l.remove(1))
print(l)
print(l.pop())
#del l
print(l)
s=[5,2,3]
l=[x*2 for x in range(5)]
print(l)
"""
List comprehension is a compact way to create a new list by applying an expression to each item in an existing list 
or iterable, optionally including a condition.
[expression for item in iterable if condition]
Example: Create a list of squares for numbers from 0 to 9.
squares = [x**2 for x in range(10)] 
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
s.sort()
print(s)
s=[5,2,3]
print(sorted(s))
s.reverse()
print(s)
# make a copy of a list
c=[1213,33]
d=c.copy()
print(d)
l1=[1,2,3,4]
l2=[2,3,4,5]
for i in l2:
    l1.append(i)

print(l1)
t=(1,2,3,4)
a,b,c,d=t
print(a,b,c,d)

l1=[1, 2, 3, 4]
l2=[3, 4, 5, 6]
# [3, 4]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)        
###############################3333
############################3
#########################
s="this is a test this is"
#Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1}
d={}
for i in s.split():
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1  
print(d)   

#Q2. Check if two strings are anagrams.
s="listen"
s1="silent"
if sorted(s)==sorted(s1):
    print("true")
else:
    print("false")
s=["one", "two", "three", "four"]
#Output: {3: ['one', 'two'], 5: ['three'], 4: ['four']}    
d={}
l=[]
for i in s:
    ln=len(i)
    if ln in d:
        d[ln].append(i)
    else:
        d[ln]=[i] 
print(d) 

# fctorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
       return n*fact(n-1)
            
print(fact(5))

# 4. Find missing numbers in a given range.
l= [1, 2, 4, 6]
#range 1–6
#Output: [3, 5]
l1=[]
for i in range(1,7):
    if i not in l:
        l1.append(i)
print(l1)

"""
Q1. Find the most frequent word in a sentence.
Input: "apple banana apple orange apple"
Output: "apple"
"""
a="apple banana apple orange apple"
a1=a.split()
f=""
max=0
for i in a1:
    c=a1.count(i)
    if c>max:
       max=c
       f=i
print(f)

#Q2. Group numbers by even and odd values.

l= [1, 2, 3, 4, 5, 6]
#Output: {'even': [2, 4, 6], 'odd': [1, 3, 5]} 
d={'even':[],'odd':[]}

for i in l:
    if i%2==0:
        d['even'].append(i)
    else:
        d['odd'].append(i)
print(d)    

"""
Q3. Count total elements in a nested list.
Input: [1, [2, [3, 4], 5]]
Output: 5
"""
l= [1, [2, [3, 4], 5]]
#Output: 5
l1=[]
for i  in l:
    if type(i)==list:
        l.extend(i)
    else:
        l1.append(i)
print(len(l1)) 

l = [1, 2, 3, [4, 5, 6, [8, 8, [9, [9]]], 9]]
i = 0
while i<len(l):
    if type(l[i]) == list:
        l[i:i+1] = l[i] # [4, 5, 6, [8, 8, [9, [9]]], 9]
    else:
        i=i+1        
print(l)

# Q4. Merge multiple dictionaries into one.
d= {'a': 1}, {'b': 2}, {'c': 3}
#Output: {'a': 1, 'b': 2, 'c': 3}  
m={}
for i in d:
    m.update(i)
print(m)  

"""
Q5. Write a recursive function to calculate the Fibonacci series.
Input: n = 6
Output: [0, 1, 1, 2, 3, 5]
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(6)])

d = {1: "h", 2: "k", 3: "ho"}
print(d)
l = ["one", "two", "three", "four"] 
d = {}
for i in l:
    length = len(i)
    if length not in d:
        d[length] = [i]
    else:
       d[length].append(i)
print(d)

# pallindrome
l=[1, 2, 3, 2, 1]
if l==l[::-1]:
    print("palindrome")
else:
    print("not pall")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
result = []

# Step by 3: i will be 0, 3, 6, 9
for i in range(0, len(l), 3):
    # Slice the list from the current index to index + 3
    result.append(l[i : i + 3])

print(result)  
l=[5,2,3]
#l1=sorted(l)
l.sort()# sort change original list
l1=sorted(l) # sorted create new list
print(l)
print(l1)

l= [1, [2, [3, 4], 5]]
#Output: 5
l1=[]
for i  in l:
    if type(i)==list:
        l.extend(i)
    else:
        l1.append(i)
print(len(l1)) 

l=[1, 2, 3, 2, 1]
if l==l[:: -1]:
    print("pallindrome")
else:
    print("not pallindrome")    



       






