import numpy as np
a= np.array([1,2,3])
b= np.array([2,3,4])

print("I am Multiply")
c= np.multiply(a,b)
print(c)
print("I am Product")
c=np.prod([a,b])
print(c)

#Product Over an Axis-0 Columnwise Multiply
print(np.prod([a,b],axis=0))
#Product Over an Axis-1 Rowwise Multiply
print(np.prod([a,b],axis=1))

#Why It is giving List, instead of Integer?
"""
In Normal Product goes to Axiswise means first Axis 0 then Axis-1 ( Axis-0 but 1-D)
In print(np.prod([a,b],axis=0)), It outputs  [ 2  6 12] bcz of axis restriction (Stop Product when Axis-0 wise Sum done)
In General, it again products if not axis restriction  = 1442 . 6 . 12  ( Product goes until there is not a element)

"""