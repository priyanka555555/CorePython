#a,b,c=1,30,10
"""
if a>b:
    print(" a is greater than b")
else:
    print("b is greater than b")   
"""
"""
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")  
else:
    print(" c isgreater")      
    """
"""
if a%2==0:
    print("a is divisible by 2")
if b%2==0:
    print("b is divisible by 2") 
if c%2==0:
    pass       
"""
"""
x=True
if x:
    print("hello")
"""
"""
if a>b: print(" a is greater")
print("a") if a >b else print("b")
res=a if a>b else b
print(res)
"""
"""
if not a>b:
    print("yes")

if a>b and a>c or  b>c:
    print("a is")   
    """
"""
if a>b:
    if a>c:
        print(" is grater")
    else:
        print("b is greater")  
else:
    if b>c:
        print("b is greater")   
    else:
        print("c is greater")           
        """
"""
score=90
attendence=95
submitted=True
if score<92:
 if attendence>90:
   if submitted:
    print("you are aligble")
   else:
    print("you are not eligible") 
 else:
   print("pass but low attendence")   
else:
 print("fail")    
 """
"""
if a<b:
    if a<c:
        print("a is greater")
"""        
#match statement
"""


day=4
match day:
    case 1:
        print("monday") 
    case 2:
        print("tuesday") 
    case  3:
        print("wednesday")  
    case _:
        print("no case are amtches")
                
"""
"""
day=5
month=3
match day:
    case 1|2|3|4 if month==3:
        print(" today is not weekend")
    case 5|6 if month==3:
        print(" today is  weekend")
    case _:
        print("today ids weekend")    
"""
"""
a=10
if a>0:
    print("yes",10)
    print("yes",10)
    print("yes",10)
"""
"""
b,c=30,30
if b>c :
    print(20,"smmalest")
elif b==c:
    print(30,"c is greater")
else:
    print(99000)    
"""
"""
marks=90
if marks<80:
    print("you are the first division")
elif marks>50 and marks<60:
    print("you are the second division")
elif marks>40 and marks<50:
    print("third")  
else:
    print("there is no condition is true")          
    
email="priya@gmail.com"
num=12345
if len(email)<0:
    print(f"email is= {email}")
elif len(str(num))>0:
    print(num)   
 
 
# short hand
a,b=100,100
if a<b:print("a is smalest")
print("a") if a>b else print("b is greater")
#multiple if in one line
print("a") if a<b else print("=") if a==b else("b")
user=""
if user:
    print(f"username= {user}")
else:
    print("guest")

age = 25
is_student = False
has_discount_code = True
if(age>20 or age<20) and  not is_student and  has_discount_code:
    print("lsdmvmv")  


name="priya"
email="priya@gmail.com"
password=1234
if (name and email) and password:
    print(f"{name},{email},{password}")  

age = 25
if age > 18:
    print("djhfs")
    if age >= 20:
        print("You can drive")
    else:
        print("You need a license")  

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
    if score<=20:
      print("khkd")
    elif score>20:
      print("wejf")
#
h1=20
if h1<10:
    pass
elif h1>10:
    print("nnfjf")
"""
def fun(x):
    match x:
     case 1:
          print(1)
     case 2:
          print(2)
     case _:
            print("not match")       
fun(1) 
fun(2)            
#list
l=[1,2,3]
match l:
    case [1,*res]:
        print("res")
    case 2:
        print(2)   
    case _:
        print("wrong")     
#tuple
t=(1,2,3)  
match t:
    case(1,2,3) :
        print("tuple")   
    case _:
        print("not match")     

# dict
d={
    "name":"priya"
}  
match d:
    case{"name":name} :
        print(f"{name}")  

st="h"
match st:
    case "h" :
        print("mATCH")           


        