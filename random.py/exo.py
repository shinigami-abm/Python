from functools import reduce

numbers = [2,5,8,11,14,17]
print(reduce( lambda x, y: x+y ,list(map( lambda x : x*x , list(filter(lambda y: y%2 != 0, numbers))))))
