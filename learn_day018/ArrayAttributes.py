import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print (a.shape)
b = a.reshape(3,2)
print(b)
a.shape = (3,2)
print (a)

a = np.arange(24)
b = a.reshape(2,4,3)
print(a)
print(b)
