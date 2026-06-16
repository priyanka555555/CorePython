
"""
function:A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
Key reasons to use functions:Code Reusability: Functions allow you to define a block of code once and use it multiple times.avoiding the need to write the same logic repeatedly 

# Defined once
def greet_user(name):
    print(f"Hello, {name}! Welcome back.")

# Reused three times with different data
greet_user("Alice")
greet_user("Bob")
greet_user("Charlie") 

##################3

parameter: A parameter is the variable listed inside the parentheses in the function definition.

argument: An argument is the actual value that is sent to the function when it is called.

#################33
Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default value:

The reduce() function is a tool that shrinks an entire list into a single value by applying a specific operation (like addition or comparison) repeatedly.
Here is the sharp 2-line definition:
Summarizer: It takes the first two elemvents of a list, performs an operation, and then carries that result forward to the next element until only one final result remains.
Sequential Logic: It is primarily used for cumulative tasks like calculating the sum, product, or maximum of all items in a sequence.
Do you want a quick comparison table of Map, Filter, and Reduce to see the difference clearly?


************************Python*************************


Python mein isinstance() function ka use ek object ka type (class) check karne ke liye hota hai. Yeh batata hai ki kya ek object ek particular class, ya uski kisi sub-class (derived class) ka instance hai ya nahi.
Developer@736
reduce()Ek function jo iterable ke sabhi elements ko ek function ke through reduce karke single value me convert karta hai.

Agar * Function ke arguments mein hai def hello(*args), toh woh Packing hai (taaki aap kitne bhi numbers bhej sako).
Agar * Function call mein hai hello(*my_list), toh woh Unpacking hai (taaki list ke elements alag-alag arguments ban jayein).

A lambda function is a small, anonymous (nameless) function in Python that is defined in a single line.
In simple terms: It is a shortcut to create a function for a quick task without using the standard def keyword.
Key Characteristics:
No Name: It doesn't have a name like a regular function.
One Line: It can only contain one single expression.
Auto-Return: It automatically returns the result of that expression.
 map() function is a built-in Python tool that takes a function and an iterable (like a list) and applies that function to every single item in the list automatically. 
Instead of writing a for loop to change each item one by one, map() does it all in one go. 

******************************************************
What is OOP and its main concepts?

Encapsulation, Abstraction, Inheritance, Polymorphism.

Difference between class and object.
1. Class

A class is a blueprint or template for creating objects.
It defines attributes (variables) and behaviors (methods/functions) that the objects of the class will have.
It doesn’t occupy memory by itself.
Object

An object is an instance of a class.
It is a real entity created from the class blueprint.
Objects occupy memory and can have different values for their attributes.

2.Difference between instance variable and class variable.
class Student:
    school = "ABC School"   # Class variable

    def __init__(self, name):
        self.name = name    # Instance variable

s1 = Student("Rahul")
s2 = Student("Priya")

s1.name = "Amit"       # Changes only s1
Student.school = "XYZ School"  # Changes for all objects

print(s1.name)     # Amit
print(s2.name)     # Priya

print(s1.school)   # XYZ School
print(s2.school)   # XYZ School

Difference between instance method, class method, and static method.
Instance Method
 A method that belongs to an object (instance) of a class.
 It can access instance variables (specific to the object) and class variables.
 The first parameter is always cls, and it is defined using the

******************************************************
# Check PEP8 violations
flake8 DictProgram.py

# Auto-format code with Black
black DictProgram.py

# Sort imports with isort
isort DictProgram.py


1. What is PEP 8?
PEP 8 = Python Enhancement Proposal 81
Defines rules for writing clean, readable, and consistent Python code
Helps developers write code in a uniform way so it’s easy to read and maintain

Think of it as:

“A standard set of rules to make your Python code look professional.”

🔹 2. What PEP 8 covers
Feature	PEP 8 Rule Example
Indentation	4 spaces per level
Maximum line length	79 characters
Variable/function names	snake_case → my_variable, calculate_total()
Class names	CamelCase → StudentProfile
Imports	Group imports: standard → third-party → local
Spaces in expressions	x = 1 + 2 (not x=1+2)
Blank lines	2 lines between top-level functions/classes
Comments	Clear, meaningful, explain why, not what


******************************************************
what is python
“Python is an interpreted language because it runs on the Python Virtual Machine, but under the hood, it is first compiled into bytecode (.pyc) before execution. So it’s technically both compiled and interpreted.”

Python is a high-level, interpreted programming language it was developed by Guido van Rossum in 1991 
1.Easy to learn
2. interpreter based
3. GUI Development
4. Database connectivity

**********
Python Interpreter : A Python Interpreter is a program that reads, understands, and executes Python code line by line.
**********************
What is a Variable:
.A variable is a name used to store data (values) in a program.
.Must start with a letter or _
.Cannot start with a number
.No spaces allowed
.Case-sensitive (Age ≠ age)
type of variables :
global and local variable
********************
data type:
Numeric Types: int float complex(3j)
text type: str
sequence type: list, tuple, range
Set type: set,
mapping type: dict
Boolean type: bool
None type
*****************************************************
function:
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.
Function Arguments:
Values that you pass to a function.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
Parameter:
Function banate time jo variables likhte hain unko parameters kehte hain.
Argument
Function call karte time jo actual values dete hain unko arguments kehte hain.v
Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.(*args ka use tab hota hai jab function me kitne arguments aayenge pata na ho.)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

. Arbitrary Keyword Arguments - **kwargs:
This way, the function will receive a dictionary of arguments and can access the items accordingly:(**kwargs ka use tab hota hai jab function me multiple key=value arguments pass karne ho aur number fixed na ho.)
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:
*****************
decorator:
A decorator in Python is a function that adds extra behavior to another function or class without changing its original code.
@classmethod:Works with the class, not the object,Takes cls as the first parameter,Can access & modify class variables
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species
   print(Person.get_species())

//// agr ham @classmethod ka use karte hain to object bnane ki jarurat nhi hote  cls  class ko refer karta hai

@staticmethod:is a decorator that makes a method behave like a normal function inside a class, without using self or cls.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))


@property
A decorator that lets you access a method like an attribute.
@dataclass :this decorator automatically creates common methods like __init__, __repr__, and __eq__ for a class.
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

@property.setter:Used to set a value with validation.
*****
Instance method → works on object data

Static method → independent logic




* Python Lambda: is a small, anonymous function (function without a name).
Lambda with Built-in Functions
Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
1.map() function applies a function to every item in an iterable
map() is a Python function that applies a given function to every item of a list (or any iterable) and returns the results.
map() Python me ek function hai jo di hui function ko list (ya kisi iterable) ke har element par apply karta hai aur result return karta hai.
 number=[1,2,3,4,5]
doubled=list(map(lambda x:x*2, number))
print(doubled)

2. filter(): The filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even=list(filter(lambda x:x==0,numbers))
print(even)

3.sorted(): The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
 sorted= sorted(students,keylambda x:x[1])
print(sorted)
******************************
Generators
Generators are functions that can pause and resume their execution.(Generator ek aisa function hota hai jo ek-ek value deta hai, sab kuch ek saath nahi.)
when a generator function in called it returns a generator object which is an iterator
Instead of using return, generators use the yield keyword.
yield function ko generator bana deta hai.

👉 Ye value return karta hai,
👉 lekin function ko band (end) nahi karta
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
**************************
Using next() with Generators
You can manually iterate through a generator using the next() function:
When there are no more values to yield, the generator raises a StopIteration exception:

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

Generator Methods:
Generators have special methods for advanced control:

send() Method
The send() method allows you to send a value to the generator:
close() Method
The close() method stops the generator:

###




Python Collections (Arrays)
There are four collection data types in the Python programming language:

List :Lists are used to store multiple items in a single variable. is a collection which is ordered and changeable. Allows duplicate members.
Tuple : is a collection which is ordered and unchangeable. Allows duplicate members.
tuple methods:
1 count():The count() method returns the number of times a specified value appears in the tuple.
2 index() : method finds the first occurrence of the specified value.
            The index() method raises an exception if the value is not found.

Set:  is a collection which is unordered, unchangeable*((but you can remove and/or add items

 ).), and unindexed. No duplicate members.
* You cannot access items in a set by referring to an index or a key.
* add one item to a set use the add() method.
*  To remove an item in a set, use the remove(), or the discard() method.
   Note: If the item to remove does not exist, remove() will raise an error.
   Note: If the item to remove does not exist, discard() will NOT raise an error.
* pop(): You can also use the pop() method to remove an item, but this method will remove a   random item, so you cannot be sure what item that gets removed.
* The clear() method empties the set:
* The del keyword will delete the set completely:

*******JoinSets******
1. union() and update(). joins all items from both sets
   set1.update(set2),set1.union(set2)
2. intersection(). method keeps only the duplicates
   The intersection() method will return a new set, that only contains the items that are     present in both sets.////You can use the & operator instead of the intersection()

3. difference(). keeps the items from the first set that are not in the other set
4. symmetric_difference(): method keeps all item EXCEPT the duplicate
*********************methods***********
1. add()
2. clear()
3. copy()
4. difference()
5. difference_update()
6. dicard(): remove the specified item
7. intersection() &
8. isdisjoint(): returns whether two sets have a intersection or not
9. issubset(): <= Returns True if all items of this set is present in another set
example:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

10. issuperset(): >= Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

11. pop(): Removes an element from the set
12. remove():Removes the specified element 
13.symmetric_difference() ^ The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
14. union() 
15. update()



The return value of the pop() method is the removed item.

Example
Dictionary : Dictionaries are used to store data values in key:value pairs.is a collection which is ordered** and changeable. No duplicate members.
1.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
 2.
the dict() constructor:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
1.
Get Keys
The keys() method will return a list of all the keys in the dictionary.
Get Values
The values() method will return a list of all the values in the dictionary.
Get Items
The items() method will return each item in a dictionary, as tuples in a list.
Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
Change Values
You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
Update Dictionary
The update() method will update the dictionary with the items from the given argument.

Remove Dictionary Items
pop() method removes the item with the specified key name: thisdict.pop("model")
popitem() method removes the last inserted item: thisdict.popitem()
del : keyword removes the item with the specified key name:del thisdict["model"]
      del thisdict The del keyword can also delete the dictionary completely: 
clear() method empties the dictionary:
values() method to return values of a dictionary:
keys() method to return the keys of a dictionary:
copy():Make a copy of a dictionary with the copy() method:
dict().Make a copy of a dictionary with the dict() function:
 *************** methods**************
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


***********************************
Short hand if
If you have only one statement to execute, you can put it on the same line as the if statement.

pass Statement:
if statements can not be empty but if you for the some reason have an if statement with no content put in pass statement to avoid getting error

match statement:
The match statement is used to perform different actions based on different conditions
The break Statement:
With the break statement we can stop the loop even if the while condition is true:
The continue Statement:
if we want to skip the partiquler element and continew with the next
 *******************************OOPS**********************************
Inheritance:it means reusability it allows one class to inherit the properties and methods of  another class
type of inheritance:
1 Single inheritance :Single inheritance enables a derived class to inherit properties from a single parent class
2.Multiple Inheritance:
 when a class can be derived from more than one base class
3.Multilevel:
 we can adopt the feature from base class to the derived class to the sub derived class
4.Hierarchical Inheritance
it provide tree structure one base have multiple derived class
5. Hybrid Inheritance:
Hybrid inheritance is a combination of more than one type of inheritance. It uses a mix like single, multiple, or multilevel inheritance within the same program. Python's method resolution order (MRO) handles such cases.
*******************************
Composition means “HAS-A” relationship
One class uses another class by creating its object.Composition ek HAS-A relationship hai jisme ek class dusri class ka object use karti hai.

class Engine:
     def start(self):
      print("Engine started")
class Car:
      def __init__(self)
      self.engine=Engine()
   
      def drive(self):
      self.engine.start()
      print("car is moving")

car=Car()
car.drive()

*******************
Encapsulation:Encapsulation is about protecting data inside a class.
Private Properties
In Python, you can make properties private by using a double underscore __ prefix


:
Get Private Property Value
To access a private property, you can create a getter method:
Why Use Encapsulation?
Encapsulation provides several benefits:

Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified

**********
Python Inner Classes:An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
***********************
Data Abstraction in Python:
Data abstraction means showing only the essential features and hiding the complex internal details. 
from abc import ABC, abstractmethod

ex.
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Main program
d = Dog()
d.speak()

Abstract Properties:
Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using 

@abstractmethod. Subclasses must implement these properties.
**********
 decorator :A decorator in Python is a function that adds extra behavior to another function or class without changing its original code
.
@classmethod:Works with the class, not the object,Takes cls as the first parameter,Can access & modify class variables

class Student:
    school = "ABC School"   # class variable

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


# Object banane se pehle
print(Student.school)

Student.change_school("XYZ School")

# Change ke baad
print(Student.school)


@staticmethod:is a decorator that makes a method behave like a normal function inside a class, without using self or cls.

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


# Static method ko class se directly call kar sakte hain
print(Calculator.add(5, 3))       # 8
print(Calculator.multiply(5, 3))  # 15

# Object se bhi call kar sakte hain (optional)
calc = Calculator()
print(calc.add(10, 7))            # 17


@property
A decorator that lets you access a method like an attribute.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks   # _marks = private variable

    @property
    def marks(self):
        return self._marks

s = Student("Rahul", 85)

# Method ko attribute ki tarah access karna
print(s.marks)   # 85


@dataclass :is a decorator that automatically creates common methods like __init__, __repr__, and __eq__ for a class.
__repr__ ek special method hai jo Python me object ka official string representation return karta hai.
from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int        

# Object creation
s1 = Student("Rahul", 85)
s2 = Student("Anita", 90)

# Print object
print(s1)  
print(s2)

@property.setter:Used to set a value with validation.
*****
Instance method → works on object data

Static method → independent logic
**************************************
Explored OOP: Inheritance, Polymorphism, Encapsulation and Inner Classes.
Learned how Decorators modify functions and methods.
Practiced Dictionaries and their useful methods.
practice with logical programs.

Exception handling:
ZeroDivisionError
Jab aap kisi number ko 0 se divide karte ho.
10 / 0  # ZeroDivisionError

2.ValueError
Jab function ko sahi type ka value nahi mile ya invalid value mile.
int("abc")  # ValueError
3.TypeError
Jab aap operation kisi wrong type ke object pe karte ho.
"5" + 5  # TypeError
4.IndexError
Jab aap list ya string me invalid index access karte ho.
lst = [1,2,3]
lst[5]  # IndexError
5.KeyError
Jab dictionary me aap aise key ko access karte ho jo exist nahi karti.
d = {"a":1}
d["b"]  # KeyError

6.FileNotFoundError
Jab aap aise file ko open karne ki try karte ho jo exist nahi karti.
open("abc.txt")  # FileNotFoundError

7.AttributeError
Jab object me aise attribute nahi hota jo aap access karne ki koshish karte ho.
x = 5
x.append(3)  # AttributeError

8.ImportError / ModuleNotFoundError
Jab Python ko module import karne me problem hoti hai.
import something_not_exist  # ModuleNotFoundError

9.OverflowError
Jab calculation numeric limit se zyada ho jaye.

10MemoryError
Jab program ke paas memory khatam ho jaye.

super() 

super() ek Python ka built-in function hai jo parent class ke methods ko child class se access karne ke kaam aata hai. Matlab agar aapne child class me koi method override kiya hai, phir bhi aap parent class ka original method call kar sakte ho.


**************************************************************************
built in function:
len()

Kya karta hai: Kisi list, string, tuple, dictionary, ya iterable ka length batata hai.

Example:

lst = [4, 2, 7, 1]
print(len(lst))  # Output: 4

s = "Python"
print(len(s))    # Output: 6

2️⃣ max()

Kya karta hai: Iterable me sabse bada element return karta hai.
Example:

lst = [4, 2, 7, 1]
print(max(lst))  # Output: 7

3️⃣ min()
 Iterable me sabse chhota element return karta hai.
Example:

lst = [4, 2, 7, 1]
print(min(lst))  # Output: 1

4️⃣ sum()
 Iterable ke saare numbers ka sum return karta hai.

Example:

lst = [4, 2, 7, 1]
print(sum(lst))  # Output: 14

5️⃣ sorted()
Iterable ko sort karke nayi list return karta hai (original list change nahi hoti).

Example:

lst = [4, 2, 7, 1]
print(sorted(lst))      # Output: [1, 2, 4, 7]
print(sorted(lst, reverse=True))  # Output: [7, 4, 2, 1]

6️⃣ zip()
 Do ya zyada iterables ko tuple me pair karke combine karta hai.
Example:
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

zipped = zip(names, scores)
print(list(zipped))  
# Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

7️⃣ enumerate()
 Iterable ke elements ke saath index bhi provide karta hai.

Example:

lst = ["a", "b", "c"]
for index, value in enumerate(lst):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c

8️⃣ any()

 Iterable me koi bhi element True ho to True return karta hai.

Example:

lst = [0, False, 5]
print(any(lst))  
9️⃣ all()

Iterable me sab elements True ho to True return karta hai.

Example:

lst = [1, True, 5]
print(all(lst))  # Output: True

lst2 = [1, 0, 5]
print(all(lst2)) # Output: False
************************************************************************
1️⃣ Instance Variables
Instance variables wo variables hote hain jo har object ke liye alag hote hain.
Object create karne ke baad har object ka apna copy hota hai.
Mostly __init__ method me define kiye jaate hain.

2️⃣ Class Variables
Class variables wo variables hote hain jo poore class ke objects me common hote hain.
Sabhi objects same value share karte hain.
Class ke andar but init ke bahar define kiye jaate hain.

**************************************************************************
Module	Use
math	Math functions like sqrt()
random	Random numbers
datetime	Date and time
os	Operating system commands
sys	System-specific parameters
json	Working with JSON data

#########################################################################################


*****************************************************************************
List (5 Programs – Questions only)
List me 10 numbers lo aur unka sum find karo.
List ke sabse bade aur sabse chhote element ko find karo.
List ko reverse karo bina built-in function ke.
List me se duplicate elements remove karo.
Do lists ko merge karke ek single list banao.
Tuple (5 Programs – Questions only)
Tuple me kitne elements hain, count karo.
Tuple ka maximum aur minimum element find karo.
Tuple ko list me convert karo.
Tuple me given element present hai ya nahi, check karo.
Do tuples ko concatenate karo.
Dictionary (5 Programs – Questions only)
Dictionary ke sabhi keys aur values print karo.
Dictionary me kisi key ka value update karo.
Dictionary me se given key delete karo.
Dictionary ka size (number of key-value pairs) find karo.
Do dictionaries ko merge karo.
Set (5 Programs – Questions only)
Set me elements add karo aur print karo.
Do sets ka union find karo.
Do sets ka intersection find karo.
Set me se duplicate elements kaise remove hote hain, show karo.
Set me given element present hai ya nahi, check karo.


88888888888888888888888888
1.I studied modules and revised file handling and exception handling.
2.completed the previously pending task.
3.practiced logic-based questions.
************************************************************************************
1."Python is an interpreted language because code is executed line by line by the Python interpreter without a separate compilation step."
2. Indentation: In Python, indentation is used to define code blocks. It replaces the use of braces {}
3.What are mutable and immutable objects? Give examples.
Mutable objects can be changed after creation, like list, dict, and set. Immutable objects cannot be changed after creation, like int, str, tuple, and frozenset."
4.Why are strings immutable in Python?

Python same string object ko reuse kar sakta hai memory save karne ke liye.
Immutable hone ki wajah se strings hashable hote hain.
Iska matlab hai aap strings ko dictionary keys ya set elements me use kar sakte ho.

5.Difference between type() and isinstance().
type() returns the exact type of an object, ignoring inheritance, while isinstance() checks if an object is an instance of a class or its subclass, respecting inheritance."
6.What is List Comprehension?
Isse aap loops + conditionals ek hi line me likh sakte ho.
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

7.What is a set? Are duplicate values allowed?

8.Difference between append() and extend() methods.
append() a
dds a single element to the list, while extend() adds all elements of an iterable to the list individually."
 9.Shallow copy vs deep copy.
Shallow Copy
Definition: Shallow copy ek nayi object create karta hai, lekin andar ke elements ke references same rehte hain.
Matlab, nested objects change honge to original me bhi reflect hoga.
 import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 100
print(original)  # Output: [[100, 2], [3, 4]]  # Original bhi change hua

DeepCopy:
Deep Copy
Definition: Deep copy ek completely independent copy create karta hai, nested objects bhi new copy ban jati hai.
Matlab, original aur copy bilkul separate ho jaate hain.
copy.deepcopy() use hota hai.
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 100
print(original)  # Output: [[1, 2], [3, 4]]  # Original safe hai

"Shallow copy creates a new object but shares nested objects with the original,
 while deep copy creates a fully independent object including nested objects."

10.What is a function? Types of functions in Python.
A function is a reusable block of code that performs a specific task. Python has built-in functions, user-defined functions, lambda (anonymous) functions, and recursive functions."
Built-in Functions
Python already provide karta hai kuch ready-made functions.
Examples: print(), len(), type(), max(), min()

11. self: self parameter current object ka reference hai.

12. 
What is a constructor (__init__) in Python
"In Python, a constructor is a special method __init__() that initializes the object’s attributes automatically when the object is created."

 13.Explain polymorphism.
 type of polymorphism
Operator Overloading
Definition: Operator overloading is when the same operator behaves differently for different types of objects.
Method Overriding
Duck Typing (Dynamic Polymorphism) – Python me type checking runtime pe hota hai; same method name different objects pe work kare.
Python me object ka type important nahi hota,
uska behavior (methods) important hota hai.
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

14.What is the use of super() function?

15.A module in Python is a file containing Python code (functions, classes, variables) that can be imported and reused in other Python programs."
built in modules:
math, os, random.

What is a package?
package in Python is a folder that contains multiple modules and an __init__.py file, used to organize related modules and manage namespaces."

16..Difference between import module and from module import *.

import module_name
Meaning: Ye poora module import karta hai.
Access: Module ke functions, classes, variables ko access karne ke liye module_name. prefix use karna padta hai.

from module_name import *
Meaning: Ye module ke saare public functions, classes, variables ko directly import kar leta hai.

Access: Module name ka prefix nahi lagana padta, direct function/variable use hota hai.
17..Differences between read(), readline(), readlines().
read() → reads entire file at once

readline() → reads one line at a time

readlines() → reads all lines and returns them as a list


18 rb – Read Binary Mode
 File ko binary format me read karta hai.
Images, audio, video, PDF jaise files ke liye use hota hai.

19.Packing (in Python)

Packing means putting multiple values into a single variable (usually a tuple or list).

Example:

data = 1, 2, 3


Here, 1, 2, 3 are packed into one tuple.

📤 Unpacking (in Python)

Unpacking means taking values out of a collection and assigning them to separate variables.

Example:

a, b, c = (1, 2, 3)


Here, values from the tuple are unpacked into a, b, and c.

20.Composition
Composition means one object contains another object and uses it to do its work.
***********************************************************************************************************************************************************
Basic Python Questions

What is Python? What are its key features?

Is Python an interpreted or compiled language?

What is the role of indentation in Python?

Differences between Python 2 and Python 3.

How do you write comments in Python?

🔹 Data Types & Variables

What are the built-in data types in Python?

What are mutable and immutable objects? Give examples.

Differences between List and Tuple.

Why are strings immutable in Python?

Difference between type() and isinstance().

🔹 Lists, Tuples, Sets, Dictionaries

What is list comprehension?

Why must dictionary keys be immutable?

What is a set? Are duplicate values allowed?

Difference between append() and extend() methods.

Shallow copy vs deep copy.

🔹 Functions & OOP

What is a function? Types of functions in Python.

Explain *args and **kwargs.

What is OOP? How is it implemented in Python?

Difference between class and object.

What is a constructor (__init__) in Python?

🔹 Inheritance & Polymorphism

What is inheritance? Types of inheritance.

What is method overriding?

What is the use of super() function?

Explain polymorphism.

What is encapsulation?

🔹 Exception Handling

What is an exception?

Explain try, except, else, finally.

How to create a custom exception?

🔹 Modules & Packages

What is a module?

What is a package?

Difference between import module and from module import *.

🔹 File Handling

How do you open a file in Python?

Differences between read(), readline(), readlines().

Explain file modes (r, w, a, rb).

🔹 Advanced / Tricky Questions

What is GIL (Global Interpreter Lock)?

What is a generator? Explain the yield keyword.

What is a decorator?

What is a lambda function?

How does memory management work in Python?

Multithreading vs multiprocessing in Python.

Revised complete Core Python concepts
Practiced string-based logical questions
****************************************************************************************************************************************
****************************************************************************************************************************************
****************************************************************************************************************************************
*******************************************************************************************************************************************
                                                                          SQL: 
1.SQL stands for Structured Query Language
2.SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987
 
CREATE DATABASE statement is used to create a new SQL database.
CREATE DATABASE databasename;
.The DROP DATABASE statement is used to drop an existing SQL database.
 DROP DATABASE databasename;

The SQL BACKUP DATABASE Statement
The BACKUP DATABASE statement is used in SQL Server to create a full back up of an existing SQL database.\


backup:C:\Users\Paras>"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u root -p new_database > "C:\Users\Paras\new_database_backup.sql"

1.Distinct
.The SQL SELECT DISTINCT Statement:it is use to return only distinct(different) values
 select distinct country from student.
.SELECT Example Without DISTINCT
 select country from student
.Count Distinct
By using the DISTINCT keyword in a function called COUNT, we can return the number of different countries.
 select count(distinct country) from student

2. WHERE Clause
   the where clause use to filter records
   it is used to extract only those records that fullfill a specified   condition
1.select * from student where country="rewa";
2.select * from student where id=1;

Operators in The WHERE Clause:
=
>
<
>=
<=
<>
select * from student where country="MP";
select * from student where id=1;
select * from student where id>3;
select * from student where id=5;
select * from student where id<=5;

between: between a certain range
  select * from  student where city between 90 and 85;

like: search for a pattern
  select * from student where city like 'r%';

in: to specify multiple possible values for a column
   select * from student where city in('rewa','satna','maihar');

3.The SQL ORDER BY
 The ORDER BY keyword is used to sort the result-set in  ascending or descending order

select * from student order by marks;
select * from student order by marks desc;
select * from student order by city;
select * from student order by city desc;
select * from student order by city,marks;
select * from student order by city asc,marks desc;

4.The SQL AND Operator
 The WHERE clause can contain one or many AND operators.
 AND: The AND operator displays a record if all the conditions are TRUE.

5.OR: The OR operator displays a record if any of the conditions are TRUE.

select * from student where country='MP' AND city lIKE '%a';
select * from student where country='MP' AND city='rewa' AND id<5 ;
select * from student where country='MP' and (city='%r' or grade='A');
select * from student;
select * from student where country='MP' or grade='%A' or marks=5
6.The NOT operator is used in combination with other operators to give the opposite result, also called the negative result.
select * from student where not city="rewa";
select * from student where grade not like '%A';
select * from student where id not between 60 and 80;
select * from student where  not marks>80;

7.SQL INSERT INTO Statement
The INSERT INTO statement is used to insert new records in a table.
insert into student(id,name,rno,grade,city,country,marks)values(6,'niya',555,'A','rewa','US',90);

Insert Data Only in Specified Columns
It is also possible to only insert data in specific columns.

Insert Multiple Rows
It is also possible to insert multiple rows in one statement.
insert into student(id,name,rno,grade,city,country,marks)values(7,'niya',655,'A','rewa','US',90),(8,'siya',666,'B','satna','US',56);

8.Alter: it is use to insert new column 
       alter table student add columnname datatype;
       add column value:
       update student set columnname="value" where id=1

    ALTER TABLE student
  ADD address varchar(10);
  update student set address="nagod" where id=1;
9.UPDATE Statement
  the update statement is used to modify the exisiting records in a table
  udate student set city="rewa" where id=2;
  1.update student set address='rewa' where id=2;
  2.update student set address='panna', city='satna' where id=2;
10.The SQL DELETE Statement
The DELETE statement is used to delete existing records in a table.
 delete  from student where id=8;
ALTER TABLE student
DROP COLUMN address;

.Delete All Records
   DELETE FROM table_name;
.Delete a Table
  DROP TABLE Customers;
11.A SQL clause that restricts the number of rows returned by a query.
select * from student limit 3 ;
select * from student order by grade  desc limit 3 ;
.OFFSET: SQL me batata hai kitni rows skip karni hai query ke result me, pehle se count karke.
 select * from student limit 3 offset 4 ;

12.SQL Aggregate Functions
An aggregate function is a function that performs a calculation on a set of values, and returns a single value.

Aggregate functions are often used with the GROUP BY clause of the SELECT statement. 
The most commonly used SQL aggregate functions are:

MIN() - returns the smallest value within the selected column
MAX() - returns the largest value within the selected column
COUNT() - returns the number of rows in a set
SUM() - returns the total sum of a numerical column
AVG() - returns the average value of a numerical column

13.Alias: give the column name using as keyword
select sum(marks) as marks from student where id<5;

14.The SQL LIKE Operator
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

The percent sign % represents zero, one, or multiple characters
The underscore sign _ represents one, single character

15.The _ Wildcard
The _ wildcard represents a single character.
It can be any character or number, but each _ represents one, and only one, character.
 
Return all customers from a city that starts with 'L' followed by one wildcard character, then 'nd' and then two wildcard characters:
SELECT * FROM Customers
WHERE city LIKE 'L_nd__';

.The % Wildcard
The % wildcard represents any number of characters, even zero characters.
Example
Return all customers from a city that contains the letter 'L':

SELECT * FROM Customers
WHERE city LIKE '%L%';

 SELECT * FROM Customers
WHERE CustomerName LIKE 'a%' OR CustomerName LIKE 'b%';

.Ends With
To return records that ends with a specific letter or phrase, add the % at the beginning of the letter or phrase.
Example
Return all customers that ends with 'a':

SELECT * FROM Customers
WHERE CustomerName LIKE '%a';

.Return all customers that starts with "b" and ends with "s":

SELECT * FROM Customers
WHERE CustomerName LIKE 'b%s';

.Contains
To return records that contains a specific letter or phrase, add the % both before and after the letter or phrase.

Example
Return all customers that contains the phrase 'or'

SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';

.Combine Wildcards
Any wildcard, like % and _ , can be used in combination with other wildcards.

Example
Return all customers that starts with "a" and are at least 3 characters in length:

SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';
.Return all customers that have "r" in the second position:

SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';

.Without Wildcard
If no wildcard is specified, the phrase has to have an exact match to return a result.

Example
Return all customers from Spain:

SELECT * FROM Customers
WHERE Country LIKE 'Spain';

.Using the [] Wildcard
The [] wildcard returns a result if any of the characters inside gets a match.
Example
Return all customers starting with either "b", "s", or "p":

SELECT * FROM Customers
WHERE CustomerName LIKE '[bsp]%';

. Using the - Wildcard
The - wildcard allows you to specify a range of characters inside the [] wildcard.

Example
Return all customers starting with "a", "b", "c", "d", "e" or "f":

SELECT * FROM Customers
WHERE CustomerName LIKE '[a-f]%';

select * from student where address like 'p%';
select * from student where address like 'p_la____';
select * from student where city like '%n%';
select * from student where city like 're%' or  city like '%na';
16.SQL JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
Different Types of SQL JOINs
Here are the different types of the JOINs in SQL:

1.(INNER) JOIN: Returns records that have matching values in both tables
select students.student_id,name,marks from students inner join marks on students.student_id=marks.student_id;
select students.student_id,name,marks ,courses from students 
inner join marks on students.student_id=marks.student_id
inner join courses on students.student_id=courses.student_id;

2.LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table

 select  students.student_id,name,marks from students
 left join marks on students.student_id=marks.student_id;

3.RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
select students.student_id, name,marks from students 
right join marks on students.student_id=marks.student_id;

4.FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
SELECT students.student_id, name, marks
FROM Students 
LEFT JOIN Marks 
ON students.student_id = marks.student_id

-- RIGHT JOIN part (Marks ke extra records)
SELECT students.student_id, name, marks
FROM Students 
RIGHT JOIN Marks 
ON students.student_id = marks.student_id;


17.UNION:

.The UNION operator is used to combine the result-set of two or more SELECT statements.
.The UNION operator automatically removes duplicate rows from the result set.

select student_id from students
union
select student_id from marks;

 18.Union all:
.The UNION ALL operator is used to combine the result-set of two or more SELECT statements.
.The UNION ALL operator includes all rows from each statement, including any duplicates.
select student_id from students
union all
select student_id from marks;

18.The EXISTS operator is used to test for the existence of any record in a subquery.
.The EXISTS operator returns TRUE if the subquery returns one or more records.
(EXISTS operator check karta hai ke koi subquery result return karti hai ya nahi.)
Agar karti hai → TRUE
Agar nahi karti → FALSE
select name from students where exists(select marks from Marks where students.student_id=marks.student_id and marks<85);

19.Group by statement: the group by statement groups rows that have the same values into a summary rows ,like find the number of customers in each country

The GROUP BY statement is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.

select count(id) as student_id, country from student group by country

20.SELECT INTO ka use hota hai
ek table ka data nikaal kar automatically naya table banane ke liye

CREATE TABLE firstclass AS
SELECT *
FROM Student
WHERE Marks >= 70;

CREATE TABLE firstclas AS
SELECT *,
'firstclas' as result
FROM Student
WHERE Marks >= 70;

21. CASE Expression:The CASE expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement). So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.

If there is no ELSE part and no conditions are true, it returns NULL.

SELECT id,
       CASE
           WHEN id > 5 THEN 'id is greater than 5'
           ELSE 'id is not greater than 5'
       END AS student_id
FROM student;
22.Null function: IFNULL() 
IFNULL() MySQL ka built-in function hai jo NULL values ko handle karta hai.

1.SELECT id, name, IFNULL(marks, 0) AS marks
FROM Student;
2.SELECT id, IFNULL(name, 'Unknown') AS student_name
FROM Student;
23. single line comment
-- Ye ek single-line comment hai
/*
Ye ek multi-line comment hai
Ye multiple lines me likha ja sakta hai
Aur query ke andar bhi safely use hota hai
*/
SQL Logical Operators
Operator	Description	Example
ALL	TRUE if all of the subquery values meet the condition	
AND	TRUE if all the conditions separated by AND is TRUE	
ANY	TRUE if any of the subquery values meet the condition	
BETWEEN	TRUE if the operand is within the range of comparisons	
EXISTS	TRUE if the subquery returns one or more records	
IN	TRUE if the operand is equal to one of a list of expressions	
LIKE	TRUE if the operand matches a pattern	
NOT	Displays a record if the condition(s) is NOT TRUE	
OR	TRUE if any of the conditions separated by OR is TRUE	
SOME	TRUE if any of the subquery values meet the condition


22.SQL Constraints
SQL constraints are used to specify rules for the data in a table.
1.NOT NULL - Ensures that a column cannot have a NULL value
2.UNIQUE - Ensures that all values in a column are different
3.PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
4.FOREIGN KEY - Prevents actions that would destroy links between tables
5.CHECK - Ensures that the values in a column satisfies a specific condition(kareye insure karta hai ki column ki value codition fallow)
6.DEFAULT - Sets a default value for a column if no value is specified
7.CREATE INDEX - Used to create and retrieve data from the database ve
**************************************
**************************************
**************************************
select * from student where country="MP";
select * from student where id=1;
select * from student where id>3;
select * from student where id=5;
select * from student where id<=5;
select * from  student where city between 90 and 85;
select * from student where city like 'r%';
select * from student where city in('rewa','satna','maihar');
select * from student order by marks;
select * from student order by marks desc;
select * from student order by city;
select * from student order by city desc;
select * from student order by city,marks;
select * from student order by city asc,marks desc;
select * from student where country='MP' AND city lIKE '%a';
select * from student where country='MP' AND city='rewa' AND id<5 ;
select * from student where country='MP' and (city='%r' or grade='A');
select * from student;
select * from student where country='MP' or grade='%A' or marks=55;
select * from student where not city="rewa";
select * from student where grade not like '%A';
select * from student where id not between 60 and 80;
select * from student where  not marks>80;
insert into student(id,name,rno,grade,city,country,marks)values(6,'niya',555,'A','rewa','US',90);
select * from student;
ALTER TABLE student
MODIFY id INT NOT NULL AUTO_INCREMENT;
INSERT INTO student (name, rno, city)
VALUES ('prabha', 101, 'rewa');
insert into student(id,name,rno,grade,city,country,marks)values(7,'niya',655,'A','rewa','US',90),(8,'siya',666,'B','satna','US',56);
ALTER TABLE student
ADD address varchar(10);
update student set address="nagod" where id=1;
SELECT COUNT(*) FROM student;
SELECT COUNT(city) FROM student;
update student set city="satna" where id=1;
update student set address='rewa' where id=2;
update student set address='panna', city='satna' where id=2;
delete  from student where id=8;
ALTER TABLE student
DROP COLUMN address;
select * from student limit 1 offset 5 ;
select * from student order by grade  desc limit 3 ;
select MIN(marks) from student as smallestPrice;
select max(marks) as maxmarks,rno from student group by rno ;
select count(name) from student;
select count(*) from student;
select count(marks) from student where marks>80;
select count(distinct name) from student;
select * from student;

//////////////////////////////////////////////////////
task:
1.Write a query to retrieve the department_name and location of people who live in location that starts with 'S'.
 ans.select department_name ,location from departments  where location like "S%";

2.Task
Write a query to find all product_name and category that have a price greater than 100.00 from the Products table.

Ans.select product_name,category from Products where price>100;

3.Task
Write a query to calculate the average salary across all companies combined. Rename the column as avg_salary.

Ans.SELECT AVG(salary) AS avg_salary FROM Works;

4.Task
Write a query to select all the distinct companies (company_name) in the Works table.
Table name: Works

Ans.SELECT DISTINCT company_name fROM Works;

5.Task
Write a query to find the total count of books whose genre is Fiction.
Note: Output column name should be fiction_count.

Ans: SELECT COUNT(genre) as Fiction_count from Books where genre like 'Fiction';

6. Task
Write a query to select only the movie names where the ratings are greater than 7 but less than 9.
Table: Cinema
Ans: select Movie_name from Cinema where Rating>7 and Rating<9;

7.Task
Write a query to retrieve book_id, title, author and published_year of the books which have NULL rating for their books.
Table name: Library

Ans:select book_id,title,author,published_year from Library where rating is null;

8.Task
Create a query to retrieve the employee_name, company, and salary for employees in the full-time category, ordered by salary in descending order
Table name: Employees

Ans: select employee_name, company,salary from Employees where category="Full-Time" order by salary desc;

9.Task
Write a query to group the employees by their department and display the total number of employees (as total_employees) in each department.
Table name: Employees

Ans: select department, count(Employee_id) as total_employees from Employees group by department;

10.Task
Write a query to retrieve the author_id, author_name, and publication_name for authors whose articles got zero views. The result should be sorted by author_id in ascending order.
Return the result table sorted by id in ascending order.
Table name: Views

Ans:select author_id, author_name,publication_name from Views where view_count=0 order by author_id ;

11.Task
Write a query to find the names of the top 3 distinct players by highest score who have won matches, including their scores.
Table 1: Players
Ans:SELECT DISTINCT Players.player_name, Players.score
FROM Players JOIN Matches ON Players.player_name = Matches.winner
ORDER BY Players.score DESC
LIMIT 3;

 12. Task
Write a query to retrieve the details of the last five matches played, including the match ID, the names of the players who participated, the name of the winning player, match date, and the final score of the winner.

There are two tables named Players and Matches.

Ans:SELECT m.match_id, m.player_1, m.player_2, m.winner, m.match_date, p.score
FROM Matches m
JOIN Players p ON m.winner = p.player_name
ORDER BY m.match_date DESC
LIMIT 5;
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

*****************************************************
C:\Users\Paras>python -m pip install Django
C:\Users\Paras> django-admin --version
C:\Users\Paras>cd my_tennis_club
C:\Users\Paras\my_tennis_club>python manage.py runserver
C:\Users\Paras\my_tennis_club>python manage.py migrate
C:\Users\Paras\my_tennis_club>python manage.py runserver
C:\Users\Paras\my_tennis_club>python manage.py startapp members

Django:Django is a back-end server side web framework.
Django is free, open source and written in Python.
Django is a Python framework that makes it easier to create web sites using Python.

1 The Model:
Manages the database
Defines tables and fields
Stores and retrieves data

2️⃣ View (Handles Logic)
Receives the request from the user
Gets data from the Model
Sends data to the Template

3️⃣ Template (Handles Presentation)
Displays data to the user
Uses HTML with Django template language

🔁 MVT Flow

User sends a request through the browser
View receives the request
Model provides the required data
Template renders the data

what the difference between project and app
Project = The complete system or website
App = A single feature or module within the project
 learned  PEP 8 Check PEP 8 violations,Auto-format code with Black,Sort imports with isort
tart the django framework install django and create project understaing diffrence between project and app
******************************************************************
what is __init__.py,asgi.py,setting.py,setting.py,urls.py,wsgi.py,db.sqlite3,manage.py in django project in hinglish
*******************************************************************
_Quick Summary Table
File	Purpose
__init__.py	Makes folder a Python package
settings.py	Project configuration
urls.py	URL routing
wsgi.py	Production server connection
asgi.py	Async & real-time support
manage.py	Run project commands
db.sqlite3	Database file

__init__.py:
This file tells Python that the folder is a Python package.
Python file hai jo Python interpreter ko batata hai ki us directory ko ek Python package ki tarah treat kiya jaaye। Jab aap us package se kuch import karte hain, toh yeh file sabse pehle run hoti hai।
It is usually empty.

asgi.py:
Yeh Asynchronous Server Gateway Interface (ASGI) entry point hai. Iska use asynchronous web servers dwara aapke project ko serve karne ke liye kiya jaata hai, khaaskar real-time applications, WebSockets, aur chat ke liye।
Uvicorn
Daphne
Hypercorn
👉 Use
Chat applications
Live notifications
Real-time features
WebSockets
High concurrency apps

settings.py:
Yeh aapke pure Django project ki main configuration file hai. Ismein saari settings hoti hain jaise ki database connection details, installed apps, security keys (SECRET_KEY), time zone (TIME_ZONE), static files ki location (STATIC_URL), aur debugging mode (DEBUG)।

urls.py:
Yeh aapke project ka "table of contents" ya URL dispatcher hai. Yeh file define karti hai ki kaun se URL pattern (web address) ko kis view function se connect karna hai. Jab koi user URL access karta hai, toh Django pehle urls.py mein us pattern ko search karta hai।
This file handles URL routing.
It connects URLs to views (functions).
path('home/', views.home)

wsgi.py:
Yeh Web Server Gateway Interface (WSGI) entry point hai. Production web servers (jaise Gunicorn, Apache, Nginx) is file ka use karke aapke Django application se communicate karte hain aur user requests ko handle karte hain。

manage.py:
Yeh ek command-line utility script hai jo aapko apne Django project ke saath interact karne deta hai. Iski madad se aap server run kar sakte hain (python manage.py runserver), database migrations apply kar sakte hain (python manage.py migrate), apps create kar sakte hain (python manage.py startapp), Django documentation

db.sqlite3:
Yeh aapke project ka default lightweight database file hai jab aap pehli baar project set up karte hain. Yeh ek single file-based relational database engine hai, jisse development ke dauran use karna aasaan hota hai। Production mein aksar iski jagah dusre powerful databases jaise PostgreSQL, MySQL, ya Oracle ka use hota hai. 
App:
admin.py,apps.py,models.py,views.py in app django in hinglish
admin.py: Yeh file Django Admin Panel ke liye hoti hai. Jab aap koi model (models.py mein define kiya hua database structure) banate hain, usko admin interface mein manage (add, edit, delete) karne ke liye, us model ko yahan register karna padta hai. Isse aapko data management ke liye ek built-in dashboard mil jaata hai.

apps.py: Yeh file aapki app ki configuration (settings) handle karti hai. Ismein AppConfig class hoti hai jo Django ko batati hai ki aapki app kaise behave karegi. Jab Django start hota hai aur INSTALLED_APPS mein aapki app ko dekhta hai, toh woh is file mein define ki gayi config ko load karta hai.

models.py: Yeh file aapke application ke database structure (database tables) ko define karti hai. Yahan aap Python classes likhte hain jo django.db.models.Model ko inherit karti hain. Har class ek database table hoti hai, aur uske attributes table ke columns (fields) hote hain. Django ka ORM (Object-Relational Mapper) in classes ko database queries mein translate karta hai.

views.py: Is file mein view functions ya classes hoti hain jo user ke web requests ko handle karti hain aur responses return karti hain. Yeh views models se data fetch kar sakti hain, us data ko process kar sakti hain, aur phir ek response (jaise ki HTML webpage) render karke user ko bhejti hain. Yeh aapki application ka main logic part hai.

Shell ka benefit

Quick testing: Model aur database ko turant test kar sakte ho

Debugging: Functions ya queries check kar sakte ho

Data manipulation: Database me directly objects create, update, delete kar sakte ho


Perfect! 😄 Chalo step by step samajhte hain ki Django shell ke 14 automatically imported objects me kya kya hota hai aur unka use kaise karte hain.

🔹 1️⃣ Common automatically imported objects

Jab tum python manage.py shell chalaoge, Django kuch objects shell me ready-to-use bana deta hai.

Yeh usually hota hai:

Object	Use
User	Django ka built-in user model (django.contrib.auth.models)
Group	User groups (permissions ke liye)
Tumhare app ke models	Jaise agar app ka naam polls hai → Question, Choice model ready hoga
settings	Django project ke settings access karne ke liye (django.conf.settings)
timezone	Date/time operations ke liye (django.utils.timezone)
reverse	URL ka naam se path nikalne ke liye (django.urls.reverse)
get_user_model	Agar custom user model use kar rahe ho, to access ke liye
slugify	Text ko slug me convert karne ke liye
now	Current datetime ke liye shortcut
cache	Django caching ke liye
connection	Database connection directly access karne ke liye
ContentType	Models ke meta info ke liye
Permission	User permissions ke liye
signals	Django signals ke liye (post_save, pre_delete, etc.
///////////////////////////////////////////////////////////////////////////
Important Concepts Covered

✔ URL namespace (polls:vote)
✔ POST method
method="post" → Data POST request ke through bheja jayega (secure & correct way for form submission).
✔ CSRF protection


name="results" → Iska URL name.


✔ Template loops
✔ Dynamic form inputs
✔ Radio button grouping
////////////////////////////////////////////////////////////
POST is an HTTP method used to send data from a client (like a web browser) to a server.

Unlike GET, which only requests data from the server, POST actually submits data to the server for processing.
Perfect! Let’s make the difference between POST and GET super clear and easy to remember. 

1️⃣ Conceptual Difference
Feature	GET	POST
Purpose	Fetch data from server	Send data to server for processing
Data location	Sent in URL (query string)	Sent in request body (hidden from URL)
Visible in URL	Yes	No
Security	Less secure (data visible, can be bookmarked)	More secure for sensitive data (hidden in request body)
Idempotent?	Yes (doesn’t change server)	No (changes server data, e.g., submitting a vote)
Bookmarkable	Yes, URL can be saved/shared	No, form submission data cannot be bookmarked
Length limit	Yes, URL length limit (~2000 characters)	No, can send large amount of data
Use case example	Search box, filtering pages	Form submission, login, voting

How Django Protects Against CSRF

Django uses a CSRF token to verify that POST requests come from your website, not a malicious site.

Token is unique for each session/user.


2️⃣ CSRF Token

Ye security ke liye hota hai.

Django POST request accept nahi karega agar CSRF token nahi hoga.

Ye Cross-Site Request Forgery attack se bachata hai.

👉 Important: POST form me hamesha {% csrf_token %} lagana zaroori hai.

Generic View: ka matlab hai pre-built view classes jo common kaam (jaise list dikhana, detail page dikhana, form handle karna) automatically kar deti hain — taaki hume baar-baar same logic na likhna pade.

1.Your project’s TEMPLATES setting describes how Django will load and render templates.
2.in view pahle loader use kiya and fir render()use kiya
3.handle http404 exceptionusing try,exept,raise then handle using get_object_or_404()¶
4.<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>isee analisec karke 1 point bna do ki kya kiya hai 4 no. ko
6. http request http response ye samjha
7. get and post samjha and csrf token 

1.TEMPLATES Setting – Created and configured the TEMPLATES setting to load and render HTML templates.
2.loader and render() – First used loader to load templates manually, then used render() as a shortcut to return    
responses easily.
3.Http404 Handling – Used  try-except with raise Http404
4.get_object_or_404() – I used it to safely fetch an object and automatically raise a 404 error if it doesn’t exist.
5.Created a form, used POST method, and added CSRF token to submit the selected choice to the vote URL.
6.HTTP Request/Response – Understood how the client sends a request and the server returns a response.
7.GET, POST Learned the difference between GET and POST 

###########################################################################
"""
"""
 from shortenerapp.models import UrlData
 obj=UrlData.objects.create(url="https://www.google.com",)
 obj=UrlData.objects.create(url="https://www.google.com",slug="priya.com")
 obj.url
'https://www.google.com'
C:\Users\Paras\geeksproject\geeksproject> python manage.py createsuperuser
Username (leave blank to use 'developer'): shortenerapp
Email address: shortenerapp@gmail.com
Password:shortenerapp123
************************************************************************888
***********************************************************************8888
*****************************************************************************8
************************************************************************88888888888888
Common Django ORM Query Methods
.all(): Retrieve all objects of a model.
.filter(): Retrieve objects that match specific conditions.
.exclude(): Retrieve objects that do not match specific conditions.
.get(): Retrieve a single object that matches the condition (raises an error if multiple objects match).
.update(): Update multiple objects at once.
.delete(): Delete records from the database

python manage.py shell
from music.models import Song, Album
Inserting
Creating and Saving a Single Object: To create and save an Album object to the database, use the following command.

>>> a = Album(title="Divide", artist="Ed Sheeran", genre="Pop")
>>> a.save()

Similarly, to create and save a Song object associated with the previously created Album:

>>> s = Song(name="Castle on the Hill", album=a)
>>> s.save()

Inserting Multiple Records: Let’s add a few more albums to the database.

>>> a1 = Album(title="Abbey Road", artist="The Beatles", genre="Rock")
>>> a1.save()

>>> a2 = Album(title="Revolver", artist="The Beatles", genre="Rock")
>>> a2.save()

Here, we’ve added two more albums, both by The Beatles. Each call to save() writes the object to the database.

2. Retrieving
Retrieving All Records: To retrieve all records from the Album model, we use the all() method.

>>> Album.objects.all()
<QuerySet [<Album: Divide>, <Album: Abbey Road>, <Album: Revolver>]>

The QuerySet is a list-like object containing all the Album instances. The __str__() method is used to print the album title.

Filtering Records: You can filter records based on specific conditions using the filter() method.

>>> Album.objects.filter(artist="The Beatles")
<QuerySet [<Album: Abbey Road>, <Album: Revolver>]>

In this example, we retrieve albums by The Beatles.

Excluding Records: The exclude() method allows you to retrieve all records except those that match a condition.

>>> Album.objects.exclude(genre="Rock")
<QuerySet [<Album: Divide>]>

Here, we exclude albums with the genre Rock and retrieve the remaining albums.

Retrieving a Single Record: To retrieve a single object based on a unique field, use get(). Note that this will raise an exception if multiple objects match.

>>> Album.objects.get(pk=3)
<Album: Revolver>

Here, we're retrieving the album with primary key (pk) 3, which is Revolver.

3. Updating
Modifying an Existing Object: To update an existing record, first retrieve the object, modify its attributes, and then save it.

>>> a = Album.objects.get(pk=3)
>>> a.genre = "Pop"
>>> a.save()

This changes the genre of the album Revolver to 'Pop' and saves the update to the database.

Bulk Update: You can also update multiple objects at once using update().

>>> Album.objects.filter(artist="The Beatles").update(genre="Classic Rock")

This will update the genre of all albums by The Beatles to 'Classic Rock'.

4. Deleting
Deleting a Single Record: To delete a specific record, first retrieve the object and then call the delete() method.

>>> a = Album.objects.get(pk=2)
>>> a.delete()

After running this, the album with pk=2 (e.g., Abbey Road) will be deleted from the database.

Deleting Multiple Records: To delete multiple records at once, use filter() or exclude() combined with the delete() method.

>>> Album.objects.filter(genre="Pop").delete()

This will delete all albums with the genre 'Pop'. Be cautious as this operation cannot be undone.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BoolanField
CharField,ChoiceField , DateTimeField in, DecimalField DurationField EmailField FileField FilePathField 
FloatField GenericIPAddressField ImageField IntegerField MultipleChoiceField NullBooleanField RegexField 
SlugField TimeField TypedChoiceField TypedMultipleChoiceField URLField UUIDField 
"""
            


