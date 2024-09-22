"""
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
The frompyfunc() method takes the following arguments:
"""
#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.

import numpy as np

# Create a ufunc with numpy what return percentage when a marks and fullmarks array is passed

# Creating The function such that what a single element will operate , bcz its vectorization
def getPerc(m,fm):
    return (m/fm)*100

# Take 2 Arrays , Operate getParc Elementwise , Give Output 1 Array , name it Percentage
Percentage = np.frompyfunc(getPerc, 2, 1)


#Testing

#Create two List
marks= np.array([86,87,71,73,82])
fullmarks=np.array([90,90,90,90,90])

# Answer Done
print(Percentage(marks,fullmarks))
