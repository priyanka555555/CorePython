# accessing item
t=("hello","jello","sello")
print(t[1])
#change
t=("hello","jello","sello")
x=list(t)
x[1]="kdcc"
t=tuple(x)
print(t)

# add
t=("hello","jello","eello")
x=list(t)
x.append("kkfj")
t=tuple(x)
print(t)
# remove
t=("hello","jello","eello")
x=list(t)
x.remove("eello")
t=tuple(x)
print(t)
#delete
t=("hello","jello","eello")
#del t
print(t)
## unpacking
t=("hello","jello","eello")
(a,b,c)=t
print(a)
print(b)
print(c)
t=("hello","jello","eello","jkhdd")
(a,b,*c)=t
print(a)
print(b)
print(c)
t=("hello","jello","eello","jkhdd")
for i in range(len(t)):
    print(t[i])