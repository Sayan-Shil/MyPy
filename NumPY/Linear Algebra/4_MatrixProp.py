import numpy as np

#Trace of elemenets : sum of principle diagonal elements
a = np.array([[1,1],[3,-1]])
print(np.trace(a))



#Rank of a matrix - 
print(np.linalg.matrix_rank(a))


