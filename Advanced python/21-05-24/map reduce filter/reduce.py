from functools import reduce
l = [1,2,3,4]
s = reduce((lambda x,y:x+y), l)
print(s)