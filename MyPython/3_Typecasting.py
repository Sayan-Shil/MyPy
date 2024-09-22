# TypeCasting 
"""
Typecasting refers to type conversion. It allows a variable to change its data type according to specific instructions.
Python naturally supports implicit typecasting, which enables automatic type conversion without any compilation errors when lower data types are assigned to higher data types.
Additionally, we can use explicit typecasting to convert a variable from one type to another as needed.

"""

# Implicit TypeCasting

a=8
b=19.5
print(a+b)                               # a=8 have been promoted to 8.0 implicitly ( Lower Int to Higher Float )

# Explicit TypeCasting

a=8
b=19.5
print(int(a + b))                        # b=19.5 have been forcefully demoted to 19 explicitly ( Higher Float to Lower Int )


# Note** 
#  It is important that the conversion must be valid  !! Any Number can be a String but All Strings cannot be number !!

a=4
print(a)
print(type(a))
a=str(a)
print(a)
print(type(a))
a="Sayan"
# a=int(a)          invalid literal for int() with base 10: 'Sayan' ( "Sayan" cannot be a valid number)
