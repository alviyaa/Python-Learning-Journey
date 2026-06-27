"""if i write direct text without quotes in string 
it is not considered as text and gives syntax error
"""
# print(Hi this is my first line of code)
print("Hi this is my first line")

# if i write 9 inside quotes then it is treated as string
print("9")
# but then is treated as integer
print(9)
# both above output will be same but if i write
print("8 + 7") # this will be treated as string so it will be print as it is
print(8 + 7) # this will add and print the sum

# we can also call multiple arguments inside print()
print("Hey, can you tell the number",7)
# if i write multiple arguments without comma this will give syntaxerror
# print("Hey, can you tell the number" 7)
print(18 * 9)
# Single line comment
# MUltiple line comment
# can be use to write multiple para
# or
 
"""hey can you leave some notes for me
"""
# or
''' Comments can be ignored by python interpreter
'''
# we can not not directly put character inside string for putting character 
# print("Apple is a fruit
# it is good for health
# and it is very good in taste") this will give syntax error
# we use escape sequence character
# if i want to print something in newline we can use \n
print("Apple is a fruit\nit is good for health\nand it is very good in taste")
# if we want toprint string inside string we cannot do it directly instead 
# print("I like "Apple", "Banana", "Mango"")
# we can use escape sequence character like \"\"
print("I like \"Apple\", \"Banana\", \"Mango\"")
print("hey",7)
print("Rainbow has",7,"colors",sep="-")
print("Rainbow has",7,"colors",sep="-",end = " ")
print("But my fav color is voilet color")
print("count no. till",10,20,sep="-->",end ="01\n")
print("Stop at 100!!!")
print("Are you ready lets start",3,2,1,sep="...",end = " plz ")
print("Play safe.....")

print("Hi python")
print(9)
print("Hi python",5,7,sep ="*")
print("Hi all",7,5,sep = "-",end = "09\n")
print("abc")
print("abc")
print("Python is used everywhere \nit can be used by various industries\npython can interpreted line by line")
print("Python is used \"everywhere\" \nit can be used by various \"industries\"\npython can \"interpreted line by line\"")