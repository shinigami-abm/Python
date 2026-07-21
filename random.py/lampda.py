students = [
    ("Ali", 20),
    ("Sara", 18),
    ("Omar", 22),
    ("Lina", 19)
]
temp = []
chek = lambda x, y : x > y  
t = ()
index = 0
print(students)
for j in range(len(students)):
    c = 0
    m = 0
    for i in students:
        if chek(i[1], m) == True:
           m = i[1]
           t = i
           index = c
        c += 1   
    students.remove(students[index])
    temp.append(t)
students = temp.copy()    
print(students)
