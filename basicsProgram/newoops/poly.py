class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

# method overriding
class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
a = Dog()
a.sound()

"""
.Duck Typing Polymorphism (Python-specific style)
Same behavior, different objects — no need for inheritance.
Duck typing means you don’t check an object’s type; you only check whether it has the required method or behavior.
"""
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

# operator overloading


