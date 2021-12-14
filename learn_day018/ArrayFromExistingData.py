import numpy as np

x = (1,2,3)
a = np.asarray(x)
print(a)

x = [(1,2,3),(4,5,6)]
a = np.asarray(x)
print(a)

x = np.arange(10,20,2)
print(x)

x = np.linspace(10,20,5, endpoint = False)
print(x)

a = np.arange(10)
print (a[slice(2,7,2)])
b = a[2:7:2]
print(b)


a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a)
print ('Now we will slice the array from the index a[1:]')
print (a[1:])


