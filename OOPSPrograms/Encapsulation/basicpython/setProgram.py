s={"hello","jello","sello"}
s1=set(("hello","jello","sello"))
for x in s: 
 print(x)
 s1=set(("hello","jello","sello"))
 s1.add("gj")
 #print(s1)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#### join sets
s3={"hello","jello","sello"}
s4={"hello","nello","kello"}
#s5=s3.union(s4)
#s5=s3.intersection(s4)# keeps only duplicate value
#s3.intersection_update(s4)
#s3.update(s4)
#print(s3)
s5=s3.difference(s4)
s3.difference_update(s4)
#print(s5)
print(s3)

s6=frozenset({"hello","jello","sello"})
print(s6)