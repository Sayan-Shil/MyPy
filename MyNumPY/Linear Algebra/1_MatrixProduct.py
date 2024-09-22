import numpy as np

#Vector Products

#Dot Product
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.dot(a,b))                 # (1i + 2j + 3k) . (5i + 6j + 7k)

#Cross Product

a = np.array([1, 2, 3])    
b = np.array([5, 6, 7])
print(np.cross(a, b))             # (1i + 2j + 3k) X (5i + 6j + 7k)



# Matrix Multiplication:

a = np.array([1, 2, 3])    
b = np.array([5, 6, 7])
print(np.matmul(a, b))          #Determinent Multiplication a1b1 + a2b2 +....



