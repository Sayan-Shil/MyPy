# Strings are immutable in nature , sequences of characters enclosed in single/double/triple brackets



a= 'Sayan' 
a= "Sayan"                                          # All are valid syntax
a= '''Sayan'''


""" String Slicing - """
#String Slicing means Cutting the Name within a range... In gerenral, every String is indexed as (0, last no. of words -1) or negatively as (-last of words, -1)
# Example - "Sayan"  or   "Sayan"
#            01234      -5-4-3-2-1

#Length of a String
name= "Sayan"
print(len(name))

#Strings are immutable , any changes in String will not change the actually variiable , we have to store mutated String another variable or same variable to reassign
#Example
a="Sayan"
print(a[1:3])                                        # print 1st Index to (3-1) index 
print(a)
a= a[1:3]                                            # reassigning the value
print(a)

#String slicing with skip value
a="0123456789"
a=a[0:10:2]                                          # print starts from 0th index, skip next 2 value and print again till (10-1) index
print(a)

print("\n\n\n\n\n")

""" String Functions """
# String Functions are pre-defined function by python itself to work a specific tasks with a string , again assure the fact that String is immutable and to change anythhig we meed to assign or reassign




""" 1. Functionality - To Manipulate Letters """
# Suppose The Name is --
name = "Sayan Shil"

print("Selected Name-\n" +name)
print("\nFunctions - To Manipulate Letters")



# lower()               --> To lowercase of all letters
print(name.lower())

# upper()               --> To uppercase of all letters
print(name.upper())

# capitalize()               --> To make  first letter capital of all words
print(name.capitalize())

# title()               --> To make as title , all first letter - Capital 
print(name.title())

# swapcase()               --> To swap the case of all letters in word
print(name.swapcase())



print("\n\n\n\n\n")



""" 2. Functionality - To Remove Whitespace """
# Suppose The Name is --
name = "  Sayan  Shil  "
print("Selected Name-\n" +name)
print("\nFunctions - To Remove Whitespace")




# strip()               --> To strip/remove entire backspace ( only useless backspace)
print(name.strip())


# lstrip()               --> To strip/remove left backspace ( only useless backspace)
print(name.lstrip())

# rstrip()               --> To strip/remove right backspace ( only useless backspace)
print(name.rstrip())

print("\n\n\n\n\n")






""" 3. Functionality - To Replace or Modify Substrings """
# Suppose The Name is --
name = "Sayan Shil"
print("Selected Name-\n" +name)

print("\nFunctions - To Replace or Modify Substrings ")



# replace(old, new)             --> replace old substring to new substring
print(name.replace("Shil", "Sahoo"))         

# zfill(width)               --> used to pad a string representation of a number with zeros on the left until it reaches a specified width
print(name.zfill(7))          # will not change if string.length >width
print(name.zfill(15))  


print("\n\n\n\n\n")



""" 4. Functionality - To Search Substrings """
# Suppose The Name is --
name = "Sayan Shil Sayan Shil"
print("Selected Name-\n" +name)

print("\nFunctions - To Search Substrings")




# index(substring)           --> Returns the index of the first occurrence of the substring. Returns -1 if not found
print(name.index("Shil"))    

# rindex(substring)           --> Returns the index of the last occurrence of the substring. Returns -1 if not found
print(name.rindex("Shil"))    

# index(substring)           --> Returns the index of the first occurrence of the substring. error if not found
print(name.index("Shil"))    

# rindex(substring)           --> Returns the index of the last occurrence of the substring. error if not found
print(name.rindex("Shil"))    



print("\n\n\n\n")


""" 5. Functionality - To  Count or Check String Properties """
# Suppose The Name is --
name = "Sayan Shil Sayan Shil Shil Shil shil"
print("Selected Name-\n" +name)
print("\nFunctions - To  Count or Check String Properties ")




# cout(substring)           --> Returns the number of occurrences of a substring , case sensitive
print(name.count("Shil"))  

# startswith(substring)           --> Returns boolean if starts with substring , case sensitive
print(name.startswith("Sayan"))  

# endswith(substring)           --> R Returns boolean if ends with substring , case sensitive
print(name.endswith("Shil"))  



print("\n\n\n\n")



""" 6. Functionality -  To Split and Join Strings """
# Suppose The Name is --
name = "Sayan & Shil & Sayan & Shil & Sayan & Shil  "
print("Selected Name-\n" +name)
print("\nFunctions -  To Split and Join Strings ")





# join(iterable)               --> Converts iterable in String , " " represents need to convert in string
list = {"Sayan", "Shil"}
print(type(" ".join(list)))  

# split(separator , maxsplit)
print(name.split())             # By Default - splitting the string at any whitespace character.
print(name.split(" "))          # If Not Any separator , entire string becomes list  
print(name.split(" & "))        # If Any separator , list item will push as seeing the separator 
print(name.split(" & ",2))      # if any maxsplit , it will iterated until particular numbered separator then behave as no separator

# partition(substring)
print(name.partition("Shil"))   # partition in such way , substring itself a list item , and left and right portion itself a list item


print("\n\n\n\n")


""" 7. Functionality -  To Check Character Types """
# Suppose The Name is --
name = "Sayan & Shil & Sayan & Shil & Sayan & Shil  "
print("Selected Name-\n" +name)
print("\nFunctions -  To Check Character Types ")



#isalpha()                     # returns true if string is alphabetic ( no non-alphabetic presnt)
print(name.isalpha())

#isdigit()                     # returns true if string is numeric ( no non-numeric presnt)
print(name.isdigit())

#alnum()                      # returns true if string has only algebric + numeric 
print(name.isalnum())

#isspace()                     # returns true if string has only space 
print(name.isspace())

#islower()                     # returns true if string is lowercase
print(name.islower())

#isupper()                     # returns true if string is uppercase
print(name.isupper())

#isidentifier()               # returns true if string is identifier ( ontain alphanumeric characters , can contains only _ , cannot start with Numbers , not if it's a reserved keyword.)
print(name.isidentifier())


print("\n\n\n\n")



""" 8. Functionality -  To Align """
# Suppose The Name is --
name = "Sayan Shil"
print("Selected Name-\n" +name)
print("\nFunctions -  To Align ")





#center(width, fillchar)            #Centers the string within a specified width, optionally padding with a specific character.
print(name.center(15, '#'))

#ljust(width, fillchar)            #Fill the string within a specified width in left, optionally padding with a specific character.
print(name.ljust(15, '#'))

#rjust(width, fillchar)            #Fill the string within a specified width in right, optionally padding with a specific character.
print(name.rjust(15, '#'))


