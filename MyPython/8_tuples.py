# List are immutable sequence data type which can be change without assigning or re-assigning
# List stores list items . Every List Items have index starting from 0

a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element

numbers = (1,2,3,4,5,6,7,8,9)
print(numbers)                                          # Direct Print the list

print("\n\n\n")

for num in numbers :                                  # Iterates with  For Loop
    print(num)

print("\n\n\n")

i=0
while i<3 :
    print(numbers[i])
    i += 1

#It has only 2 methods ->  index() and count() same like List
