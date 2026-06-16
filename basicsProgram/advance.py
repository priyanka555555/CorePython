arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
s5=set()
sr1=[]
for i in arr:
   if i not in s5:
      s5.add(i)
   else:
      sr1.append(i)    
print(s5) 

list = [4, 7, 8, 3, 2, 1, 9]
#test=str(list)
delim = "*"
st="" 
#Output : 4*7*8*3*2*1*9 
for i in list:
   st=st+str(i)+"*"
st=st[:-1]   
print(st)  

s = "geeksforgeeks is best"
li=[2,4,7,10]
st=str(li)
ch="*"
for i in st:
     s=s.replace(i,ch)
print(s)       
li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]





      # Python3 code to demonstrate working of
# Similar characters Strings comparison
# Using dictionary

# initializing strings
test_str1 = 'e:k:s:g'
test_str2 = 'g:e:k:g'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing delim
delim = ':'

# initializing dictionaries
dict1 = {}
dict2 = {}

# loop through characters in string 1
for char in test_str1.split(delim):
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
print(dict1)        

# loop through characters in string 2
for char in test_str2.split(delim):
    if char in dict2:
        dict2[char] += 1
    else:
        dict2[char] = 1
print(dict1)         

# compare dictionaries
res = True
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        continue
    else:
        res = False
        break

# printing result
print("Are strings similar : " + str(res))

li= ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
s=str(li)
# output [gfg,xit,is]
# Suffix to remove
s1= 'x'
for i in li[:]:
    if i.endswith(s1):
        li.remove(i)
print(li) 

#['G', 'e', 'k', 's']
s = "hello word"
result = ""
d=""
for ch in s:
    if ch  not in result:
        result =result+ch
    else:
        d=d+ch

print(d)

"""
Input : test_list = ["gfgBest", "forGeeks", "andComputerScienceStudents"] 
Output : ['gfg Best', 'for Geeks', 'and Computer Science Students'] 
Explanation : Words segregated by Capitals.
"""
lst = ["gfgBest", "forGeeks", "andComputerScienceStudents"] 
l=[]
for i in lst:
    for j in i:
      if j.isupper():
         i=i.replace(j," "+j)  
      
    l.append(i)  
print(l)

# Remove words containing list characters
a = ['gfg', 'is', 'best', 'for', 'geeks']
li=[]

#output=['is','for']
remove_chars = ['g', 'e']
for i in a:
    for j in i:
        if j in remove_chars:
           break
    else:   
     li.append(i)
print(li)  
print("1.....................")          

"""
Input : test_list = ["geeksforgeeks", "best", "geeks", "and"], pref = "geek" 
Output : [['geeksforgeeks', 'best'], ['geeks', 'and']] 
Explanation : At occurrence of string "geeks" split is performed.
"""
l1=["geeksforgeeks", "best", "geeks", "and"]
pref = "geek"
l2=[]
for i in l1:
    if i.startswith(pref):
       l2.append([i]) 
    else:
        l2[-1].append(i)    
print(l2) 

######################################################33333333
#Convert Character Matrix to single String
a = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
#gfgisbest
s=""
for i in a:
    for j in i:
      s=s+str(j)
print(s)
print("1..................")
"""
nput : test_list1 = ["Gfg", "is", "not", "best", "and", "not", "CS"], 
test_list2 = ["Its ok", "all ok", "wrong", "looks ok", "ok", "wrong", "thats ok"], sub_str = "ok" 
Output : ['Gfg', 'is', 'best', 'and', 'CS'] 
Explanation : All retained contain "ok" as substring in corresponding idx, e.g : Gfg -> Its ok ( has ok ) as substr.
"""
"""
Input : test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T'], repl_chr = '*', ret_chr = 'G' 
Output : ['G', '*', 'G', '*', '*', '*', '*', '*', '*'] 
Explanation : All characters except G replaced by *
"""
tl = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
res=[]
repl_chr = '*'
ret_chr = 'G'
s=[]
for i in tl:
    if i=='G':
       res.append(i)#G,G
    else:
        res.append("*")#
print(res)        

##############333
#Converting all Strings in a list to integers
a = ['2', '4', '6', '8']
#[2, 4, 6, 8]
for i in range(len(a)):
    a[i]=int(a[i]) 
print(a)   
#######################################################3
a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]
#[{'name': 'Alice', 'age': 25, 'city': 'New York'}, {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': 22, 'city': 'Chicago'}]

li = []
for value in b:
    d = {}
    for i in range(len(a)):
        d[a[i]] = value[i]
    li.append(d)

print(li)

########################333
a = [["a", 1], ["b", 2], ["c", 3]]
d = {}
for i in a:
    d[i[0]] = i[1]
print(d)

a = [[1, 2], [3, 4], [5, 6]]
b = [[3, 4], [5, 7], [1, 2]]
c=[]
#[[5, 6], [5, 7]]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
           c.append(a[i])
print(c)         

# Uncommon elements in Lists of List
a = [[1, 2], [3, 4], [5, 6]]
b = [[3, 4], [5, 7], [1, 2]]
c=[]
#[[5, 6], [5, 7]]
for i in range(len(a)):
        if a[i] not in b:
           c.append(a[i])
for i in range(len(b)):
        if b[i] not in a:
           c.append(b[i]) 
print(c)  

# Select Random value from list of lists
"""
Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix.
"""
import random
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
for i in test_list:
    for j in i:
       b= random.randint(0,j)
print(b)

# Reverse Row sort in Lists of List

a = [[4, 1, 6], [7, 8], [4, 10, 8]]
for i in a:
    i.sort(reverse=True)
print(a)


#####################################################3333
####################################################33333
#Advance List Programs
#Count unique items in a list
l = [1, 2, 2, 5, 8, 4, 4, 8]
l1=[]
c=0
for i in l:
    if i not in l1:
        l1.append(i)
        c=c+1
print(c)

# List product excluding duplicates
l = [1, 3, 5, 6, 3, 5, 6, 1]
s=set(l)
n=1
for i in s:
  n=n*i
print(n)  

#Extract elements with Frequency greater than K
lst = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
l = []
for i in lst:
    if lst.count(i) > K and i not in l:
        l.append(i)
print(l)

          

   
















