import numpy as np
import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
test = pd.Series(my_data,labels)
test2 = pd.Series(arr,labels)
test3 = pd.Series(d)
test4 = pd.Series(data = [110,120,130])
print(test4)
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])

print(ser1)
print(ser2)
print(ser1['USA'])
print(ser1 + ser2)
