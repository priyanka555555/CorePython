def fun(n):
    if n<=0: # a condition that stop the recursion
        print("completed") 
    else:
        print(n)
        fun(n-1) #Recursive case the function calling itselt with the modified arguments  

fun(5)               
#Check the recursion limit:
import sys
#sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())       
############
# sum of list items using recursion
"""
def sum_list(my_list):
  if len(my_list) == 0:
    return 0
  else:
    return my_list[0] + sum_list(my_list[1:])
                          
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


1 + sum_list([2, 3, 4, 5])
1 + (2 + sum_list([3, 4, 5]))
1 + (2 + (3 + sum_list([4, 5])))
1 + (2 + (3 + (4 + sum_list([5]))))
1 + (2 + (3 + (4 + (5 + sum_list([])))))
1 + (2 + (3 + (4 + (5 + 0)))) (Base case reached: sum_list([]) returns 0)
Calculation: 
"""
# factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
       return n*fact(n-1)
            
print(fact(5))

def fun(n):
   if n<=0:
      print("done")
   else:
      print(n)   
      fun(n-1)
fun(5)      
 #################  
def fun(n):
  if n<=0:
    print("done")
  else:
    print(n)   
    fun(n-1)
fun(5)

class A:
    abc=123
    @staticmethod
    def fun1():
       return A.abc# we can call explicit
    @classmethod
    def fun(cls):
       cls.abc=120
       return cls.abc
    
a= A()
print(a.fun())
print(a.fun1())
b=A()
print(b.abc)
print(b.fun1())

print("1..................")
def fact(n):
    if n<=1:
        return 1
    else:
       return n*fact(n-1)
            
print(fact(5))








    
          
   












 