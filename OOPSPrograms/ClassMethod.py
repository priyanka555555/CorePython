"""
class Calculator:
    def add(self,a,b):
       return a+b
    def sub(self, a,b):
        return a-b
cal=Calculator()
print(cal.add(10,20))    
print(cal.add(100,20)) 
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
    def fun():
        print("hello world")
p1=Person("priya",90)

#del Person.fun()
print(p1)
p1.fun()


            
