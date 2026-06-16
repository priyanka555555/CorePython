"""
inheritance: it means reusebility we can adopt feature from base class to derived class
types of Inheritance in Python
1.Single: A child class inherits from one parent class.
in single inheritance their is two class base and derived

2.Multiple: A child class inherits from multiple parent classes, with Python using Method Resolution Order (MRO) to resolve method conflicts.
 multiple inheritance, a child class can inherit from more than one parent class.

3.Multilevel: Features are inherited in a chain, such as from a parent to a child, and then to a grandchild.

4.Hierarchical: Multiple child classes inherit from a single parent class.

5.Hybrid: A combination of two or more of the above types
Hybrid inheritance = Combination of multiple types of inheritance (single, multiple, multilevel) in a single program.

1.When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
When you define a new __init__() function in the Child class, it replaces (overwrites) the __init__() function of the Parent class. 
As a result, the Child class stops using the Parent’s setup logic and only follows its own.

super(): function that will make the child class inherit all the methods and properties from its parent:
note:By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.

1.__mro__ attribute: shows a tuple of classes in the order Python searches for methods.
2. mro() method: returns a list of classes in the MRO.
"""
#simple program
class BaseCass:
    def fun(self):
        print("base class")
class DerivedClass(BaseCass):
    def fun1(self):
        print("derived class")
        
d=DerivedClass()
d.fun()
d.fun1()  

class School:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"    
        
class Student(School):
     def __init__(self,address,name,age):
        #School.__init__(self,name,age)
        super().__init__(name,age)
        self.address=address
         #self.name=name
         #self.age=age
         
     def __str__(self):
         return f"{self.address} {self.name} {self.age}" 
     
        
s=Student("priya",70,"satna")
print(s)

#multiple innheritance ex 1
class BaseClass1:
    def __init__(self,name):
        self.name=name

class BaseClass2:
    def __init__(self, sirname):
        self.sirname=sirname

class ChildClass(BaseClass1,BaseClass2):
    def __init__(self, name,sirname):
        BaseClass1.__init__(self,name)
        BaseClass2.__init__(self,sirname)
    def __str__(self):    
        return f"{self.name} {self.sirname}"
obj=ChildClass("priya","patel")   
print(obj)  

################3 ex2
print("2......................")


##################333
"""
class Base1:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Base1 init")

class Base2:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Base2 init")

class Child(Base1, Base2):
    def __init__(self):
        super().__init__()

obj = Child()
"""

print("1...................................")
 
class BaseCass:
    def __init__(self, name):
        self.name = name
    def fun(self):
        print("base class")

class DerivedClass(BaseCass):
    def __init__(self, name):
        # super() automatically finds BaseCass and passes 'self' for you
        super().__init__(name)

    def __str__(self):
        return f"{self.name}"
         
    def fun1(self):
        print("derived class")

d = DerivedClass("priya")
d.fun()  
print(d) 
d.fun1()

#############################################3\
"""
print("1..........................")
class A:
    def show(self):
        print("A method")

class B(A):
    def show(self):
        print("B method")

class C(A):
    def show(self):
        print("C  method")

class D(B, C):
    pass

obj = D()
obj.show()  
"""
print("1.......................................")

class BaseClass1:
    def fun(self):
        print("baseclass")     
class BaseClass2():  
    def fun(self) :
        print("derived class") 
    def B(self):
        print("B")    
class DerivedClass(BaseClass1,BaseClass2):
      def __init__(self,name):
          self.name=name
      def __str__(self):
          return f"{self.name}"   
          
      def fun(self):
          print("derived class")
d=DerivedClass("priya") 
print(d)
d.fun()
d.B()
 
 ################################### multiple inheritance
 # single inheritance
class BaseClass:
    def fun(self):
        print("baseclass")
class DerivedClass(BaseClass):
    def fun1(self):
        pass
d=DerivedClass()
d.fun()  
print("1.......................")
# multilavel inheritance
class BaseClass:
    def fun(self):
        print("baseclass")
class DerivedClass(BaseClass):
    def fun(self):
        print("derivedClass")
class SubDerivedClass(DerivedClass) :
       pass

d=SubDerivedClass()
d.fun() 
# multiple inheritance a child class can inherit multiple base class
print("1.......................")
class BaseClass:
    def fun(self):
        print("baseclass")
class DerivedClass:
    def fun(self):
        print("derivedClass")
class SubDerivedClass(DerivedClass,BaseClass) :
       pass

d=SubDerivedClass()
d.fun() 
print("1.............................")
# Hierarchical inheritance
class BaseClass:
    def fun(self):
        print("baseclass")
class DerivedClass1(BaseClass):
    def fun(self):
        print("derivedClass1")
class DerivedClass2(BaseClass):
    def fun(self):
        print("derivedClass2")        

d=DerivedClass2()
d.fun() 
d1=DerivedClass1()
d1.fun() 
# hybrid
# Base class 1
class Vehicle:
    def vehicle_type(self):
        print("This is a vehicle")

# Base class 2
class Engine:
    def engine_type(self):
        
        print("This is an engine")

# Derived class using multiple inheritance
class Car(Vehicle, Engine):
    def car_name(self):
        print("This is a car")

# Further derived class (multilevel inheritance)
class SportsCar(Car):
    def sport_feature(self):
        print("This is a sports car with turbo feature")

# Test
sc = SportsCar()
sc.vehicle_type()   # From Vehicle (base)
sc.engine_type()    # From Engine (base)
sc.car_name()       # From Car (derived)
sc.sport_feature()  # From SportsCar (most derived)

print("1........................................")
class A:
    def base(self):
        print("A")
class B:
    def derived(self):
        print("B") 
class C(A,B):              
    def multi(self):
        print("multiple")
class D(C):
    def multilevel(self):
        print("multilevel")
d=D()
d.base()
d.derived()
d. multi()
d.multilevel()     





 




             
