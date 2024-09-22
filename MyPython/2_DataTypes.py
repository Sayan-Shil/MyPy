# Data Types ---->
"""
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None

"""

#Example-

ExampleOfInteger= 50                     # In Python, we do not need to mention variable datatype 
ExampleOfFloat = 85.665
ExampleOfString = "Sayan Shil"
ExampleOfBoolean = True
ExampleOfNone = None

print(type(ExampleOfInteger))            # type(<variable>) used to check the type of the variable
print(type(ExampleOfFloat))
print(type(ExampleOfString))
print(type(ExampleOfBoolean))
print(type(ExampleOfNone))


# Note** 
"""
Python determines the type of the variable  dynamically . so like C/C++/JAVA , we dont need to type (int a =7; float a=8.65)
The Type of variable can change according to assigned value. In case rewrite a variable with same name , it will do "reassign"

"""

a=9
b=9                                       # a= integer = 9                        b=integer=9
print(a==b)                               # True
a="Sayan"                                 # a= string = "Sayan" (reassign)        b=integer=9
print(a==b)                               # False