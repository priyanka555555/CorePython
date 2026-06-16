"""class Person:
    def greet(self):
        print("Hello! Welcome to Python OOPS")

# Creating an object
p = Person()

# Calling method using object
p.greet()
"""
"""
class calculator:
    def add(self,a,b):
        print("The sum is:",a+b)
    def sub(self,a,b):
        print("The difference is:",a-b)
    def mul(self,a,b):
        print("The product is:",a*b)
    def div(self,a,b):       
        print("The quotient is:",a/b)
cal=calculator()
cal.add(10,5)
cal.mul(10,5)
cal.sub(10,5)       
cal.div(10,5)
"""
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
  """
"""
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()
"""
"""
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"{self.brand},{self.model},{self.year}")
        

obj=Car("Toyota","Corolla",2020)
obj.display()
"""
class Person:
  species="human"
  species1=""
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age
Person.species1="jiya"
print(p1.name)
print(p1.species)
print(p1.species1)
#print(p1.age) #






