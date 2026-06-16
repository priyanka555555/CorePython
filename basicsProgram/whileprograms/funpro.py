"""
Python me function ko generally immutable object isliye maana jata hai kyunki ek baar function define ho gaya to uske internal code (logic) 
ko directly change nahi kar sakte. 

def fun():
    print("hello world")
fun() 
fun()   
"""
"""
function:A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
Key reasons to use functions:Code Reusability: Functions allow you to define a block of code once and use it multiple times.
avoiding the need to write the same logic repeatedly 
def greet_user(name):
    print(f"Hello, {name}! Welcome back.")
# Reused three times with different data
greet_user("Alice")
greet_user("Bob")
greet_user("Charlie") 

 parameter :A parameter is the variable listed inside the parentheses in the function definition.
 argument:An argument is the actual value that is sent to the function when it is called.

"""

def fun(a,b): # a, b are parameters
    return a+b #If a function doesn't have a return statement, it returns None by default.
print(fun(10,20)) # 10,20 is arguments # this is a positional arguments
print(fun(13,20))

#Default Parameter Values
#You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#2.

def fun(name="priya"):
 #print("name is ",name)
  return name

print(fun("sriya"))

print(fun())

#2.
#Keyword Arguments
#You can send arguments with the key = value syntax.

def fun1(name,age):
  print("name is ",name,"age is ",age)
#fun1(name="priya",age=20)  
#with keyword arguments, the order of the arguments does not matter
fun1(age=90,name="jiya")

###########
"""
Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
"""
#Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("dog", "Buddy")

# positional arguments switching the order change the result
def fun(name,age):
  print("name is " ,name," age is " ,age)
fun("knsdlnk",40) 
"""
Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments:
"""
#Example
def fun2( animal,name,age):
  print("animal",animal,"name is ",name,"age is ",age)
fun2("dog",name="kiya",age=90)  

def fun3(fruits):
  for i in fruits:
    print(i)
fruits=["apple","banana","papaya"]   
print(fruits)

##########
def fun4(person):
  print(person["name"])
  print(person["age"])
p={"name":"priya","age":40}  
fun4(p)
###################
def fun5():
   
  return [1,2,3]
#f=fun5()
x,y,z=fun5()
print(x,y,z)


def fun6():
  return(2,4)
#x=fun6()
x,y=fun6()
print(x,y)

def fun7():
  return{1,3}
#x=fun6()
x,y=fun7()
print(x,y)
# dict
def fun8():
    return {"a":1, "b":5}

(a, v1), (b, v2) = fun8().items()
print(a, v1, b, v2)

#Combining Positional-Only and Keyword-Only
def fun9(a,b,/,*,c,d):
  return a+b+c+d
f=fun9(10,20,c=9,d=3)
print(f)

#Arbitrary Arguments - *args
#If you do not know how many arguments will be passed into your function, add a * before the parameter name.
def funn(*num):
  return num
x=funn(1,2,3,4,5)
print(x[2])
#
# combine positional args and *args
print("1.....................................................")
def funn(name,*num) :
   for  i in num:
    print(name,i)
funn("priya",1,2,3,4,5)
print("1.....................................................")
# A function that calculates the sum of any number of values:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total =total+num
  return total

print(my_function(1, 2, 3))
print("3.....................................................")
#Finding the maximum value:
def funn(*num):
  mx=num[0]
  for i in num:
    if i>mx:
      mx=i
  return mx 
print(funn(1,9,3,4))   
print("4.....................................................")
# **args
"""
Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:
"""
def fun(**args):
   print(args[a])#10
   print(args[b])#20
   print(args)# {'a': 10, 'b': 20}
  #return args
fun(a=10,b=20) 
print("5.....................................................")
def fun(name,**args):
   print(args[a])#10
   print(args[b])#20
   print(name)#priya
   print(args)#{'a': 10, 'b': 20}
  #return args
fun("priya",a=10,b=20) 
print("5.....................................................")
def newfun(email,**details):
  print("username ",email)
  for key,value in details.items():
    print(key,":",value)
newfun("priya@gmail.com",name="priya",age=90)    
print("5.....................................................")
#Combining *args and **kwargs The order must be:
# 1.regular parameters
# 2.*args
# 3.**kwarg
def fun(name,*args,**argss):
  print(name)
  print(args)
  print(argss)
fun("priya",1,2,3,a=10,b=30,c=90)  
##########33

def funn(a,b,c):
  return a+b+c
l=[1,2,3]
print(funn(*l))
#dict unpack Unpacking Dictionaries with **
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) 

def fun4(person):
  print(person["name"])
  print(person["age"])
p={"name":"priya","age":40}  
fun4(p)

def fun(**num):
  return num
print(fun(a=10,b=30))

#Unpacking Lists with *
#If you have values stored in a list, you can use * to unpack them into individual arguments:
def fun(a,b,c):
  return a+b+c
num=[1,2,3]
res=fun(*num)
print(res)
print("hello world")
#####################################################33333
def fun(l): 
 n = len(l)
 for i in range(n):
    for j in range(n):
      
        if l[i] <l[j]:
            t = l[i]
            l[i] = l[j]


            l[j] = t

 print(l)   

l=[1,3,4,2]
fun(l)
##########################33
a,b=b,a
print(a,b)
#1. Maximum of Three Numbers
#Write a Python function to find the maximum  number
def fun(l):
  m=l[0]
  for i in l:
    if i>m:
      m=i
  print(m)
l=[9,4,3,2]
fun(l)
#Write a Python function to find the minimum  number
##########################
keys = ['a', 'b', 'c']
value= [1,2,3]
d=dict.fromkeys(keys,value)
print(d)
################
def funn(*num):
  return num
x=funn(1,2,3,4,5)
print(x)
#############################################
def hello(*,name):
  return name
n=hello(name="priya")
print(n)

def hello(name,/):
  return name
n=hello("priya")
print(n)

# function can return tuple and set and list and dict
def listfun():
  return[1,2,3,4]

a,b,c,d=listfun()
print(a,b,c,d)
#################### return tupple
def tuplep():
  return(1,2,3,4)

a,b,c,d=listfun()
print(a,b,c,d)

################ rteurn set

def setp():
  return{1,2,3}
a,b,c=setp()
print(a,b,c)

###############return dict


def dictp():
  return{'a':1,'b':2}
(a,v),(b,v)=dictp().items()

print(a,v,b,v)
########################### * arguments
def fun(*name):
  return name
print(fun("priya","diya","siya"))

def fun(** details):
  return details
d=fun(name="diay",age=35)
print(d)

#combination of regular parameter, *args,*kwargs

def fun(title,*details,**name):
  return [title,details,name]
p=fun("pyhton","rewa",name="priya")
print(p)

a="rewa",
print(type(a))
  
######################################3

def fun(*num):
  sum=0
  for i in num:
    sum=sum+i
  return sum
f=fun(1,2,3,4,5)
print(f)

########## max number
def fun(*num):
  mx=num[0]
  for i in num:
    if i>mx:
      mx=i
  return mx    
f=fun(1,2,9,4,5)
print(f)
##########################

def my_function(**myvar):
  return myvar
print(my_function(name = "Tobias", age = 30, city = "Bergen"))

def fun3(fruits):
  for i in fruits:
    return i
f=["apple","banana","papaya"]   
print(*f) #apple banana papaya unpack the list 
print(f)#['apple', 'banana', 'papaya'] output with list

#list unpacking in function
def add(a,b,c):
    return a,b,c

my_list = [10, 20, 30]
print(add(*my_list))

#basic unpacking
l=[1,2,3,4]
a,b,c,d=l
print(a,b,c,d)

numbers = [1, 2, 3]
print(*numbers)# unpacking
##########
#Agar * Function ke arguments mein hai def hello(*args), toh woh Packing hai (taaki aap kitne bhi numbers bhej sako).
def fun(*num):
  return num
l=fun(1,2,3)

print(l)
#Agar * Function call mein hai hello(*my_list), toh woh Unpacking hai (taaki list ke elements alag-alag arguments ban jayein).

def fun(a,b,c):
  return a,b,c
l=fun(1,2,3)
# print(*l)

# print("11111111111111")
def fun(a,b,c):
  return a,b,c
l1=[1,2,3]
print(*fun(*l))#1 2 3
print(fun(*l))#(1, 2, 3)
######### unpacking dict

def fun(name,age):
  return {"name":name,"age":age}
f={"name":"priya","age":30}
print(fun(**f))

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)
######################################
def greet():
    print("Hello")
#greet.print("hii")# we can not modify
greet()  
########### if i want to change the code then we can create new function
def greet():
    print("Hello")

greet()

def greet():
    print("Hi")

greet()  

#note we can not chnge the function name but we can store function name in the variable and then we can call with new name
# function pythonme ek object hota hai
#example:

def greet():
    print("Hello")

say_hello = greet
greet()
say_hello()

print("hhhhhhhhhhhhhhhhhhhhhhhhhhhh")
def greet():
    print(greet.message)

greet.message = "Hello"
greet()
greet.message = "Hi"
greet()

##############
def greet():
    print("Hello")

result = greet()
print("Result:", result)

##"#### LIGB local inclosing global built-in
x="global"

def outer():
  x="Enclosing"
  def inner():
    x="local"
    print(x)
  inner()
  print(x)
outer()
print(x)

def fun():
  print("hello")
fun() 
print("1...........................................")
def deco(func):
   def wrapper(self):
     self.a="before"
     print(self.a)
     func(self)
     print("after calling  function")
   return wrapper
class Demo:
  @deco
  def fun(self):
    print("hello world")
d=Demo()
print(d.fun()) 










