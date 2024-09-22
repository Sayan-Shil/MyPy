"""Vectorization"""
# Converting iterative statements into a vector based operation is called vectorization.
# It is faster as modern CPUs are optimized for such operations.

""" Broadcasting """
#The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. 
# Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes. 
# Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python.
#  It does this without making needless copies of data and usually leads to efficient algorithm implementations. 
# There are, however, cases where broadcasting is a bad idea because it leads to inefficient use of memory that slows computation.


#When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimension and works its way left. Two dimensions are compatible when
# ---> they are equal, or
#--> one of them is 1.

# If not , then ValueError: operands could not be broadcast together when you are operating +/*/- or add/multiply

#Can (1,3) + (4,3) possible? 
# Yes... (1,3) RMN - 3 ,  (4,3) RMN - 3 ,  So, 1 is done ( ,3)  , then (1,4) , 1 presnt so largest number 4 is taken (4,3)

import numpy as np
a= np.arange(1,4).reshape(1,3)
b= np.arange(1,13).reshape(4,3)
c=np.array(1)
print(a)
print(b)
print(b+c)

#Application-
# Vector Quantization *=( Image Encoding )




