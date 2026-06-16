"""mydict = {
"thisdict" : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},
"thisdict1" : {
  "brand": "Fordd",
  "model": "Mustangg",
  "year": 1965
},
"thisdict2" : {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
}
for x in mydict.items():
  print(x)
#print(mydict["thisdict1"]["brand"])
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    