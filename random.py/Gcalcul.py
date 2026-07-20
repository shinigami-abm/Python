a= int(input("How many students you want to put in this calculater\n"))
students= []

for i in range(a):
    name = input("Give me his name\n")
    print("Give me his grades in this order:")
    poo = float(input("poo: "))
    asd = float(input("asd: "))
    math = float(input("math: "))
    s = {
        "Name" : name,
        "Poo" : poo,
        "Asd" : asd,
        "Math" : math,
    }
    students.append(s)

for i in students:
    i["AVR"]= ( i["Math"] + i["Poo"] + i["Asd"] ) / 3
    m = max(i["Poo"], i["Asd"], i["Math"])
    for k, v in i.items():
        if k != "name" and v == m:
           bs = k
    i["Best Subject"] = bs      
    if i["AVR"] > 10:
       i["Status"] = "passed"
    else:
       i["Status"] = "failed"
print("======================== CLASS REPORT ==========================")
a = len(students[0].keys())
for k in students[0].keys():
    if a != 1:
       print( k, end = " || ")
       a -= 1
    else:
      print(k)

for s in students:
    a = len(s.values())
    for v in s.values():
        if a != 1: 
           print(f"{v} ||", end=" ")
           a -= 1
        else:
          print(v)  
print("\n ========== SATTISTICS ==========")
print(f"The number of the students is : {len(students)}")
p = 0
f = 0
cavr = 0
for s in students:
    cavr += s["AVR"]
    if s["Status"] == "passed":
        p +=1
    else:
        f +=1
mavr=0
inx=0
for i in range(len(students)):
    if students[i]["AVR"] > mavr:
       mavr = students[i]["AVR"] 
       inx = i 
print(f"passed        :  {p}") 
print(f"failed        :  {f}")
print(f"calss avrage  :  {cavr/len(students)}")
print(f"Best Student  : {students[inx]['Name']}({students[inx]['AVR']})")
