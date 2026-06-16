
import os
class Student:
   
      #    def __init__(self,name=None,rno=None,marks=None):
      #     self.name=name
      #     self.rno=rno
      #     self.marks=marks
          
          #self.file_path = 'D:\\priyaFile.txt'
            
         def add(self,name,rno,marks):
          with open("D:\\priyaFile.txt","a") as f:
              f.write(f"Name: {name}, Roll No: {rno},marks:{marks}\n")
              f.close()
             
         def display(self):
            with open("D:\\priyaFile.txt", "r") as f:
               
           #  for x in f:
               print(f.read())
             
         def removeFile(self):
           if  os.path.exists("D:\\priyaFile.txt"):
             os.remove("D:\\priyaFile.txt")
           else:
              print("the file does not exist")  

         def deleteRecord(self,rno_to_delete):
             
             with open("D:\\priyaFile.txt", "r") as f:
                  lines = f.readlines()
             with open("D:\\priyaFile.txt", "w") as f:
               for line in lines:
                 rno  = line.strip().split(",") #line = "Name:John, Roll:123 " split(",") -> ['Name:John', ' Roll:123']
                 roll_num = rno[1].split(":")[-1].strip() #rno[1] -> ' Roll:123' split(":") -> [' Roll', '123'] [-1] -> '123' .strip() -> '123' 
                 if roll_num != rno_to_delete:
                    f.write(line)
                 else:
                    found = True

        
             
#pick = int(input("Enter choice: "))
#st=Student("niya",132,90)  
while True:
      pick = int(input("Enter choice: "))
      st = Student()
   
      match pick:
            case 1:
                  name = input("Enter Name: ")
                  rno = input("Enter Roll No: ")
                  marks = input("Enter Marks: ")
                  st.add(name,rno,marks)
            case 2:
                  st.display()
            case 3:
                  rno_del = input("Enter Roll No to delete: ")
                  st.deleteRecord(rno_del)
            case 4:
                  st.removeFile()
            case 5:
                  print("Exiting...")
                  break
            case _:
                  print("Invalid choice.")

         
         
