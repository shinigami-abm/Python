def sum(*num):
    s = 0
    for i in num:
        s += i
    return s

def max(*num):
    m = num[0]
    for i in num:
        if i > m:
           m = i
    return m

def avr(*num):
    return sum(*num) / len(num)

def min(*num):
    m = num[0]
    for i in num:
        if m > i:
            m = i
    return m

def stat(*num):
    s = {
      "count" : len(num),
      "avr" : avr(*num),
      "sum" : sum(*num),
      "max" : max(*num),
      "min" : min(*num)
    }
    return s

print(stat(0, 12, 5, 8, 99, 15, -1))
