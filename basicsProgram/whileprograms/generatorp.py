"""
A generator in Python is a special type of function or expression that creates an iterator 
which produces a sequence of values one at a time, on demand, using the yield keyword instead of return. 
This approach is called "lazy evaluation" and is highly memory-efficient, especially for large or infinite sequences, 
because it doesn't store the entire sequence in memory at once

yield keyword: The presence of yield in a function makes it a generator function.
when function hits yield it sends back the value and pauses iteself it remember exactly where it left off and waits for next request

2. Why use Generators?
1. Memory Efficiency: Generators produce items one at a time and only when requested,
takes almost zero memory because it only generates the next number when asked.
2.Lazy Evaluation: Processing starts only when you request the data, making the initial program start-up much faster

###########3
Generator Expression
This is like a List Comprehension but uses parentheses () instead of brackets [].
"""
def genp():
    yield 1
    yield 2
    yield 3
    
for i in genp():
    print(i)    

print("****************")
def genf(n):
    count=1
    while count<=n:
        yield count
        count=count+1

for i in genf(5):
    print(i)

print("****************")  
def genf1(num):
   for i in range(num):
       yield i

g=genf1(10)
print(next(g))#You can manually iterate through a generator using the next() function:
print(next(g))

print("****************") 
def genf2():
    yield "priya"    
    yield "riya"
    yield "diya"
obj= genf2()
print(next(obj))  

#generator expression
x=(a*a for a in range(5))
x=sum(a*a for a in range(5))
#print(list(x))
print("****************")
#list comprehension
y=[a*a for a in range(5)]
y=sum([a*a for a in range(5)])
print(y)

print("****************")

def genf2():
    while True:
       res=yield 
       print(res)
obj=genf2()
next(obj)#next(gen): Isse "Priming" kehte hain. Iske bina generator kaam nahi karega. Ye code ko pehli baar yield tak pahunchakar rok deta hai.
obj.send("hello")
obj.send("world")

##Generator ek special function hai jo yield ka use karke apna execution temporarily pause kar deta
#  hai aur apni state (jagah) yaad rakhta hai. Ye next() se start hota hai aur 
# .send() ke zariye bahar se data receive karke coroutine ki tarah kaam kar sakta hai.
def genf2():
    yield 1
    yield 2
obj=genf2()
print(next(obj)) 
obj.close()   
print("1....................")
def fun():
    yield 1
    yield 2
    yield 3
f=fun()    
print(next(f)) 
print(next(f))

print("1....................")
def fun1():
    yield 1
    yield 2
    yield 3
for i in fun1():
    print(i) 

def fun2():
    while True:
     res=yield
     print(res)
f=fun2()
next(f)
f.send("hello")           

def fun(n):
    for i in range (n):
        yield i
        
f=fun(1000)  
print(next(f))  

print(next(f))
print(next(f))

###########3
l=["he","we"]
d={
    "name":"priya",
    "age":20
}
d.update({"name":"diya"})
print(d["name"])
d["new_name"]=d.pop("name") 
for key,value in d.items():
 print(key,":",value)  


      



































