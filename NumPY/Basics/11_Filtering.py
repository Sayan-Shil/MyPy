import numpy as np
#Getting some elements out of an existing array and creating a new array out of them is called filtering.
#In NumPy, you filter an array using a boolean index list.

np1=np.array([1,2,3,4,5,6])
x=([True,False,False,True,True,False])

print(np1)
print(x)
print(np1[x])

#Filter Array - we need for in loop

x=[]
for elemants in np1 :
    if elemants %3 ==0:
        x.append(True)
    else :
        x.append(False)

print(x)
print(np1[x])


# Most precise way - Numpy beauty

x = np1 %3 ==0
print(np1[x])




