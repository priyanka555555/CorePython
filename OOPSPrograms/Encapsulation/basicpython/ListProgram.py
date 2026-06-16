lst=["hello","world","jello"]
print(lst)
print(lst[:1])
print(lst[0])

lst=["hello","world","jello"]
lst1=["lkgk","kgkj"]
if "hello" in lst:
    print("yse")

lst=["hello","world","jello"]  
lst[1]="sello"
print(lst)
lst[0:2] = "kksdnf","kknflak"
print(lst)

lst.insert(3,"llll")
print(lst)

lst.append("hello")
print(lst)
lst.insert(1,"jjj")
print(lst)
lst.extend(lst1)
print(lst)
lst.append(lst1)
print(lst)
lstt=["hkk","hello","jello","jflkf"]
lstt.remove("hello")
print(lstt)
lstt.pop()
lstt.pop(0)
print(lstt)
#del lstt[1]
#print(lstt)
#del lstt
lst2=["hello","world","jello"] 

print(lst2)
lst2.clear()
print(lst2)
lst3=["hello","world","jello"]
for x in lst3:
    print(x)

lst2=["hello","world","jello"] 
for x in range(len(lst2)):
    print(lst2[x])
lst2=["hello","world","jello"]
[print(x) for x in lst2] 

print("hello")


lst2=["hello","world","jello"]
new_lst=[x for x in lst2 if 'h' in x]
print(new_lst)


lst2=["hello","World","jello"]
#lst2.sort(reverse=True)
lst2.reverse()
print(lst2)
lst2=["hello","World","jello"]
lst2.sort(key=str.lower)
print(lst2)
lst2=["hello","World","jello","World"]
lst3=["hello","World","jello"]
#lst4=lst2.copy()
#lst4=list(lst2)
lst4=lst2[:]
print(lst4)
lis=lst2.count("World")
print(lis)



