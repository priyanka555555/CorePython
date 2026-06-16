#Python String Formatting
"""
An f-string (formatted string literal) is a way to embed variables or expressions directly inside a string by prefixing
it with the letter f and placing the values inside curly braces { }.
In short: It is the fastest and easiest way to mix text and data in Python without using plus signs + or complex formatting methods.
Example:
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
Before Python 3.6 we had to use the format() method.
to specify a string as an f-string, simply put an f in front of the string literal, 

Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
* A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
* You can perform if...else statements inside the placeholders:
* Use a comma as a thousand separator:

.format() is a string method used to insert values into a string using placeholders. While f-strings are now more popular,
.format() was the standard way to handle dynamic text before Python 3.6. 

How it Works
You define a string with curly braces {} as placeholders and then call the .format() method to provide the values that should fill them
* Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

main diff.
When you use .format(), Python has to look up the format method, call it as a function, and pass arguments to it. This extra "middleman" step takes time.
f-strings are not function calls. Python converts them directly into optimized bytecode at runtime. It’s like a shortcut that skips the overhead of calling a function.

python dynamic:
Python is a dynamically typed language the type of variable decided at run time not before
"""

txt=f"hello pyhton 3.6"
print(txt)

num=50
x=f"this is {num}"# variables
x1=f"this is {num:.2f} dollars"
print(x)
print(x1)

a=10
x1=f"this is {a*10}"# operation
print(x1)

name="priya"
x2=f"my name is {name.upper()}"# function
print(x2)

num=4
x3=f"{'even' if num%2==0 else 'odd'}"
print(x3)

num=50000
s=f"{num:,}"#se a comma as a thousand separator:
print(s)


def fun(x):
   return x
s=f"{fun(100)}"
print(s)

# format
price=90
txt="the price is {}" 
txt1="the price is {:.2f}"
print(txt.format(price))   
print(txt1.format(price)) 

# multiple values
name="priya"
age=40

txt="name is {0} age is {1}"
print(txt.format(name,age))

details="name is {name} age is {age}"
print(details.format(name="priya",age=90))

t="hello {}"
print(t.format(20))





