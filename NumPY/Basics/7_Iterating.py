import numpy as np

# Iterating Numpy Arrays

#Normal

#1D Array
np1= np.array([1,2,3,4,5,6,7,8,9])
for i in np1 :                             
    print(i)


#2D Array
np2= np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Print Rows
print("Printing Rows")
for rows in np2 :
    print(rows)
#For All Column / Elements in Rows
print("Printing Elements")
for rows in np2:
    for elements in rows:
        print(elements)



#3D Array
np3= np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(np3.shape)

print("Printing All Elemnats")

for  box in np3 :
    for subbox in box:
        for elemants in subbox:
            print(elemants)


# Use npiter() --> Go to basic level

for x in np.nditer(np1):
    print(x)
    
for x in np.nditer(np2):
    print(x)


for x in np.nditer(np3):
    print(x)



