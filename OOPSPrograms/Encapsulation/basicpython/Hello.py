#import sys
#print(sys.version)
str="priyanka patel"
s=len(str)
res=""
for i in range(s):
    if i%2==0:
        res=res+res.upper()
    else:
        res=res+res.lower()
print(res)            