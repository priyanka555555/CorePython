"""
class Baseclass:
    def fun(self):
        print("parent class")
class DerivedClass(Baseclass):
        def fun1(self):
         print("derived class")  
obj=DerivedClass()
obj.fun()
obj.fun1()  
"""
"""
class Baseclass1:
        def fun(self):
         print("parent class")
class BaseClass2:
        def fun1(self):
         print("parent class1")
class childclass(Baseclass1,BaseClass2):
        def fun2(self):
            print("child class") 
                   
obj=childclass()
obj.fun()
obj.fun1() 
obj.fun2() 
"""
class Baseclass1:
        def fun(self):
         print("parent class")
class BaseClass2(Baseclass1):
        def fun1(self):
         print("parent class1")
class childclass(Baseclass1):
        def fun2(self):
            print("child class") 
                   
obj=childclass()
obj.fun() 
obj.fun2()
obj1= BaseClass2()
obj1.fun()
obj1.fun1()


