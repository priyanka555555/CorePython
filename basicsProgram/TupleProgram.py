"""
thistuple=("apple", "banana")
x=list(thistuple)
x.append("cherry")
thistuple=tuple(x)
print(thistuple)
"""
"""
thistuple=("apple", "banana")
x=list(thistuple)
x.remove("apple")
thistuple=tuple(x)
print(thistuple)

#del thistuple
"""
thistuple=("apple", "banana","cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

