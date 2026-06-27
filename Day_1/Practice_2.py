# Print this exact 3-line message using only one single print() statement
print("Item Name: Laptop\nPrice: \tRs. 50,000\nStatus:\t\"Available\"")

"""Create three separate variables for a date: day = 18, month = 06, and year = 2026. 
Print them together so they look exactly like a real date on a single line: 18/06/2026.
"""
day = 18
month = "06"
year = 2026

print(day,month,year,sep = "/")

"""
Write two separate print() statements. 
The first should print Loading... and the second should print Done!.
Modify the code so they both print on the exact same line with a small arrow pointing between them, like this: Loading... ➔ Done!.
"""
print("Loading...",end=" --> ")
print("Done!")

print("Welcome to Day 1 of the Python Sprint! Total hours left: 90")
