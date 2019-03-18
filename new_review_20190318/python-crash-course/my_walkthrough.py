# -*- coding: utf-8 -*-

# list comprehension:
list = [1,2,3,4]
out = []
#for num in list:
#    out.append(num**3)
#print(out)  

out = [num**3 for num in list]
print(out)
