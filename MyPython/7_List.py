# List are mutable sequence data type which can be change without assigning or re-assigning
# List stores list items . Every List Items have index starting from 0

fruits = ["Apple", "Mango", "Jackfruit"]
print(fruits)                                          # Direct Print the list

print("\n\n\n")

for fruit in fruits :                                  # Iterates with  For Loop
    print(fruit)

print("\n\n\n")

i=0
while i<3 :
    print(fruits[i])
    i += 1



# List Methods to manipulate List , Remember List is mutable type !!

#Adding
my_list = [1, 2, 3]
my_list.append(4)          # Output: [1, 2, 3, 4]                            add elemant 4 in the list ( single )
my_list.extend([5, 6])     # Output: [1, 2, 3, 4, 5, 6]                      add a list [5,6] ( multiple )
my_list.insert(0, -1)      # Output: [-1, 1, 2, 3, 4, 5, 6]                  add elemant -1 in 0th indexed

#Removing Elements
my_list.remove(3)            # Output: [-1, 1, 2, 4, 5, 6]                   remove 3-index element 
popped_item = my_list.pop()  # Output: [-1, 1, 2, 4, 5], popped_item = 6     remove last elemant
my_list.clear()              # Output: []                                    clear list

#Searching and Counting
my_list = [1, 2, 3, 2, 1]
index = my_list.index(2)       # Output: 1                                   return index of element of 2
count_of_1 = my_list.count(1)  # Output: 2                                   return number of occurance of element of 1

#Sorting and Reversing
my_list = [3, 1, 4, 2]
my_list.sort()              # Output: [1, 2, 3, 4]                           sorting in Timsort ( Merge Sort extention ) in O(nlogn)
my_list.sort(key=str)       # Output: [1, 2, 3, 4]                           sorting after converting all items in String
my_list.reverse()           # Output: [4, 3, 2, 1]                           reversing list

#Copy and clone
my_list = [1, 2, 3]
new_list = my_list.copy()   # Output: [1, 2, 3]                              copy and clone 



