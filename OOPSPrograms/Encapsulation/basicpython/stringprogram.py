
st="hello"
new_st="j"+st[1:]# create nuw object 
print(new_st)

st="hello"
print(id(st))
new_st="world"+st
print(id(new_st))

# Slicing
st="""hello ,world"""
print(st[1:7])
print(st[:5])
print(st[5:])

# negative index
print(st[-3:-1])
# modify String
st="hello world"
print(st.upper())
print(st.lower())
print(st.strip())
print(st.replace('h','j'))
print(st.split())

#F-string
age=20
name="priya"
print(f"{name},age {age:.2f}")

print(st.index("h"))
print(st.find("n"))

num=2
print(num**3)

####################33
x=["hello" ,"world"]
z=["hello world"]

#print(x is z)
#print(x is not z)
#print(x==z)

print("hello" in x)
print("hello"  not in x)


     

