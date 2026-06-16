dis={
    "name":"priya",
    "age":25
}
#dis.popitem()
#print(dis)
x=dis.keys()

print(dis)
print(dis["name"])
print(dis["age"])
print(dis.keys())
print(dis.values())
print(dis.items())
print(dis.get("name"))
print(x)

dis["name"]="jiya"
print(dis)
dis.update({"year":2026})
print(dis)
#dis.pop("name")

dis1={
    "name":"priya",
    "age":25,
    "year":2026
}
for x in dis1.items():
    print(x)
dis2={
    "name":"priya",
    "age":25,
    "year":2026
}
for x in dis2.keys():
    print(x) 
dis1={
    "name":"priya",
    "age":25,
    "year":2026
}
disc=dis1.copy()
disc=dict(disc)
print(disc)
######### nested dict
mydict={
    "dict1":{
        "name":"priya",
        "age":25

    },
    "dict2":{
        "name":"siya",
        "age":30
    }
   
}
for x,obj in mydict.items():
 print(x)
 for y in obj:
    print(y+":",obj[y])





