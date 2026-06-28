name = "John Doe"
a1 = 8
# 1a = 7
a1_ = 9
# a1@ gives syntax error
Age = 8
age = 8
my_variable_name = 'abc'
user_age = 20
# this is a single-line comment
# this is
# a multi-line
# comment
print('Hey Everyone')
print('My fav color is','black','wine','leavender')

my_name = 'abc'
# to see the type of my_name we can use type() function
print(type(my_name))

# one concept: to verify that a particular variable is a specific type before performing operations on it. 
# This is where the isinstance() function comes in

account_balance = '100'
# account_balance / 2  #this give type error
# to see if account_balance is an integer
# you can check using the isinstance() function 
print(isinstance(account_balance, int)) #false

# the isinstance() function 
# also allows you to check for multiple types at once.
account_balance = 1000
print(isinstance(account_balance, (int,float)))