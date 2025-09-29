def sum (a,b):
#   print(a +b)
    return a+b 
 
def mul (a,b):
 return a*b

def dev (a,b):
    return a/b

def com(a,b):
    if a<b:
        return b
    else: 
       return a
a = input()
b = input()



print(dev(mul(sum(a, b), b), a))

#print(com(a, b)) 
