class Person:
    def __init__(self,name,age,id):
        self.name=name
        self.__age=age
        self._id=id

    def fun(self):
        return self.__age    
    
ob=Person("priya",20,1)
print(ob.name)
print(ob._id)
print(ob.fun())
