def look(x):
   c=0
   for i in range(x + 1): 
       if i != 0:
          if x%i== 0:
             c +=1
   if c > 2 or c == 1:
      return True
   else:
      return False
  
y = int(input("Give me a number.\n")) 
if look(y) == True:
    print(f"Your number '{y}' is not prime")
else:
    print(f"{y} is prime")
