import platform
x=platform.system()
print(x)

#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
#The dir() function returns all properties and methods of the specified object, without the values.
#This function will return all the properties and methods, even built-in properties which are default for all object.
"""
dir() function in Python is a tool that provides a list of all the functions and features (attributes and methods)
 available inside an object or a module.

 @Types of Import Statements
1. Import From Module: This allows importing specific functions, classes, or variables rather than the whole module.
"""

x=10
s="hello"
print(dir())

import math
print(dir(math))

my_list = [1, 2, 3]
print(dir(my_list))

from math import sqrt, factorial
#from math import *
#import math as m
print(sqrt(16))


print(factorial(6))
print("1.......................")

import random
print(random.randint(1,5))
#Locating a Module
import sys
for p in sys.path:
    print(p)



