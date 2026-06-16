# 1. add two number
a=10
b=30
c=a+b
print(c)

# 2.Maximum of two numbers
a,b=10,5
if a>b:
    print("a is greater",a)
else:
    print("a is greater",b)    

#3.Factorial of a number using while loop
num=5
i=1
f=1
while i<=num:
   f=f*i
   i=i+1
print(f)
# Factorial of a number using for loop
f=1
for i in range(1,6):
    f=f*i
print(f)    

# 4.Find simple interest
p=5000
r=2
t=5
si=p*r*t/100
print(si)

# 5.An Armstrong number 153=1*1*1 + 5*5*5 + 3*3*3
num=151
"""
l1=0
for i in range(1,8):
    if i in l1:
        l1=l1+2
    else:
        l1=l1+1
print(l1) 

list=[1,2,3,4,5] 
sum=0 
for i in list:
    sum=sum+i
print(sum)  

list=[10,2,3,4,5]
list.sort(reverse=True)
print(list)

###########3
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

l=[5,4,3,4,3,2,3]
rev=[]
for i in range(len(l) - 1, -1, -1):
    rev.append(l[i])
print(rev)
"""

# output=[1,2,4,5,7][1,2,1,2]
"""
l=[1,2,3,4,5,6,7]
n=len(l)
l2=[]
l1=0
for i in range(n):#3
    
    if i%2==0:#4
     l1=l1+1
     l2=l1
     print("........",l2) 
    else:
     l1=0
     l1=l1+i
     l2=l1# 
 """
l=[5,4,3,4,3,2,3]
rev=[]
for i in range(len(l) - 1, -1, -1):
    rev.append(l[i])
print(rev)

st="hello javaj"
d={}

for i in range(len(st)):
    if st[i] not in "aeiou":
        if st[i] not in " ":
         c=0
         for j in range(len(st)):# e
            if st[i]==st[j] :# h==h
                c=c+1
            d[st[i]]=c # h:2 
print(d)        
   
#####################
st="hello javaj"
st1=""
d={}
for i in range(len(st)):
    if st[i] not in "aeiou":
      if st[i] not in " ":    
        if st[i] in d:
            d[st[i]]=d[st[i]]+1
        else:
            d[st[i]]=1

print(d)      
######## 1.AccendingList Item
l=[8,3,4,5,6,7]
ln=len(l)
for i in range(ln):
   for j in range(i+1,ln):
      if l[i]>l[j]:
         t=l[i]
         l[i]=l[j]
         l[j]=t
   print(l[i])     

# 2.change list item # replace
a = [10, 20, 30, 40]
a[0]=30
print(a)

# 3.Replace List Values
l=[10, 20, 30, 40]
print(l)

# 4. append
a = [2, 5, 6, 7]
a.append(10)
print(a)

# 5.insert
a = [2, 5, 6, 7]
a.insert(2,"hello")
print(a)

#6.extend
a = [2, 5, 6, 7]
b= [8, 5, 6, 7]
a.extend(b)
print(a)

#7. Remove List Item
b= [8, 5, 6, 7]
b.remove(8)
print(b)

# 8.Clear entire List
b= [8, 5, 6, 7]        
b.clear()
print(b) 

print("end................")
#9.Input: arr[] = [54, 43, 2, 1, 5] Just traverse and print the numbers.
#Output: 54 43 2 1 5
arr = [54, 43, 2, 1, 5]
for i in arr:
   print(i)
print("end................")   
# 10. Length of The List
l=[54, 43, 2, 1, 5]
print(len(l))
print("end................")

# 11.Sum The List
l=[54, 43, 2, 1, 5]
sum=0
for i in l:
   sum=sum+i
print(sum)   

print("end................")
# 12. Decrement List Values : Just decrement the numbers by 1.
l=[54, 43, 2, 1, 5]
for i in l:
   print(i-1)

print("end................")
# 13.Minimum of two numbers in Python
a=10
b=30
print(min(a,b))

print("end................")
# 14. Interchange first and last element
l=[54, 43, 2, 1, 5]
l[0],l[-1]=l[-1],l[0]
print(l)
print("end................")

# 15.Count element in a List
l=[4, 3, 2, 1, 5,4]
c=0
for i in l:
   c=c+1
print(c)
print("end................")

# 16.Sum and Average of List
a = [10, 20, 30, 40, 50]
sum=0
ln=len(a)
for i in a:
   sum=sum+i
   avg=sum/ln
print(sum) 
print(avg)   

# 17.Multiply All Numbers in the List
a = [1, 2, 3, 4, 5]
m=1
for i in a:
   m=m*i
print(m)   

# 18.Smallest number in a List
a = [6, 2, 3, 4, 5]
s=a[0]
for i in a:
   if i<s:
     s=i
print("smallest",s)  

#19.Largest number in a List
a = [6, 2, 3, 4, 5]
l=a[0]
for i in a:
   if i>l:
     l=i
print("largest",l) 

# 20. Second largest number in a List
a = [6, 2, 3, 4, 5]
for i in range(len(a)):
   for j in range(len(a)):
      if a[i]>a[j]:
         t=a[i]
         a[i]=a[j]
         a[j]=t
       
print("second largest",a[1]) 

# 21.Even numbers in a List
a = [6, 2, 3, 4, 5]
l=[]
for i in a:
   if i%2==0:
      l.append(i)
print("even number", l)

# 22. Count Even and Odd Numbers in a List
a = [6, 2, 3, 4, 5]
ec=0
oc=0
for i in a:
   if i%2==0:
      ec=ec+1
   else:
      oc=oc+1  
print("count of even no", ec)
print("count of odd no", oc)   

# 23.Positive numbers = 15, 20, 30
a = [-10, 15, 0, 20, -5, 30, -2] 
l=[]
for i in a:
   if i>0:
      l.append(i)
print(l)

# 24. Negative numbers in a List
lst = [12, -7, 5, 64, -14]
l=[]
#Output: -7, -14
for i in lst:
   if i<0:
     l.append(i)
print(l)   

# 25. Count positive and negative numbers in a List
a = [10, -20, 30, -40, 50, -60, 0]
cp=0
cn=0
for i in a:
   if i>=0:
      cp=cp+1
   else:
      cn=cn+1
print("count postive num",cp) 
print("count negative num",cn) 

# 26.Remove multiple elements from a List
a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]
l=[]
#Resulting list = [10, 30, 50, 70]
for i in a:
   if i not in remove:
      l.append(i)
print(l) 

# 27.Remove empty tuples from a List
l= [(1, 2), (), (3, 4), (), (5,)]
#Output: [(1, 2), (3, 4), (5,)]
l1=[]
for i in l:
   if len(i)!=0:
      l1.append(i)
print(l1)    

# 28.Print duplicates from a list of integers
a = [10, 20, 30, 20, 50, 60, 10]
s=set()
l=[]
for i in a:
   if i in s:
      l.append(i) 
   else:
      s.add(i)
print(l)  

# 29.Remove first element from List
a = [10, 20, 30, 20, 50, 60, 10]
a.pop(0)
print(a)

# 30 Remove duplicates from List or Get Unique Values from a List
#a = [1, 2, 2, 3, 4, 4, 5]
a = [1, 2, 1, 1, 3, 4, 3, 3, 5]
#output=[1, 2, 3, 4, 5]
o=[]
for i in a:
   
   if i not in o:
      o.append(i)
print(o)   

# 31. Merge Two Lists
l1 = [1, 2, 2, 3, 4, 4, 5]
l2 = [1, 2, 2, 3]
l1.extend(l2)
print(l1)
A = [4, 9, 1, 17, 11]
B = [9, 74, 21, 45]
#[9] output
