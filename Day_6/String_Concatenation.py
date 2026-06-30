# In Python, you can combine multiple strings together with the plus (+) operator.
# This process is called string concatenation.
my_str_1 = "Hello"
my_str_2 = "World"

str_plus_str = my_str_1 + " " + my_str_2
print(str_plus_str)  # Hello World

# but note that this only works with strings. If you try to
# concatenate a string with a number, you'll get a TypeError:

name = "John Doe"
age = 26
# name_and_age = name + age
# print(name_and_age) # TypeError: can only concatenate str (not "int") to str
# To fix that, you can convert the number into a string with the built-in str() function
name_and_age = name + str(age)
print(name_and_age)

# We can  also use the augmented assignment operator for concatenation. 
# This is represented by a plus and equals sign (+=), 
# and performs both concatenation and assignment in one step. 
name = "John Doe"
age = 26
name_and_age = name
name_and_age += str(age) # name_and_age = name_and_age + str(age)
print(name_and_age)                                                                                                                                      