print("hello world")
l = [1, 1, 1, 2, 2, 3]
d = {}

for i in l:
    if i in d:
        d[i].append(i) 
    else:
        d[i] = [i]    

print(d)

