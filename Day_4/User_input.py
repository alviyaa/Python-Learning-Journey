a = input("Enter your name : ")
print("My name is:",a)

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
print(x + y)
# or
x = input("Enter 1st number : ")
y = input("Enter 2nd number : ")
print(int(x) + int(y))

# Ask the user for their name
name = input("Enter your name: ")
# Ask the user for their age and convert the input string into an integer
age = int(input("Enter your age"))
# Calculate the year they will turn 100 based on the current year (2026)
year = 2026 + (100 - age)
# print the year
print("By",year,"You will turn 100 years old")