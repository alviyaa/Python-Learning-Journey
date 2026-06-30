my_str = "Python, Programming"
# we can find the length of string using len() built-in function
print(len(my_str))

fruit = "apple"
fruit_length = len(fruit)
print(fruit_length)
# if i want to access all the character of fruit
print(fruit[0:5])
# if i remove 0 the output will remain same
# we can omit the start and stop indices,
# and Python will default to 0 or the end of the string,
print(fruit[:5])
# if i want index from 1
print(fruit[1:5])
# if if remove index from both side python automatically apply the len(fruit)
print(fruit[:])  # print(fruit[:5]) both are same

# if i apply negative indexing
print(fruit[0:-3])
# python automatically apply len(fruit) after : like thi
# fruit[0:len(fruit)-3] and start from 0 but 3 is not included, goes till n-1

print(fruit[-1:-3])  # 4:2 does not give anything in output
# if i write reverse of above
print(fruit[-3:-1])  # 2:4

name = "Alviya"
length_of_name = len(name)
print(length_of_name)
print(name[-4:-2])  # 2:4
print(name[-4:-2:2])

my_str = "Hello Python"
print(my_str[1:4])
print(my_str[:7])
print(my_str[8:])
# Note that slicing a string does not modify the original string:
print(my_str)

# there's also an optional step parameter, which is used
# to specify the increment between each index in the slice.
print(my_str[0:11:2])
# we can reverse the string by setting step to -1
print(my_str[::-1])

word = "Python"
print(word[1:5])

animal = "Monkey"
year = "1998"
grab = animal[0] + animal[-1] + year[2:]
print(grab)

letters = "ABCDEF"
print(letters[::2])