"""
try:try block contain logical code and it can throw error
except:it is use to handle error
else: else block lets you execute code when there is no error.
finally: it always execute with try and except
*.raise keyword is used to forcefully create an error (exception).
ex
 Why use it?
You use raise for Validation. For example, if a user enters a negative age,
 Python won't stop them (because -5 is a valid number), but your logic says age can't be negative. So, you "raise" an error.
1.
 ValueError: Triggered when a function receives an argument of the correct type but an inappropriate value.
python
int("abc")  # Cannot convert alphabetic string to integer

2.TypeError: Raised when an operation is applied to an object of the wrong type.
python
"5" + 5  # Cannot add string and integer

3. Lookup and Index Errors
These occur when trying to access items in collections like lists or dictionaries.
IndexError: Raised when a sequence index is out of range.
python
lst = [1, 2, 3]
print(lst[5])  # Index 5 does not exist

4.KeyError: Raised when a dictionary key is not found.
python
d = {"name": "Alice"}
print(d["age"])  # "age" key is missing
5.
 Arithmetic Errors
Errors related to mathematical calculations fall under this category. 
ZeroDivisionError: Raised when dividing by zero.
python
result = 10 / 0

6.OverflowError: Occurs when a numerical result is too large to represent.
python
import math
math.exp(1000)  # Result exceeds limit for float

7. Name and Attribute Errors
These relate to identifiers (variables, functions) and object properties. 

NameError: Raised when a local or global name is not found.
print(unknown_var)  # Variable has not been defined

8.AttributeError: Triggered when an attribute reference or assignment fails.
python
x = 10
x.append(5)  # Integers do not have an 'append' method

5. File and Import Errors
These occur during external interactions or while loading code. 
FileNotFoundError: A subclass of OSError raised when a file is missing.
python
open("ghost_file.txt")  # File does not exist
Use code with caution.

ImportError / ModuleNotFoundError: Raised when an import statement fails.
import non_existent_module
Use code with caution.


StopIteration: Raised by an iterator to signal there are no further items.
KeyboardInterrupt: Raised when a user interrupts the program (usually via Ctrl+C).

IndentationError Raised when indentation is not correct in Python code.
SyntaxError	Raised when there is a mistake in Python syntax.
SystemExit	Raised when sys.exit() is called to terminate the program.

"""
#
try:
    x=10
    print(x)
except NameError:
    print("Variable x is not defined")    
except:
    print("Something else went wrong")    

print("1.......................") 

try:
    print("hello world") 
except:
     print("Variable x is not defined") 
else:
     print("Nothing went wrong")          

try:
    print("hello world") 
except:
     print("Variable x is not defined") 
else:
     print("it execute if try not throw error")     
finally:
     print("Nothing went wrong") 
print("1...........................")
#file open
try:
  f = open("d://product.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
"""
ex. raise
x=-1
if x<0:
    raise Exception("sorry no number below zero")
"""
"""
age=-5
if age<0:
    raise ValueError("age cannot be negative")
"""
# try except else finally
try:
    x=10
    y='l'
    z=x/y
except ZeroDivisionError:
    print("denominator should not be zero")
except TypeError:
    print("enter only numeric number")
else:
    print(z)    
finally:
    print("execution complete")  

#######################3333
def fun(age):
    if age<0:
        raise ValueError("enter postive age")
    #print(f"Age set to {age}")           
try:
    fun(-5)
except ValueError as e:
    print(e)    
"""
a=int("hello")#ValueError:
print(a)
"""
"""
b=10+"hello" # TypeError
print(b)
"""
"""
l=[1,2,3,4]
print(l[5])#IndexError: list index out of range
"""
"""
d={
    "name":"priya"
}
print(d["age"])#KeyError:
"""
"""
e=10/0
print(e)#ZeroDivisionError:
"""
#print(unknown_var) # NameError Variable has not been defined
"""
x=10
print(x.append()) # AttributeError: 'int' object has no attribute 'append'
"""
#f=open("d:\\priya.txt") #FileNotFoundError

#import non_existent_module #ModuleNotFoundError: No module named 'non_existent_module'
print("1.........")
a=int('1')
print(a)
import os

# Path to an empty folder
folder_path = "d:/priyafall"

try:
    os.rmdir(folder_path)
    print("Folder deleted successfully!")
except FileNotFoundError:
    print("Folder not found.")
except OSError:
    print("Error: Folder is not empty or cannot be deleted.")
folder_path = "d:/priyafile.txt"
try:
    os.remove(folder_path)
    print("Folder deleted successfully!")
except FileNotFoundError:
    print("Folder not found.")
except OSError:
    print("Error: Folder is not empty or cannot be deleted.")    

print(bool(False))