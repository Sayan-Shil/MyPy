import numpy as np

# There are 6 general mechanisms for creating arrays: 

""" 1) Converting Python sequences to NumPy arrays """

#.array()
np1 =np.array([1,2,3,4,5,6,7,8,9]) 
print("The 1-D Array -> \n" ,np1, np1.ndim)
print("\n")
np2 = np.array([[1,2,3],[4,5,6]])
print("The 2-D Array -> \n" , np2,np2.ndim)
print("\n")
np3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("The 3-D Array -> \n" , np3,np3.ndim)



""" 2) Intrinsic NumPy array creation functions """

# 1D Array Creation using arrange() and linespace()

#arange(starting , ending* , gap)
np4 = np.arange(10)
print(np4) #Array Of 0-9
np4 = np.arange(1,10)  #Array starting from 1
print(np4)
np4 = np.arange(1,10,2) # Skipping Value
print(np4)

#linespace(Starting* , ending* , gap*) -
np5=np.linspace(1.,2.,6)  # Return Array from 1 to 2 with (6-1) equal interval
print(np5)


#2D creation functions e.g. numpy.eye, numpy.diag, and numpy.vander

#eye() --> Gives identity Matrix 
print(np.eye(3))      # I3 identity matrix
print(np.eye(3, 5))   # I3 identity matrix but on the 3 x 5 Matrix

#diag() --> Gives Diagonal Matrices
print(np.diag([1, 2, 3])) # A matrix whose diagonals are 1,2,3
print(np.diag([1, 2, 3], 1))  #A Super Diagonal Matrix of 1 shift  (A superdiagonal matrix is a square matrix where all the non-zero elements are located just above the main diagonal.)
print(np.diag([[1,2],[3,4]])) # Provide Only diagonal elemants if >1D square matrix is given

# vander() --> Gives Vandermonde Matric (A Vandermonde matrix is a matrix where each row is a geometric progression of the corresponding elements from a given set of numbers.)
vander= np.array([1,2,3,4,5])
print(np.vander(vander))                    #Default Decreasing
print(np.vander(vander, increasing=True))   #Increasing Way
print(np.vander(vander,2,increasing=True))  #Restrict to 2

vander= np.array([4,5,6])
print(np.vander(vander,4,increasing=True))   # 1,1,1   4,5,6    4*4 , 5*5 , 6*6  , 4*4*4, 5*5*5, 6*6*6



 # Applicable for All n-D

 #zeros --> For Null matrix
print(np.zeros((2, 3)))   #Takes size and provide Null matrix According to size
#indices()  --> provided a stacked indices matrix
print(np.indices((3, 3))) 




""" 3) Replicating, joining, or mutating existing arrays """

#join with index
a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]   # b - 1,2
b += 1      #b - 2,3
print('a =', a, '; b =', b)

#Block() to join multiple arrays
A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
print(np.block([[A, B], [C, D]]))








