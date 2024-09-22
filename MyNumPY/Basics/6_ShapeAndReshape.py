import numpy as np

#Create a 1-D Array and get Shape
np1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

#Create a 2-D Array and get Shape (Rows,Column)

np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np2)
print(np2.shape)

#Reshape in 2D
np3= np1.reshape(3,4)
print(np3)

#Reshape in 3D

np4= np1.reshape(2,3,2)
print(np4)

#Flattened in 1D
np5=np4.reshape(-1)
print(np5)


#Transpose:

a= np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a.transpose())
