#. Reverse a String - Reverse the given string without using slicing
"""
st="python"
rev=" "
for i in st:
    rev=i+rev
print(rev)    
"""
#2. Count Vowels and Consonants - Count vowels and consonants in a string
st="Priyanka"
ch=st.lower()
countv=0
countc=0

for i in st:
    if i in "aeiou":
     countv=countv+1  
    else:
     countc=countc+1
     
            
print(f"vowel count {countv}")   
print(f"vowel count, {countc}") 

st="Priyanka"
ch=st.lower()
v=""
c=""

for i in st:
    if i in "aeiou":
     v=v+i  
    else:
     c=c+i
     
            
print("vowel element "+v)   
print("vowel element "+c) 

#4. Remove Duplicate Characters - Remove duplicate characters while preserving order.
st1= "programming"
rev=""
print(rev)
for s in st1:
  if s not in rev:
    rev=rev+s
print(rev)  
#5. First Non-Repeating Character - Find the first character that does not repeat.

st2 = "aabbccd"

for i in range(len(st2)):
    count = 0
    
    for j in range(len(st2)):
        if st2[i] == st2[j]:
            count =count+ 1
    
    if count == 1:
        print("First non-repeating character:", st2[i])
        
# Reverse Words in a Sentence - Reverse word order in a sentence.
st3 = "Hello World Python"
#print(st3.split()) 
rev=""
rev=" ".join(st3.split()[::-1])
print(rev)   

#7. Count Character Frequency - Count frequency of each character in a string.
st4= "banana"
s=0

for i in st4:
   st=st4[0]
   if i in st:
      s=s+1
print(s)      
      
      

    






