s="hello"
s="world"
print(s)

"""
# reverse string
list=["hello","world","hello","python"]
list.reverse()
print(list)
"""
"""
# cheack pallindrome
num=121
num = 121
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
"""
"""
s = "madamm"
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome string")
else:
    print("Not a palindrome string")
"""
#count vowels in string
"""
str="priyanka"
count=0
for x in str:
    if x in "aeiou":
     count=count+1
print(count)
"""
"""
str = "priyanka"
vowels = 0
consonants = 0

for x in str:
    if x in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
"""
"""
str="priya"
for x in str:
    if x in "aeiou":
        print("vowels  "+x)
    else:
        print("consonent  " +x)
print("vowels") 
"""
s = "hello world"
result = ""

for ch in s:
    if ch not in result:
        result =result+ch

print(result)

s = "helloworld"
#print(s.index("z"))#ValueError
print(s.find("z"))


