import numpy as np

"""Aren't Sum and Add are same? """
#Addition is done between two arguments whereas summation happens over n elements.
# Add is not part of vectorized Summation

a= np.array([1,2,3])
b= np.array([2,3,4])

print("I am Add")
c= np.add(a,b)
print(c)
print("I am Sum")
c=np.sum([a,b])
print(c)

#Summation Over an Axis-0 Columnwise Multiply
print(np.sum([a,b],axis=0))
#Summation Over an Axis-1 Rowwise Multiply
print(np.sum([a,b],axis=1))

#Why It is giving List, instead of Integer?
"""
In Normal Sum Summation goes to Axiswise means first Axis 0 then Axis-1 ( Axis-0 but 1-D)
In print(np.sum([a,b],axis=0)), It outputs  [3,5,7] bcz of axis restriction (Stop Summation when Axis-0 wise Sum done)
In General, it again sum if not axis restriction 3+5+7= 15  ( Sum goes until there is not a element)

"""
print("\n\n\n")
np1 = np.arange(1, 13).reshape([2,3,2])
print(np1)

# If We Represent elemant
# 1 = 0 i + 0 j + 0 k         2= 0 i + 0 j + 1 k
# 3 = 0 i + 1 j + 0 k         4= 0 i + 1 j + 1 k      i=0
# 5 = 0 i + 2 j + 0 k         6= 0 i + 2 j + 1 k

# 7 = 1 i + 0 j + 0 k         8= 1 i + 0 j + 1 k
# 9 = 1 i + 1 j + 0 k         10= 1 i + 1 j + 1 k     i=1
# 11 = 1 i + 2 j + 0 k        12= 1 i + 2 j + 1 k


#Summation Over an Axis-0 Columnwise Multiply  -> 
print("\n\nHere is Axis-0 in 3D \n")  
print(np.sum(np1,axis=0))
#Summation Over an Axis-1 Rowwise Multiply
print("Here is Axis-1 in 3D \n")
print(np.sum(np1,axis=1))
#Summation Over an Axis-2 Heightwise Multiply
print("Here is Axis-2 in 3D \n")
print(np.sum(np1,axis=1))