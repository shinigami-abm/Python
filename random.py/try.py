name = input("give me the name of the file.\n")
try:
   f = open(name ,"r")
except:
     print("File not found.")
else:
    for i in f:
        print(i)
