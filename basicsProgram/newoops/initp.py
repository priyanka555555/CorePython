"""
init__ method in Python is a constructor. It runs automatically when a new object of a class is created. 
Its main purpose is to initialize the object’s attributes and set up its initial state. When an object is created,
memory is allocated for it, and __init__ helps organize that memory by assigning values to attributes.

Why Use __init__()?
Without the __init__() method, you would need to set properties manually for each object:

self:self is a parameter that is use to store memory address of current object
self because it acts as a unique identifier for each object.

It is used to access properties and methods that belong to the class.

Why Use self?
Without self, Python would not know which object's properties you want to access:

################33

1. Class Property (Shared)
A variable defined inside the class but outside any method. It is shared by all objects of that class. 
If you change it for the class, it changes for everyone.

Example: school_name = "KV School" (Same for all students).
2. Object Property (Personal)
A variable defined inside __init__ using the self keyword. It belongs only to that specific object. Each object can have its own unique value.
Example: self.name = "Rahul" (Every student has their own name).

Class Methods
Methods are functions that belong to a class. They define the behavior of objects created from the class.
Note: All methods must have self as the first parameter.

diff __init__ vs without __init__()c
1. With __init__: Data is written into the "Permanent Memory" of the object (it gets officially registered and saved).
2. Without __init__: Data only stays on the function's "Working Table" (it is temporary and gets cleared as soon as the task is finished).
@ The __str__: method is a special function that defines how an object should be displayed as readable text when you print it.
@ You can delete methods from a class using the del keyword:

"""
class Person:
    def __init__(self,name,age,address="rewa"):
        self.name=name# instance property or object property
        self.age=age
        self.address=address

p=Person("priya",90)
print(p.name) 
print(p.age)
print(p.address)

#Use self to access object properties:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def access_property(self):
        print("hello",self.name)  
p=Person("priya",90)
p.access_property()
print(p.age)

# access method using self parameter

class Person:
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def method(self):
        print("hello world",self.name)   
    def access_method(self):
        self.method()
p=Person("priya",40)
p.access_method()
print(p.name,p.age)

print("1................")

#Access multiple properties using self:
class Person:
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def access(self) :
        #print(f"{self.name},{self.age}") 
        return f"{self.name},{self.age}"
p=Person("diya",50)
print(p.access())    


# class property

class Person:
    school_name="ABC"

    def __init__(self,name):
        self.name=name

p1=Person("priya")
p2=Person("diya") 
print(p1.school_name)
print(p2.school_name)  
print(p1.name)  
print(p2.name)    

#### modyfy class property

class Person:
    school_name="ABC"

    def __init__(self,name):
        self.name=name
        
p1=Person("priya")
p2=Person("diya") 
Person.school_name="AB" # modyfy class property
p1.school_name="xyz" # modify class property for the first object only
print(p1.school_name)#xyz
print(p2.school_name)# AB
print(p1.name)  
print(p2.name)  

print("1..........................")

#Add New Properties You can add new properties to existing objects:
class Person:
    def __init__(self,name):
        self.name=name
p=Person("priya") 
print(p.name)
p.age=90 # add new property
print(p.age)       

#without __innit__() # Methods with Parameters
class Person:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
p=Person()  
print(p.add(1,2))  
print(p.sub(5,3))

###################################3
#Methods can modify the properties of an object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
print(p1.name)
p1.celebrate_birthday()
p1.celebrate_birthday()
p1.celebrate_birthday()
           
#The __str__ method is a special function that defines how an object should be displayed as readable text when you print it.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      return f"{self.name} , {self.age}" 
p=Person("priya",90)
print(p)   

#delete method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      return f"{self.name} , {self.age}" 
  def fun(self):
      print("hello")
p=Person("priya",90)
print(p)

#del Person.fun()
#print(p.fun())   









