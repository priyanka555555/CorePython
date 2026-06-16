d={"a":100,"c":5,"b":30}
#output {"c":5,"b":30,"a":100}

l=sorted(d,key=lambda x:x)
l1=dict(sorted(d.items(),key=lambda x:x[1]))
print(l1)

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = []
neg = []
for i in arr:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg) 

i=0
j=0
result=[]
while i<len(pos) and j <len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i=i+1
    j=j+1
result.extend(pos[i:])
#result.extend(neg[j:])
print(result)


l = [1, 4, 6, 8, 7, 4]
seen=set()
dup=[]
for i in l:
    if i in seen:
        dup.append(i)
    else:
        seen.add(i)
print(dup)
print(seen)

l1=[1,2,3,4]
l2=["A","B","C","D"]
d={}
for i in range (len(l1)):
    if l1[i] not in d:
        d[l1[i]]=l2[i]  

print(d)

l=[1,2,3]
from itertools import permutations
for i in permutations(l):
    print(i)


d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
result = {}
seen = set()

for key, values in d.items():
    new_list = []
    for x in values:
        if x not in seen:
            new_list.append(x)
            seen.add(x)
    result[key] = new_list
print(result)    

# Output: {'a': [1, 2, 3], 'b': [4, 5], 'c': [6]}
"""
for i in range(len(l) -1,-1,-1):
    if l[i]>=max:
        l1.append(i+1)
        max=l[i]
l1.reverse()
print(l1)        
"""
d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
result = {}
seen = set()
for key, value in d.items():
    l=[]
    for x in value:
        if x not in seen:
            l.append(x)
            seen.add(x)
    result[key]=l
print(result) 

d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
#output {'a': [6], 'b': [12], 'c': [11]}
result={}
for key,value in d.items():
    s=0
    l=[]
    for v in value:
        s=s+v
        result[key]=[s]
print(result)

t = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}
# {'best': [4, 19], 'gfg': [3, 6, 7], 'is': [2, 3, 10]}
res = {key: sorted(t[key]) for key in sorted(t)}
print(res)

t = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}
# {'best': [4, 19], 'gfg': [3, 6, 7], 'is': [2, 3, 10]}
res={}
for key in sorted(t):# sorted(t) returns a list of keys in sorted order
    res[key]=sorted(t[key])# sorted(t[key]) sorts the list of values corresponding to the current key
print(res)

{'gfg': 4, 'is': 2, 'best': 5}
#output ({'best': 5, 'is': 2, 'gfg': 4})
t = {'gfg': 4, 'is': 2, 'best': 5}
res={}  
for key in sorted(t):
    res[key]=t[key]
print(res)

d = {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [5, 6]}
#output {'a': [6], 'b': [12], 'c': [11]}
result={}
for key,value in d.items():
    s=0
    l=[]
    for v in value:
        s=s+v
        result[key]=[s]

print(result)
################

d={'a': 10, 'b': 45, 'c': 23}
max=0
max_key=""
for i,j in d.items():
    if j>max:
        max=j
        max_key=i
print(max)
print(max_key)

d = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)

l=[1,2,3]
d = {'b': 2, 'a': 1, 'c': 3}
print(d.items())
print(d.values())
print(d.keys())
print(d.get('b'))
d.popitem()
d.pop("b")
print(d)
d.update({'e':3})
print(d)

