# Set is a collection of non-repetitive elements.
#  1. Sets are unordered => Element’s order doesn’t matter
#  2. Sets are unindexed => Cannot access elements by index
#  3. There is no way to change items in sets.
#  4. Sets cannot contain duplicate values

s = set() # no repetition allowed!
s.add(1)
s.add(2)
s.add(2)
print(s)  # or set ={1,2} 

#Set Functions
s1= {1,2,3}
s2 ={3,4,5}

#Adding Elements
s1.add(7)                     # add Item
s1.update([1,2,5,6,8])        # add List
print(s1)
print("\n\n")

#Removing elements
s1.remove(3)                 #Removes a specified element from the set. Raises a KeyError if the element is not found.  
print(s1)
s1.discard(2)                #Removes a specified element from the set. will not raise a KeyError if the element is not found.  
print(s1)
s1.pop() 
print(s1)
print("\n\n")
#Set Operation

a= {1,2,3,4,5}
b= {4,5,6,7,8,9}

print(a.union(b)) 
print(a | b)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)

