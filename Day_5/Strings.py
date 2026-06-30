name = "Alviya"
# print("Hello", + name) 
"""In Python, the + symbol can be used as a unary operator (like +5 or -3).
When you write +name, Python tries to apply the unary plus operator to name.
But name is a string, and strings don't support unary plus.
→ Hence the error: TypeError: bad operand type for unary +: 'str'
instead if we want to concatenate we can write like this"""
print("Hello, "+name) 
# or simply if we want to print the value of name then
print("Hello",name)

# if we try to concatenate one datatype to another it gives error
# like we do with string and int
# concatenate = name+ 8
# print(concatenate)
# instead we can do strong typing
concatenate = name+ str(8)
print(concatenate) 

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

# Dynamic typing
a1 = 6
a1 = "letter"
# here we can smoothly change the value of variable

# Multi-line strings
# st = "A string is a "sequence of characters surrounded by either single or double quotation marks.""
# this give error because we cannot directly use double quotes inside string
st = "A string is a \"sequence of characters surrounded by either single or double quotation marks.\""
print(st)
# or we can enclose with single quote
st = 'A string is a "sequence of characters surrounded by either single or double quotation marks".'
print(st)

lang = "Python Programming"
# if i want to access any character, for that we can use indexing
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])
print(lang[6])
print(lang[7])
print(lang[8])
print(lang[9])
print(lang[10])
print(lang[11])
print(lang[12])
print(lang[13])
print(lang[14])
print(lang[15])
print(lang[16])
print(lang[17])
# print(lang[18]) throws an error because the 18th character is not present

sentence = "A string is a sequence of characters surrounded by either single or double quotation marks."
# if i want to access all character of above variable named sentence instead of writing indexing manually
# we can use for loop 
for character in sentence:
    print(character) # here all sentence character are going to character and printing it one by one

