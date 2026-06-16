s="aabbccddeaa"
#output a2b2c2d2e1a2
s1=""
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c=c+1
    else:
        s1=s1+s[i-1]+chr(c)
        c=1


print(s1)
