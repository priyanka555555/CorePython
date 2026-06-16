"""
txt="hello world and jgj"
print("hello"  in txt)# true
print("hello" not in txt)#false
print(len(txt))
"""
"""
txt="hello and jgj"
if "world" not in txt:
   print("no","world is not present in txt ")

# you can return a range of characters by using the slice 
# specify tha start index and the end index separated by a colon
   x=str("hello ,world")
   print(x[1:5])
   print(x[:5])
   print(x[2:])
   print(x[-4:-2])
"""
"""
a="hello world"
b=" HELLO WORLD"
print(a.upper())
print(b.lower())
print(b.strip()) #The strip() method removes any whitespace from the beginning or the end:
print(a.replace("world","hello"))
print(a.split(","))
"""
# F-String
"""
age=30
price=50
print(f"hello world",{age})
txt=f"the price is{price:.2f}"
txt=f"the price is{20*5}"

print(txt)
"""
#escape character \":
#txt = "We are the so-called \"Vikings\" from the north."
#txt = "Hello\tWorld!"
#print(txt)
"""
a="hello world"
b="HELLO WORLD"
print(a.upper())
print(b.lower())
print(b.strip()) #The strip() method removes any whitespace from the beginning or the end:
print(a.replace("world","hello"))
print(a.split(","))
print(a.capitalize())
print(b.casefold()) #Converts string into lower case
print(b.center(20,"h"))
"""
"""
txt="i love apple, apple are my favorite fruit"
x=txt.count("apple")
print(x)

txt = "My name is Ståle"

x = txt.encode()

print(x)
"""
"""
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
"""
"""
#The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
"""
#The expandtabs() method sets the tab size to the specified number of whitespaces.
"""
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(1)

print(x)
 """ 
"""
he find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
"""
"""
txt="hello world ,4"
x=txt.find("p")
print(x)
"""
"""
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
"""
"""
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"

x = txt.isalnum()

print(x)
"""
"""
The isalpha() method returns True if all the characters are alphabet letters (a-z).
txt = "CompanyX"

x = txt.isalpha()

print(x)

The isascii() method returns True if all the characters are ascii characters  (a-z).
txt = "Company123"

x = txt.isascii()

print(x)

join(): join method is use to combine elements of a list into a single string 
join() is used to combine elements of a list (or iterable) if all items is string
"""
l=['p','a','t','e','8']
l1="".join(l)
print(l1)

print(ord('A'))#convert  ASCII 
print(chr(ord('A')))

x=str("hello ,world")
print(x[1:5])
print(x[:5])
print(x[2:])
print(x[-4:-2])

s="hello world"
print(s.count("o"))




