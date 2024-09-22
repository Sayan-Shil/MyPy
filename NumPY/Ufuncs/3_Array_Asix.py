# reference - https://www.sharpsightlabs.com/blog/numpy-axes-explained/
import numpy as np

# Axes are like Co-ordinate System :
#Axes -0 --> X-Axis --> Rows
#Axes -1 --> Y-Axis --> Columns
#Axes -2 --> Z-Axis -->Hight/Depth

np1 = np.arange(0, 12).reshape([3,4])
print(np1)

# It becomes a matrix like -->  
"""
[[ 0  1  2  3]                  Size=[3,4] represents 3 rows , 4 columns , In terms of Axis - 4 Elemants along Axis-1 . 3 Elemants Along Axis -0
 [ 4  5  6  7]                  0= (0,0)   1=(0,1)   2=(0,2)   3= (0,3)     
 [ 8  9 10 11]]                 4= (1,0)   5=(1,1)   6=(1,2)   7= (1,3)
,                               8= (2,0)   9=(2,1)   10=(2,2)  11= (2,3)                                                                                """  
 
