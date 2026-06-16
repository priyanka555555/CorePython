"""
Reference Counting :

in Python is a memory management technique.
Python keeps a count of how many references (variables) are pointing to an object.
Q1:how to manage python memory
Python uses reference counting and garbage collection to manage memory. Objects are stored in heap memory and variables are references stored in namespaces.

1. What is reference counting?
 Every object has a reference count:
 Counts how many variables refer to it
 a=[1,2,3]
 b=a
 Reference count of list = 2
 when 
 del a
 count becomes 1
 when counts=0
 memory is immediately freed
2. What is garbage collection?
A mechanism to clean up unused objects, especially circular references.
reference counting alone cannot handle circular references
example:
a=[]
b=[]
a.append(b)
b.append(a)


if.
del a
del b
then objects still reference each other -> memory leak
solution:
python uses garbage collector(GC)


3.Why is garbage collection needed if reference counting exists?
Because reference counting fails with circular references.

. What is PyMalloc?
A specialized allocator for small objects to improve performance.

6. What are Python memory layers?
Arena → Pool → Block

7. What is memory fragmentation?
Unused memory gaps that cannot be reused efficiently.

8. Explain generational GC.
Objects are grouped by lifetime. Younger objects are cleaned more frequently
9. How to detect memory leaks?
tracemalloc
gc.get_objects()
Profilers
'''
Memory Leak
Caused by:

Circular references
Global variables

High Memory Usage
Large lists/dicts
Unnecessary copies
'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
8. Important Internal Concepts
➤ Interning
Small integers & strings are reused
a = 10
b = 10
# Same memory location
➤ Immutable vs Mutable
Immutable objects → new memory on change
Mutable objects → same memory modified
"""
"""
def funn(func):
    print("hello") 
@funn     
def fun():
    print("hello") 
fun() 



*****************************
Deep Copy

A deep copy creates a completely independent copy of the original object, including all nested objects.
Changes in copied data do not affect the original object.
Example:
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print(a)   # [[1, 2], [3, 4]]
print(b)   # [[100, 2], [3, 4]]


A shallow copy creates a new object, but nested objects inside it are still shared with the original object.

Changes in nested data affect both copies.
Only the outer object is copied.
Shallow copy creates a new outer object, but inner objects are shared.

Example:

import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100

print(a)   # [[100, 2], [3, 4]]
print(b)   # [[100, 2], [3, 4]]
Deep Copy

A deep copy creates a completely independent copy of the original object, including all nested objects.

Changes in copied data do not affect the original object.

Example:
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print(a)   # [[1, 2], [3, 4]]
print(b)   # [[100, 2], [3, 4]]

Shallow Copy

A shallow copy creates a new object, but nested objects inside it are still shared with the original object.

Changes in nested data affect both copies.
Only the outer object is copied.

Example:

import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100

print(a)   # [[100, 2], [3, 4]]
print(b)   # [[100, 2], [3, 4]]

#################################################33
mutable vs immutable:

Mutable objects can be modified after creation,
while immutable objects cannot be modified once created.
mutable object can be changed after creation:
 same memory can be modified
list, set, dictionary
a = [1, 2, 3]

a[0] = 100


print(a)

immutable: immutable objects cannot be changed after creation.
int,string,tuple

a = "hello"
# a[0] = "H"   -> Error

for loop:
Used when number of iterations is known or when you are iterating over a sequence (list, string, range).

while loop
Used when condition is not fixed and loop runs until condition becomes False.


What is the difference between:

abstraction
encapsulation
Abstraction hides implementation details and shows only essential features, while encapsulation hides data and restricts direct access to it.
"""
#output [[1,2,3],[4,5,6],[7,8,9]]
    
l = [1,2,3,4,5,6,7,8,9]
n = 3
result = []
for i in range(0, len(l), n):
    result.append(l[i:i+n])
print(result)

    

