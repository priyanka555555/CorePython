#Python range
#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
"""
Syntax
range(start, stop, step)

Parameters:

start (optional): Starting number of the sequence (default is 0)
stop: Number at which the sequence stops (not included)
step (optional): Difference between consecutive numbers (default is 1)

1.Can you access elements of a range object by index?
Yes, the range object supports indexing (e.g., my_range[0]) and slicing, similar to lists
2.Can you use floating-point numbers with range()?
No, the range() function only accepts integer arguments for start, stop, and step
"""

x=range(1,11,1)
for i in x:
    print(i)
#x[0]=2  #we can not change   
print(x[0]) 

my_list = list(range(1, 6)) 
print( my_list) 
my_list[2] = 100 
print( my_list) 

# range supports membership testing with in operator
x=range(0,10)
if 9 in x:
    print("yes")
print(6 in x)    

#Ranges support the len() function to get the number of elements in the range.
x=range(0,10)
print(len(x))
