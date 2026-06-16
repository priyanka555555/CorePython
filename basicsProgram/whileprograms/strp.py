
"""
s="swiss"
for i in s:
   if s.count(i)==1:
    print(i)
"""
def fun(strr):
    for ch in strr:   
        if strr.count(ch) == 1:
          print(ch) 
          break      
    
fun("swiss")
print("1........................")
def fun1(str1):
   print(str1[0])

# fun1("Priyanka")   
print("1........................")

def fun1(str1):
   for i in str1:
      if str1.count(i)==1:
         print(i)
         break
fun1("Priyanka")  

#####################################333
def fun(strr):
    for ch in strr:   
        if strr.count(ch) == 1:
          print(ch) 
          break      
    
fun("swiss")

print("1............................")


def fun(s):
 for ch in range(len(s)):
    if ch==1:
       print(s[ch])
       
fun("swiss")

print("1............................")

def fun(s):
   for i in range(len(s)):
      c=0
      for j in range(len(s)):
         if s[i]==s[j]:
            c=c+1
      if c==1:
         print(s[i]) 
         break     
fun("swiss")

print("1............................")

s="hello"
print(id(s))
s1=s.upper()# create a new object
print(id(s1))




