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


