import numpy as np

np1=np.array([1,6,7,2,3,5])
x = np.where(np1==3)
print(np1)
print(x)
#(array([4]),) #It is a tuple
print(x[0])   ##returns array[4]  means [4]



# Find the even
print(np1)
y= np.where(np1 % 2 == 1)
print(y[0])
print(np1[y[0]])

