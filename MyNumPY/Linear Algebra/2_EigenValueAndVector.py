import numpy as np
a=np.array([[1,2],[3,4]])

# Return a list with Eigen Vector and Eigen value
print(np.linalg.eig(a))

# Return only Eigen value
print(np.linalg.eigvals(a))

"""
Eigen value: 
If there is matrix A,

Characteristics Equation - |a- xI|=0 
Corresponding to roots ( Values of x) are = Eigen Value


"""