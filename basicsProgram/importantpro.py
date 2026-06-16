s="aabbccddeaa"
#output {a:4,b:2,c:2,d:2,e:1}
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)# #output {a:4,b:2,c:2,d:2,e:1}
res=""
for key,value in d.items():
    res=res+key+str(value) 

print(res)      

# 2. 
s="aabbccddeaa"
#output a2b2c2d2e1a2
s1=""
count=1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count=count+1 
    else:
        s1=s1+ s[i-1] + str(count) 
        count = 1
#print(s1) 
res=s1+s[-1]+str(count)       
print(res) 

#Remove duplicates from a string
s = "geeksforgeeks"
s1=""
for i in s:
    if i not in s1:
        s1=s1+i
print(s1)        

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

max_consecutive = 1
current_count = 1

for i in range(len(l) - 1):
    if l[i+1] == l[i] + 1:
        current_count += 1
    else:
        if current_count > max_consecutive:
            max_consecutive = current_count
        current_count = 1
if current_count > max_consecutive:
    max_consecutive = current_count

print(max_consecutive) 

l = [1, 2, 3, [4, 5, 6, [8, 8, [9, [9]]], 9]]
l1 = []

for i in l:
    if type(i) == list:#[4, 5, 6, [8, 8, [9, [9]]], 9]
        l.extend(i)
    else:
        l1.append(i)

print(l1)
print("next...................................")

l = [1, 2, 3, [4, 5, 6, [8, 8, [9, [9]]], 9]]
i = 0
while i<len(l):
    if type(l[i]) == list:
        l[i:i+1] = l[i] # [4, 5, 6, [8, 8, [9, [9]]], 9]
    else:
        i=i+1        
print(l)

list = [1,2,3] 
"""
 [1], [1, 2], [1, 2, 3], [1, 3]
 [2], [2, 3], [3]
"""
for i in range(len(list)):#0,1,2
    for j in range(i, len(list)):#(0,3),(1,3),(2,3)
      
        print(list[i:j+1]) #[0:1],[0:2],[0:3],[1:2],[1:3],[2:3]


l="helloworld"
#output : h1e1l3o2w1r1d1        
d={}
res=""
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for key,value in d.items():
    res=res+key+str(value)  
print(res)

st="h@%$^*(5ello123!@3"
#output "hello"
s1=""
s2=""
for i in st:
    if i.isalpha():
        s1=s1+i  
print(s1)

st="h@%$^*(5ello123!@3"
#output: "h5ello1233"
s2=""
for i in st:
    if i.isalpha():
        s2=s2+i
    elif i.isdigit():
        s2=s2+i
print(s2)
"""
dic = {"name":"ram","age": 12, "phone": 12345678909}
#out = {"first_name":"ram", "age": 12,"no": 12345678909}
for key in dic:
    if key=="name":
        dic["first_name"]=dic.pop("name")
    elif key=="phone":
        dic["no"]=dic.pop("phone")
    else:
        dic[key]=dic[key]    
print(dic)

dic = {"name":"ram","age": 12, "phone": 12345678909}
#out = {"first_name":"ram", "age": 12,"no": 12345678909}
dic["first_name"]=dic.pop("name")
dic["no"]=dic.pop("phone")
print(dic)
"""
l=[1,1,1,2,2,3,3,4,4,4,6,6,6,7,8,7]
#output{1:[1,1,1]:[2,2],3:[3,3],4:[4,4,4],6:[6,6,6],7:7,8:[8,8,8]}
d={}
for i in l:
    if i in d:
        d[i].append(i) 
    else: 
     d[i]=[i] 
print(d)  

#######################################33333
############################################
############################################

s="aabccaabbbcab"
s1=""
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c=c+1
       
    else:
         s1=s1+s[i-1]+str(c)
         c=1
print(s1) 
res=s1+s[-1]+str(c)
print(res)

list = [1,2,3] 
for i in range(len(list)):
    for j in range(i,len(list)):
        print(list[i:j+1])

l=[1,1,1,2,2,3,3,4,4,4,6,6,6,7,8,7]
d={}
for i in l:
    if i in d:
        d[i].append(i)
    else:
        d[i]=[i] 
print(d)           
for i in d:
    if len(d[i])==1:
        d[i]=i
print(d)  
##################################333
s="geekforgeeks"
# output [o,r,k,s]
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d) 
l=[]
for key, value in d.items():
    if value%2!=0:
        l.append(key)
print(l) 
########################################################

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

############################################################
s="priyanka patel"
# output "PrIyaNkA pAtEl"
s1=""
for i in range(len(s)):
    if i%2==0:
        s1=s1+s[i].upper()
    else:
        s1=s1+s[i].lower() 
print(s1)

############################################################################33

s="hello"
s1="hello"

"""
list comprehention is a compact way to create a new list by applying an expression to each item in an exiting list
"""          
    





      




