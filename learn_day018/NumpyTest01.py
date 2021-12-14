import numpy as np

a = np.array([1,2,3])
print("1D" , a)
a = np.array([[1, 2], [3, 4]])
print("2D", a)
a = np.array([[[1, 2], [3, 4]], [[5,6], [7,8]]])
print("3D", a)

a = np.array([1,2,3,4,5], ndmin = 2)
print(a)

a = np.array([1,2,3,4,5], dtype=complex)
print(a)

dt = np.dtype('i8')
print(dt)
dt = np.dtype([('age',np.float64)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)


student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print (student)
a = np.array([('Ryan', 21, 50),('Sam', 18, 75)], dtype = student)
print(a)