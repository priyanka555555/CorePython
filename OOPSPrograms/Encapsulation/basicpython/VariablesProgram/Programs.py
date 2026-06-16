name="priya"# global variable
def fun():
  print(name)
fun()
fun()

def fun():
  x=10#  local variable
global x
x=70
print(x)
fun()  

class Hello:
  def __init__(self,name):
       self.name=name# instance variable belongs to an object each object has its own copy
  
h1=Hello("priya") 
h2=Hello("jiya")
print(h1.name)
print(h2.name)


class Hello:
   name="hello"# Class variable
   def __init__(self,name):
      self.name=name
#h2=Hello("priya")
#h3=Hello("jiya")
#print(h2.name)
#print(h3.name)
Hello.name="jello" 
print(Hello.name)   

###################3
fruits=["apple","banana","cherry"]
a,b,c=fruits
print(a +" "+b+" "+c+" ")

#####################################3
x=1
y=3.5
z=3j
a=float(x)
b=int(y)
c=complex(x)
#d=int(z) : You cannot convert complex numbers into another number type.
d=str(z)
print(a)
print(b)
print(c)
print(d)

#################3
import random
print(random.randint(1,10))
print(random.randrange(1,10))

    

