"""
x="hello"# Global variable
def fun():
    #x="hello world" # local variable
    global x
    x="hello world"
    print(x)
fun()   
print(x) 
"""
"""
x=range(1,10)
print(x)
print(list(x))
"""
"""
dict={"name":"priya","age":80}
print(dict)
"""
"""
x=frozenset({"apple","banana","cherry","cherr"})
print(x)
"""

"""
x=b"hello"
x=bytearray(5)
x = memoryview(bytes(5))
x=None
print(x)
"""
"""
x=3j
print(type(x))
  """  
import random

print(random.randrange(1, 10))