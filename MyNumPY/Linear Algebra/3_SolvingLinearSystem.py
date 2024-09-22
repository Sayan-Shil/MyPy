import numpy as np

#Solving Linear System
"""
Solve - x+y=4 , 3x-y=0 , then find (x,y)

Turn into Matric
A            X   =  sol

| 1  1 |   | x |   | 4 |
| 3 -1 | * | y | = | 0 |
"""

# Build A Matrix
A = np.array([[1,1],[3,-1]])
sol= np.array([4,0])

solution = np.linalg.solve(A, sol)
print(solution)



#Determinant - np.linalg.det()
a=np.arange(0,9).reshape(3,3)
print("The Determinant of \n" ,a, "\nIs-->")
print(np.linalg.det(a)) 

#Inverse  #Only for non-singular ( det=0)
a=np.arange(0,9).reshape(3,3)
print("The Inverse of \n" ,a, "\nIs-->")

if np.linalg.det(a)!=0 :
    print(np.linalg.inv(a)) 
else:
    print("Singular Matrices has no inverse")