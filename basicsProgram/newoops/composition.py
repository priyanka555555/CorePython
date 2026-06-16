#composition means one class contains the object of the  other class.
#it is a Has a relationship
#example: car has a engine, bike has a engine,
#Life Cycle: If the Car object is deleted, the Engine object inside it will also be destroyed automatically."
# if there is no car what will engion do

#Difference: Inheritance vs Composition
#Inheritance: "Is-a" (Dog is an Animal).
#Composition: "Has-a" (Car has an Engine).

#Inheritance: Use it when you want the new class to be a version of the old class (e.g., Smartphone is-a Phone).
#Composition: Use it when you want to combine different parts to build a complex class (e.g., Computer has-a CPU).

"""
Inheritance (Is-a)
If you want to use all the properties and methods of another class directly, and there is a natural type relationship, use Inheritance.
Composition:
In Composition, you store an object of another class inside your class, and
access its methods/properties through that object.

"""
class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self):
        # Composition: car class has object of Engine class
        self.my_engine = Engine()

    def drive(self):
        print(self.my_engine.start())
        print("Car is driving!")

c = Car()
c.drive()

class Weapon:
    def shoot(self):
        print("Weapon fired!")

class Soldier:
    def __init__(self, weapon):
        self.weapon = weapon  # yahan weapon parameter me object aa raha hai

    def attack(self):
        self.weapon.shoot()   # object ke method ko call kar rahe hain

# Objects create karna
gun = Weapon()          # Weapon class ka object
john = Soldier(gun)     # gun object Soldier ke constructor me pass ho gaya
john.attack()           # attack call → Weapon fired!
l=[1,5,4,2,0,0,0]
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l) 
l1=[]
for i in l:
    if i>0:
        l1.append(i)  
l1.sort()
l2=[]
for i in l:
    if i==0:
        l2.append(i)    
l1.extend(l2) 
print(l1)

class Engine:
    def fun(self):
        print("engine")
class Car:
    def fun1(self) :
        self.engine=Engine()
    def fun2(self) :
        return self.engine.fun()
obj=Car()
obj.fun1()
obj.fun2()                