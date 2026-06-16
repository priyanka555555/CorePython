"""""
str="hellool"
order=""
for ch in str:
    if ch not in order:
        order=order+ch
print(order)        
"""
"""
s = "helloworld"

for i in range(97, 123):   # a to z
    count = 0
    ch = chr(i)
    for l in s:
        if l == ch:
            count += 1
    if count > 0:
        print(ch, ":", count)
"""
"""
s = "helloworld"
ch="l"
count=0
for i in s:
    if i==ch:
        count=count+1
print(ch,":",count)     
"""
"""
s = "helloworld"

max_count = 0
max_char = ""

for i in range(97, 123):   # a to z
    count = 0
    ch = chr(i)
    for l in s:
        if l == ch:
            count += 1
    if count > max_count:
        max_count = count
        max_char = ch

print("Highest occurrence character:", max_char)
print("Count:", max_count)
 """
    #REVERSE EACH CHAR
# REVERSE EACH WORD
"""
s = "hello world,java, python"
st = s.split(" ")

for i in st:
    print(i[::-1], end=" ")

"""
"""
s = "hello world"
print(s[::-1])
"""
"""
#pallindrome
s = "madam"
rev = ""

for ch in s:
    rev = ch + rev

#print(rev)
if rev==s:
    print("pallindrome")
else:
    print("not pallindrome")
"""
"""
#armstrong number
n=151
sum=0
copy_n=n
order=len(str(n))
while(n>0):
    digit=n%10
    sum=sum+digit **order
    n=n//10
if(sum==copy_n):
    print("armstrong")
else:
    print("not armstrong")        
"""
s="hello world"
s1="l"
c=0
for i in s:
    if s1 in i:
        c=c+1
print("l",":",c)   
print("1...........")

s = "ppriyaa" 
s1 =  {}    

for i in s:
    if i in s1:
        s1[i]=s1[i]+1
    else:
        s1[i]=1
print(s1)        


l=[1,1,2,3,1]
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1 
    else:
         d[i]=1 
print(d) 

s = "hello"
v='aeiou'
s1=""
c=0
for i in s:
    if i not in v:
        s1=s1+i
        c=c+1
print(s1) 
print(c)       






