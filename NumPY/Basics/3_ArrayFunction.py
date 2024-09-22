import numpy as np
# Findind index of maximum,minimum Number

# argmax , argmin
a=np.array([[2,6,4,7,5],[3,4,2,1,0]])
maxIndex = np.argmax(a, axis=0)
print(maxIndex)
maxIndex = np.argmax(a, axis=1)
print(maxIndex)

maxIndex= np.argmax(a)
print(maxIndex)

minIndex = np.argmin(a, axis=0)
print(minIndex)
minIndex = np.argmin(a, axis=1)
print(minIndex)
minIndex= np.argmin(a)
print(minIndex)



