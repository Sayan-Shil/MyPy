# In Python, Loop Statements are -- while and for only...

# while Loop






# for loop : In Python, a for loop is used to iterate over an iterable (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence

"""
Syntax-

for variable in iterable:
    # Code to execute for each item

"""

#1. Iterating Over a List:

fruits= {"Apple", "Mango", "Pineapple", "Orange", "Guava"}

for fruit in fruits:                                                # here, fruits are list and fruit is varible of fruits type
    print(fruit)




#2 Iterating over Mulriple Sequences 

flowers = {"Rose", "Jasmine", "Marigold" }
friend= {"Arnab", "Bibek", "Shuvradip"}

for flowers,friend in zip(flowers,friend):
    print(f"My Friend - {friend} likes - {flowers}")               # Using Zip() we can zip two or more variables that can be used as alternatives 



#3 Iterating over a range:

for i in range(11):                                                # iterates starts from 0 to 10 , 11 excludes
    print(i)

for i in range(10,21):
    print(i)                                                       # iterates starts from 10 included to 20 , 21 excluded





# Break and Pass 

for i in range(1,22):
    if i%8==7 :
        break
    print(i)


for i in range(10):
    if i % 2 == 0:
        pass                                                       # Later, you might add code to handle even numbers
    else:
        print(i)                                                   # For now, only print odd numbers
 
