thislist=["hello","java","python","php"]
thislist=list(("hello","java","python","php"))
list1=[1,2,3,4,5]
list2=[True,False]
print(len(thislist))
print(type(list1))
print(list1)
# Access index and negative index
print(thislist[2])
print(thislist[-2])
print(thislist[1:3])
print(thislist[:4])
# Change item value
thislist[1]="priya"
thislist[1:3]=["niya","siya"]
thislist[1:3] = ["watermelon"]
thislist.insert(2,"jiya")
# append items To add an item to the end of the list, use the append() method:
thislist.append("orange")
#Extend List To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
thislist.remove("banana")
thislist.pop(1)
thislist.pop()
thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#del thislist
"""
for i in range(len(thislist)):
   print(thislist[i])
"""
"""
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
"""
"""
fruits=["apple","banana","orange","kiwi"]
newlist=[]
for x in fruits:
    if "b" in x:
        newlist.append(x)
print(newlist)   
"""
l1=[1,2,3,4]
l2=[3,4,5,6]
print(id(l1))
l1[0]=11
print(id(l1))
print(l1[1:4])
l1.append(12)# add one item end of the list
print(l1)
l1.extend(l2)# append
print(l1)
l1.insert(0,10)# to add element using index
print(l1)
l1.remove(10)
print(l1)
l1.pop()
print(l1)
l1.pop(1)
print(l1)
del l1[3]
print(l1)
#print(x for x in l1 if 11  in x)
l1.sort()
l1.reverse()
print(l1)

#### tuple
t1=(1,2,3,4,1)
print(t1.count(1))
print(t1.index(2))
## set
s1={1,2,3,4,6}
s2={1,2,3,4,5}

#s1.update(s2)
#s1.remove(1)# it will throw error if specify value is not present in the set
#s1.discard(18) # it not return error if the specify value is not preset
#s1.pop()
#del s1# delete the set completely
#s1.clear()# empties the set
# join the set
#s3=s1.union(s2)# create new object and combine both set
#print(s3)
#s3=s1.intersection(s2)
#s3=s1.difference(s2)
s3=s1.symmetric_difference(s2)
print(s3)
s1.add(11)
print(s1)
######################################33
#programs
# 
#output={1:3,2:1,3:1}
l=[1,1,2,3,1]
d={}
for i in l:
    #print(i)
    if i in d:
        d[i]=d[i]+1 
    else:
         d[i]=1 
print(d)        
######################################### remove duplicates
l=[1,1,2,3,1]
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(r)

########################## count first ocurence
l=[1,2,1,2,3,4,3,4,7,4,9]
for i in l:
    if l.count(i)==1:
        print(i)
        break

#############################
print("*"*50)
l1=[1,2,3,4]
l2=["A","B","C","D"]
#output{1:"A",2:"B",3:"C",4:"D"}
l3={}

# for i in range(len(l1)):
#     l3[l1[i]] = l2[i]

# print(l3)

# for k ,v in zip(l1,l2):
#     l3[k] = v 
# print(l3)

d = dict(zip(l1,l2))
print("HIII")
print(d)



# for i in l1:
#   for j in l2:
#    if i in l3:
#       l3[i]=l3[i]+l2[j]
  
#   else:
#      l3[i]=1
# print(l3)       


##################
print("skh")
l1=[1,2,3,4]
l2=["A","B","C","D"]

l3={}
i=0
while i < len(l1):
    l3[l1[i]] = l2[i]  
    i=i+1 
    
print(l3)          
#########################3
l=[2,3,4,5,6,12,14] 
#s=set((2,3,4,5,6,12,14))
for i in l:
    if i%2!=0:
       print(i)

#################33
l = [2,3,4,5,6,12,14]
d = {}

for i in range(len(l)):
    if l[i]%2!=0:
        d[i]=l[i]       
print(d)      
 ########3333
l = [2,3,4,5,6,12,14]

res = {x for x in l if x % 2 != 0}  
print(res)
#################
s1={1,2,3,4}
s1.add(5)
print(s1)

l=[2,3,4,5,6,12,14] 
s=set()
for i in l:
    if i%2!=0:
       s.add(i)
print(s)
#############################
l=[[1,2,3],
   [2,3,4],
   [3,4,5]]
# print(l[0][1])
print("*"*50)

#################################
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

#wap first largest
l=[1,2,9,4,7]
fs=l[0]
for i in l:
    if i>fs:
        fs=i
print(fs)    
print("################################################")
#wap second largest first smmalest
l=[4,3,5,7,1,9]
fs=l[0]
fl=l[0]
for i in l:
    if i<fs:
     fs=i
    elif i>fl:
        fl=i 

print("first smmalest ",fs)
print("first largest ",fl)        

#wap accending order
l=[11,3,5,7,1,9]

ln=len(l)
for i in range(ln):
    for j in range(i+1,ln):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
    
    print(l[i])
#print(set(l)) #{1, 3, 5, 7, 9, 11} 
#print(l) # [1, 3, 5, 7, 9, 11] 
# ans shold be in list
print("next program")    
############3second largest
l=[11,3,5,7,1,9]
ln=len(l)
s_l=l[0]
for i in range(ln):
    for j in range(i+1,ln):
        if l[i]<l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
    #11,9,7,5,3,1
print("second largest ",l[1])      

print("********")

l = [11, 3, 5, 7, 1, 9]
ln = len(l)
for i in range(ln):
    for j in range(i + 1, ln):
        if l[i] > l[j]:
            t = l[i]
            l[i] = l[j]
            l[j] = t
print(l) 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Interchange first and last element
l = [11, 3, 5, 7, 1, 9]
l[0],l[-1]=l[-1],l[0]
print(l) #output [9, 3, 5, 7, 1, 11]

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# swap two element
l = [11, 3, 5, 7, 1, 9]
l[2],l[1]=l[1],l[2]
print(l)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Reverse a List
l = [11, 3, 5, 7, 1, 9]  
l.reverse()
print(l)  
print("next")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Cloning or Copying a List
"""
l = [11, 3, 5, 7, 1, 9]  
l.copy()
print(l)
"""
#Count element in a List
l = [11, 3, 5, 7, 1, 9]  
print(l.count(3))

################33
l = [11, 3, 5, 7, 1, 9] 
sum=0
ln=len(l)
evg=0
for i in l:
    sum=sum+i
    evg=sum/6
print(sum)  
print(evg)  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ postive number in list
###########
a = [-10, 15, 0, 20, -5, 30, -2] 
for i in a:
    if i>0:
     print(i)
#Using filter()
l1 = [-10, 15, 0, 20, -5, 30, -2]
l=list(filter(lambda x:x>=0,l1)) 
print(l)  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#ount positive and negative numbers in a List
a = [-10, 15, 0, 20, -5, 30, -2]
cp=0
cn=0
for i in a:
    if i>=0:
        cp=cp+1
    else:
        cn=cn+1    

print("count of postive number ",cp)
print("count of negative number ",cn)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Remove multiple elements from a List

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
######Remove empty tuples from a List  
l=[(1,2),(),(1,3),()]

for t in l:
  ln=len(t)
  if ln!=0:
       print(list(t))

#another way
l2=[(1,2),(),(1,3),()]
lm=list(filter(None,l2))# rmove all falsy value
print(lm)       
###################################33
#Remove first element from List
l = [11, 3, 5, 7, 5, 9] 
l.pop(0)
print(l)
## Get Unique values from a List
l = [11, 3, 5, 7, 1, 9] 
s=set(l)
print(s)
############################################################3
fruits=["apple","banana","orange","kiwi"]
newlist=[]
for x in fruits:
    if "b" in x:
        newlist.append(x)
print(newlist)  

##############################practice of the list
l=[1,2,3,4]
l1=[1,2,3,4,5]
#access+changes
l[0]=10
print(l)

l[1:3]=[11,12]
print(l)

l.append(20)
print(l)

l.extend(l1)
print(l)
l.insert(10,30)
print(l)
l.remove(30)
print(l)
l.pop()
print(l)
l.pop(0)
print(l)
del l[1] 
print(l)
#del l
#l.clear()
print(l)
#list comprehension
l3=[1,2,3,4,5,6]
s=[x for x in l3 ]
print(s)


l=[4,3,5,7,1,9]
fs=l[0]
fl=l[0]
for i in l:
    if i<fs:
     fs=i
    elif i>fl:
        fl=i 

print("first smmalest ",fs)
print("first largest ",fl)        

"""
l=[[1,2,3],[2,3,4],[2,3,5]]
d={}

for i in range(len(l)):
  #d[i]=0
 
  for j in range(len(l[i])):
    a=0
    a=a+l[i][j]#
    d[i]=a # 0
print(d) 
#0:6,6:19,19:29
0:3,0:4,0:5
"""
l=[5,4,3,4,3,2,3]
l = [25, 1, 4, 20, 5, 9, 3, 12, 2, 7]

# 1. Corrected Sort (Ascending: 0, 1, 2...)
for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]: # To sort ascending, we swap if the current is smaller
            t = l[i]
            l[i] = l[j]
            l[j] = t

print("Sorted List:", l) 

# 2. Corrected Filtering
arr = [2, -3, 4, 1, 1, 7]
#Output: 3
for i in arr:
    if i<0:
     print(abs(i))    

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]

# Separate positives and negatives
l1 = []
l2 = []

for i in arr:
    if i >= 0:
        l1.append(i)
    else:
        l2.append(i)

# Alternate merge
p = 0
n = 0
result = []

while p < len(l1) or n < len(l2):
    if p < len(l1):
        result.append(l1[p])
        p += 1
    if n < len(l2):
        result.append(l2[n])
        n += 1

print(result)

l=[1,2,3]
# 7
l1=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        l1.append(l[i:j+1])
print(l1) 
max=0
#l1=[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
l2=[]
for i in l1: 
    s=0
    for j in i:
        s=s+j
    l2.append(s)    
result=sorted(l2)
print(result[-1]+1)    
l=[1,2,3]
res=1
for x in l:
    if x <= res:
        res =res+x 
   
print(res)  
###############################################################################
l = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3 
l1=[]
#Output : [4, 3] 
for i in l:
    c=0
    for j in l:
        if i==j:
           c=c+1
        if c>=K and i not in l1:  
          l1.append(i)   

print(l1)
#########################################
l = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3 
l1=[]
for i in l:
    
    if l.count(i)>=K and i not in l1:
        l1.append(i)
print(l1)

#############################################
a = [1, 2, 3]
from itertools import  permutations
for i in permutations(a):
    print(i)
a = [1, 2, 3]

for i in range(3):
    for j in range(3):
        for k in range(3):
            
            # Check if the indexes are not the same
            if i != j and j != k and i != k:
                print(a[i], a[j], a[k])



a = ["a", "b"]
b = [1, 2]
# [('a', 1), ('a', 2), ('b', 1), ('b', 2)]
l=[]
d={}
for i in a:
    for j in b:
       l.append((i,j))
        
print(l)  

# Input1: 1 1 2 3 4 5 1 2 1 
#Output1: 2 3 4 5 2 
l=[1 ,1, 2 ,3 ,4, 5 ,1 ,2 ,1]
l1=[]
for i in l:
    if i!=1:
       
       l1.append(i)
         
print(l1)
a = ['Gfg', 'is', 'best'] 
b = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] 
#['Gfg', 'is', 'best', 'is', 'Gfg', 'Gfg', 'Gfg', 'best', 'is', 'is', 'best', 'Gfg']
l1=[]
for i in b:

    if i not in a:
        l1.append(a[i])
print(l1)        
###############################3
l = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2 
l1=[]
#Output : [(4, 5, 5, 4)]
for i in l:
    if i.count(K)==N:
        l1.append(i)
print(l1)
a = [(2, 'B'), (1, 'A'), (3, 'C')]
b = sorted(a, key=lambda x: x[0])
print(b)

r1 = 0 
r2 = 10 
x=list(range(r1,10))
print(x)


########################3
l=[1,2,3]
from itertools import permutations
for i in permutations(l):
    print(i)