#Q1. Check if a key exists in a dictionary
"""
d={"a":10,"b":20,"c":30}
key="b"
if key in d:
    print("key in exists")
else:
    print("key does not exist")    
"""
"""
#Q2. Find the sum of all values in a dictionary
d={"a":10,"b":20,"c":30}
total=0
for value in d.values():
    total=total+value
print("Total:",total)

#Q3.Find the key with the maximum value

d={"a":10,"b":20,"c":30}
max_key=max(d,key=d.get)
print("Key with maximum value:",max_key)

d={"a":10,"b":20,"c":30}
max=0
for key in d:
    if d[key]>max:
        max=d[key]
print("Maximum value:",max)
#Q4. Create a dictionary from two lists
keys=["a","b","c"]
values=[10,20,30]
d=dict(zip(keys,values))
print(d)

#Q6. Sort a dictionary by values
d={"a":170,"b":20,"c":30}
for values in sorted(d.values()):
    for key in d:
        if d[key]==values:
            print(key,":",d[key])

#Q7. Remove duplicate values from a dictionary
d = {"a": 10, "b": 20, "c": 10, "d": 20,"e": 30}
result = {}
for k, v in d.items():
    if v not in result.values():
        result[k] = v

print(result)

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
# Result: {1: 'a', 2: 'b', 3: 'c'}


"""
from collections import defaultdict

l = [1,1,1,2,2,3]

d = defaultdict(list)
for i in l:
    d[i].append(i)

print(dict(d))



