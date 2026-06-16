class Person:
    def __init__(self,fname,lname):
       self.firstname=fname
       self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
#obj=Person("priya","patel")
#obj.printname()        
class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
       # self.graduationyear=2019
        self.graduationyear=year
    def display(self):
        print(self.firstname,self.lastname,self.graduationyear)
            
x=Student("priya","patel",2022) 
x.display()
#print(x.firstname,x.lastname,x.graduationyear) 
#print(x.graduationyear)      
     
           