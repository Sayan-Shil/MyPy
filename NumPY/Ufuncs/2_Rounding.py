import numpy as np
x=np.array([5.52524,65.1245])


#Truncation -Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
print(np.trunc(x))
print(np.fix(x))

#Rounding - The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

print(np.around(x,3))


#Floor & ceil - floor() previous , ceil() next
print(np.floor(x))
print(np.ceil(x))

