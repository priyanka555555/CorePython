"""
python function:
1.all(): function return true if all items in an iterable are true. otherwise it returns false
if the iterable object is empty the all() functions also return True
all(iterable)

2. abs(): it return abslute value
3. any(): return true if any itemm in an iterable object are true
4. ascii(): The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
5. returns the binary version of a number
6. returns the boolean value of the specified object
7.bytearray() : returns an array of byte
8.bytes(): returns a byte object
9.callable(): returns true if the specified object is callable otherwise false
x=5
print(callable(x))# normal variable is not callable
10. complex(): return a complex number by specifying a real number and imaginary number
11. chr():returns a character from the specified Unicode code.
12. dict(): returns a dictionary array
13. dir(): return all property and method of the specified object
14. divmod():The divmod() function returns a tuple containing the quotient  and the remainder 
15. enumerate(): takes a collection and returns it as an enumerate object
16.slice():the slice function returns a clice object
17. repr(): returns a readable version of an object
18. reversed() function returns a reversed iterator object
19.
"""
a=all([1,2,3])
b=all([0,2,3])
c=all((1,2,3))
print(c)# true
print(a)# true
print(b)# false
d=abs(3+7j)
print(d)
print(abs(-9))

# any()
a=any([0,2,3])
print(a)

x = ascii("My name is Ståle")
print(x)

x=bin(36)
print(x)

x=bool(0)# false
x=bool(1)# True
x=bool()# false
a=bool(True)# True
a=bool(False)# False
a=bool([1,2])# true
x=bytearray(4) # bytearray(b'\x00\x00\x00\x00')
print(x)

# callable()
def x():
    a=6
print(callable(x))  # true
 # complex()
x=complex(10)
print(x)

x=chr(97)# a
print(x)

class Person:
  name="John"
  age=36
  country="Norway"
delattr(Person,'age')# the person object will no longer contain an age property

x=dict(name="priya",age=90)
print(x)

class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

# divmod()
x=divmod(5,2)
print(x)

#zip()
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(dict(x))










