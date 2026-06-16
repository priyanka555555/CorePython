"""
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  """
x= "hello"
def func():
    x= "hi"
    x= "hey"
    print(x)
func()
print(x)





  