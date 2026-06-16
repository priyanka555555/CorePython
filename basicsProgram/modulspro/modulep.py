#a Python module is a file containing pre-written code (like functions, variables, or classes) that you can use in your other programs.#
#A Python module is a file containing Python code (functions, classes, variables, and statements) that can be reused in other program
#How to Create a Module
#Any file saved with a .py extension is a module
"""
Types of Modules
Python supports various types of modules to cover different programming needs. 
Built-in Modules: These come bundled with the Python installation and provide essential functionalities (e.g., math, os, sys, random). 
There are several built-in modules in Python, which you can import whenever you like.

User-Defined Module:. User-Defined Modules: These are modules you create yourself, such as calc.py.

@ we can use the module we just created, by using the import statement:
@Variables in Module he module can contain functions,also variables of all types (arrays, dictionaries, objects etc):
Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

4. Package Modules: A package is a directory containing multiple modules, usually with an __init__.py file.
Example Directory

mypkg/
    __init__.py
    calc.py
    utils.py
    st = "hello javaj"
d = {}



"""
st="hello javaj"
d={}

for i in range(len(st)):
    if st[i] not in "aeiou":
        if st[i] not in " ":
         c=0
         for j in range(len(st)):# e
            if st[i]==st[j] :# h==h
                c=c+1
            d[st[i]]=c # h:2 
print(d)        
   
#####################
st="hello javaj"
st1=""
d={}
for i in range(len(st)):
    if st[i] not in "aeiou":
      if st[i] not in " ":    
        if st[i] in d:
            d[st[i]]=d[st[i]]+1
        else:
            
            d[st[i]]=1

print(d)





            

