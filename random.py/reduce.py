from functools import reduce 

words = ["apple","banana","kiwi","strawberry"]
print(reduce(lambda x, y : x if len(x) > len(y) else y , words))
