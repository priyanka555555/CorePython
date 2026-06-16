"""
class A:
    def fun(self):
        print("first class")
class B:
    def __init__(self):
        self.ob=A()#Composition

    def display():
     pass
"""
"""
sum values
list1=[4,2,3,5,7]
sum=0
for x in list1:
    sum=sum+x
print(sum)    
"""
"""
first max and first min
list1=[4,2,3,5,7]
first_max=max(list1)
first_min=min(list1)
print(first_max)
print(first_min)
"""
"""
list1=[4,2,3,5,7]
list2=["apple","banana","orange","apple"]
x=set(list2)

list2=list(x)
print(list2)
"""
"""
list1 = [4, 2, 3, 5, 7, 2, 3, 4]

unique_list = []
for item in list1:
    if item not in unique_list:
        unique_list.append(item)

print("List without duplicates (order maintained):", unique_list)

"""
"""
list1 = [4, 2, 3, 5, 7, 2, 3, 4]
list2= ["apple","banana","orange","apple"]
#list3=list1+list2
list2.extend(list1)
print(list2)
"""
"""
tup=(1,2,3,4,5)
print(len(tup))
"""      

class Engine:
    def start(self):
        return "Engine started "

class Car:
    def __init__(self):
        self.engine = Engine()  # Car creates the Engine

    def drive(self):
        return f"Car is driving. {self.engine.start()}"


car = Car()
print(car.drive())
