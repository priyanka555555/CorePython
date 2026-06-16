num=5
i=1
while i<=num:
    j=1
    while j<=10:
        print(i,"*",j,"= ",i*j)
        j=j+1
    print("#######################")
    i=i+1   

"""

for i in range(1,5):
    #print("#######################")
    for j in range(1,11):
         
         print(i,"*",j,"= ",i*j)
""" 
"""
#check prime number

i=1
num=5
c=0
while i<=num:
    if num%i==0:
        c=c+1
    i=i+1    
if c==2:
    print("prime") 
else:
    print("not prime")           
"""