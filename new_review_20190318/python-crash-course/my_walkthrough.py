# -*- coding: utf-8 -*-

# list comprehension:
lst = [1,2,3,4]
out = []
#for num in list:
#    out.append(num**3)
#print(out)  

out = [num**3 for num in lst]
print(out)

def square(num):
    return num**2

seq = [1,2,3,4]

list[map(square, lst)]

