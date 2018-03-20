import numpy as np
import matplotlib.pyplot as plt

x= np.array([1,2,3,3,4,7,8,9])
y= x ** x
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.2,0.2])
axes1.plot(x,y,'r')
axes2.plot(y,x,'b')
plt.show()
