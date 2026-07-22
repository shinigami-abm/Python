f = open("SUUU.md" ,"r")

s = input("Give me the name of the students.\n")
ctrl = False
for i in f:
    temp = list(i.split(" "))
    if temp[0].upper() == s.upper():
       print(f"{s} has been found.")
       ctrl = True
if ctrl == False:
    print(f"{s} can not be found in the file")
