dis={
    "name":"priya",
    "age":40
}
dis["name"]="jiya"
print(id(dis))
dis["your_name"]=dis.pop("name")
print(id (dis))

dis1={
    (1,2,3):"numbers"
}
print(dis1)

#dis.update({"year":2020})
#print(dis)
#remove the dict
#dis.pop("your_name")#remove the specfy
#dis.popitem()# remove the last inserted item
#del dis["age"]
#dis.clear()
for x in dis.keys():
  print(x)
for x in dis.values():
  print(x)  
for key,value in dis.items():
  print(key,":",value) 
    
""""
#unpacking
t=(1,2,3,4,5)
(a,b,c,*d)=t
print(a)
print(b)
print(d)
## one vlaue to multiple varibkes
x=y=z="hello"
print(x)
#type conversion
a=10
b=str(12)
print(type(a))
print(type(b))
# Random number
import random
print(random.randint(1,5))
print(random.randrange(2,4))
#string
st=" hello world"
print(id(str))
print(st[1:3:1])# forword drection
print(st[-1::-1])# backward direction
print(st.strip())# remove white space from starting and ending
print(st.split("/"))# breaking sting into list based on seperator
st1=st+"world"
print(id(st1))
s="hello"
s1="hello"
print( s is s1)#  check object identity it returns true because dono variables same object ko point kr rhe hain
print(s==s1)#check  a vlaue equlity
l1=[1,2,3]
l2=[1,2,3]
print(l1==l2)
print(l1 is l2)
print(st[1])
print(len(st))
print(st.lower())
print(st.upper())
print(st.title())
print(st.startswith(" "))
print(st.endswith("d"))
print(st.swapcase())# convert capital to sammal
print(st.count("h"))
print(st.find("z"))# if the char not find find() return -1
#print(st.index("z")) # it throw error if the specy char not find
print("*".join(st))# concate any number of string
"""
