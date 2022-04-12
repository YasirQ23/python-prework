# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the
# function. The first line of the code has been defined as below.
def hello_name(user_name):
    """Print simple greeting"""
    print(f"hello {user_name.upper()}!")
        
hello_name(input("Please enter your username:"))


# Question 2
# Write a python function, first_odds that prints the odd numbers from 
# 1-100 and returns nothing
def first_odds():
    """Print the odd numbers from 1-100, return nothing"""
    for x in range(1,101,2):
        print(x)
    return None  
      
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number
# of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """return max number on a list"""
    return max(a_list)

print(max_num_in_list([1,2,3,4,25]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is
# divisible by 4, but not divisible by 100, unless it is also divisible by 
# 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    """Check if the enter year is a leap year."""
    x = int(a_year)
    if x % 400 == 0:
        return (True)
    elif x % 100 == 0:
        return (False)
    elif x % 4 == 0:
        return (True)
    else:
        return (False)

print(is_leap_year(input("Enter any year to check if it is a leap year: ")))

# Question 5
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
# are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    """Tells if given list has consecutive numbers."""
    x = a_list
    x.sort()
    new_list = list(range(min(x),max(x) + 1))
    return x == new_list

print(is_consecutive([1,2,3,5]))