# print("enter numbers")
# a = int(input())
# b = int(input())
# x = lambda a, b: a + b
# print( x(a, b))

#A decorator in Python is a function that takes another function as an argument, 
# adds some extra functionality to it, and returns a new modified function without changing the original function’s code.

def deco(ar):
    def h():
        print("Deepak")
        ar()
    return h  

@deco #fun = deco(fun)
def fun():
    print("Hi Priyanka")
    print("this side sartth")
    
    
fun()
# p=deco(fun())
#k = deco(fun)
#k()
