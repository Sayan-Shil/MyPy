import numpy as np

# Copy Vs View

np1 = np.array([0,1,2,3,4,5])

#Create  a view

np2 = np1.view()
print("Original np1-->",np1)
print("View np1-->",np2)

np1[0]=41

print("Changed np1-->",np1)
print("Original np1-->",np2)    #Both are changing...

np3=np.copy(np1)
print(np3)
np1[1]=41


print("Changed np1-->",np1)
print("Original np1-->",np2)
print("Copy np1-->",np3)


np3[0]=51

print("Changed np1-->",np1)
print("Original np1-->",np2)
print("Copy np1-->",np3)
