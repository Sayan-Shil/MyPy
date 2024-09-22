import numpy as np

np1=np.array([1,6,7,2,3,5])
print(np1)
print(np.sort(np1))


np2=np.array(["Sayan","Arka", "Bibek","Shuvrodip","Arnab","Arpan"])
print(np2)
print(np.sort(np2))



np2= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2)
print(np.sort(np2))

# Sorting Axis Along -->

a = np.array([[4,2,5],[1,3,6]])

#Axis-None Return a 1-D List with all elemants sorted
print("Axis-None")
print(np.sort(a,axis=None))        # Merge Two List [4,2,5,1,3,6] , Sort [1,2,3,4,5,6]

print("Axis-0")
print(np.sort(a,axis=0))           #Columnwise Sorting

print("Axis-1")
print(np.sort(a,axis=1))           #Rowwise Sorting