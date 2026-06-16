
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(p)  # Output: Alice, 25 years old

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person'{self.name}', {self.age} years old"

p = Person("Alice", 25)
  # Output in shell: Person('Alice', 25)
print(p)  # Output: Person('Alice', 25)   

