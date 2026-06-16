class BaseClass:
    def __init__(self,companyname):
        self.companyname=companyname
    def display(self):
        #print("baseclass")
        pass

class childClass(BaseClass):
    def __init__(self, companyname,name,id,salary):
        super().__init__(companyname)
        self.name=name
        self.id=id
        self.salary=salary
    def display1(self):
        print(self.companyname,self.name,self.id,self.salary)    

            
obj=childClass("bridgefix","priya",123,90000)  
obj.display1()      