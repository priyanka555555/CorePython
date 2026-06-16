#thisset={"apple","banana","cherry"}
#print(thisset[1]) #You cannot access items in a set by referring to an index or a key.
#print("banana" in thisset)
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x=thisdict.get("model")
x=thisdict.keys()
x=thisdict.items()
thisdict["color"]="red"
print(x)
"""
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    x=thisdict.items
    
    print(x)
"""
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#thisdict.pop("model")

for x in thisdict:
 print(thisdict[x])

#for x in thisdict.values():
#for x in thisdict.keys():
#for x in thisdict.items():
#for x, y in thisdict.items():
mydict=thisdict.copy()
print(mydict)
"""
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  },
  "child4":{
      "name" : "Linus",
      "year" : 2011
  }
}
#for x ,y in myfamily.items():
#print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y +" :",obj[y])
"""
thisdict={
    "name":"priya",
    "age":40

}
#x=thisdict.clear()
#x=thisdict.copy()
#x=thisdict.get("name")
#x=thisdict.keys()
#x=thisdict.items()
thisdict.pop("name")


print(thisdict)

 
