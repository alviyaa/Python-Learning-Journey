# 1. The AI User ID Generator
# first ask a user fir their first name and the birth year
first_name = input("Enter your name: ")
birth_year = input("Enter you birth year: ")

# Calculate the length of the first name
length = len(first_name)
# create a user id by joining name, length,birthyear
user_Id = first_name + str(length) + birth_year
print("Your generated AI User ID is:", user_Id)

# 2. The Character Extractor
text = "Artificial_Intelligence"
print(text[0])
print(text[-1])

# 3.  The Data Type Referee
data_packet = 42
banned_words = "malware exploit hacking"
print(isinstance(data_packet, int))
print("exploit" in banned_words)


current_semester = 4
message = "I am currently in semester number " + str(current_semester)
print(message)

xyz = "Hello World!"
print(xyz)

# Given the word:word = "PYTHON"
# Task: Create a new variable that contains just the first letter
# and the last letter glued together.Expected Output: "PN"
# Hint: Remember that indexing starts at 0
word = "Python"
grab = word[0] + word[-1]
print(grab)

# You have a username where the first letter was
# accidentally typed lowercase:name = "alex"
# Task: Create a new variable where the first letter is uppercase "A",
# and glue it to the rest of the letters ("l", "e", "x") by fetching them one by one.Expected Output: "Alex"
name = "alex"
new_name = "A" + name[1] + name[2] + name[3]
print(new_name)

first = "Harry"
middle = "Kumar"
last = "Singh"
extract = first[0] + middle[0] + last[0]
print(extract)

animal = "Monkey"
year = "1998"
user_name = animal[0] + animal[-1] + year[-2] + year[-1]
print(user_name)

