x=10
print(isinstance(x ,int))# it returns true
class Hello:
    pass
he=Hello()
print(isinstance(he,Hello))
print("***************************")

a=10
b=[1,2,3,4]
print(isinstance(b,(list,str,int)))# in this case function perform as logical or 

## the function iterate each type  in tuple and check if b is instance of the list or str or int and return true
print("***************************")
class Animal:
    pass
class Dog(Animal):
    pass
dog=Dog()
print(isinstance(dog,Animal))# it returns true it is also instance of parent class
print(isinstance(dog,Dog)) # it return true
print("***************************")
s="hello"
d={"name":"priya"}
print(isinstance(s,str))
print(isinstance(d,dict))
print("***************************")
class Myclass:
    def fun(self):
        return"hello"
obj=Myclass()
print(isinstance(obj.fun(),str))    

############################################################
print("***************************")
sum_numbers=0
st=[]
nested_list=0
mixed_list = [10, "apple", 5.5, [1, 2],[2,4]]
for item in mixed_list:
    if isinstance(item,(int ,float)):
        sum_numbers=sum_numbers+item
    elif isinstance(item,str):
        st.append(item.upper())
    elif isinstance(item,list):
        nested_list=nested_list+1

print(sum_numbers)  
print(st)  
print(nested_list)

a=[1,2,3,4,5]
#a.insert(-20,20)# [20, 1, 2, 3, 4, 5]
a.insert(20,20)
print(a.index(20))






