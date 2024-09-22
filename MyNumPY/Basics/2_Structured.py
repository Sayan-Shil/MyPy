import numpy as np

#A structured dtype allows you to define custom, more complex data types with multiple fields, similar to columns in a table. Each field can have a different data type, like in a record or a database row.

# Define a cutstom dtype with fields: name, run, ball 
runstat = [('name', 'U20'), ('run', int), ('ball', int)]
values = [('Virat Kohli', 55, 30), ('MahendraSingh Dhoni', 78, 52),('Rohit Sharma',34,21 ), ('Rinku Singh', 49,26)]

# Create a structured array
arr = np.array(values, dtype=runstat)  #Specify that dtype is dtype
print(arr)
print(arr)

print(np.sort(arr, order='run') )
print(np.sort(arr, order=['run', 'ball']))

d = np.dtype([('x', 'i8'), ('y', 'f4')])
print(d.names)