"""2
decorator is a function which takes another function as an argument and returns a function as output
we can add extra  functionality to a function without changing the original function
for example i have a function which is printing hello world and i want to add some extra functionality 
so we can create decorator and pass original function as an argument 
to add extra functionality in the decorator
and return the wrapper function

* We can apply a decorator using the @ symbol above the function we want to enhance. 
This is equivalent to passing the function as an argument to the decorator. 
* @classmethod:Works with the class, not the object,Takes cls as the first parameter,Can access & modify class variables
* @staticmethod :@staticmethod is a decorator that defines a method inside a class but does not take self or cls as the first argument.
* @dataclass :this decorator automatically creates common methods like __init__, __repr__, and __eq__ for a class.
###########3333
wrapper:A wrapper function is a function inside a decorator that wraps the original function and adds extra behavior before or after calling it.

*args and **kwargs make a decorator generic. This allows a single decorator to work across different types of functions, 
 No matter how many. number of arguments they have, without causing any errors.

type of decorator
1. Function decorator
2. Class method decorator: 
3. Static method decorator
4. Dataclass decorator
1.method decorator:A method decorator is a function that is applied to a class method to modify or enhance its behavior without changing the original method code.
def classdeco(func):
   def wrapper(self):
       print("before method call")
       func(self)

       print("after method call")
   return wrapper   
      
class Demo:
    @classdeco
    def hello(self):
    
        print("hello world")
d=Demo() 
d.hello()

2.A class decorator: is a function that is applied to a class to modify or enhance the class itself without changing its original code.
def classDeco(cls):
    cls.hello="world"
    return cls
        
@classDeco
class Demo:
    pass
obj=Demo()
print(obj.hello)

"""
def greet(hellofun):
    def wrapper():
        print("i am good")
        hellofun()
        print("i am fine")
    return wrapper
@greet
def hello():
    print("hello world")
hello()  

def adddeco(addfun):
    def wrapper(a,b):
        print("i am good")
        res=addfun(a,b) 
        print(res)
    return wrapper

@adddeco
def add(a,b):
    return(a+b)
@adddeco
def multy(a,b):
    return(a*b)

add(10,20)
multy(10,20)

############ using *args
def decofun(fun):
    def wrapper(*args):
        a= fun(*args)
        print(a)
    return wrapper
@decofun
def fun(*args):
    return sum(args)
fun(1,2,3,4,5)
# using **kwargs
def decofun(fun):
    def wrapper(**kwargs):
        a=fun(**kwargs)
        print(a)
    return wrapper
@decofun
def fun(**kwargs):
    return kwargs
fun(a=1, b=2, c=3, d=4, e=5)

# example of class method 
class MyClass:
    class_variable = "I am a class variable"
    
    @classmethod
    def class_method(cls):
        print("This is a class method.")
        MyClass.class_variable = "I am a variable"
        print(cls.class_variable)
MyClass.class_method()
# example of static method
class MathOperations:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def multiply(a, b):
       print(a * b)

# Calling static methods
MathOperations.add(5, 3)     
MathOperations.multiply(5, 3) 
# example @dataclass
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    salary: float

# Creating instances
emp1 = Employee("Alice", 25, 50000)
emp2 = Employee("Bob", 30, 60000)

print(emp1)
print(emp2)

################
import time
def time_it(func):

    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()    
        
        print(f"Execution time: {end_time - start_time:.1f} seconds")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    print("Function Finished!")

slow_function()

##############################################33333
def decofun(func):
    def wrapper(*args, **kwargs):
        # Decorator logic (optional)
        res = func(*args, **kwargs)
        return res
    return wrapper
@decofun
def fun():
    print("hello world")

@decofun
def fun1(a, b):
    return a + b 

@decofun  # Added decorator here too
def fun2(**kwargs):
    return kwargs

fun()

#We need to print these because they 'return' values
print(f"Result of fun1: {fun1(10, 20)}")
print(f"Result of fun2: {fun2(a=10, b=30,c=50)}")

#####################3
import functools

def my_decorator(func):
    @functools.wraps(func) # it copied the details of original function to wrapper function
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def login_user():
    """Ye user ko login karta hai."""
    pass

print(login_user.__name__) # Output: login_user (Agar wraps nahi hota toh 'wrapper' aata)
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())

def decofun(func):
    def wrapper(a):
        func(a.upper())
    return wrapper 
@decofun
def fun(a):
    print(a)
fun("hello")

l=[1,2,3]
n=9
# 9 18 27
for i in l:
    print(i*n)
    

def fun():
    print("hello")
   
import copy

# ls1=[1,2,3,[100,200]]
# ls2=copy.deepcopy(ls1)
# print(ls2)
# print(ls1)

# ls2[3][0]=100000
# print(ls2)
# print(id(ls1[3]))
# print(id(ls2[3]))


# what is REPL?
# what is dynamic typeing?
# what is signature

# a=10
# a="10"

# def func(a:int,b:str)->bool:
print("1...................")
l=[1,2,3,4,5,6,8]
#[[1,2,3,5],[4,6,8]]

def deco(func):
    def wrapper():
        return func()
    return wrapper

@deco
def fun():
    return 10
print(fun())

###################################
def deco(func):
    def wrapper():
        func()   #return ignored
    return wrapper
@deco
def fun():
    return 10
print(fun())

############################
"""
1. Decorator runs at definition time
def deco(func):
    print("DECORATOR")
    return func

@deco
def fun():
    print("HELLO")

fun()
✅ Output:
DECORATOR
HELLO
🧠 Trap:
decorator function pehle run hota hai
function call baad me hota hai
🔥 2. Wrapper not returning value
def deco(func):
    def wrapper():
        func()
    return wrapper

@deco
def fun():
    return 10

print(fun())
✅ Output:
None
🧠 Trap:
return value lost
🔥 3. Wrapper returns function result
def deco(func):
    def wrapper():
        return func()
    return wrapper

@deco
def fun():
    return 10

print(fun())
✅ Output:
10
🔥 4. Missing wrapper return (BIG BUG)
def deco(func):
    def wrapper():
        func()
    return wrapper

@deco
def fun():
    print("Hi")

fun()
✅ Output:
Hi
🔥 5. Function replaced by None
def deco(func):
    print("DECORATING")

@deco
def fun():
    print("Hi")

fun()
❌ Output:
DECORATING
TypeError
🧠 Trap:
decorator didn't return function
🔥 6. Multiple decorators order
def d1(func):
    def w():
        print("D1")
        func()
    return w

def d2(func):
    def w():
        print("D2")
        func()
    return w

@d1
@d2
def fun():
    print("HELLO")

fun()
✅ Output:
D1
D2
HELLO
🔥 7. Decorator execution order confusion
@d1
@d2
def fun():
    pass
🧠 Flow:
fun = d1(d2(fun))

🔥 8. Function name changes
def deco(func):
    def wrapper():
        return func()
    return wrapper

@deco
def fun():
    pass

print(fun.__name__)

❌ Output:
wrapper
🧠 Trap:
original name lost
🔥 9. Fix using wraps
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper
🔥 10. Arguments missing in wrapper
def deco(func):
    def wrapper():
        return func()
    return wrapper

@deco
def add(a, b):
    return a + b

print(add(2,3))
❌ Error:
TypeError
🧠 Fix:
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
💥 BONUS TRICK (very asked)
def deco(func):
    def wrapper():
        print("A")
        return func()
    return wrapper

@deco
def fun():
    return "B"

print(fun())
✅ Output:
A
B
🧠 FINAL MASTER RULES

👉 Always remember:

Decorator runs at definition time
Wrapper runs at function call time
Function is replaced by wrapper
Missing return → None
Missing args → TypeError
🔥 ONE-LINE INTERVIEW ANSWER

👉
"A decorator replaces a function with a wrapper that controls execution flow, and mistakes in return handling or arguments lead to common runtime bugs."
"""
