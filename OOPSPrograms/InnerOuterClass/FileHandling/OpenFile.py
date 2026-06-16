#f=open("D:\\priyaFile.txt","r")
#with open("D:\\priyaFile.txt")as f:
#print(f.read(5))
"""
with open("D:\\priyaFile.txt") as f:
   # print(f.readline())# read single line
   # print(f.readlines())# read  multiple line
   for x in f:
      print(x)

#f.close()
  """
#Open the file "demofile.txt" and append content to the file:
"""
with open("D:\\priyaFile.txt","a") as f:
    f.write("i am software developer")
with open("D:\\priyaFile.txt") as f:
    print(f.read())   
    f.close()
    """
#Overwrite Existing Content
#"x" - Create - will create a file, returns an error if the file exists
"""
with open("D:\\priyaFiles.txt","x") as f:
   f.write("hello python developer")
 """ 
"""
"a" - Append - will create a file if the specified file does not exists
with open("D:\\priyaFiles.txt","a") as f:
   f.write("hello python developer")
"""
"""
"w" - Write - will create a file if the specified file does not exists
with open("D:\\priyaFiles.txt","w") as f:
   f.write("hello python developer")
"""
#with open("D:\\priyaFiles.txt") as f:
  #  print(f.read())
  #  f.close()  
# Delete File
# To delete a file, you must import the OS module, and run its os.remove() function:
"""
import os
os.remove("d:\\priyaFiless.txt")
"""
# Check if File exist:
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
"""
import os
if  os.path.exists("D:\\priyaFiless.txt"):
    os.remove("D:\\priyaFiless.txt")
else:
    print("the file does not exist")  
""" 
# delete folder To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("D:\\newfile")  


