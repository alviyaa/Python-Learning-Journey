# Creating a variable and assigning value to it
name = "abc"

# if i write 
# name = abc --> this give error
roll_no = 9
course = "b.tech(c.s)"
# using variable 
print(name)
print(roll_no)
print(course)

# Variable naming rule
# we can no start variable name with number
# 1a = 10

a1 = 10 # this is correct
print(a1)

# we can not use in built function for variable name
# this are reserved words(Keywords)
# int = 8

a = 1
b = 6.7
c = "abf"
d = True
e = None
f = complex(8,9)

# we can also see which type of data variable holds using type() function
print(type(name))
print(type(roll_no))
print(type(course))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# integers
a = 7
print(type(a))
b = a + 10
print(b)
c = a * 10
print(c)
d = a / 10
e = a % 10
print(d)
print(e)

a = 10
b = 20
print(a + b)

# float
a = 190.5
print(a)
print(type(a))

# Boolean 
a1 = True
b1 = False
print(type(a1),type(b1))

# Strings
num1 = "abc"
print(num1)
print(type(num1))

# In string we can do many operation like concantenation
# name = "alviya"
# print(name + num1)
# or
name = "alviya"
concatenate = name+ "   ahmad"
print(concatenate)

# if we try to concatenate one datatype to another it gives error
# like we do with string and int
# concatenate = name+ 8
# print(concatenate)
# instead we can do strong typing
concatenate = name+ str(8)
print(concatenate) 

# Complex number
j = 1.7-6.6j
print(j)
print(j.real,j.imag) # here 1.7 is real number and -6.6 is imaginary number

# Dynamic typing
a1 = 6
a1 = "letter"
# here we can smoothly can the value of variable

# strong typing
a = "Abc"
b = a+ "1"
print(b) # it will be concatenated bcz both are string
# but if we write
# b = a+ 1
# print(b) 
"""this give typeerror because in 
concatenation we cannot concatenate using different datatype 
instead if we want to concatante string, 
both the side should have same datatype"""

# String Formatting
a = 7
print("The value of a is -",a)
first_name = "Alviya"
last_name = "Ahmad"
print("My first name is {} and my last name is {} ".format(first_name,last_name))
print("My first name is {0} and my last name is {1} ".format(last_name,first_name))
print("My first name is {1} and my last name is {0} ".format(last_name,first_name))
print("My first name is {a} and my last name is {b} ".format(b=last_name,a=first_name))

# Input Type
a = input("Enter a name:")
print(a)
b = input("Enter a number")
print(b)
print(a + b)
# print(int(a) + int(b))

a = 10
b = a / 10
print(b)
print(a + 10)
print(a * 20)
print(a / 9)
print(a % 10)
