"""
Remove K length Duplicates
"""

s="aabbccddeaa"
#a2b2c2d2e1a2
s1 =  {}    
for i in s:
    if i in s1:
        s1[i]=s1[i]+1
    else:
        s1[i]=1
print(s1)        

s = "aabbccddeaa"
c1 = {}
for i in s:
    if i in c1:
        c1[i] = c1[i] + 1
    else:
        c1[i] = 1
print(c1)        
res = ""
for key, value in c1.items():
    res=res+ key + str(value)

print(res)


# Check if string is symmetrical or palindrome
s="madam"
rev="" 
for i in s:
    rev=rev+i
if s==rev:    
  print("pallindrome") 
else:
  print("not pallindrome") 

#Length of String
s1="madam" 
print(len(s1))

#Reverse words in a String
h="hello world java"
for i in h:
   print(i)
   
s = "aabbccddeaa"
# a2b2c2d2e1a2
c1={}
for i in s:
    if i in c1:
        c1[i]=c1[i]+1
    else:
        c1[i]=1
print(c1)        
res=""
for key,value in c1.items():
    res=res+ key+str(value)
    
print(res)
############################333
s="aabbccabb"
s1=""
count=1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count=count+1 
    else:
        s1=s1+ s[i-1] + str(count) 
        count = 1
print(s1) 
res=s1+s[-1]+str(count)       
print(res)

# 3.Avoid Spaces in string length
h="hello world python"
print(h.replace(" ",""))

h="hello world python"
h1=""
for i in h:
    if i!=" ":
       h1=h1+i
print(h1) 

# Print even-length words in string

h="hello world python helopr"
h2=h.split()
h1=[]
for i in h2:
    if len(i)%2==0:
        h1.append(i)
print(" ".join(h1))

s1 = "apple"
s2 = "grape"
a1=s1.lower()
a2=s2.lower()
c=0
for i in set(a1):
    if i in a2:
     c=c+1
print(c)

# Count number of vowels using sets
s="helloworlda"
v="aeiou"
c=0
for i in s:
    if i in v:
      c=c+1
print(c) 

#Remove duplicates from a string
s = "geeksforgeeks"
seen = set()  
res = ""      
for char in s:
    if char not in seen:
        seen.add(char)
        res=res+char
print(seen)
print(res)

# first occerence
s="geeksforgeeks"
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c=c+1 
    if c==1:            
     print(s[i]) 
     break 

#Maximum frequency character
st="geeksforgeeks" 
for i in range(len(st)):
    c=0
    for j in range(len(st)):
        if st[i]==st[j]:
            c=c+1 
    if c>=4:
     print(st[i]) 
     break
#another way 
print("1.................................")

##########3
s = "hello world"
max_char = ''
max_count = 0

for char in s:
    count = s.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print(max_char)
print("1............")
#extract characters with odd frequencies
s = "hello world"
s1=[]
j=""
for i in s:
    count=s.count(i)#1
    if count%2!=0:
     s1.append(i)
print("".join(set(s1)))

print("1............")

#Specific Characters Frequency
s = "hello world"
l1="o" 
c=0
for i in s:
    if i in l1:
      c=c+1
print(l1,c)  
print("1............")

# Frequency of Numbers in String 
s = "geeks4feeks is No. 1 4 geeks"
digit="1234567890"
c=0
for i in s:
   if i in digit:
     c=c+1
print(c)

# remove special character
n = "Geeks$For$Geeks"
sp="$"
s=[]
for i in n:
   if i not in sp:
      s.append(i)
print("".join(s))
print("1............")

"""
Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4
Output : hello geeks geeks computer 
         science portal
"""
str = "hello geeks for geeks  is computer science portal"
st=str.split()
store=[]
for i in st:
   if len(i)>=4:
      store.append(i)
print(store)      

print("1............")

"""
Input: "PythonProgramming", i = 6
Output: "Pythonrogramming"
"""
s = "PythonProgramming"
i = 6
st=[]
for j in range(len(s)):
   if j!=i:
     st.append(s[j]) 
print("".join(st))   


#Check if a given string is binary string or not
s = "101010000111"
for i in s:
 if i in "01":
      print("yes")
      break
 else:
      print("not")   

s = ["Lion", "Li", "Tiger", "Tig"]
a = "Lion"
for i in s:
   if i.startswith(a) or a.startswith(i):
      print(i,end=" ")

#Find uncommon words from two Strings
"""
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
Output: ['Learning', 'from'].
"""
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
a=A.split()
b=B.split()
l=[]
for i in b:
   if i not in a:
      l.append(i)
print(l) 

# Swap commas and dots in a String
"""
s = "14, 625, 498.002"
s1=s.replace(",",".")
for i in s1:
  print()
"""  
import itertools
s = "GFG"
li = [''.join(p) for p in itertools.permutations(s)]
print(li)

"""
Input: str = "Java"
Output: v
"""
str1 = "Javrkaa"
length = len(str1)
middle = length // 2
print(str1[middle])

# Convert integer to string
"""
n = 42
s = str(n)
print(s) # 42
"""
n="42"
s=int(n)
print(s)

#Split string into list of Characters
s = "geeks"
#Output: ['g', 'e', 'e', 'k', 's']
s1=[]
for i in s:
   s1.append(i)
print(s1)   

a = ['Geeks', 'for', 'Geeks']
print(" ".join(a))

#Convert a List of Characters into a String 
a = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(a))

#Convert Object to String

# Sort a list of strings
a = ["banana", "apple", "cherry"]
a.sort()
print(a)

#Convert tuple to string
tup = ('Learn', 'Python', 'Programming')
print(" ".join(tup))

#Check if String is Empty or not
s=""
if s=="":
   print("this is empty string")
else:
   print("not empty string")  

# Convert String to Set   
s = "Geeks"
s1=set(s)
print(s1) 

s={'G', 'e', 'k', 's'}
s1="".join(s)
print(s1)

# 
s = "Python is Fun!"
v="aeiou"
for i in s:
   if i in v:
      print(i)
#####################################3333
# ######################################3
#Repeat the Strings   
a = "Hi"
b ="There"
c=a+b+a
print(c)

#Convert String to LowerCase
s="Hello"
print(s.lower())

#Reverse String
s = "mam"
#Output: "olleH"
rev=""
for i in s:
   rev=i+rev
if rev==s:
      print("pallindrome")
else:
   print("not pallindrome")      


# Find Pattern
s = "Hello"
p = "llo"
#Output: 2
print(s.index(p))

#Decimal number to binary number
#Reverse Words

s="hello world java"
s1=s.split()
rev=""
for i in s1:
   rev=i+" "+rev
print(rev) 


#################3
s = "Hello"
#Output: ell
print(s[1:4])

# c1 = 'a', c2 = 'z'
#Output: "a b c d e f g h i j k l m n o p q r s t u v w x y z "
c1 = 'a'
c2 = 'z'
l=[]
for i in range(97,123):
   s=chr(i)
   l.append(s)
print(" ".join(l))

#Advance String Programs
#Convert numeric words to numbers
   

print("1........................")
"""
arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
#[4, 5, 3, 8, 2, 1, 7]
s5=set()
sr1=[]
for i in arr:
   if i not in s5:
      s5.add(i)
   else:
      sr1.append(i)
        
print(len(s5))  
"""  

d = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
s = "four zero one four"
d1={}
for key,value in d.items():
    s=s.replace(key,value)
print(s)  

s = "aaabbccaaaa"
c=1
s1=[]
#['aaa', 'bb', 'cc', 'aaaa']
for i in range(len(s)-1):
   if s[i]==s[i+1]:
      c=c+1
   else:
      s1.append(s[i]*c)
      c=1 
s1.append(s[-1]*c)      
print(s1) 

#  left Rotate a string
s="GeeksforGeeks"
d=2
left=""
right=""
#Output: Left Rotation: "eksforGeeksGe" 
#Right Rotation: ksGeeksforGee

for i in range(2,len(s)): 
   left=left+s[i]
print(s1)  
for i in range(2):
   left=left+s[i]
print(left) 

#Right Rotation: ksGeeksforGee
s1="GeeksforGeeks"
d=2
right=""
n=len(s1)
for i in range(n-d,n):
 right=right+s1[i]
for i in range(n-d):
   right=right+s1[i]
print(right) 

print("1.....................")
s = "hello world hello everyone"
s1=s.split()
d={}
for i in s1:
   if i in d:
      d[i]=d[i]+1
   else:
      d[i]=1
print(d)

g='GFGaBstuforigeeks' 
#Output : ['GFG', 'Bst', 'f', 'r', 'g', 'ks']
res=[]
temp=""
v="aeiouAEIOU"
for i in g:
   if i in v:
      if temp!="":
         res.append(temp)# 
         temp="" 
   else:
      temp=temp+i # ks
if temp!="":
 res.append(temp)     
print(res)

#Convert Snake case to Pascal case
s= 'geeksforgeeks_is_best'
#GeeksforgeeksIsBest
res = ''.join(word.capitalize() for word in s.split('_'))
print(res)

#Avoid Last occurrence of delimitter
"""
correct program
list = [4, 7, 8, 3, 2, 1, 9]
#test=str(list)
delim = "*"
st="" 
#Output : 4*7*8*3*2*1*9 
for i in list:
   st=st+str(i)+"*"
st=st[:-1]   
print(st)   
"""
s = "geeks"
r=1
left=""
right=""
ln=len(s)
#left shift = "eeksge"
#right shift = "ksgee"
for i in range(1,ln):
   left=left+s[i]
left=left+s[:2]   
print(left) 

for i in range(ln-2,ln):
   right=right+s[i]
right=right+s[:3]   
print(right)   
###########################################################################33
# Mirror Image of String
sr = 'void'
# output= biov
srt=""
for i in sr:
   srt=i+srt
print(srt.replace('d','b')) 

####################################
"""
text = "apple orange banana"
words_to_replace = ["apple", "banana"]
Output: "K orange K"
"""
text = "apple orange banana"
words_to_replace = ["apple", "banana"]
for i in words_to_replace:
   text=text.replace(i,'k')
print(text)   

####################################33
# Replace Different characters in String at Once  
s = 'geeksforgeeks is best'
#output g11ksforg11ks 4s 61st
# Initializing mapping dictionary
d = {'e': '1', 'b': '6', 'i': '4'} 
for key,value in d.items():
   s=s.replace(key,value)
print(s)

# Multiple indices Replace
"""
s = "geeksforgeeks is best"
li = [2, 4, 7, 10]  # Indices to replace
ch = '*'  # Replacement character
output ge*k*fo*ge*ks is best
"""
s = "geeksforgeeks is best"
l=list(s)
li=[2,4,7,10]
ch="*"
for i in li:
     l[i]=ch
print("".join(l))   

#Remove multiple empty spaces
li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]
#['Hello world', 'Python is great', 'Extra spaces here']
s=[" ".join(i.split()) for i in li]
print(s) 

#Remove punctuation
s="Hello, World! Python is amazing."
#output Hello World Python is amazing
s1=list(s)
l=[]
rev=",!."
for i in s1:
   if i not in rev:
      l.append(i)
print("".join(l)) 

# Similar characters Strings comparison
# initializing strings
"""
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
"""

#####################################333
#Remove K length Duplicates
"""
Input: s = "abcababcabc", k = 3
Output: abcababc
Explanation: The repeated consecutive substring "abc" is reduced to a single occurrence, giving "abcababc".
""" 

# Find all duplicate characters
"""
Input: "GeeksforGeeks"
Output: ['G', 'e', 'k', 's']
"""
d = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
s = "four zero one four"
d1={}
for key,value in d.items():
    s=s.replace(key,value)
print(s) 
 







       
   












   
    












