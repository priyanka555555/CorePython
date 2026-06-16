# Anonymous Nature: It removes the need to name a function you only use once, keeping your code from looking cluttered or "heavy."
# Instant Clarity: For simple tasks like math or filtering, it places the logic exactly where it's needed so you can understand it at a glance.
"""
lambda vs def Keyword
In Python, both lambda and def can be used to define functions, but they serve slightly different purposes. 
While def is used for creating standard reusable functions, lambda is mainly used for short, anonymous functions that are needed only temporarily.
The reduce() function is a tool that processes an entire list to produce a single value.
It takes the first two elements of a list, performs an operation, and then carries that result forward to the next element until only one final result remains.


PEP 8: Python Enhancement Proposal
PEP 8 is a style guide for writing clean and readable Python code.
PEP 8 is a set of rules to write clean, readable, and professional Python code.
1. Indentation
Use 4 spaces for indentation.

2. Line Length
Maximum 79 characters per line

3. Variable Names
Use lowercase with underscores

4. Function Names
Use lowercase and underscores

5. Spaces
Use spaces around operators

6.Imports
Write imports at the top
import math
import os

3. Tools for PEP 8

You can use tools like:

flake8 : flake8 checks your code for errors and style issues (PEP 8 rules).
flake8 myfile.py
pylint
black : black automatically formats your code.
black myfile.py

These automatically check or format your code.

"""
x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(10, 20))
print(y(1, 20))


############
def fun(n):
    return lambda a: a + n


f = fun(10)
print(f(20))

# The map() function applies a function to every item in an iterable:
l = [1, 2, 3, 4, 5]
x = list(map(lambda a: a * 2, l))
print(x)


# select the items base on the condition
l = [1, 2, 3, 4, 5, 6, 7]
x = list(filter(lambda a: a % 2 == 0, l))
print(x)

# sorted() can use lambda as a key
# The sorted() function can use a lambda as a key for custom sorting:
words = ["apple", "pie", "banana", "cherry"]
sort = sorted(words, key=lambda x: x)
print(sort)

t = lambda x: x + 10
print(t(10))
################################3
l = [1, 1, 2, 3, 1]
# output {1:3,2:1,3:1}


d = dict(enumerate(l))
for i, j in d.items():
    print(i, ":", j)
###########  o
l = [1, 1, 2, 3, 1]
# d={}
# for i in l:
#     #print(i)
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
###########
print("1111111111111111111111111")
rex = {}
for i in l:
    rex[i] = rex.get(i, 0) + 1  #
print(rex)
################
print("1111111111111111111111111")
l = [1, 1, 1, 2, 3]
rev = []
for i in l:
    if i not in rev:
        rev.append(i)  # 1,2,3
print(rev)
print("1111111111111111111111111")
###########
l = [1, 1, 1, 2, 3]
store = set()

for i in l:
    if i not in store:
        store.add(i)

print(store)
print("1111111111111111111111111")
import math

x = lambda a: math.sqrt(a)
print(x(4))
# Write a lambda function to check if a number is even or odd, returning the string "Even" or "Odd".
x = lambda a: "even" if a % 2 == 0 else "odd"
print(x(4))
# Given a list of integers, use filter() with a lambda to extract only the even numbers.
l = [1, 2, 3, 4, 5, 6]
y = list(filter(lambda a: a % 2 == 0, l))
print(y)
# Use map() with a lambda to square every number in a given list of integers.
# map() Python me ek function hai jo di hui function ko list (ya kisi iterable) ke har element par apply karta hai aur result return karta hai.

l = [1, 2, 3, 4, 5, 6]
s = list(map(lambda a: a * 2, l))
print(s)
# From a list of words, use filter() with a lambda to return only the words that start with a specific letter (e.g., "A").
l = ["hello", "world", "apple"]
s = list(filter(lambda a: a.startswith("a"), l))
print(s)

# Write a program to sort a list of tuples (e.g., [('English', 88), ('Science', 90)]) by their numerical grade using a lambda function as the key.
lt = [("d", 50), ("b", 40)]
x = sorted(lt, key=lambda a: a[1])
print(x)
# Sort a list of dictionaries (e.g., [{'name': 'Ali', 'age': 20}, ...]) by the 'age' value using a lambda key.
ld = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 18},
    {"name": "John", "age": 25},
]
x = sorted(ld, key=lambda a: a["age"])
print(x)
"""
print("Enter two numbers")
num = input()
x=lambda a,b:a+b,num
print(x)
"""
#################################
x = lambda a: "even" if a % 2 == 0 else "odd"
print(x(4))
# using with list comprehenssion

func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())
print("1...................")

# Using with reduce()
# reduce() function repeatedly applies a lambda expression to elements of a list to combine them into a single result.

from functools import reduce

l = [1, 2, 3, 4, 5]
r = reduce(lambda x, y: x + y, l)  # first 2 element 1+2=2,(x+y)=2+3
# r=reduce(lambda x,y:x+y,l)
print(r)

##########33333333
l = [1, 2, 3, 4, 5]
x = list(map(lambda a: a * 2, l))
print(x)

from functools import reduce

l = [1, 2, 3, 4, 5]
r = reduce(lambda x, y: x + y, l)
print(r)
##########################333
################################3
x = lambda x: x + 10
print(x(10))
l = [1, 2, 3, 4, 5]
y = [lambda x: i for i in l]
print(y)

from functools import reduce

l = [1, 2, 3, 4, 5]
r = reduce(lambda x, y: x + y, l)  # first 2 element 1+2=2,(x+y)=2+3
# r=reduce(lambda x,y:x+y,l)
print(r)

l = [1, 1, 2, 3, 1]
d={}
for i in l:
    if i in d:
        d[i].append(i)
    else:
        d[i]=[i]  
print(d)
for i ,j in d.items():
    if len(j)==1:
        d[i]=i
print(d)

l = [1, 1, 2, 3, 1]
l1 = (1, 1, 2, 3, 1)
l.insert(0,l1)
print(l)



