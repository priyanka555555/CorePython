#immutable
s="hello"
print(id(s))
s=s+"world"
print(id(s))

#hashable we can use dict and set safely
s=["hello","world"]
s1={}
s1["name"]="priya"
print(s1)
