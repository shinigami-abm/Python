students = [
    ("Ali", 20, 14.5),
    ("Mouna", 21, 18.0),
    ("Omar", 20, 12.0),
    ("Sara", 22, 17.5),
    ("Yacine", 21, 9.5),
    ("Lina", 20, 15.0)
]
st = set()
for i in students:
 st.add(i[1])

dst = {}
for i in students:
        dst[i[0]]={
                "grade" : i[2]
        }
temp= []
for key, value in dst.items():
    for k, v in value.items():  
     temp.append(v)
     if v > 10: 
        print(key, v)

m=0
for i in temp:
    if m<i:
        m=i 
for key, value in dst.items():
    for k, v in value.items():
        if m == v:
            print(key)
u20 = []
temp = [] 
for student in students:
    if student[1] == 20 :
       temp.append(student)
for i in range(len(temp)):
    m=0
    index = 0
    for j in temp:
        if m < j[2]:
           m = j[2]
           index = j
    u20.append(index)
    temp.remove(index)
print(u20)
