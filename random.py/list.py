age = [10, 12, 17, 21, 15, 30, 8, 19, 45, 16, 999, 55, 1, 5]
minor = []
adult = []
for i in age:
    if i > 18: adult.append(i) 
    else: minor.append(i)
minor.remove(10)
print("we have", len(adult) ,"adults in age.") 
print("we have", len(minor), "minors int age")
