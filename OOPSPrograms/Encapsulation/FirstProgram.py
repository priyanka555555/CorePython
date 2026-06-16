#Private
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age# private property
    #def display(self):
       # print(self.name,self.age)
obj=Person("priya",30) 
print(obj.name)
#print(obj.__age)     
            
to get private Property
"""
"""
class Person:
    def __init__(self,name ,age):
        self.name=name
        self.__age=age
    def get__age(self):
        return self.__age    
obj=Person("priya",30)
print(obj.name) 
print(obj.get__age())  
"""
#to modify private property using set
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get__age(self):
         return self.__age
    def set__age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age must be postive") 
obj=Person("priya",20)
print(obj.name) 
print(obj.get__age()) 
obj.set__age(26)
print(obj.get__age())              
"""
"""
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
#print(student.get_status())
"""
#Protected property using single _ underscore
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't
      
