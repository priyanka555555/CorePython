x=10#global variable
def fun():
    print(x)
fun() 
####3
def fun1():
    x=10# canot access out side of the function
    print(x)
fun1() 

def fun1():
    x=100# canot access out side of the function
    print(x)
    def funn(): # we canaccess in side of the function
        print(x)
    funn()    

fun1() 

################3333 
def fun1():
    x=0# canot access out side of the function
    print(x)
    def funn(): # we canaccess in side of the function
        nonlocal x # we can chnage outer fuctions of variable
        x=70
        print(x)
    funn()    

fun1() 

y=90
def fun2():
   # global y
    y=30
    print(y)
fun2()
print(y)  


       
    