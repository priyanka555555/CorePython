# s="naabccaabbbcabb"
# #output a2b1c2a2b3c1a1b1
# n=len(s)
# # print(n)
# s1=""
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c=c+1#3
       
#     else:
#          s1=s1+s[i-1]+str(c)#c1a1
#          c=1
# # print(s1) 
# res=s1+s[-1]+str(c)         
# print(res) 

st="abcabdebac"
#"'abc','bca','cabde','abde','bde','debac','ebac','bac','ac','c'"
l=[]
max=0
for i in range(len(st)):
    s=""
    for j in range(i,len(st)):
        if st[j] in s:
            break
        s=s+st[j]
    l.append(s)  
print(l)

s1=""
for i in l:
    
    if len(i)>max:
        max=len(i)
        s1=i
print(s1)        

st="abcabdebac"
#"'abc','bca','cabde','abde','bde','debac','ebac','bac','ac','c'"
l=[]
for i in range(len(st)):
    s=""
    for j in range(i,len(st)):
        if st[j] in s:
            break
        else:
            s=s+st[j]
    l.append(s)        
print(l) 
max=0 
s1=""
for i in l:
    if len(i)>max:
        max=len(i)
        s1=i
print(s1) 

l=[5,4,3,4,3,2,3]
# output [1,2,4,5,7]
max=0
l1=[]
for i in range(len(l)-1,-1,-1):
   if l[i]>=max:
       l1.append(i+1)
       max=l[i]
l1.reverse()
print(l1)         








     



