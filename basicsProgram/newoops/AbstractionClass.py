
"""
Data abstraction means showing only the essential features and hiding the complex internal details. 
2. How to achieve Abstraction in Python?
To achieve abstraction in Python, we use the abc (Abstract Base Classes) module.
Key Components:
1.Abstract Class: This is a class for which you cannot create an object. It acts only as a "Blueprint" or a roadmap.
2.Abstract Method: This is a method that has only a name but no code (body). It is marked with the @abstractmethod decorator.
We can implement the abstract method in the child class. If we do not define (implement) the abstract method in the child class, it will throw an error.
3.Concrete Class: A class that inherits from an abstract class and provides the actual code (definition) for its methods is called a concrete class.

Abstraction: It is the process of hiding complexity at the design level by showing only the essential features of an object.
Encapsulation: It is the technique of protecting data at the implementation level by wrapping it with methods into a single unit (class). 

Abstraction answers "What" an object does (Interface).
Encapsulation answers "How" to hide and secure that data (Privacy)
"""
from abc import ABC,abstractmethod
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass
    def fun(self):
        print("hello world")
class English(Greet) :
     def say_hello(self):
         print("hello")  
e=English()
e.say_hello() 
e.fun()

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def fun(self):
        pass
    def fun1(self):
        print("i am car")
class Audi(Car):
    def fun(self):
        print("i am audi")   
class BMW(Car):
    def fun(self):
        print("i am bmw")        
Aui = Audi()
a=BMW()
a.fun()
Aui.fun()
Aui.fun1()







