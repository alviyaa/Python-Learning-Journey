# Take a number from input and store it in num
num = int(input("Enter a number : "))
# use the num to find the square of that number
square = num ** 2
# use the square to see what is the square of the number you entered
print("The square of number is :",square)

# Rectangle area finder
length = int(input("Enter the length of a rectangle: "))
width = int(input("Enter the width of a rectangle: "))
area = len * width
print("The Area of rectangle is :",area)

# Bill Splitter
total_amount = float(input("enter the total restaurant bill amount :"))
friends = int(input("How much friends sharing it :"))
pay = total_amount // friends
print("each person needs to pay :",pay)
