# In some programming languages, characters surrounded by single quotes are treated differently than characters surrounded by double quotes, 
# but in Python, they're treated equally. So, you can use either when working with strings
my_str_1 = 'Hello'
my_str_2 = "World"
print(my_str_1 + my_str_2)

# If you need a multi-line string, you can use triple double quotes or single quotes:
my_str_3 = """Multi-line 
string """
my_str_4 = '''Another
multiline
string'''
print(my_str_3)
print(my_str_4)

msg = "It's sunny day"
quote = 'She said, "Hello World!"'
print(msg)
print(quote)

msg = 'It\'s sunny day'
print(msg)
quote = "She said, \"Hello World!\""
print(quote)

# you may need to check if a string contains one or more characters. For that, Python provides the in operator, 
# which returns a boolean that specifies whether the character or characters exist in the string or not.
Quote = "How have you been"
print('How' in Quote) #returns true
print('Hi' in Quote) #false
print('e' in Quote) #true
print('z' in Quote) #false

# To get the length of a string, you can use the built-in len() function.
my_str = "Python is very simple language"
print(len(my_str)) #30 character are there in above string

my_str = "Hello World"
# To access a character by its index, you use square brackets ([]) with the index of the character
print(my_str[0])
print(my_str[1])

# Negative indexing is also allowed, 
# so you can get the last character of any string with -1, the second-to-last character with -2
print(my_str[-1])
print(my_str[-2])

# Strings are immutable data types in Python. This means that you can reassign a different string to a variable:
greeting = "Hi"
greeting = "Hello"
print(greeting)

# But direct modification of a string isn't allowed:
# you can't change the original object itself by adding, removing, or replacing any of its elements.
greeting = "hello"
greeting[0] = "H"
print(greeting[0])