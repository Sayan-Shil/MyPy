import numpy as np

# Slicing Numpy Arrays

np1= np.array([1,2,3,4,5,6,7,8,9,10])

# Return 3 index to 8 index
print(np1[3:8])

# Return 3 to the end
print(np1[3:])

# Negative Counting
print(np1[-4:-1])
print(np1[-1])

#Return 3 to 8 in steps of 2
print(np1[3:8:2])

#Return entire array with 2 steps
print(np1[::2])


#Slice 2-D array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1,2])

print(np2[0:1,1:3])
print(np2[0:2,1:3])


