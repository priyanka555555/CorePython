class A:
    def show(self):
        print("In A") 
class B(A):
    def show(self):
        print("In B") 
class C(A):
    def show(self):
        print("In C")  
class D(B,C):
    def show(self):
       pass
d=D()
d.show()   
print(D.mro())   

x=lambda a,b:a+b
print(x(10,20))

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Parent ka greet call ho raha hai
        print("Hello from Child")

c = Child()
c.greet()



